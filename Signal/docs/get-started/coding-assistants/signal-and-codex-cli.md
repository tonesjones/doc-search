---
title: "Signal and Codex CLI"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-codex-cli.html"
content_id: "65oFgOMUlhg2AGqVvrDekQ"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.503454+00:00"
---

# Signal and Codex CLI

How to register the Black Duck's MCP server with Codex.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- Codex. If you need to install Codex, see [Codex Documentation](https://developers.openai.com/codex/cli/).
- A Signal Enterprise or Developer subscription.

## 

Follow the steps to add Black Duck's MCP server on the Codex OpenAI extension:

1. Open the NPM configuration file in your personal directory, or create one if it doesn't exist yet.

   Note: For macOS and Linux: `~/.npmrc`.

   For Windows users `%USERPROFILE%\.npmrc` .

   You can also place the `.npmrc` file at the root level of your project directory if you share the access credentials for your LLM across the team.
2. Paste the following code in the NPM configuration file you just created:

   ```
   {
     "mcpServers": {
       "Black Duck": {
         "type": "stdio",
         "command": "npx",
         "args": ["-y", "@blackducksoftware/mcp-server@latest"],
         "env": {
           "BLACKDUCK_MCP_GATEWAY_KEY": "YOUR_LLM_API_KEY"
         }
       }
     }
   }
   ```
3. Replace the API key placeholder in the last alphabetical line with your API key.

   Note:

   Use an environment variable to avoid unintended exposure of your keys, and never commit keys directly in source files.

## Install with a Codex CLI command

You can run this codex command to set the MCP for the project your current working directory points to:

```
codex mcp add black-duck --env BLACKDUCK_MCP_GATEWAY_KEY=$ANTHROPIC_AUTH_TOKEN -- npx @blackducksoftware/mcp-server@latest
```

## Verify your setup

Ask Codex to scan your work for security vulnerabilities using Black Duck MCP server.
