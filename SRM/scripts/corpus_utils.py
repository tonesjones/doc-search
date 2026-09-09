"""Small safe-write and content-normalization helpers for the SCA corpus."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any


VOLATILE_MANIFEST_FIELDS = frozenset({"lastIndexBuild", "lastTocFetch", "scrapedAt", "lastCheckedAt"})


def content_hash(text: str) -> str:
    """Return SHA-256 for Markdown with stable line endings and no trailing blank lines."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def markdown_body(text: str) -> str | None:
    """Return Markdown after a YAML front-matter block, or None when it is invalid."""
    if not text.startswith("---\n"):
        return None
    _, separator, body = text[4:].partition("\n---\n")
    return body.rstrip("\n") if separator else None


def atomic_write_text(path: Path, text: str) -> None:
    """Write UTF-8 through a sibling temp file and atomically replace the destination."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def write_text_if_changed(path: Path, text: str) -> bool:
    """Atomically write only when the exact generated text changed."""
    if path.is_file() and path.read_text(encoding="utf-8") == text:
        return False
    atomic_write_text(path, text)
    return True


def _without_volatile(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _without_volatile(item) for key, item in value.items() if key not in VOLATILE_MANIFEST_FIELDS}
    if isinstance(value, list):
        return [_without_volatile(item) for item in value]
    return value


def manifest_substantively_equal(old: dict[str, Any], new: dict[str, Any]) -> bool:
    """Ignore bookkeeping timestamps when deciding whether a refresh changed corpus data."""
    return _without_volatile(old) == _without_volatile(new)


def json_text(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"
