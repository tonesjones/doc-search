---
title: "Coverity MCP Server"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-mcp-server.html"
content_id: "fg3ewbZtSWRxOU56xr55UQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:42.696556+00:00"
---

# Coverity MCP Server

Install the Coverity MCP Server as an npm package or from a
downloadable archive to enable Coverity scans from an AI coding
agent.

As of 2026.6.0, Coverity scans can be run using an MCP server that
integrates with an AI coding agent. The Coverity MCP Server is
available as an npm package or as a downloadable archive.

## Prerequisites

The Coverity MCP Server requires the following:

- Coverity Static Analysis 2026.3.0 or later is installed.
- A valid Coverity Static Analysis license is available.
- A coding agent with MCP server support is available.
- (Optional) Coverity Connect Server — required only to
  accelerate High Fidelity Incremental (HFI) scans.
- (Optional) Node.js 18 or later — required only when using the npm
  package.

Supported operating systems:

- Linux AMD64 and ARM64
- Windows AMD64
- macOS AMD64 and ARM64

## Install via npm

To install the Coverity MCP Server using npm, run the following
command:

```
npx -y @black-duck/coverity-mcp-server -version
```

To view the README documentation for the MCP server, run the following
command:

```
npm view @black-duck/coverity-mcp-server readme
```

The README documentation contains instructions for configuring the MCP server
with a coding agent.

## Install via archive

To download the MCP server archive, run the following command:

```
curl -O https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/coverity-mcp-server/coverity-mcp-server-linux64-2026.6.0.zip
```

Replace `linux64` in the filename with the moniker for your
operating system:

| Operating system | Moniker |
| --- | --- |
| Linux AMD64 | `linux64` |
| Linux ARM64 | `linux-arm64` |
| macOS AMD64 | `macosx` |
| macOS ARM64 | `macos-arm` |
| Windows AMD64 | `win64` |

After downloading the archive, extract it by running the following command:

```
unzip coverity-mcp-server-linux64-2026.6.0.zip
```

Replace `linux64` with the appropriate moniker for your
operating system.

Follow the instructions in the README.md file in the
extracted archive to configure the MCP server with a coding agent.
