---
title: "Signal and Cursor"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-cursor.html"
content_id: "xfJP0kGn4qmGIC3PUpLwdQ"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.520471+00:00"
---

# Signal and Cursor

How to register the Black Duck's MCP server with Cursor.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- Cursor. If you need to install Cursor, see [Cursor Documentation](https://www.cursor.com/).
- A Signal Enterprise or Developer subscription.

Follow the steps to add Black Duck's MCP server in Cursor:

1. In Cursor, navigate to Settings > Tools & MCP > New MCP Server.
2. Paste the following code:

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

**Alternative Installation Methods**

You can use other methods that best suit your operating system and local development environment. To add an MCP Server in Cursor, see [Cursor MCP Documentation](https://cursor.com/docs/context/mcp).
