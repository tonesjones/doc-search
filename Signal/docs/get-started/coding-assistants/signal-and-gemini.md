---
title: "Signal and Gemini"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-gemini.html"
content_id: "MLHjCljNoqFGucMPEZxovw"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.535436+00:00"
---

# Signal and Gemini

How to register the Black Duck's MCP server with Gemini CLI.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- Gemini CLI. If you need to install Gemini CLI, see [Gemini Installation](https://geminicli.com/docs/get-started/installation/).
- A Signal Enterprise or Developer subscription.

Follow the steps to add Black Duck's MCP server with Gemini CLI:

1. Create or edit the file `~/.gemini/settings.json`. 

   Tip: You can also add `.gemini/settings.json` in the root directory of your project, if you want to share the configuration.
2. Add the following JSON snippet to the file:

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
3. Replace the API key placeholder (`YOUR_LLM_API_KEY`) in the last alphabetical line with your API key.

   Note:

   Use an environment variable to avoid unintended exposure of your keys, and never commit keys directly in source files.

If you have any questions, see the Gemini documentation for [Gemini MCP Server Documentation](https://geminicli.com/docs/tools/mcp-server/#how-to-set-up-your-mcp-server).
