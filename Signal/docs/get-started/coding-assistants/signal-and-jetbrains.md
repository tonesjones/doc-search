---
title: "Signal and JetBrains"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-and-jetbrains.html"
content_id: "ott~fFzYya3Nqp3i6mX24g"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.552729+00:00"
---

# Signal and JetBrains

How to register the Black Duck's MCP server with JetBrains AI Assistant.

**Prerequisites:**

- Node.js 24 or higher. If you need to download Node.js, see [Node.js download](https://nodejs.org/en/download).
- JetBrains in any compatible IDE. If you need to install JetBrains, see [JetBrains Documentation](https://www.jetbrains.com/help/idea/ai-assistant-in-jetbrains-ides.html).
- A Signal Enterprise or Developer subscription.

Note: The following instructions are for the JetBrains IDE, however JetBrains AI Assistant is compatible with other IDEs, such as IntelliJ IDEA, WebStorm, PyCharm, etc.

Follow the steps to add Black Duck's MCP server in JetBrains:

1. In the JetBrains IDE, Navigate to Settings/Preferences > Tools > AI Assistant > Model Context Protocol (MCP).
2. Click on the + button.
3. Add a new MCP server with the following configuration:

   ```
    "Black Duck": {
         "type": "stdio",
         "command": "npx",
         "args": ["-y", "@blackducksoftware/mcp-server@latest"],
         "env": {
           "BLACK_DUCK_OPENAI_API_KEY": "YOUR_AUTH_TOKEN"
         }
       }
   ```

   Note: You may need to specify the full executable path if `npx` is not on your system path.
4. Replace the authentication token placeholder with your token.

## Verify your setup

To verify if your setup is working correctly, follow the steps:

1. Reload your IDE window.
2. Check the Status column in the MCP configuration.
3. Check the listing of available tools.

   Note: The MCP server may automatically prompt for trust and authentication when first accessed.

If you have any questions, see [JetBrains MCP Documentation](https://www.jetbrains.com/help/ai-assistant/mcp.html).
