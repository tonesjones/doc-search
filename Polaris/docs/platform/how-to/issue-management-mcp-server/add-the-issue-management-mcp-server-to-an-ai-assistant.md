---
title: "Add the Issue Management MCP server to an AI assistant"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/add-the-issue-management-mcp-server-to-an-ai-assistant.html"
content_id: "zXYe4JB_T63r75Sv8kXOSQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:24.480233+00:00"
content_hash: "2b507fa1d67ce3310732e46f498def15d445fd380805ee8ff335fec607f13750"
---

# Add the Issue Management MCP server to an AI assistant

After you add the Issue Management MCP server to an AI assistant, you can query your Polaris security findings using natural language.

The Issue Management MCP server is hosted in Polaris and can be added to AI assistants that support the Model Context Protocol (MCP). No installation or deployment is required—you simply configure your AI assistant (client) to connect to your Polaris instance.

The following procedures describe how to add the Issue Management MCP server to supported AI assistants.

## Add the Issue Management MCP server to Claude Code

Use the Claude Code CLI to connect to the Issue Management MCP server with your Polaris access token.

Before you begin:

- Ensure you have Claude Code installed on your system.
- Create a Polaris access token for authentication. See [Make an access token](../make-an-access-token.md) for more information.

Use the Claude Code CLI to connect to the Issue Management MCP server hosted on your Polaris instance.

1. Run the following command to add the MCP server.

   ```
   claude mcp add polaris-issue-management-mcp-server "https://polaris.blackduck.com/api/mcp" --transport http -H "Api-Token:<token>"
   ```

   If necessary, replace `https://polaris.blackduck.com/api/mcp` with your Polaris instance's URL (`https://poc.polaris.blackduck.com/api/mcp`, `https://eu.polaris.blackduck.com/api/mcp`, or `https://ksa.polaris.blackduck.com/api/mcp`).

   Replace `<token>` with your Polaris access token.
2. Start Claude Code.
3. Query the MCP server to verify the connection. 

   Ask Claude: `"What's my portfolio ID?"`

   If the server is configured correctly, Claude will invoke the `get_portfolio_id` tool and return your organization's portfolio identifier.

The Issue Management MCP server is now connected to Claude Code. You can query your security findings using natural language queries. For example:

- "Show me the most common critical vulnerabilities in my portfolio"
- "What's the most vulnerable project in my portfolio?"
- "List my open security issues"
- "How do I fix issue [issue-id]?"

Note: For more information on working with MCP servers and Claude Code, see [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp#option-2%3A-add-a-remote-sse-server).

## Add the Issue Management MCP server to GitHub Copilot

Update your MCP configuration file in VS Code to connect to the Issue Management MCP server with your Polaris access token.

Before you begin:

- Ensure you have VS Code with the GitHub Copilot extension installed.
- Create a Polaris access token for authentication. See [Make an access token](../make-an-access-token.md) for more information.

GitHub Copilot in VS Code uses an `mcp.json` configuration file to connect to MCP servers. You can configure the connection at the workspace level or user level.

1. Access the `mcp.json` configuration file.

   Choose one of the following options:

   - **Workspace-level configuration:** Create a file named `mcp.json` in the `.vscode` directory at your workspace root. This configuration applies only to the current workspace.
   - **User-level configuration:** Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and select MCP: Open User Configuration. This configuration applies to all workspaces.
2. Add the following configuration to the `mcp.json` file.

   ```
   {
     "servers": {
       "polaris-issue-management-mcp-server": {
         "type": "http",
         "url": "https://polaris.blackduck.com/api/mcp",
         "headers": {
           "Api-Token": "${input:polaris-api-token}"
         }
       }
     },
     "inputs": [
       {
         "id": "polaris-api-token",
         "type": "promptString",
         "description": "Polaris API Token",
         "password": true
       }
     ]
   }
   ```

   If necessary, replace `https://polaris.blackduck.com/api/mcp` with your Polaris instance's URL (`https://poc.polaris.blackduck.com/api/mcp`, `https://eu.polaris.blackduck.com/api/mcp`, or `https://ksa.polaris.blackduck.com/api/mcp`).
3. Restart VS Code or reload the window to apply the configuration.

   Tip: To reload the window, open the Command Palette and select Developer: Reload Window.
4. Query the MCP server to verify the connection.

   The first time the MCP server starts, VS Code may prompt you to enter your Polaris API token.

   Open GitHub Copilot chat and ask: `"What's my portfolio ID?"`

   If the server is configured correctly, GitHub Copilot will invoke the `get_portfolio_id` tool and return your organization's portfolio identifier.

The Issue Management MCP server is now connected to GitHub Copilot. You can query your security findings using natural language queries. For example:

- "Show me the most common critical vulnerabilities in my portfolio"
- "What's the most vulnerable project in my portfolio?"
- "List my open security issues"
- "How do I fix issue [issue-id]?"

Note: For more information on configuring MCP servers in VS Code, see [Add and manage MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).
