"""Shared safe-write and hashing helpers for the local documentation corpus."""

from __future__ import annotations

import hashlib
import os
import tempfile
from pathlib import Path


def content_hash(text: str) -> str:
    """Return the SHA-256 digest of normalized Markdown content."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def markdown_body(text: str) -> str | None:
    """Return the Markdown after YAML front matter, or None if front matter is missing."""
    if not text.startswith("---\n"):
        return None
    _, separator, body = text[4:].partition("\n---\n")
    return body.rstrip("\n") if separator else None


def atomic_write_text(path: Path, text: str) -> None:
    """Write UTF-8 text via a sibling temporary file, then atomically replace it."""
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
