---
title: "To authenticate Black Duck SCA within Code Sight"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-authenticate-black-duck-sca-within-code-sight.html"
content_id: "TlDk6QlwNJyv_DafdjccCw"
version: "2026.9.0"
section: "Authenticating to Servers in Code Sight"
scraped_at: "2026-10-06T23:39:51.229872+00:00"
---

# To authenticate Black Duck SCA within Code Sight

Authenticating yourself enables Black Duck SCA to run project scans on your system and compare the results
with the KnowledgeBase on a Black Duck SCA server.
The KnowledgeBase identifies which components are open-source software, and among those components,
identifies those that might need remediation.

If Black Duck®
Detect is not already present on your system, authentication enables Code Sight to download this software.
(Detect is the engine that provides local support for Black Duck SCA.)

1. After you install Code Sight, the Black Duck SCA tile on the
   Products and Licenses panel
   prompts you to enable Black Duck SCA.

   Figure 1. Authentication: Prompt to enable Black Duck SCA
     
    [image: Authentication: Black Duck tile]
2. Click Enable Black Duck SCA.

   Code Sight displays the Authentication controls for
   Black Duck SCA.
3. Enter your credentials and server information, then click Change Credentials for both
   the username/URL and the password panels.

   Note:
   Depending on the URL you enter, you might encounter a warning about using a self-signed certificate.
   For more information, see Authenticating a server that uses a self-signed certificate.

   If the connection is successful, Code Sight returns to the Products and Licenses panel.
4. The choices now depend on how your system was set up.
   - If Black Duck®
     Detect was already installed on your system, Code Sight can now run it.
   - If Detect was not already installed, click Install to download that scan engine.

     Installing Detect can take a little while.

   Figure 2. Authentication: Prompt to install Rapid Scan SCA
     
    [image: Authentication: Black Duck installation]
