---
title: "To authenticate Polaris within Code Sight"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-authenticate-polaris-within-code-sight.html"
content_id: "bpCpM4EuE_SZ~vVX8ssAfw"
version: "2026.9.0"
section: "Authenticating to Servers in Code Sight"
scraped_at: "2026-10-06T23:39:51.331844+00:00"
---

# To authenticate Polaris within Code Sight

Authenticating yourself enables Polaris to run project scans on your system and compare the results.
It also grants you the ability to install Sigma, use Auto mode,
and manually run Rapid Scan Static (Sigma) scans.

If Rapid Scan Static (Sigma) is not already present on your system,
authentication enables Code Sight to download this software.

Note:
You can run Polaris in Local View even if the Sigma scan engine is not installed locally.

1. After you install Code Sight in a JetBrains IDE (including IntelliJ), Visual Studio, or VS Code, the Polaris tile on the
   Products and Licenses panel
   prompts you to enable Polaris.

   Figure 1. Authentication: Prompt to enable Polaris
     
    [image: Authentication: Polaris tile]
2. Click Enable Polaris.

   Code Sight displays the Authentication
   controls for Polaris.
3. Enter your credentials and server information.

   Note:
   Depending on the URL you enter, you might encounter a warning about using a self-signed certificate.
   For more information, see Authenticating a server that uses a self-signed certificate.

   If the connection is successful, Code Sight returns to the Products and Licenses panel.
4. The choices now depend on how your system was set up.
   - If Rapid Scan Static was already installed on your system, Code Sight can now run it.
   - If Rapid Scan Static was not already installed, click Install to download the Sigma scan engine.

   Figure 2. Authentication: Prompt to install the scan engine
     
    [image: Authentication: Sigma installation]
