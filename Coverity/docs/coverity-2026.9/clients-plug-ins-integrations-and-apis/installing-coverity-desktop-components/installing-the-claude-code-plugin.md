---
title: "Installing the Claude Code plugin"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/installing-the-claude-code-plugin.html"
content_id: "a_Dffg7hmQ4xkDaYINt99g"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:17.404530+00:00"
---

# Installing the Claude Code plugin

Install and configure the Claude Code plugin to integrate Claude Code with Coverity
Connect and Sigma.

Before installing the plugin, ensure that:

- You have Claude Code installed.
- You have access to a Coverity Connect 2026.9 instance.
- You know the name of the Coverity Connect stream associated with your
  codebase.
- A browser is available on the machine where Claude Code is running.

Note: The plugin opens a browser on the machine where Claude Code is running to
authenticate with Coverity Connect. This authentication workflow does not support
remote or headless environments.

1. Download the Claude Code plugin distribution from the Black Duck
   repository.

   Go to [Claude Code plugin downloads](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/blackduck-claude-code/latest).
2. Extract the downloaded distribution archive.

   The archive contains the local Claude Code marketplace and the Coverity
   plugin files.
3. Add the local marketplace to Claude Code.

   From within a Claude Code session, run:

   ```
   /plugin marketplace add /path/to/blackduck-claude-code
   ```

   Alternatively, from the command line, run:

   ```
   claude plugin marketplace add /path/to/blackduck-claude-code
   ```
4. Install the Coverity plugin.

   From within a Claude Code session, run:

   ```
   /plugin install coverity@blackduck-local
   ```

   Alternatively, from the command line, run:

   ```
   claude plugin install coverity@blackduck-local
   ```
5. Set up the plugin.

   From within a Claude Code session, enter a request in the
   following format:

   ```
   Setup the Coverity plugin: https://my-connect-server.com, my-stream-name
   ```

   Replace the example values with the URL of your Coverity
   Connect instance and the name of the stream associated
   with your codebase.

   During setup:
   - A browser opens so that you can authenticate with Coverity Connect and
     grant Full API Access.
   - The plugin downloads Sigma and the applicable workflow configuration
     from Coverity Connect.
6. Start a new Claude Code session.

   Use one of the following methods:
   - Run `/clear` to clear the current conversation and start
     a new session.
   - Run `/compact` to compact the current conversation and
     restart the session without exiting Claude Code.
   - Exit and restart Claude Code.

   Important: You must restart the session after setup. The
   plugin adds its workflow instructions when the session starts, so the
   instructions do not apply to the session in which you ran setup.

The Claude Code plugin is installed and connected to Coverity Connect. The plugin
can use Sigma and the workflow configuration associated with the selected stream.
