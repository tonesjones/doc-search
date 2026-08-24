#!/usr/bin/env python3
"""Call the installed Codex/`bd` production answer path and emit one trace object."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "high"
CORPUS_VERSION = "2026.7"
SKILL_PATH = Path(r"C:\Users\Owner\.codex\skills\bd\SKILL.md")
AGENTS_PATH = ROOT / "BlackDuck SCA" / "AGENTS.md"

# Limit trace discovery to the SCA corpus. This prevents routing/index/supporting
# files from being mistaken for product evidence while preserving their order.
SCA_MARKDOWN_RE = re.compile(
    r"BlackDuck SCA[/\\][^\r\n\]\[\)`'\"<>]+?\.md",
    re.IGNORECASE,
)


def _normalize_corpus_path(value: str) -> str | None:
    value = value.replace("\\", "/").strip().strip(".,:;(){}")
    value = re.sub(r"/{2,}", "/", value)
    marker = "blackduck sca/"
    offset = value.casefold().find(marker)
    if offset < 0:
        return None
    relative = value[offset:]
    path = ROOT / Path(relative)
    try:
        path.resolve().relative_to(ROOT.resolve())
    except (OSError, ValueError):
        return None
    return relative if path.is_file() else None


def corpus_paths(text: str) -> list[str]:
    """Return unique, existing SCA Markdown paths in first-seen order."""
    found: list[str] = []
    seen: set[str] = set()
    for match in SCA_MARKDOWN_RE.finditer(text):
        normalized = _normalize_corpus_path(match.group(0))
        if normalized and normalized.casefold() not in seen:
            seen.add(normalized.casefold())
            found.append(normalized)
    return found


def prompt_revision() -> str:
    digest = hashlib.sha256()
    for path in (SKILL_PATH, AGENTS_PATH):
        digest.update(str(path).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return f"bd-skill-sha256:{digest.hexdigest()}"


def version_mismatch_trace(payload: dict[str, Any]) -> dict[str, Any] | None:
    """Fail closed when an explicit SCA version is not the pinned corpus version."""
    requested = payload.get("product_version")
    if not isinstance(requested, str) or not requested.strip():
        return None
    requested = requested.strip()
    if requested.casefold() in {CORPUS_VERSION.casefold(), "latest"}:
        return None
    relative = "BlackDuck SCA/AGENTS.md"
    return {
        "answer": (
            f"The local Black Duck SCA documentation corpus is pinned to {CORPUS_VERSION} and does not establish "
            f"behavior for {requested}. I cannot determine the {requested} answer from the available version-matched "
            "documentation."
        ),
        "processed_query": None,
        "retrieved_chunks": [{
            "file": relative,
            "rank": 1,
            "score": None,
            "content": AGENTS_PATH.read_text(encoding="utf-8"),
            "metadata": {"product": "blackduck-sca", "version": CORPUS_VERSION},
        }],
        "citations": [{"file": relative}],
        "model": "deterministic-version-guard",
        "model_parameters": {},
        "prompt_revision": prompt_revision(),
        "adapter_metadata": {
            "entrypoint": "codex production adapter version guard",
            "guard": "EXPLICIT_VERSION_NOT_PINNED",
            "requested_version": requested,
            "available_version": CORPUS_VERSION,
        },
    }


def production_prompt(payload: dict[str, Any]) -> str:
    return "\n".join([
        "Use the installed bd skill to answer this Black Duck documentation question.",
        f"Requested product: {payload['product']}",
        f"Requested documentation version: {payload.get('product_version') or 'unspecified'}",
        "Preserve the customer's requested scope and cite the local version-matched Markdown evidence.",
        f"Question: {payload['question']}",
    ])


def file_version(path: Path) -> str | None:
    """Read the product pin from a topic's small YAML front matter."""
    with path.open(encoding="utf-8") as handle:
        for index, line in enumerate(handle):
            if index > 30 or (index > 0 and line.strip() == "---"):
                break
            if line.casefold().startswith("version:"):
                return line.split(":", 1)[1].strip().strip('"').strip("'") or None
    return CORPUS_VERSION if path.name.casefold() in {"agents.md", "index.md"} else None


def parse_event_stream(stdout: str) -> dict[str, Any]:
    answer = ""
    evidence_paths: list[str] = []
    seen_paths: set[str] = set()
    usage: dict[str, Any] | None = None

    for line in stdout.splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
            usage = event["usage"]
        item = event.get("item")
        if not isinstance(item, dict):
            continue
        item_type = item.get("type")
        if item_type == "agent_message" and isinstance(item.get("text"), str):
            answer = item["text"]
        if item_type != "command_execution":
            continue
        # Both the command and its displayed output are context available to the
        # production answer path. Preserve their first-seen order as rank.
        observed = "\n".join(
            value for value in (item.get("command"), item.get("aggregated_output"))
            if isinstance(value, str)
        )
        for path in corpus_paths(observed):
            key = path.casefold()
            if key not in seen_paths:
                seen_paths.add(key)
                evidence_paths.append(path)

    if not answer:
        raise RuntimeError("Codex event stream did not contain a final answer")

    chunks = []
    for rank, relative in enumerate(evidence_paths, start=1):
        path = ROOT / relative
        chunks.append({
            "file": relative.replace("\\", "/"),
            "rank": rank,
            "score": None,
            "content": path.read_text(encoding="utf-8"),
            "metadata": {"product": "blackduck-sca", "version": file_version(path)},
        })

    answer_citations = corpus_paths(answer)
    return {
        "answer": answer,
        "processed_query": None,
        "retrieved_chunks": chunks,
        "citations": [{"file": path.replace("\\", "/")} for path in answer_citations],
        "model": MODEL,
        "model_parameters": {"reasoning_effort": REASONING_EFFORT},
        "prompt_revision": prompt_revision(),
        "adapter_metadata": {
            "entrypoint": "codex exec -> installed bd skill",
            "usage": usage,
            "retrieval_scores_available": False,
        },
    }


def main() -> int:
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        payload = json.load(sys.stdin)
        question = payload.get("question")
        if not isinstance(question, str) or not question.strip():
            raise ValueError("input must contain a non-empty question")
        if payload.get("product") != "blackduck-sca":
            raise ValueError("this adapter is restricted to product blackduck-sca")

        guarded = version_mismatch_trace(payload)
        if guarded is not None:
            json.dump(guarded, sys.stdout, ensure_ascii=False)
            sys.stdout.write("\n")
            return 0

        command = [
            "codex", "exec", "--json", "--ephemeral", "--color", "never",
            "-s", "danger-full-access", "-m", MODEL,
            "-c", f'model_reasoning_effort="{REASONING_EFFORT}"',
            "-C", str(ROOT), production_prompt(payload),
        ]
        process = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            creationflags=getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0),
        )
        try:
            stdout, stderr = process.communicate(timeout=600)
        except subprocess.TimeoutExpired as exc:
            # codex.exe uses helper children on Windows. Kill only this adapter's
            # process tree so inherited pipes cannot keep the evaluator hanging.
            subprocess.run(
                ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                capture_output=True,
                text=True,
                check=False,
            )
            process.kill()
            process.communicate()
            raise RuntimeError("codex exec exceeded the 600-second adapter limit") from exc
        if process.returncode:
            detail = stderr.strip()[-2000:]
            raise RuntimeError(f"codex exec exited {process.returncode}: {detail}")
        json.dump(parse_event_stream(stdout), sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0
    except Exception as exc:  # Adapter errors are returned to the evaluator via stderr.
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
