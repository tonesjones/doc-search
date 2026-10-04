# Black Duck Signal Documentation Index

> Auto-generated catalog for local RAG. Do not hand-edit topic rows — update `sources/signal-latest/manifest.json` statuses and run `python scripts/build-index.py --product signal-latest`.

## Corpus status

| Field | Value |
|-------|-------|
| Product | Black Duck Signal |
| Product key | `signal-latest` |
| Version | **latest** |
| Map ID | `xmDr3Yryk7OYDGb__OGKlg` |
| TOC nodes | **32** |
| Progress | **32/32 done** (100.0%) · 0 pending · 0 skipped · 0 error |
| Last index build | 2026-10-04T23:34:30.495155+00:00 |
| Manifest | [sources/signal-latest/manifest.json](sources/signal-latest/manifest.json) |
| Raw TOC | [sources/signal-latest/toc.json](sources/signal-latest/toc.json) |

### Status legend

| Mark | Status | Meaning |
|------|--------|---------|
| `[ ]` | pending | Not scraped yet |
| `[x]` | done | Markdown written under `docs/` |
| `[-]` | skipped | Intentionally not scraped |
| `[!]` | error | Last scrape failed; retry later |

## How to resume

1. Filter `manifest.json` for `status` `pending` (or `error` to retry).
2. `python scripts/scrape-pending.py --product signal-latest --all-pending`
3. `python scripts/build-index.py --product signal-latest` to refresh this index.

**Content API template:**

```
https://docs.blackduck.com/api/khub/maps/xmDr3Yryk7OYDGb__OGKlg/topics/{contentId}/content
```

## Section overview

| Section | Topics | Pending | Done | Skipped | Error | Local root |
|---------|--------|---------|------|---------|-------|------------|
| Get Started with Black Duck Signal | 18 | 0 | 18 | 0 | 0 | `docs/get-started/` |
| BYOLLM | 8 | 0 | 8 | 0 | 0 | `docs/byollm/` |
| Overview of Black Duck Signal | 1 | 0 | 1 | 0 | 0 | `docs/overview/` |
| Signal Reference Guide | 1 | 0 | 1 | 0 | 0 | `docs/reference/` |
| AI security, data protection, and trust | 1 | 0 | 1 | 0 | 0 | `docs/ai-security/` |
| Signal release notes | 1 | 0 | 1 | 0 | 0 | `docs/release-notes/` |
| Signal FAQ | 1 | 0 | 1 | 0 | 0 | `docs/faq/` |
| Reference guide | 1 | 0 | 1 | 0 | 0 | `docs/reference/` |

## Table of contents

- [x] [Overview of Black Duck Signal](docs/overview/overview-of-black-duck-signal.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/overview-of-black-duck-signal.html)
- [x] [Get Started with Black Duck Signal](docs/get-started/get-started-with-black-duck-signal.md) _(+4)_ · [source](https://docs.blackduck.com/r/signal/black-duck-signal/get-started-with-black-duck-signal.html)
  - [x] [Signal CLI](docs/get-started/signal-cli.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-cli.html)
  - [x] [Coding Assistants](docs/get-started/coding-assistants.md) _(+8)_ · [source](https://docs.blackduck.com/r/signal/black-duck-signal/coding-assistants.html)
    - [x] [Signal and Claude Code](docs/scan-changes/with-a-coding-assistant/black-duck-signal-and-claude-code.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-claude-code.html)
    - [x] [Signal and Codex CLI](docs/get-started/coding-assistants/signal-and-codex-cli.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-codex-cli.html)
    - [x] [Signal and Cursor](docs/get-started/coding-assistants/signal-and-cursor.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-cursor.html)
    - [x] [Signal and Gemini](docs/get-started/coding-assistants/signal-and-gemini.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-gemini.html)
    - [x] [Signal and JetBrains](docs/get-started/coding-assistants/signal-and-jetbrains.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-jetbrains.html)
    - [x] [Signal and Visual Studio with GitHub Copilot](docs/get-started/coding-assistants/signal-and-visual-studio-with-github-copilot.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-visual-studio-with-github-copilot.html)
    - [x] [Signal and VS Code with GitHub Copilot](docs/scan-changes/with-a-coding-assistant/black-duck-signal-and-github-copilot.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-vs-code-with-github-copilot.html)
    - [x] [Signal and Windsurf](docs/get-started/coding-assistants/signal-and-windsurf.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-windsurf.html)
  - [x] [Signal and Code Sight VS Code Extension](docs/scan-changes/in-your-ide/signal-with-code-sight-vs-code-extension.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-code-sight-vs-code-extension.html)
  - [x] [Using Bridge CLI with Signal](docs/get-started/using-bridge-cli-with-signal.md) _(+5)_ · [source](https://docs.blackduck.com/r/signal/black-duck-signal/using-bridge-cli-with-signal.html)
    - [x] [Scan local files](docs/scan-changes/from-the-command-line/perform-a-file-scan.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/scan-local-files.html)
    - [x] [Scan uncommitted changes](docs/scan-changes/from-the-command-line/perform-a-diff-scan.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/scan-uncommitted-changes.html)
    - [x] [Scan changes against a reference branch](docs/scan-changes/from-the-command-line/perform-diff-scan-against-a-reference-branch.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/scan-changes-against-a-reference-branch.html)
    - [x] [Scan a full project](docs/scan-project/full-project-scan-with-sarif-report-only.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/scan-a-full-project.html)
    - [x] [Bridge Reference Guide](docs/get-started/using-bridge-cli-with-signal/bridge-reference-guide.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/bridge-reference-guide.html)
- [x] [BYOLLM](docs/byollm/byollm.md) _(+6)_ · [source](https://docs.blackduck.com/r/signal/black-duck-signal/byollm.html)
  - [x] [Signal's LLM Agents](docs/byollm/signals-llm-agents.md) _(+1)_ · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-s-llm-agents.html)
    - [x] [Agent Capability Requirements](docs/byollm/signals-llm-agents/agent-capability-requirements.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/agent-capability-requirements.html)
  - [x] [BYOLLM configuration from the CLI](docs/byollm/byollm-configuration-from-the-cli.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/byollm-configuration-from-the-cli.html)
  - [x] [BYOLLM configuration using Config Files](docs/byollm/byollm-configuration-using-config-files.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/byollm-configuration-using-config-files.html)
  - [x] [Preflight validation](docs/byollm/preflight-validation.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/preflight-validation.html)
  - [x] [Troubleshooting](docs/byollm/troubleshooting.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/troubleshooting.html)
  - [x] [Environment Variables Index](docs/byollm/environment-variables-index.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/environment-variables-index.html)
- [x] [Signal Reference Guide](docs/reference/signal-reference-guide.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-reference-guide.html)
- [x] [AI security, data protection, and trust](docs/ai-security/ai-security-data-protection-and-trust.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/ai-security-data-protection-and-trust.html)
- [x] [Signal release notes](docs/release-notes/signal-release-notes.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-release-notes.html)
- [x] [Signal FAQ](docs/faq/signal-faq.md) · [source](https://docs.blackduck.com/r/signal/black-duck-signal/signal-faq.html)
- [x] [Local notes: Signal CLI usage and options (field reference)](docs/reference/signal-cli-local-notes.md) · [source](local:///C:/Users/TonyJiang/.claude/skills/bd/Signal/AGENTS.md)

---

*Generated from Fluid Topics map `xmDr3Yryk7OYDGb__OGKlg` (latest). Official docs: [Black Duck Signal](https://docs.blackduck.com/r/signal/black-duck-signal/).*
