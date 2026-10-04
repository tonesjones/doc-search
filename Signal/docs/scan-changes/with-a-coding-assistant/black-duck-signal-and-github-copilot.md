---
title: "Signal and VS Code with GitHub Copilot"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-vs-code-with-github-copilot.html"
content_id: "yJEbl~KQUC2yDwoSiqgacg"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:50.108378+00:00"
---

# Signal and VS Code with GitHub Copilot

How to integrate Signal in VS Code with GitHub Copilot.

Note: Available with: **Signal Developer** and **Signal Enterprise**.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- Visual Studio Code. If you need to download Visual Studio Code, see [Visual Studio Code download](https://code.visualstudio.com/download?_exp_download=fb315fc982).
- GitHub Copilot plugin. If you don’t have GitHub Copilot in Visual Studio Code, use the Extensions Marketplace to install it. For more details, see [GitHub Copilot - Getting Started](https://docs.github.com/en/copilot/get-started/quickstart).
- A Signal Enterprise or Developer subscription.

Follow the steps to add Black Duck's MCP server to VS Code:

1. In VS Code, open the Command Palette by pressing Command + Shift + P.
2. Search for: `"MCP: Add Server"` and select it.
3. Select `Command (stdio)` as MCP server type.
4. When you see "Enter Command," enter `npx @black-duck/mcp-server@latest` and press enter.
5. When you see "Enter server ID," give the server a name. We suggest black-duck.
6. Choose whether the MCP server is available globally or only in the current workspace.
7. In the mcp.json file, add the following configuration.

   ```
   {
     "servers": {
       "black-duck": {
         "type": "stdio",
         "command": "npx",
          "args": ["@black-duck/mcp-server@latest"],
         "env" : {
           "BLACKDUCK_MCP_GATEWAY_KEY": "YOUR_LLM_API_KEY",
           "BLACKDUCK_MCP_LOG_LEVEL": "info" 
       }
       }
     }
   }
   ```

   About this code example:

   - Replace the API key placeholder with your API key.
   - If you see a link that says "Start" after you have finished editing the file, click it.
   - When troubleshooting, set `BLACKDUCK_MCP_LOG_LEVEL` to "debug."

## Verify your setup

1. Open a new chat window.
   - Shift + Command + I on MacOS or Linux
   - Shift + Alt + I on Windows
2. Ask Copilot to scan some of your code using Black Duck.
