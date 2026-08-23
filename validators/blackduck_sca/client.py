from __future__ import annotations

import json
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from validators.core.safety import validate_sca_base_url

USER_MEDIA = "application/vnd.blackducksoftware.user-4+json"
PROJECT_MEDIA = "application/vnd.blackducksoftware.project-detail-7+json"


class SCARequestError(RuntimeError):
    def __init__(self, status: int | None, category: str, message: str):
        super().__init__(message)
        self.status = status
        self.category = category


@dataclass
class Response:
    status: int
    headers: dict[str, str]
    body: bytes

    def json(self) -> Any:
        return json.loads(self.body.decode("utf-8")) if self.body else None


def load_runtime_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


class SCAClient:
    def __init__(self, base_url: str, api_token: str, timeout: float = 30.0, observed_version_hint: str | None = None):
        self.base_url = validate_sca_base_url(base_url)
        if not api_token:
            raise ValueError("BLACKDUCK_API_TOKEN is required")
        self._api_token = api_token
        self._bearer: str | None = None
        self.timeout = timeout
        self.observed_version_hint = observed_version_hint

    def _request(self, method: str, path: str, *, headers: dict[str, str] | None = None, body: bytes | None = None) -> Response:
        url = self.base_url + (path if path.startswith("/") else "/" + path)
        request = urllib.request.Request(url, data=body, method=method, headers=headers or {})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return Response(response.status, {k.lower(): v for k, v in response.headers.items()}, response.read())
        except urllib.error.HTTPError as exc:
            category = "AUTHENTICATION_FAILED" if exc.code == 401 else "AUTHORIZATION_FAILED" if exc.code == 403 else "API_UNAVAILABLE"
            raise SCARequestError(exc.code, category, f"SCA request returned HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise SCARequestError(None, "ENVIRONMENT_UNAVAILABLE", "SCA environment request failed") from exc

    @staticmethod
    def _find_bearer(value: Any) -> str | None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key.casefold() in {"bearertoken", "access_token", "token"} and isinstance(child, str) and child:
                    return child
            for child in value.values():
                found = SCAClient._find_bearer(child)
                if found:
                    return found
        return None

    def authenticate(self) -> Response:
        response = self._request("POST", "/api/tokens/authenticate", headers={
            "Accept": USER_MEDIA,
            "Authorization": f"token {self._api_token}",
        })
        bearer = self._find_bearer(response.json())
        if not bearer:
            raise SCARequestError(response.status, "AUTHENTICATION_FAILED", "Authentication response did not contain a bearer token")
        self._bearer = bearer
        return response

    def get(self, path: str, accept: str = "application/json") -> Response:
        if not self._bearer:
            self.authenticate()
        return self._request("GET", path, headers={"Accept": accept, "Authorization": f"Bearer {self._bearer}"})

    def post_json(self, path: str, payload: dict[str, Any], media_type: str) -> Response:
        if not self._bearer:
            self.authenticate()
        return self._request("POST", path, headers={
            "Accept": media_type,
            "Content-Type": media_type,
            "Authorization": f"Bearer {self._bearer}",
        }, body=json.dumps(payload).encode("utf-8"))

    def observed_version(self) -> str | None:
        if self.observed_version_hint:
            return self.observed_version_hint
        response = self._request("GET", "/")
        text = response.body.decode("utf-8", errors="replace")
        patterns = (
            r"(?i)version\s*[:=]\s*[\"']?(\d{4}\.\d+(?:\.\d+)?)",
            r"(?i)>\s*(\d{4}\.\d+(?:\.\d+)?)\s*<",
        )
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        return None

    def projects(self, *, limit: int = 1, name: str | None = None) -> Response:
        query: dict[str, str | int] = {"limit": limit}
        if name:
            query["q"] = f'name:"{name}"'
        return self.get("/api/projects?" + urllib.parse.urlencode(query), PROJECT_MEDIA)

    def project_versions(self, project_path: str, *, limit: int = 100, name: str | None = None) -> Response:
        query: dict[str, str | int] = {"limit": limit}
        if name:
            query["q"] = f'versionName:"{name}"'
        path = project_path.rstrip("/") + "/versions?" + urllib.parse.urlencode(query)
        return self.get(path, "application/vnd.blackducksoftware.project-detail-5+json")


def collection_count(payload: Any) -> int | None:
    if not isinstance(payload, dict):
        return None
    for key in ("totalCount", "total", "count"):
        if isinstance(payload.get(key), int):
            return payload[key]
    items = payload.get("items")
    return len(items) if isinstance(items, list) else None
