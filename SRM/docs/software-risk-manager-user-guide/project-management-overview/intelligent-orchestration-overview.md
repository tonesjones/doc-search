---
title: "Intelligent Orchestration Overview"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/intelligent-orchestration-overview.html"
content_id: "lzxb8vU5U1sdbFamnGlGKQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:23.058408+00:00"
content_hash: "05f3d1e1ea4f66838926d72ece89f3aa00d5a58b0d921199f246c9f93ed09cd0"
---

# Intelligent Orchestration Overview

Intelligent Orchestration can determine which security tools are best suited for a
particular analysis, depending on factors such as code changes, risk score, and security
policies. In Software Risk Manager, Intelligent Orchestration is enabled by adding a
pre-scan policy to a project.

Note: Intelligent Orchestration requires a separate IO license and
must be properly configured before use. For instructions, see "Enabling Intelligent
Orchestration" in the *Software Risk Manager Install Guide*.

**To configure Intelligent Orchestration for a project:** 

1. Click the Projects icon in the navigation bar to open the Projects page, then
   select Intelligent Orchestration from the project's dropdown configuration
   options.

   [image: image]
2. Click the toggle switch to "on" to open the configuration window.

   [image: image]
3. Enter the name of the project in the Project Name field (required).

   The IO
   Project Name refers to an existing project in your IO server.
4. Select the SCM Type.

   There are three options: GitHub, GitLab, and
   Bitbucket.
5. Enter the required configuration information according to the selected SCM type,
   as described below:

   **Type: GitHub**
   - SCM Owner
   - SCM Repository Name
   - GitHub API URL
   - GitHub Username
   - GitHub Token

   **Type: GitLab**
   - SCM Owner
   - SCM Repository Name
   - GitLab API URL
   - GitLab Token

   **Type: Bitbucket**
   - SCM Owner
   - SCM Repository Name
   - Bitbucket API URL
   - Bitbucket Host Type:

     Bitbucket supports three host types:
     - Cloud
     - Server
     - DataCenter
   - BitBucket Username (Cloud only)
   - BitBucket Password (Cloud only)
   - Bitbucket API Version (Server/DataCenter)
   - Bitbucket Project Key (Server/DataCenter)
   - Bitbucket Username (Server/DataCenter)
   - Bitbucket Password (Server/DataCenter)
6. Click Save.
