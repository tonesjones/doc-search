#!/usr/bin/env python3
"""Answer one evaluation question through the checked-out documentation router."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluation.core import EvaluationError, redact  # noqa: E402
from evaluation.profile import (  # noqa: E402
    DEFAULT_PROFILE_PATH,
    evidence_path_allowed,
    load_profile,
    profile_metadata,
)

OUTPUT_SCHEMA = ROOT / "evaluation" / "schema" / "adapter-output.schema.json"
DEFAULT_MODEL = "gpt-5.6-terra"
DEFAULT_REASONING = "medium"
FRONT_MATTER_VERSION = re.compile(r'^version:\s*["\']?([^"\'\r\n]+)', re.MULTILINE)
PROMPT_TEMPLATE = """Use only this checkout to answer the question.
Read SKILL.md and products.json first. Resolve the product, then read its SKILL.md when present and its AGENTS.md.
Open the relevant local Markdown or versioned OpenAPI source. Do not use the web or general knowledge.
Return an answer with local file citations. For each cited source, return one exact excerpt copied from that file.
Make the excerpts support every material step, option, and value in the answer.
When the documentation lists short and long command options, prefer the self-documenting long options.
When the documentation provides an environment variable for a secret, use it instead of putting the secret on the command line.
Return evidence only from BlackDuck SCA/docs, BlackDuck SCA/sources/openapi, or evaluation/guidance.
Do not return SKILL.md, AGENTS.md, products.json, indexes, or checkpoint files as answer evidence.
If the requested version is unavailable, say that the checkout does not establish the answer for that version.

Product: {product}
Requested version: {version}
Question: {question}
"""


def prompt_revision(profile: dict[str, Any]) -> str:
    digest = hashlib.sha256()
    digest.update(PROMPT_TEMPLATE.encode("utf-8"))
    digest.update(profile_metadata(profile)["instruction_revision"].encode("ascii"))
    return f"sha256:{digest.hexdigest()}"


def build_command(output_path: Path, model: str, reasoning: str) -> list[str]:
    return [
        "codex", "exec", "-", "--json", "--ephemeral",
        "--sandbox", "read-only", "--cd", str(ROOT), "--model", model,
        "--config", f'model_reasoning_effort="{reasoning}"',
        "--output-schema", str(OUTPUT_SCHEMA), "--output-last-message", str(output_path),
    ]


def source_version(path: Path) -> str | None:
    if path.suffix.casefold() == ".md":
        match = FRONT_MATTER_VERSION.search(path.read_text(encoding="utf-8", errors="replace")[:4096])
        return match.group(1).strip() if match else None
    parts = [part.casefold() for part in path.parts]
    if "openapi" in parts:
        index = parts.index("openapi")
        return path.parts[index + 1] if len(path.parts) > index + 1 else None
    return None


def repository_relative(value: str, root: Path = ROOT) -> str:
    candidate = Path(value.replace("\\", "/"))
    if candidate.is_absolute():
        try:
            candidate = candidate.resolve().relative_to(root.resolve())
        except ValueError as exc:
            raise EvaluationError(f"evidence path is outside the checkout: {value}") from exc
    return candidate.as_posix()


def verified_excerpt(source: str, claimed: str, relative: str) -> str:
    if claimed in source:
        return claimed
    words = claimed.split()
    if not words:
        raise EvaluationError(f"evidence excerpt is empty: {relative}")
    match = re.search(r"\s+".join(re.escape(word) for word in words), source)
    if not match:
        raise EvaluationError(f"evidence excerpt is not present in source: {relative}")
    return match.group(0)


def validate_output(
    value: dict[str, Any], payload: dict[str, Any], profile: dict[str, Any], root: Path = ROOT,
) -> dict[str, Any]:
    if not isinstance(value, dict) or not isinstance(value.get("answer"), str) or not value["answer"].strip():
        raise EvaluationError("adapter output must contain a non-empty answer")
    evidence = value.get("evidence")
    citations = value.get("citations")
    if not isinstance(evidence, list) or not isinstance(citations, list):
        raise EvaluationError("adapter output evidence and citations must be lists")

    chunks: list[dict[str, Any]] = []
    evidence_files: set[str] = set()
    requested = payload.get("product_version")
    for item in evidence:
        if not isinstance(item, dict) or not isinstance(item.get("file"), str) or not isinstance(item.get("excerpt"), str):
            raise EvaluationError("each evidence item must contain file and excerpt strings")
        relative = repository_relative(item["file"], root)
        if not evidence_path_allowed(relative, profile, root):
            raise EvaluationError(f"evidence path is outside the selected profile: {relative}")
        path = root / relative
        text = path.read_text(encoding="utf-8", errors="replace")
        excerpt = verified_excerpt(text, item["excerpt"], relative)
        version = source_version(path)
        if requested and version and version != requested:
            raise EvaluationError(f"evidence version {version} does not match requested version {requested}: {relative}")
        chunks.append({
            "file": relative,
            "content": excerpt,
            "metadata": {"product": profile["product"], "version": version},
        })
        evidence_files.add(relative.casefold())

    normalized_citations: list[dict[str, str]] = []
    for citation in citations:
        if not isinstance(citation, dict) or not isinstance(citation.get("file"), str):
            raise EvaluationError("each citation must contain a file string")
        relative = repository_relative(citation["file"], root)
        if relative.casefold() not in evidence_files:
            raise EvaluationError(f"citation has no validated evidence excerpt: {relative}")
        normalized_citations.append({"file": relative})

    return {
        "answer": value["answer"],
        "retrieved_chunks": chunks,
        "citations": normalized_citations,
    }


def version_guard(payload: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any] | None:
    requested = payload.get("product_version")
    if not requested or requested in profile.get("available_versions", [profile["product_version"]]):
        return None
    answer = (
        f"This checkout is pinned to {profile['product_version']} and does not establish the requested "
        f"{requested} behavior. I cannot determine the answer without version-matched evidence."
    )
    return {"answer": answer, "retrieved_chunks": [], "citations": [], "model": "deterministic-version-guard", "model_parameters": {}}


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        profile = load_profile(DEFAULT_PROFILE_PATH)
        if payload.get("product") != profile["product"]:
            raise EvaluationError(f"profile {profile['id']} cannot answer product {payload.get('product')!r}")
        guarded = version_guard(payload, profile)
        if guarded is not None:
            guarded["prompt_revision"] = prompt_revision(profile)
            print(json.dumps(redact(guarded)))
            return 0

        model = os.environ.get("DOC_SEARCH_MODEL", DEFAULT_MODEL)
        reasoning = os.environ.get("DOC_SEARCH_REASONING_EFFORT", DEFAULT_REASONING)
        prompt = PROMPT_TEMPLATE.format(
            product=payload["product"], version=payload.get("product_version") or "unspecified",
            question=payload["question"],
        )
        with tempfile.TemporaryDirectory(prefix="ds07-") as temp:
            output_path = Path(temp) / "answer.json"
            completed = subprocess.run(
                build_command(output_path, model, reasoning), input=prompt, text=True,
                encoding="utf-8", errors="replace", capture_output=True, timeout=600, check=False,
            )
            if completed.returncode != 0:
                raise EvaluationError(f"Codex exited {completed.returncode}: {completed.stderr.strip()}")
            value = json.loads(output_path.read_text(encoding="utf-8"))
        result = validate_output(value, payload, profile)
        result.update({
            "model": model,
            "model_parameters": {"model_reasoning_effort": reasoning},
            "prompt_revision": prompt_revision(profile),
            "adapter_metadata": {"evidence_method": "model-reported excerpt, repository-validated with whitespace normalization"},
        })
        print(json.dumps(redact(result)))
        return 0
    except (EvaluationError, json.JSONDecodeError, KeyError, OSError, subprocess.TimeoutExpired) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
