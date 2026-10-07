---
title: "Signal and Visual Studio with GitHub Copilot"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-visual-studio-with-github-copilot.html"
content_id: "kGoc2aLOgnL2lv5hMYw4jg"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.581321+00:00"
---

# Signal and Visual Studio with GitHub Copilot

How to register the Black Duck's MCP server in Visual Studio with GitHub Copilot.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- Visual Studio. If you need to download Visual Studio, see [Visual Studio download](https://visualstudio.microsoft.com/downloads/).
- GitHub Copilot plugin. If you don’t have GitHub Copilot in Visual Studio, use the Extensions Marketplace to install it. For more details, see the official [GitHub Copilot - Getting Started](https://docs.github.com/en/copilot/get-started/quickstart).
- A Signal Enterprise or Developer subscription.

Follow the steps to add Black Duck's MCP server in Visual Studio with GitHub Copilot:

1. In Visual Studio, access the Copilot Chat window by pressing Control + \, then press C.
2. Select the Select tools and skills button.

   [image: image]
3. Click on the + button at the top right of the menu.

   [image: image]
4. Select Add custom MCP server.
5. Enter the following information:

   - Server ID: blackduck-mcp-server
   - Type: stdio
   - Command: `npx
     @black-duck/mcp-server@latest`
   - Environment Variables: BLACKDUCK_MCP_GATEWAY_KEY = YOUR_LLM_API_KEY

     Note: Replace the API key placeholder with your API key.
6. Click Save to save the MCP configuration in `$HOME/.mcp.json`.

## Verify your setup

1. Verify if the Black Duck MCP server is enabled in the Select tools and skills menu.

   [image: image]
2. Run a full scan by typing the following command into Copilot Chat:

   ```
   Scan my code with Black Duck
   ```
3. Run an incremental scan by typing the following code into Copilot Chat:

   ```
   Scan my code changes with Black Duck
   ```

If you need additional support, see [Visual Studio MCP Server Documentation](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=visualstudio#options-for-adding-an-mcp-server).
