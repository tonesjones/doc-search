---
title: "Test internal DAST projects with Polaris Secure Tunnel"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/test-internal-dast-projects-with-polaris-secure-tunnel.html"
content_id: "3NFnv5cw5RtBgkh9NOkusw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:40.641137+00:00"
content_hash: "afe57a2a99098d593a152a6154f9b9d5144d998ebcf1bcb6da9d4f0c7dc5fc4b"
---

# Test internal DAST projects with Polaris Secure Tunnel

You can use Polaris Secure Tunnel, a feature of the Black Duck Bridge, to securely access internal web applications and APIs for the purpose of running DAST tests with Polaris fAST Dynamic. Tests can be started from the Web UI, API, or Bridge CLI.

## Bridge CLI versions

Using Polaris Secure Tunnel requires that you download and install the Bridge CLI. Secure tunnel support differs by Bridge CLI version.

Secure Tunnel functionality was introduced in Bridge CLI version 3.1.0. With this version, secure tunnels are project specific: You need to specify the application and DAST project name when creating a secure tunnel in the Bridge CLI workflow. DAST tests must then be started in either the Polaris Web UI or via the API.

With Bridge CLI version 3.7.0 and later, a secure tunnel is started automatically if you start a DAST test directly from the Bridge CLI, using the `polaris.assessment.types="DAST"` argument.

Bridge CLI version 4.3.0 and later supports shared, tenant-wide secure tunnels that you can reuse across different internal DAST projects. You can create a shared secure tunnel in My Organization > Secure Tunnels and then link it with a DAST project in the Polaris Web UI. In the Bridge CLI workflow, you specify the tunnel name only and Secure Tunnel determines which DAST project to open a secure connection to. The previous project-specific workflow is still supported.

With all Bridge CLI versions, Secure Tunnel functionality works on Mac and Linux only. For a full list of prerequisites, see the Polaris Secure Tunnel section of the Bridge CLI documentation.

This documentation describes both the project-specific and tenant-wide methods of creating a secure tunnel. See the Bridge CLI documentation for more information, the complete list of commands, and additional uses for secure tunnels.

## About Secure Tunnel

With Polaris Secure Tunnel, you can establish a tenant-wide secure TLS connection (port 443) directly to a target web application or API in your private network, without the need to open any ports or allow list Polaris IP ranges.

[image: secure tunnel architecture]

Secure Tunnel uses the [Teleport Access Platform](https://goteleport.com/) for secure and self-service connectivity to private applications. Teleport functionality is integrated with the Bridge CLI (version 3.1.0 and later) and requires no account setup or additional installation. Secure tunnels can be managed in the Polaris UI or the Bridge CLI.

## Prerequisites

Before you begin, make sure that you have:

- Created an access token or service account token. See [Make an access token](../make-an-access-token.md) and [Service Accounts for Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/d9540d417e952b4580e8f0dd120ba6de.topic) for more information.
- Created a DAST project configured as internal (select the Entry Point URL is in a private network option). See [Create DAST projects for web applications and APIs](create-dast-projects-for-web-applications-and-apis.md).
- Downloaded and installed the Bridge CLI. See [Download the Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic).
- Reviewed the Secure Tunnel system requirements. See [Using Polaris secure tunnel](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/ae8dc35e863863d358eb74906b7d6359.topic).

## Create a secure tunnel to a specific internal DAST project

Use the Bridge CLI to open a secure tunnel between Polaris and an internal target in your private network. You can skip this task if you plan to run DAST tests on the target directly from Bridge; see [DAST configuration requirements](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) for details. Note that Bridge does not create DAST projects in Polaris.

1. Sign in to Polaris.
2. Open your terminal.
3. Pass your access token or service account token to the Bridge CLI using an environment variable:

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=YOUR_TOKEN
   ```

   Note: You can use either an access token created in the Polaris UI or a service account token.
4. In your terminal, run the Bridge CLI with the options shown in the following example:

   ```
   bridge-cli --stage polaris-secure-tunnel polaris.application.name="My Application" polaris.project.name="Internal DAST project"
   ```

   - Set the `--stage` argument to `polaris-secure-tunnel`.
   - For `polaris.application.name`, specify an application that is associated with a DAST entitlement.
   - For `polaris.project.name`, specify an internal DAST project.
5. Teleport establishes a *secure tunnel* on port 443 between Polaris and your private network.

   Important: Leave the Secure Tunnel session running in your terminal until your testing is compete.
6. (Optional) Go to **Profiles** > **Edit Profile** to run a connection test.

Now the secure tunnel is open, you can run a DAST test on the project, either from the Polaris web UI or API. When the test is complete, stop the Secure Tunnel session in your terminal, or leave the connection open for further DAST tests on the same internal project.

Note: Each project can have only one active secure tunnel connection at a time. While you leave a Secure Tunnel session open, other tests for the configured project will be routed through that same secure tunnel.

### Create a tenant-wide secure tunnel in Polaris and start DAST tests

With the Secure Tunnels feature of Polaris, you can create and manage secure tunnels directly in the Polaris UI. You still need to use the Bridge CLI to establish a secure connection from your private network to Polaris. Here is an overview of the process:

1. Create a secure tunnel in My Organization > Secure Tunnels.
2. Create a DAST project configured for an internal web application or API target (see [Create DAST projects for web applications and APIs](create-dast-projects-for-web-applications-and-apis.md)). Ensure that you:
   1. Select the Entry Point URL is in a private network option.
   2. Select the name of the secure tunnel from the Tunnel to use dropdown.
3. From your private network, pass your Polaris access token to the Bridge CLI using an environment variable:

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<ACCESS_TOKEN>
   ```
4. Run Bridge CLI to open a secure connection to your Polaris tenant via the secure tunnel you created:

   ```
   bridge-cli --stage polaris-secure-tunnel \
       polaris.serverUrl="https://<YOUR_POLARIS_SERVER>" \
       polaris.tunnel.name="<YOUR_TUNNEL_NAME>"
   ```

   - For `polaris.serverUrl`, specify the base URL for the Polaris server instance, for example `https://polaris.blackduck.com`, `https://poc.polaris.blackduck.com`, `https://ksa.polaris.blackduck.com`, or `https://eu.polaris.blackduck.com`.
   - For `polaris.tunnel.name`, specify the name of the tunnel configured in the Web UI.
5. Start DAST tests on internal projects configured to use the secure tunnel. You can do this from the Web UI, API, or in a separate instance of the Bridge CLI.

   The `polaris-secure-tunnel` process must remain running for the tunnel to stay active.

When a test is started and a secure tunnel is already connected, Bridge CLI will not start it again; instead, the existing connection will be used and will *not* be closed after the scan completes. If the secure tunnel is not connected, Bridge CLI will start the tunnel, scan the target, and close the tunnel once the scan is completed.

## Test a DAST project

Follow these steps to run a DAST test from the Polaris user interface:

1. There's more than one way to start this procedure:
   - Go to Portfolio, select an application, click the three-dot [image: test project 3 dot icon] icon at the end of the project's row, and select New Test.
   - Go to Portfolio, select an application, select a DAST project, and open the DAST Profiles page. Click the three-dot [image: test project 3 dot icon] icon at the end of the profile's row, and select New Test.
   - Go to Tests and select New Test.
2. Select the DAST profile to scan with the Application and Project dropdown menus.

   [image: test dast proj]

   Note: Depending on how you start a test, the Application, Project, and Profile values may already be filled in.
3. (Optional) Select Test Connection.

   This test can take a few minutes to complete and ensures:
   - The Entry Point URL is valid.
   - Polaris can connect to the web application.
   - Polaris can authenticate with the web application.
4. Select Begin Test.

Monitor test progress on the Tests page (accessible from the left-hand navbar). Newer tests appear near the top of the page. Filter tests by date, type, mode, status, and the application, project, or branch/profile tested.

Note: If the test fails, you can download test artifacts for troubleshooting. See [Download test artifacts](../download-test-artifacts.md) for more information.
