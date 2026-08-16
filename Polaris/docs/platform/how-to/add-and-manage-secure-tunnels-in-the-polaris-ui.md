---
title: "Add and manage secure tunnels in the Polaris UI"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/add-and-manage-secure-tunnels-in-the-polaris-ui.html"
content_id: "gX_1rchgT4VdrlCPTSPZyw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:06.499896+00:00"
content_hash: "06c952fe94cd94b976c50db12314bcb634c5ed06319d25828323e352910afd79"
---

# Add and manage secure tunnels in the Polaris UI

Use Polaris Secure Tunnel, a feature of the Black Duck Bridge, to securely access web applications, APIs, and
on-premises services in your private network. Secure tunnels are outbound-only encrypted
connections from a machine inside a private network to Polaris,
established by running Bridge with the `polaris-secure-tunnel` workflow. Use secure tunnels to access DAST targets (web applications and APIs), on-premise SCM servers, and integration URLs that are only accessible on a private network.

## Prerequisites

Before you begin, make sure that you have:

- Installed Bridge CLI version 4.3.0 or later. See [Download the Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic).
- Reviewed the Secure Tunnel system requirements.
  See [Using Polaris secure tunnel](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/ae8dc35e863863d358eb74906b7d6359.topic).
- Created an access token or service account token. See [Make an access token](make-an-access-token.md), [Service Accounts for Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/d9540d417e952b4580e8f0dd120ba6de.topic), and  for more
  information.

## Add a secure tunnel

Create your secure tunnel in Polaris so it can be
associated with internal DAST projects and on-premises SCM integrations.

1. Go to My Organization > Secure Tunnels.
2. Click Create Tunnel.
3. Enter a Name for the secure tunnel. You must reference this name when running the `polaris-secure-tunnel` workflow in the Bridge CLI.
4. (Optional) Enter a Description.

   The description is displayed alongside the tunnel name in the tunnel
   list.
5. Click Save.

The secure tunnel is created with a status of Disconnected by default.

## Run secure tunnel in the private network

After registering the tunnel in Polaris, run the `polaris-secure-tunnel` workflow
from the Bridge CLI from a machine inside your private network. This process connects to the specified named Teleport instance in Polaris, downloads the Teleport agent and configuration, and then runs the Teleport agent to establish a secure TLS tunnel on port 443. The secure tunnel is then connected.

From your private network, run the Bridge CLI
with the `polaris-secure-tunnel` workflow and specify the secure tunnel name you configured in Polaris.

See [Connect to an internal DAST target from the Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/13132819f3ced5c3e7fdea47460c8d65.topic) in the Bridge CLI
documentation for the full command syntax and options.

## Confirm the tunnel is in a Connected state

Before using a secure tunnel with DAST projects or SCM integrations, confirm
that the tunnel is active. Disconnected tunnels will block SCM bulk onboarding.

1. Go to My Organization > Secure Tunnels.
2. In the tunnel list, confirm that the relevant tunnel shows a status of
   Connected.

   Note: A tunnel's status may take up to 20 minutes to update from
   Connected to
   Disconnected after a connection is
   closed.

Your secure tunnel is now ready to use. You can use it to access:

- Internal DAST targets. See [DAST configuration requirements](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic).
- On-premises SCM integrations, including:
  - Bulk repository onboarding. See GitHub Enterprise Server.
  - Event-based test automation. See [Event-Based Test Automation in Polaris for SCM Integrations](event-based-test-automation-in-polaris-for-scm-integrations.md).

## Edit or delete a secure tunnel in the Polaris UI

You can rename or remove a secure tunnel from the Polaris tunnel list at any time.

Important: If you change a tunnel's name, you must restart the Bridge CLI workflow using the new tunnel
name.

1. Go to My Organization > Secure Tunnels.
2. Locate the tunnel you want to modify and click the three-dot menu
   (...) next to its name.
3. Select Edit or Delete.
