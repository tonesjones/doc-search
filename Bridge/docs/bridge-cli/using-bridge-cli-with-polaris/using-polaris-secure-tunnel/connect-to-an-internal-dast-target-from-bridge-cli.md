---
title: "Connect to an internal DAST target from Bridge CLI"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/connect-to-an-internal-dast-target-from-bridge-cli.html"
content_id: "LAqlJet_AOwzEjLu0kJVpQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:06.119486+00:00"
---

# Connect to an internal DAST target from Bridge CLI

Polaris Secure Tunnel enables teams to securely connect to internal web applications and APIs (inside a private network) for the purposes of running dynamic tests using [Polaris fAST Dynamic](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/72b5b3601c618e30303c8fa224dca111.topic) (DAST). This document explains how to run Secure Tunnel from the Bridge CLI, establishing a secure TLS connection between Polaris and an internal target for tests run from the Polaris UI. To learn more, see [Test an internal web application or API with Polaris Secure Tunnel](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/72b5b3601c618e30303c8fa224dca111.topic) in the Polaris Platform documentation.

Tip: When tests on internal targets are started using the Bridge CLI (available in Bridge CLI version 3.7.0 or later), Bridge establishes a secure tunnel automatically. See DAST configuration requirements for more information.

## Prerequisites

- The following reading is recommended before starting:
  - Consult the *Polaris Secure Tunnel* documentation to understand functionality and system requirements.
- A Polaris access token has been created. See [Make an access token](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0d97d272fb42796be0f9f52928a17d57.topic) for instructions
- A secure tunnel has been created in the Polaris web UI under My Organization > Secure Tunnels.
- A DAST project has been created for an internal target (web application or API) in the Polaris UI:

  - The Entry Point URL is in a private network check-box must have been selected when creating the project. For instructions, see the [fAST Dynamic documentation](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/72b5b3601c618e30303c8fa224dca111.topic).
  - The name of the secure tunnel has been assigned to the DAST project's entry point URL in the Polaris UI.
- The tunnel must be connected using the Polaris secure tunnel workflow, otherwise Bridge CLI will log an error as `Tunnel <Tunnel-name> is not connected. Shared tunnels must be started separately using the Polaris Secure Tunnel Workflow`.
- Bridge CLI (version 4.3.0 or higher) is installed on a local machine (or a virtual machine or other runner that both has access to the internal DAST target and can reach the Polaris instance on port 443).

## Instructions

1. Ensure that a secure tunnel has been created using the Bridge CLI `polaris-secure-tunnel` workflow as described in Create a secure tunnel using Bridge CLI.
2. Create a new test on the internal DAST project from the Polaris user interface or via the API.

   Note: The tunnel session must remain open until the scan is complete

Note: With Bridge 4.3.0 and later, users can create a secure tunnel from the Polaris Web UI and associate it with a DAST application or project.

- Shared tunnels must be started separately using the Polaris Secure Tunnel Workflow"
