---
title: "Create a secure tunnel using Bridge CLI"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/create-a-secure-tunnel-using-bridge-cli.html"
content_id: "tQT0QGztOhw9W7eNtpI2fA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:05.500668+00:00"
---

# Create a secure tunnel using Bridge CLI

Establish an outbound-only encrypted connection from a machine inside a private network to the Polaris cloud platform by running Bridge CLI with the `polaris-secure-tunnel` workflow.

A Polaris secure tunnel is an outbound-only encrypted connection from a machine inside a private network to the Polaris cloud platform. It is established by running Bridge CLI with the `polaris-secure-tunnel` workflow on a machine that can reach the internal resources.

Once the tunnel is running, Polaris can communicate with resources inside the private network.

## Prerequisites

- The following reading is recommended before starting this task:
  - Consult the *Polaris Secure Tunnel* documentation to understand functionality and system requirements.
- A Polaris access token has been created. See [Make an access token](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0d97d272fb42796be0f9f52928a17d57.topic) for instructions.
- A secure tunnel has been created in the Polaris web UI under My Organization > Secure Tunnels.
- Bridge CLI (version 4.3.0 or higher) is installed on a local machine (or a virtual machine or other runner that both has access to the internal DAST target and can reach the Polaris instance on port 443).

## Instructions

1. Pass the Polaris access token to Bridge CLI using an environment variable:

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<your-access-token>
   ```
2. Run Bridge CLI with the `polaris-secure-tunnel` workflow:

   ```
   bridge-cli --stage polaris-secure-tunnel \
       polaris.serverUrl="https://<your-polaris-server>" \
       polaris.tunnel.name="<your-tunnel-name>"
   ```

   - For `polaris.serverUrl`, specify the base URL for the Polaris server instance, for example `https://polaris.blackduck.com`, `https://poc.polaris.blackduck.com`, `https://ksa.polaris.blackduck.com`, or `https://eu.polaris.blackduck.com`.
   - For `polaris.tunnel.name`, specify the name of the tunnel configured in the Polaris web UI.

   If the command is successful, Bridge CLI:

   1. Connects to the specified Polaris server instance.
   2. Connects to the specified named Teleport instance in Polaris.
   3. Downloads the Teleport agent and configuration to the same location that Bridge CLI is running from.
   4. Runs the Teleport agent with the configuration file.
   5. Establishes a secure TLS tunnel on port 443 between the specified Polaris instance and the internal resource in the private network.
3. Bridge CLI starts a new Teleport process each time the `polaris-secure-tunnel` workflow is executed, rather than reusing an existing process.
4. Bridge CLI will log an error message if a tunnel is not found with a matching name.

An outbound-only encrypted connection is established. The process must remain running for the tunnel to stay active.
