---
title: "Working with a Jenkins Freestyle Project"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/working-with-a-jenkins-freestyle-project.html"
content_id: "y_Kn~HNzDh9fi6xqSAqxXg"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:18.067462+00:00"
---

# Working with a Jenkins Freestyle Project

After the administrator has configured the Sigma installations, you can define the build
job and configure Sigma as a build step for either freestyle projects or pipelines. This
section describes a freestyle project.

A Freestyle project provides the user with a form in the Jenkins UI to configure the
build by defining the following:

- A build step to run the Sigma tool
- A post-build action to record issues

You can run Sigma either as a quality gate or to report issues.
