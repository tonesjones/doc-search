---
title: "Installation Using the Native Installer"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/installation-using-the-native-installer.html"
content_id: "UXAd62XB56~BHPDn30Zu7Q"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:47.306763+00:00"
content_hash: "fc8028a26ec56d73ec82f59b4ba8f19a5a4920d4b91e2ca8a3c3928b648a5873"
---

# Installation Using the Native Installer

This section describes the Software Risk Manager native installer. For Docker or
Kubernetes installation instructions, please see the [codedx-docker](https://github.com/codedx/codedx-docker) and [srm-k8s](https://github.com/codedx/srm-k8s) pages respectively.

Note: A Kubernetes-based installation is necessary when using Tool Orchestration or Scan
Service (needed to run Coverity and Black Duck scans).

The Software Risk Manager installer is self-contained as it includes all of the software
necessary to run Software Risk Manager and is dependent upon its own Tomcat, Apache, and
MariaDB services. The services automatically start whenever Software Risk Manager is
restarted.

Note: While multiple Software Risk Manager installations are supported, it is discouraged to
run them on the same machine. This will likely lead to resource contention, resulting in
performance degradation in those installations.

Some of the Software Risk Manager dependencies listen for network activity (e.g., the web
server to accept incoming requests). If a port conflict is detected, you will be
prompted with a suggested alternate port. It is your choice to accept that port or
change it.

When first starting the installer downloaded for your platform, you should see the
following screen.

  
 [image: image]   

Click Next and select whether this is a fresh install or an upgrade.

  
 [image: image]   

Click Next to continue.
