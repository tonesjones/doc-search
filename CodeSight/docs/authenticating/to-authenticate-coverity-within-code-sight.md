---
title: "To authenticate Coverity within Code Sight"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-authenticate-coverity-within-code-sight.html"
content_id: "9Y86Lps4mT5MPMr38rRNIA"
version: "2026.9.0"
section: "Authenticating to Servers in Code Sight"
scraped_at: "2026-10-06T23:39:51.281853+00:00"
---

# To authenticate Coverity within Code Sight

Authenticating yourself enables Coverity Analysis to share triage data with a central server.
It also enables Coverity Analysis to download full-project scans from that server, which improves the quality of local analysis.

If Coverity Analysis is not already present on your system, authentication enables Code Sight to download this software.

1. After you install Code Sight, the Coverity tile on the
   Products and Licenses panel
   prompts you to enable Coverity.

   Figure 1. Authentication: Prompt to enable Coverity
     
    [image: Authentication: Coverity tile]
2. Click Enable Coverity.

   Code Sight displays the Authentication controls for
   a Coverity (Code Analysis) server.
3. Enter your credentials and server information, then click Change Credentials for both
   the username/URL and the password panels.

   Note:
   Depending on the URL you enter, you might encounter a warning about using a self-signed certificate.
   For more information, see Authenticating a server that uses a self-signed certificate.

   If the connection is successful, Code Sight returns to the Products and Licenses panel.
4. The choices now depend on how your system was set up.
   - If Coverity Analysis was already installed on your system, Code Sight can now run it.
   - If Coverity Analysis or Rapid Scan Static was not already installed, click Install to download that scan engine.

     Installing Rapid Scan Static runs fairly quickly.
     Installing Coverity Analysis can take quite some time.

   Figure 2. Authentication: Prompts to install scan engines
     
    [image: Authentication: Coverity and Rapid Scan installation]
