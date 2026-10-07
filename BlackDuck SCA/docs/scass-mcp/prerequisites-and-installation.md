---
title: "Prerequisites & Installation"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/prerequisites-installation.html"
content_id: "DgJGMtjH38Eb8y0N~7n4vg"
version: "latest"
section: "SCASS MCP Server"
scraped_at: "2026-10-04T23:32:44.334808+00:00"
content_hash: "007aedf6fcad85228daf45aced60a2905de0ea82225cbed9d2ad4da2bdbeb7f0"
---

# Prerequisites & Installation

## Prerequisites

| Requirement | Details |
| --- | --- |
| **Black Duck SCA instance** | A running instance with a user account and API token. |
| **Python 3.13+** | Required to run the MCP server. |
| **uv** | Python package manager (used via `uvx`). |
| **Java 11+** | *Optional* — required only for source scanning via Detect. |

## Supported Clients

| Client | Setup Method |
| --- | --- |
| Claude Code | CLI command |
| Claude Desktop | JSON config file (UI) |
| VS Code | `.vscode/mcp.json` |
| GitHub Copilot | CLI command (requires resources-as-tools workaround) |
| Cursor | `.vscode/mcp.json` (same as VS Code) |

## Installation & Setup

**Claude Code (CLI)**

```
claude mcp add blackduck-bdsca-mcp \   
  --env BLACKDUCK_BDSCA_URL=https://<your-instance-url> \   
  --env BLACKDUCK_BDSCA_TOKEN=<api-token> \   
  -- uvx \ 
  --managed-python --python 3.13 \   
  --from 'blackduck-sca-mcp' bdsca
```

**Claude Desktop**

Add via the UI, or ensure your config file contains:

```
{
  "managedMcpServers": [
    {
      "name": "blackduck-bdsca-mcp",
      "source": "user",
      "transport": "stdio",
      "command": "/bin/uvx",
      "args": [
        "--managed-python",
        "--python", "3.13",
        "--from", "blackduck-sca-mcp", "bdsca"
      ],
      "env": {
        "BLACKDUCK_BDSCA_URL": "https://<your-instance-url>",
        "BLACKDUCK_BDSCA_TOKEN": "<api-token>"
      }
    }
  ]
}
```

**VS Code**

Add to .vscode/mcp.json in your project:

```
{
  "servers": {
    "blackduck-bdsca-mcp": {
      "command": "uvx",
      "args": [
        "--managed-python",
        "--python", "3.13",
        "--from", "blackduck-sca-mcp", "bdsca"
      ],
      "env": {
        "BLACKDUCK_BDSCA_URL": "https://<your-instance-url>",
        "BLACKDUCK_BDSCA_TOKEN": "<api-token>"
      }
    }
  }
}
```

**GitHub Copilot**

GitHub Copilot CLI currently does not implement the full MCP spec — it is missing
handling of MCP resources. To work around this, expose resources as tools by setting
`BLACKDUCK_MCP_ENABLE_RESOURCES_AS_TOOLS=true`.

```
copilot mcp add blackduck-bdsca-mcp \
  --env BLACKDUCK_BDSCA_URL=https://<your-instance-url> \
  --env BLACKDUCK_BDSCA_TOKEN=<api-token> \
  --env BLACKDUCK_MCP_ENABLE_RESOURCES_AS_TOOLS=true \
  -- uvx \
  --managed-python --python 3.13 \
  --from 'blackduck-sca-mcp' bdsca
```

**Cursor**

Use the same .vscode/mcp.json configuration as VS Code above.
