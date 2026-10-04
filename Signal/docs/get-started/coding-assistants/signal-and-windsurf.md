---
title: "Signal and Windsurf"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-windsurf.html"
content_id: "M9QKObrq2p30Hbe8vmi1ew"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.600759+00:00"
---

# Signal and Windsurf

How to register the Black Duck's MCP server with Windsurf.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- Windsurf. If you need to install Windsurf, see [Windsurf Documentation](https://codeium.com/windsurf).
- A Signal Enterprise or Developer subscription.

Follow the steps to add Black Duck's MCP server on Windsurf:

1. In Windsurf, navigate to Windsurf Settings > Cascade > MCP Servers.
2. Edit the `mcp_config.json` file.
3. Paste the following code in the file:

   ```
   {
     "mcpServers": {
       "Black Duck": {
         "command": "npx",
         "args": ["-y", "@blackducksoftware/mcp-server@latest"],
         "env": {
           "BLACKDUCK_MCP_GATEWAY_KEY": "YOUR_LLM_API_KEY"
         }
       }
     }
   }
   ```
4. Replace the API key placeholder in the last alphabetical line with your API key.

   Note:

   Use an environment variable to avoid unintended exposure of your keys, and never commit keys directly in source files.

## Alternative installation methods

You can use different methods to install Black Duck's MCP server. To see alternative methods, see [Windsurf MCP Documentation](https://docs.windsurf.com/windsurf/cascade/mcp).

**Installation with Node.js and `npx`**

1. Navigate to `~/.codeium/windsurf/mcp_config.json`.
2. If the file doesn't exist, create one. If it exists, edit the file and paste the following code:

   ```
   {
     "mcpServers": {
       "Black Duck": {
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
