---
title: "Configuring a Declarative Pipeline"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-a-declarative-pipeline.html"
content_id: "XE4u1f5zL7AWpQCFzZwsXw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:25.306193+00:00"
---

# Configuring a Declarative Pipeline

To define a declarative pipeline, you use a Jenkinsfile file that contains the
Pipeline script. The basic steps are as follows:

1. Create Jenkinsfile.

   Include the following code snippet as the content of the Jenkinsfile
   depending on whether you want to use Sigma as a quality gate or whether you
   want to report Sigma issues within Jenkins. Make sure to replace the
   following tokens in the template with actual values.
   - `GIT_REPO_URL`: This is the URL to the Git repository
     where the source code is stored.
   - `SIGMA_TOOL_NAME`: This is the name of the Sigma
     installation you specified when you configured the Sigma
     installation.

   **Template for using Sigma as a quality gate**

   ```
   pipeline {
       agent any
    
       stages {
           stage('Sigma') {
               steps {
                   sigma ignorePolicies: false, sigmaToolName: '<SIGMA_TOOL_NAME>'
               }
           }
           stage('Sigma Results') {
               steps {
                   archiveArtifacts 'sigma-results.json'
               }
           }
       }
   }
   ```

   **Template for using Sigma to report issues within Jenkins**

   ```
   pipeline {
       agent any
        
       stages {
           stage('Sigma') {
               steps {
                   sigma ignorePolicies: true, sigmaToolName: '<SIGMA_TOOL_NAME>'
               }
           }
           stage('Sigma Results') {
               steps {
                   archiveArtifacts 'sigma-results.json'
                   recordIssues(tools: [[$class: 'SigmaTool']])
               }
           }
       }
   }
   ```
2. Check Jenkinsfile into your source code reopsitory that contains the code for
   Sigma to scan.
3. Define a pipeline following the steps in Defining a Jenkins Pipeline. Make sure to select Pipeline
   script from SCM from the Pipeline Definition field in step 3.
4. Configure the SCM to pull the source code to scan from a repository.

   Select the SCM from which to pull the source code to scan from a repository. By
   default, the build will search for `Jenkinsfile` in the
   source code pulled from the repository.

   Use the following Pipeline
   dialog to specify this information.

   [image: image]

   For example, you might fill out these fields as follows:

   - Definition: Pipeline script from SCM
   - SCM: Git
   - Script Path: Jenkinsfile
   - Lightweight checkout: checked
   - Pipeline Syntax: a link to a utility that helps you define the
     correct Pipline syntax for your build
