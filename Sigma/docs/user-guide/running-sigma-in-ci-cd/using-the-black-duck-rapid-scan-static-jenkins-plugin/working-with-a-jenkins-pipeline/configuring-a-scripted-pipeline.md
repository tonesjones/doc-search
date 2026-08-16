---
title: "Configuring a Scripted Pipeline"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-a-scripted-pipeline.html"
content_id: "z39hIG3aPaNbV4pjhYcHjQ"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:24.571007+00:00"
---

# Configuring a Scripted Pipeline

1. Define a pipeline following the steps in Defining a Jenkins Pipeline. Make sure to select Pipeline
   script from the Pipeline Definition field in step 3.
2. Include the following code snippet in the Script text area of the build
   configuration, making sure to replace the following tokens in the template with
   actual values. 

   - `GIT_REPO_URL`: This is the URL to the Git repository
     where the source code is stored.
   - `SIGMA_TOOL_NAME`: This is the name of the Sigma
     installation you specified when you configured the Sigma installation.

   **Template for using Sigma as a quality gate**

   ```
   node {
       stage('Clone Repo') {
           git '<GIT_REPO_URL>'
       }
       stage('Sigma') {
           sigma ignorePolicies: false, sigmaToolName: '<SIGMA_TOOL_NAME>'
       }
       stage('Sigma Results') {
           archiveArtifacts 'sigma-results.json'
       }
   }
   ```

   **Template for using Sigma to report issues within Jenkins**

   ```
   node {
       stage('Clone Repo') {
           git '<GIT_REPO_URL>'
       }
       stage('Sigma') {
           sigma ignorePolicies: true, sigmaToolName: '<SIGMA_TOOL_NAME>'
       }
       stage('Sigma Results') {
           archiveArtifacts 'sigma-results.json'
           recordIssues(tools: [[$class: 'SigmaTool']])
       }
   }
   ```
