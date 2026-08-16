---
title: "Detect Jenkins Plugin"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-jenkins-plugin.html"
content_id: "osFQOeISkf4iSUUa_KHODg"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:45:55.889944+00:00"
---

# Detect Jenkins Plugin

The Black Duck® Detect for Jenkins plugin enables you to install and run Detect in your Jenkins instance.

Detect scans code bases in your projects and folders to perform compositional analysis and functions as a Black Duck SCA intelligent scan client. Detect sends scan results to Black Duck SCA, which generates risk analysis when identifying open source components, licenses, and security vulnerabilities.

Detect is designed to run in the native build environment of the project that you want to scan. It uses the same global configuration as your Jenkins instance and provides a pass-through for Detect. You can run as a post-build action in a Jenkins Freestyle job or run as a Pipeline step using a Pipeline script in a PipeLine job.
After running a Detect scan following the Jenkins build, you can view the scan results in your Black Duck SCA instance.

Refer to How it Works to learn more about Detect.

## Basic workflow

1.      Make sure you satisfy system and other requirements.

- Install the Detect plugin in Jenkins.
- Configure Black Duck connection and plugin.

2.      Run a Jenkins build on your project.

3.      Detect scans the project, for example, the scan might be a step in a Jenkins Pipeline job or post-build action in a Freestyle job.

4.      Detect sends the scan results to Black Duck SCA for analysis.

After running a Detect scan following the Jenkins build, you can view the scan results in your Black Duck SCA instance.
