---
title: "Installing the Black Duck Rapid Scan Static Jenkins Plugin for Sigma"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/installing-the-black-duck-rapid-scan-static-jenkins-plugin-for-sigma.html"
content_id: "VaW5Hy84zK9Spb4WFTKXSA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:15.427585+00:00"
---

# Installing the Black Duck Rapid Scan Static Jenkins Plugin for Sigma

## Prerequisites

Make sure the following third-party plugins are installed before you install the
Sigma plugin.

- Credentials Plugin version 2.1.10 or higher (<https://plugins.jenkins.io/credentials/>)
- Matrix Project Plugin version 1.18 or higher (<https://plugins.jenkins.io/matrix-project/>)
- Warnings Next Generation Plugin 9.4.0 or higher (<https://plugins.jenkins.io/warnings-ng/>)

## Public installation

The Black Duck
Rapid Scan Static Jenkins plugin is publicly available at:
<https://plugins.jenkins.io/black-duck-sigma/>. On the releases tab,
all of the releases available are listed along with installation commands that can
be used via the CLI. The plugin can also be installed through your Jenkins Server.
Follow these steps:

1. Go to Manage Jenkins > Manage Plugins.
2. Click the Available tab.
3. In the search box, search for Black Duck
   Rapid Scan Static
4. Check the Install checkbox for the plugin
5. At the bottom of the page, click Download now and install after
   restart

## Manual installation

The Black Duck Rapid Scan Static
Jenkins plugin can also be installed manually, using the
Jenkins plugin packaged in an .hpi file. To manually install
Sigma and the Black Duck Rapid Scan Static
Jenkins plugin, follow these steps.

Note: To complete this process, you need to be an administrator
that can manage the Jenkins server.

1. **Download Sigma and the Black Duck Rapid Scan Static
   Jenkins Plugin**
   1. Download the Sigma binary; see Getting the Binary for
      detailed information. If you have different Jenkins agents
      installed on different operating systems, download the binaries for
      the operating systems of the Jenkins agents that will be used. (i.e.
      Linux, MacOS, or Windows).
   2. Download the `black-duck-sigma-<VERSION>.hpi` file from the Black Duck Community page: <https://community.blackduck.com/s/>. The Jenkins
      plugin is packaged in the .hpi file.
2. **Install the Black Duck Rapid Scan Static Jenkins Plugin**
   1. Go to Manage Jenkins > Manage Plugins.
   2. Click the Advanced tab.
   3. Click Upload Plugin.
   4. Click Choose File and select the .hpi file
      that you downloaded. For example,
      black-duck-sigma.hpi.
   5. Click Upload.
   6. Click Restart Jenkins if you can restart Jenkins immediately. Otherwise, the next
      time Jenkins is restarted, the plugin will be installed.
