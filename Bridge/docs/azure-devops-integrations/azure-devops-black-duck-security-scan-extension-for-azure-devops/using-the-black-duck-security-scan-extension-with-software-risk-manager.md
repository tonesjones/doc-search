---
title: "Using the Black Duck Security Scan Extension with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-extension-with-software-risk-manager.html"
content_id: "QP7DhnK0me9Si8QutqBYZQ"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:29.487814+00:00"
---

# Using the Black Duck Security Scan Extension with Software Risk Manager

As a Black Duck® Software Risk Manager™ (SRM) customer, you can use ADO Extension to automate SCA and SAST
scanning in your CI pipeline.

Here is a simplified example for `azure-pipelines.yml` that you can use to
integrate with SRM:

```
trigger:
  - main

pool:
  vmImage: ubuntu-latest
  
variables:
  - group: srm
  
steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Software Risk Manager'
  inputs:
    SRM_URL: $(SRM_URL)
    SRM_APIKEY: $(SRM_APIKEY)
    SRM_ASSESSMENT_TYPES: "SCA,SAST"

### Uncomment below configuration to add custom logic based on return status   
# - task: CmdLine@2
#   displayName: 'Command Line'
#   condition: not(eq(variables['BlackDuckSecurityScan.status'], '0'))
#   inputs:
#     script: |
#       echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)
```

Here is a detailed example for azure-pipelines.yml that you can use to integrate with
SRM:

```
trigger:
  - main

pool:
  vmImage: ubuntu-latest

variables:
  - group: srm
  
steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Software Risk Manager'
  condition: not(eq(variables['Build.Reason'], 'PullRequest'))
  inputs:
     SRM_URL: $(SRM_URL)
     SRM_APIKEY: $(SRM_APIKEY)
     SRM_ASSESSMENT_TYPES: "SCA,SAST"
     SRM_PROJECT_NAME: $(Build.Repository.Name)
     
     ## Project id in SRM Server
     ### Uncomment below configuration if SRM_PROJECT_NAME didn't specified
     # SRM_PROJECT_ID: $(SRM_PRJECT_ID)
  
     ## Branch name in the SRM Server  
     SRM_BRANCH_NAME: $(SRM_BRANCH_NAME)
     ## Parent Branch name in SRM server
     SRM_BRANCH_PARENT: $(SRM_BRANCH_PARENT) 
     # SRM_WAITFORSCAN: false   # Used to support the async mode

     ## Path to Coverity CLI
     COVERITY_EXECUTION_PATH : "/Users/johndoe/bridge-install-dir/srm-coverity/cov-thin-client-macosx-2023.6.1/bin/coverity"
     ## Path to the Black Duck Detect jar file to use
     DETECT_EXECUTION_PATH: "/Users/johndoe/bridge-install-dir/srm-blackduck/tools/blackduck-detect/10.0.0/detect-10.0.0.jar"

     # PROJECT_DIRECTORY: "$(PROJECT_DIRECTORY)"
    
     ### Coverity (SAST) Tool Settings
     # COVERITY_CLEAN_COMMAND: 'mvn clean'
     # COVERITY_BUILD_COMMAND: 'mvn clean install'
     # COVERITY_ARGS: '--config-override capture.build.build-command=mvn install'
     # COVERITY_CONFIG_PATH: /Users/tmp/coverity.yml
    
     ### Detect Tool Settings
     # DETECT_SEARCH_DEPTH: 2
     # DETECT_ARGS: '--detect.diagnostic=true'
     # DETECT_CONFIG_PATH: '/Users/tmp/application.properties'
    
     ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
     # INCLUDE_DIAGNOSTICS: 'true'
   
### Uncomment below configuration to add custom logic based on return status    
# - task: CmdLine@2
#   displayName: 'Command Line'
#   condition: not(eq(variables['BlackDuckSecurityScan.status'], '0'))
#   inputs:
#     script: |
#       echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)
```

Table 1. List of mandatory and optional parameters for Software Risk Manager

| **Input parameter** | **Description** | **Mandatory / optional** |
| --- | --- | --- |
| `SRM_URL` | SRM Server URL | Mandatory |
| `SRM_APIKEY` | SRMAPI KEY | Mandatory |
| `SRM_ASSESSMENT_TYPES` | SRM Assessment Types separated by comma. Accepted values: `SAST` or `SCA` or `SAST, SCA` | Mandatory |
| `SRM_PROJECT_NAME` | Project name in SRM Server. Default: `$(Build.Repository.Name)` | Optional |
| `SRM_PROJECT_ID` | Project ID in SRM Server | Optional |
| `SRM_BRANCH_NAME` | Branch name on the SRM Server. The branch is created if it doesn't already exist. If a new branch name is passed to `SRM_BRANCH_NAME` parameter, `SRM_BRANCH_PARENT` should also be passed. Otherwise, an error message will be displayed to the user.  If an existing branch name is passed to `SRM_BRANCH_NAME`, `SRM_BRANCH_PARENT` is not required. | Optional |
| `SRM_BRANCH_PARENT` | Parent Branch name in SRM server | Optional |
| `COVERITY_EXECUTION_PATH` | Path to Coverity CLI | Optional |
| `DETECT_EXECUTION_PATH` | Path to the Detect jar file to use | Optional |
| `PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `SRM_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |
