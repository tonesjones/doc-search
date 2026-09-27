from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from evaluation.core import EvaluationError, revision_hash

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE_PATH = ROOT / "evaluation" / "profiles" / "sca-2026.7.json"


def load_profile(path: Path = DEFAULT_PROFILE_PATH, root: Path = ROOT) -> dict[str, Any]:
    profile = json.loads(path.read_text(encoding="utf-8"))
    required = {"id", "product", "product_version", "entrypoint", "instruction_files", "evidence_roots"}
    missing = sorted(required - profile.keys())
    if missing:
        raise EvaluationError(f"profile is missing fields: {', '.join(missing)}")
    for field in ("instruction_files", "evidence_roots"):
        if not isinstance(profile[field], list) or not profile[field]:
            raise EvaluationError(f"profile {field} must be a non-empty list")
    for relative in profile["instruction_files"]:
        if not _within(root, relative).is_file():
            raise EvaluationError(f"profile instruction file is missing: {relative}")
    for relative in profile["evidence_roots"]:
        if not _within(root, relative).is_dir():
            raise EvaluationError(f"profile evidence root is missing: {relative}")
    return profile


def profile_metadata(profile: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    instructions = [_within(root, item) for item in profile["instruction_files"]]
    return {
        "evaluation_profile": profile["id"],
        "entrypoint": profile["entrypoint"],
        "checkout_revision": _git(root, "rev-parse", "HEAD"),
        "checkout_dirty": bool(_git(root, "status", "--porcelain", "--untracked-files=no")),
        "instruction_revision": revision_hash(instructions),
        "source_revision": _git(root, "rev-parse", "HEAD^{tree}"),
    }


def evidence_path_allowed(relative: str, profile: dict[str, Any], root: Path = ROOT) -> bool:
    try:
        path = _within(root, relative)
    except EvaluationError:
        return False
    if not path.is_file() or path.suffix.casefold() not in {".md", ".json"}:
        return False
    if not _git_file_tracked(root, path.relative_to(root.resolve()).as_posix()):
        return False
    return any(_is_relative_to(path, _within(root, evidence_root)) for evidence_root in profile["evidence_roots"])


def _within(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not _is_relative_to(path, root.resolve()):
        raise EvaluationError(f"path escapes repository: {relative}")
    return path


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=root, text=True, encoding="utf-8", errors="replace",
        capture_output=True, check=False,
    )
    if completed.returncode != 0:
        raise EvaluationError(f"git {' '.join(args)} failed: {completed.stderr.strip()}")
    return completed.stdout.strip()


def _git_file_tracked(root: Path, relative: str) -> bool:
    completed = subprocess.run(
        ["git", "ls-files", "--error-unmatch", "--", relative], cwd=root,
        text=True, encoding="utf-8", errors="replace", capture_output=True, check=False,
    )
    return completed.returncode == 0
