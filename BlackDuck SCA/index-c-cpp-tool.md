# Black Duck C/CPP Tool Documentation Index

> Auto-generated catalog for local RAG. Do not hand-edit topic rows — update `sources/c-cpp-tool-latest/manifest.json` statuses and run `python scripts/build-index.py --product c-cpp-tool-latest`.

## Corpus status

| Field | Value |
|-------|-------|
| Product | Black Duck C/CPP Tool |
| Product key | `c-cpp-tool-latest` |
| Version | **latest** |
| Map ID | `3JcuocdfP6Yh0iupxpNOwQ` |
| TOC nodes | **22** |
| Progress | **22/22 done** (100.0%) · 0 pending · 0 skipped · 0 error |
| Last index build | 2026-10-04T23:27:44.353213+00:00 |
| Manifest | [sources/c-cpp-tool-latest/manifest.json](sources/c-cpp-tool-latest/manifest.json) |
| Raw TOC | [sources/c-cpp-tool-latest/toc.json](sources/c-cpp-tool-latest/toc.json) |
| Docs roots | `docs/c-cpp-tool/`, `docs/knowledgebase-vulnerability-feed-server/`, `docs/scass-mcp/` |

### Status legend

| Mark | Status | Meaning |
|------|--------|---------|
| `[ ]` | pending | Not scraped yet |
| `[x]` | done | Markdown written under `docs/` |
| `[-]` | skipped | Intentionally not scraped |
| `[!]` | error | Last scrape failed; retry later |

## How to resume

1. Filter `manifest.json` for `status` `pending` (or `error` to retry).
2. `python scripts/scrape-pending.py --product c-cpp-tool-latest --all-pending`
3. `python scripts/build-index.py --product c-cpp-tool-latest` to refresh this index.

**Content API template:**

```
https://docs.blackduck.com/api/khub/maps/3JcuocdfP6Yh0iupxpNOwQ/topics/{contentId}/content
```

## Section overview

| Section | Topics | Pending | Done | Skipped | Error | Local root |
|---------|--------|---------|------|---------|-------|------------|
| Black Duck C/CPP Tool | 15 | 0 | 15 | 0 | 0 | `docs/c-cpp-tool/black-duck-c-cpp-tool/` |
| SCASS MCP Server | 6 | 0 | 6 | 0 | 0 | `docs/scass-mcp/` |
| Black Duck Tools | 1 | 0 | 1 | 0 | 0 | `docs/c-cpp-tool/black-duck-tools/` |

## Table of contents

- [x] [Black Duck Tools](docs/c-cpp-tool/black-duck-tools.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/black-duck-tools.html)
- [x] [Black Duck C/CPP Tool](docs/c-cpp-tool/black-duck-c-cpp-tool.md) _(+9)_ · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/black-duck-c/cpp-tool.html)
  - [x] [Black Duck C/CPP tool release notes](docs/c-cpp-tool/black-duck-c-cpp-tool/black-duck-c-cpp-tool-release-notes.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/black-duck-c/cpp-tool-release-notes.html)
  - [x] [Black Duck C/CPP tool overview](docs/c-cpp-tool/black-duck-c-cpp-tool/black-duck-c-cpp-tool-overview.md) _(+2)_ · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/black-duck-c/cpp-tool-overview.html)
    - [x] [Black Duck C/CPP tool quickstart guide](docs/c-cpp-tool/black-duck-c-cpp-tool/black-duck-c-cpp-tool-overview/black-duck-c-cpp-tool-quickstart-guide.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/black-duck-c/cpp-tool-quickstart-guide.html)
    - [x] [How does the tool run?](docs/c-cpp-tool/black-duck-c-cpp-tool/black-duck-c-cpp-tool-overview/how-does-the-tool-run.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/how-does-the-tool-run-.html)
  - [x] [Supported platforms](docs/c-cpp-tool/black-duck-c-cpp-tool/supported-platforms.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/supported-platforms.html)
  - [x] [Installation](docs/c-cpp-tool/black-duck-c-cpp-tool/installation.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/installation.html)
  - [x] [Executing the Black Duck C/CPP tool](docs/c-cpp-tool/black-duck-c-cpp-tool/executing-the-black-duck-c-cpp-tool.md) _(+1)_ · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/executing-the-black-duck-c/cpp-tool.html)
    - [x] [Configuring a yaml file](docs/c-cpp-tool/black-duck-c-cpp-tool/executing-the-black-duck-c-cpp-tool/configuring-a-yaml-file.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/configuring-a-yaml-file.html)
  - [x] [API token](docs/c-cpp-tool/black-duck-c-cpp-tool/api-token.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/api-token.html)
  - [x] [Bazel](docs/c-cpp-tool/black-duck-c-cpp-tool/bazel.md) _(+1)_ · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/bazel.html)
    - [x] [Bazel setup](docs/c-cpp-tool/black-duck-c-cpp-tool/bazel/bazel-setup.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/bazel-setup.html)
  - [x] [The BOM](docs/c-cpp-tool/black-duck-c-cpp-tool/the-bom.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/the-bom.html)
  - [x] [Frequently asked questions](docs/c-cpp-tool/black-duck-c-cpp-tool/frequently-asked-questions.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/frequently-asked-questions.html)
- [x] [SCASS MCP Server](docs/scass-mcp/scass-mcp-server.md) _(+5)_ · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/scass-mcp-server.html)
  - [x] [Overview & Capabilities](docs/scass-mcp/overview-and-capabilities.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/overview-capabilities.html)
  - [x] [Prerequisites & Installation](docs/scass-mcp/prerequisites-and-installation.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/prerequisites-installation.html)
  - [x] [Configuration & Security](docs/scass-mcp/configuration-and-security.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/configuration-security.html)
  - [x] [Using the MCP Server](docs/scass-mcp/using-the-mcp-server.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/using-the-mcp-server.html)
  - [x] [Troubleshooting](docs/scass-mcp/troubleshooting.md) · [source](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/troubleshooting.html)
  - [x] [Local notes: command-line flags and workflows (community reference)](docs/c-cpp-tool/black-duck-c-cpp-tool/local-notes-command-line-flags-and-workflows.md) · [source](local:///C:/TestCode/bdsca-c-cpp-demo/bd-ccpp-scanner.md)

---

*Generated from Fluid Topics map `3JcuocdfP6Yh0iupxpNOwQ` (latest). Official docs: [Black Duck C/CPP Tool](https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/).*
