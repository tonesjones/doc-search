---
title: "Working with a Jenkins Pipeline"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/working-with-a-jenkins-pipeline.html"
content_id: "RYeTZVnbOLj1OrT6EuxTow"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:23.315236+00:00"
---

# Working with a Jenkins Pipeline

After the administrator has configured the Sigma installations, you can define the build
job and configure Sigma as a build step for either freestyle projects or pipelines. This
section describes the Pipeline option.

A Jenkins Pipeline (or Pipeline) is a suite of plugins that supports continuous delivery
pipelines in Jenkins. The definition of a Pipeline is written to a text file,
Jenkinsfile, that can be stored in a project's source control repository.

A Jenkinsfile can be written using two types of syntax: scripted and declarative.
