---
title: "Installing Sigma Manually"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/installing-sigma-manually.html"
content_id: "bHk9Hp8LFlU2nDroz0JURQ"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:17.413201+00:00"
---

# Installing Sigma Manually

To manually install Sigma onto a Jenkins agent, you need to configure a Sigma tool in
order for Sigma to be located by the plugin for use.

1. Download the Sigma binary.
2. Copy the Sigma binary onto the Jenkins agent you want to run it.
3. In Jenkins, navigate to Manage Jenkins > Global Tool
   Configuration.
4. Click Rapid Scan Static installations.
5. Click Add Rapid Scan Static.
6. Specify the name for the installation.
7. Unselect the checkbox Install Automatically.
8. In the Installation directory field, specify the path to the directory
   where Sigma is located on the agent.

   You might see a warning that the path is not on the Jenkins controller, also
   known as *Jenkins master* for older versions. That is ok, the validation is
   checking to see if the path exists.

If you opt for manual installation, there are no checks to determine if Sigma exists
at the specified installation directory, and there are no checks to ensure that
Sigma is up to date. Installing updated versions of Sigma is the responsibility of
the Jenkins administrators who copy Sigma onto a Jenkins agent. If Sigma cannot be
found during a build, the build will fail.
