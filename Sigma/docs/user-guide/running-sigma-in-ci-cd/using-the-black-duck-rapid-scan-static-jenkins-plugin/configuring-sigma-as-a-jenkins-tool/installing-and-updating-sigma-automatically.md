---
title: "Installing and Updating Sigma Automatically"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/installing-and-updating-sigma-automatically.html"
content_id: "29hmSw_LIKn78hW5A6Nguw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:16.739057+00:00"
---

# Installing and Updating Sigma Automatically

**Prerequisites**

To install Sigma automatically, you must download and host Sigma on a system that
Jenkins and the Jenkins agents can access. For example, you can download Sigma and
host it on your Artifactory instance or another file sharing tool.

The tool installer configuration defines a URL to Sigma. Use this URL to download
Sigma and install it on the Jenkins agent running the build.

Note: This scenario provides automatic reinstall under certain
conditions.

**Follow these steps to install and configure Sigma:**

1. Download the Sigma binary.
2. In Jenkins, navigate to Manage Jenkins > Global Tool
   Configuration.
3. Click Rapid Scan Static installations.
4. Specify the name for the installation.
5. Select the checkbox Install Automatically.
6. In the Sigma installations dialog, specify the URL where Sigma is hosted in the
   Binary Download URL field.
7. In the Sigma installations dialog, specify the Connection Timeout (in
   seconds) if the default value of 30 seconds is not sufficient.

If you opt for automatic installation, when a build is configured and a Sigma Tool
installation is selected, the build will ensure that Sigma is installed and up to
date on the Jenkins agent under the following conditions:

- Sigma is not present on the Jenkins agent.
- The Binary Download URL has changed since the last time the Sigma tool was
  installed.
- Sigma hosted at the URL specified by the Binary Download URL has an updated
  timestamp more recent than that of Sigma installed on the Jenkins agent.

By performing these checks, the installer ensures that the Jenkins agents use the
most recent version of Sigma hosted at the Binary Download URL location.
