---
title: "Using the Black Duck Security Scan Extension with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-extension-with-coverity.html"
content_id: "EHp9b_mEnoivm_8zBR94Ew"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:27.369571+00:00"
---

# Using the Black Duck Security Scan Extension with Coverity

On push events, a full Coverity scan will be run and results are committed to the Coverity server database.

On pull request events, comments are added to pull requests for new issues found by the scan if `COVERITY_PRCOMMENT_ENABLED` is set to `true` (see example below). Note that scan results are not committed to Coverity server database in this case.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments

Before running the pipeline with Black Duck Security Scan Extension, make sure the specified project and stream exist in your Coverity server. Configure sensitive data such as user names and passwords using pipeline variables.

Here is a simplified example for `azure-pipelines.yml` that you can use to integrate with Coverity Cloud:

```
trigger:
  - main

pool:
  vmImage: ubuntu-latest

variables:
  - group: Coverity
  
steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Coverity Scan'
  inputs:
    COVERITY_URL: $(COVERITY_URL)
    COVERITY_USER: $(COVERITY_USER)
    COVERITY_PASSPHRASE: $(COVERITY_PASSPHRASE)
    
    ### Pull Request Comments
    # COVERITY_PRCOMMENT_ENABLED: true
    # AZURE_TOKEN: $(System.AccessToken) 
    
    ### To enable the use of self-signed certificates
    # NETWORK_SSL_TRUSTALL: true
    # NETWORK_SSL_CERT_FILE: '/Users/Config/cert.pem'

    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'
    
  ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
  # continueOnError: true
  
### Uncomment below configuration to add custom logic based on return status    
# - task: CmdLine@2
#   displayName: 'Command Line'
#   condition: not(eq(variables['BlackDuckSecurityScan.status'], '0'))
#   inputs:
#     script: |
#       echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)
```

Note: `continueOnError` is required to use returned status from Black Duck Security Scan Extension in subsequent tasks if `MARK_BUILD_STATUS` is not set or set to FAILED.

Here is a detailed example for`azure-pipelines.yml` that you can use to integrate with Coverity Cloud:

```
trigger:
  - main

pool:
  vmImage: ubuntu-latest

variables:
  - group: coverity
  
steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Coverity Full Scan'
  condition: not(eq(variables['Build.Reason'], 'PullRequest'))
  inputs:
    COVERITY_URL: $(COVERITY_URL)
    COVERITY_USER: $(COVERITY_USER)
    COVERITY_PASSPHRASE: $(COVERITY_PASSPHRASE)
    COVERITY_PROJECT_NAME: $(Build.Repository.Name)
    COVERITY_STREAM_NAME: $(Build.Repository.Name)-$(Build.SourceBranchName)
    COVERITY_POLICY_VIEW: 'Outstanding Issues'
    # COVERITY_WAITFORSCAN: false   # Used to support the async mode 
    
    ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
    # INCLUDE_DIAGNOSTICS: true
    
    # PROJECT_DIRECTORY: "$(PROJECT_DIRECTORY)"
    
    ### Coverity (SAST) Tool Settings
    # COVERITY_CLEAN_COMMAND: 'mvn clean'
    # COVERITY_BUILD_COMMAND: 'mvn clean install'
    COVERITY_ARGS: '--config-override capture.build.build-command=mvn install'
    # COVERITY_CONFIG_PATH: /Users/tmp/coverity.yml
    
    ### To enable the use of self-signed certificates
    # NETWORK_SSL_TRUSTALL: true
    # NETWORK_SSL_CERT_FILE: '/Users/Config/cert.pem'

    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'
    
    ### Coverity (SAST) Tool Settings
    ### Clean command for Coverity
    # COVERITY_CLEAN_COMMAND: 'mvn clean'
    
    ### Build command for Coverity
    # COVERITY_BUILD_COMMAND: 'mvn clean install'
    
    ### Additional arguments for Coverity
    # COVERITY_ARGS: '--config-override capture.build.build-command=mvn install'
    
    ### Coverity config file path location
    # COVERITY_CONFIG_PATH: /Users/tmp/coverity.yml

    ### To enable the use of self-signed certificates
    # NETWORK_SSL_TRUSTALL: true
    # NETWORK_SSL_CERT_FILE: '/Users/Config/cert.pem'
    
  ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
  # continueOnError: true

- task: BlackDuckSecurityScan@2
  displayName: 'Coverity PR Scan'
  condition: eq(variables['Build.Reason'], 'PullRequest')
  inputs:
    COVERITY_URL: $(COVERITY_URL)
    COVERITY_USER: $(COVERITY_USER)
    COVERITY_PASSPHRASE: $(COVERITY_PASSPHRASE)
    COVERITY_PROJECT_NAME: $(Build.Repository.Name)
    COVERITY_STREAM_NAME: $(Build.Repository.Name)-$(System.PullRequest.targetBranchName)
    
    ### Below configuration is used to enable feedback from Coverity security testing as pull request comment
    COVERITY_PRCOMMENT_ENABLED: true
    ## Use the parameter below to add comments for issues filtered 
    ## by impact. Default is High if unset
    ## NOTE: Issues matching COVERITY_POLICY_VIEW are ignored if set
    # COVERITY_PRCOMMENT_IMPACTS: 'High,Medium,Low,Audit'
    AZURE_TOKEN: $(System.AccessToken) # Mandatory when COVERITY_PRCOMMENT_ENABLED is set to 'true'   
    
    ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
    # INCLUDE_DIAGNOSTICS: true
    
    # PROJECT_DIRECTORY: "$(PROJECT_DIRECTORY)"
    
    ### Coverity (SAST) Tool Settings
    # COVERITY_CLEAN_COMMAND: 'mvn clean'
    # COVERITY_BUILD_COMMAND: 'mvn clean install'
    COVERITY_ARGS: '--config-override capture.build.build-command=mvn install'
    # COVERITY_CONFIG_PATH: /Users/tmp/coverity.yml

    ### To enable the use of self-signed certificates
    # NETWORK_SSL_TRUSTALL: true
    # NETWORK_SSL_CERT_FILE: '/Users/Config/cert.pem'

    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'
  
    ### Coverity (SAST) Tool Settings
    ### Clean command for Coverity
    # COVERITY_CLEAN_COMMAND: 'mvn clean'
    
    ### Build command for Coverity
    # COVERITY_BUILD_COMMAND: 'mvn clean install'
    
    ### Additional arguments for Coverity
    # COVERITY_ARGS: '--config-override capture.build.build-command=mvn install'
    
    ### Coverity config file path location
    # COVERITY_CONFIG_PATH: /Users/tmp/coverity.yml
    
  ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
  # continueOnError: true
  
### Uncomment below configuration to add custom logic based on return status    
# - task: CmdLine@2
#   displayName: 'Command Line'
#   condition: not(eq(variables['BlackDuckSecurityScan.status'], '0'))
#   inputs:
#     script: |
#       echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)
```

Note: If you are using Coverity Connect, you need to add `COVERITY_LOCAL: true` to the two `condition ->
inputs` sections in the example above.

Note: `continueOnError` is required to use returned status from Black Duck Security Scan Extension in subsequent tasks if `MARK_BUILD_STATUS` is not set or set to FAILED.

Table 1. List of mandatory and optional parameters for Coverity

| **Input parameter** | **Description** | **Mandatory / optional** |
| --- | --- | --- |
| `COVERITY_URL` | Coverity URL | Mandatory |
| `COVERITY_USER_NAME` | Coverity Username | Mandatory |
| `COVERITY_PASSPHRASE` | Coverity Password | Mandatory |
| `COVERITY_PROJECT_NAME` | Coverity Project Name. Default value is the name of the repository, which includes repository name. | Optional |
| `COVERITY_STREAM_NAME` | Coverity Stream name. Default value in non PR context is set as `$BUILD_REPOSITORY_NAME-$BUILD_SOURCEBRANCHNAME`.  Default value in PR context is set as `$BUILD_REPOSITORY_NAME-$SYSTEM_PULLREQUEST_TARGETBRANCHNAME`. Note:  - If the branch name contains special characters like /,\,* etc. which Coverity doesn’t support then the scan will fail. In this case, user needs to provide stream name in yml or classic editor. For example, if a branch name is **dev/new-feature,** then for Coverity, stream name won’t be created in Coverity server and scan will fail because the branch name contains “/”. - The prefix refs/heads/ is removed from $BUILD_SOURCEBRANCH and $SYSTEMPULLREQUEST_TARGETBRANCH when using them as default values. | Optional (Mandatory for Azure manual trigger). |
| `COVERITY_INSTALL_DIRECTORY` | Installation directory of Coverity | Optional |
| `COVERITY_POLICY_VIEW` | ID or name of policy view to be used to enforce the “break the build” policy.    If issues are found in the specified this view, build will be failed.  Example: `coverity_policy_view: '100001'` or `coverity_policy_view: 'Outstanding Issues'` | Optional |
| `COVERITY_PRCOMMENT_ENABLED` | Option to enable automatic creation pull request comments for new issues found in the pull request.    Baseline full scan results must exist on the server for this feature to work.    **Note**: The merge request from the feature branch to the main branch must exist for this feature to work.    **Default**: false   **Note**: When both `COVERITY_PRCOMMENT_ENABLED` and `COVERITY_POLICY_VIEW` are configured for a Coverity PR scan, the `COVERITY_POLICY_VIEW` setting will be ignored, and PR comments will be generated only for new issues that match the specified impact filter (`COVERITY_PRCOMMENT_IMPACTS`).  Further details can be found here.   Replaces deprecated `COVERITY_AUTOMATION_PRCOMMENT` parameter. | Optional |
| `COVERITY_PRCOMMENT_IMPACTS` | Comma-separated list of impacts that will cause Pull Request scans to fail.  Issues detected in the Pull Request that match any of the listed impact levels will be uploaded to Coverity, added as Pull Request comments and trigger build failure.  Valid impacts are: `High`, `Medium`, `Low` and `Audit`.  **Default**: `High` | Optional |
| `AZURE_TOKEN` | Azure Access Token  Example: `AZURE_TOKEN: $(System.AccessToken)` or `AZURE_TOKEN: $(PAT_TOKEN)` | Mandatory if `COVERITY_PRCOMMENT_ENABLED` is set true. |
| `COVERITY_LOCAL` | Set this to false if you are using Coverity cloud deployment. Black Duck Security Scan Extension will install Coverity Thin Client as necessary. Set this to true if you are using on-prem Coverity Connect.  If enabled, Black Duck Security Scan Extension will install the Coverity Analysis on the local system in order to execute the scan. You can use an existing installation of Coverity tools by setting the ‘coverity_install_directory’ option.  Example: `COVERITY_LOCAL: true`  **Default**: `false`. | Optional |
| `COVERITY_VERSION` | The version of Coverity to use.  **Example**: `COVERITY_VERSION: '2023.6.0'`  **Classic Editor UI Changes**:  The Coverity version has been moved from the `Scan Options Group` to the `Coverity (SAST) Tool Options Group`. | Optional |
| `PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `COVERITY_CLEAN_COMMAND` | Clean command for Coverity. | Optional |
| `COVERITY_BUILD_COMMAND` | Build command for Coverity. | Optional |
| `COVERITY_ARGS` | Additional arguments for Coverity. | Optional |
| `COVERITY_CONFIG_PATH` | Coverity config file path location. | Optional |
| `COVERITY_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |

Table 2. List of network parameters

| **Input parameter** | **Description** | **Mandatory / optional** |
| --- | --- | --- |
| `NETWORK_SSL_TRUSTALL` | Disables SSL certificate verification. Use with caution.  **Default**: false | Optional |
| `NETWORK_SSL_CERT_FILE` | File path to configure the HTTPS calls to accept a self-signed certificate. | Optional |

- `NETWORK_SSL_TRUSTALL` and `NETWORK_SSL_CERT_FILE` cannot both be specified at the same time.
- **Classic Editor**:

  In the Classic Editor SSL Certificates can be configured within the `Network Options` section:

  [image: Azure (classic) Network Options]
