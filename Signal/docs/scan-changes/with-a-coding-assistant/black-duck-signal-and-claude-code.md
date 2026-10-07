---
title: "Signal and Claude Code"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-claude-code.html"
content_id: "ixkusxIoyIQQXA5nwicHGg"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:50.062440+00:00"
---

# Signal and Claude Code

How to register the Black Duck MCP server with Claude.

Note: Available with: **Signal Developer** and **Signal Enterprise**.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- Claude Code. If you need to install Claude, see [Claude Code - Quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart).
- A Signal Enterprise or Developer subscription.

Follow the steps to register Black Duck's MCP server for Claude Code:

1. Install with CLI commands

   ```
   $ claude mcp add black-duck --transport stdio --scope user --env BLACKDUCK_MCP_GATEWAY_KEY=YOUR_LLM_API_KEY -- npx @black-duck/mcp-server@latest
   ```

   About this codeblock:

   - This two-part instruction stores the MCP configuration in Claude’s system, then uses NPX to install and run the Black Duck MCP server and establish communication between the two.
   - Be sure to substitute your API key environment variable after `key=`.
   - Including `--scope user` sets the MCP at the *user level* and not system-wide. This prevents other users from accessing the MCP server with your credentials.

## Verify your setup

1. Start Claude Code.

   ```
   $ claude
   ```
2. Ask Claude to scan some of your files using Black Duck.

   [image: A screenshot of Claude Code with user input that asks Claude: "Scan showtime.py for security vulnerabilities using Black Duck."]

**Alternative installation methods**

If this method didn't work for you, or you prefer a different method, see [installing MCP servers](https://docs.anthropic.com/en/docs/claude-code/mcp#installing-mcp-servers).
