---
title: "Using the Black Duck Security Scan Extension with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-extension-with-black-duck-sca.html"
content_id: "Vogk8UFLaKNiLhwRVR7hIg"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:25.045145+00:00"
---

# Using the Black Duck Security Scan Extension with Black Duck SCA

Black Duck Security Scan Extension supports both self-hosted (e.g., on-prem) and Black Duck-hosted Black Duck® SCA Hub instances.

In the default Black Duck® SCA Hub permission model, projects and project versions are created on the fly and as needed. Ensure that permissions needed to create projects and project versions are granted on Black Duck® SCA Hub.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments

Configure sensitive data like user names, passwords and URLs using pipeline variables.

Note: Detect specific options can be passed through Detect environment variables.

Here is a simplified example of `azure-pipelines.yml` that you can use with Black Duck® SCA:

```
trigger:
  - master

pool:
  vmImage: ubuntu-latest
  
variables:
  - group: Blackduck
  
steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Black Duck Scan'
  ### Configuration to set specific detect environment variables
  env:
    DETECT_PROJECT_NAME: $(Build.Repository.Name)
  inputs:
    BLACKDUCKSCA_URL: $(BLACKDUCK_URL)
    BLACKDUCKSCA_TOKEN: $(BLACKDUCK_TOKEN)
    
    ### Mandatory when BLACKDUCKSCA_PRCOMMENT_ENABLED or BLACKDUCKSCA_FIXPR_ENABLED is set true
    # AZURE_TOKEN: $(System.AccessToken)
    
    ### Pull Request Comments
    # BLACKDUCKSCA_PRCOMMENT_ENABLED: true
    
    ### Fix Pull Request creation
    # BLACKDUCKSCA_FIXPR_ENABLED: true
    
    ### SARIF report generation 
    # BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
    
    ### To enable the use of self-signed certificates
    # NETWORK_SSL_TRUSTALL: true
    
    ### Mark build status if policy violating issues are found
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

    ### Uncomment below to upload to Advanced security  
    #- task: AdvancedSecurity-Publish@1
    #   inputs:
    #     SarifsInputDirectory: '.bridge/Blackduck SCA SARIF Generator' # When the bridge version is lower than 3.5.0
    #     SarifsInputDirectory: '$(Build.SourcesDirectory)/.blackduck/integrations/blackducksca/sarif' # When the bridge version is greater than 3.5.0
```

Note: `continueOnError` is required to use returned status from Black Duck Security Scan Extension in subsequent tasks if `MARK_BUILD_STATUS` is not set or set to FAILED.

Here is a detailed example of `azure-pipelines.yml` that you can use with Black Duck SCA:

```
trigger:
  - master

pool:
  vmImage: ubuntu-latest
  
variables:
  - group: Blackduck

steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Black Duck Full Scan'
  condition: not(eq(variables['Build.Reason'], 'PullRequest'))
  ### Use below configuration to set specific detect environment variables
  env:
    DETECT_PROJECT_NAME: $(Build.Repository.Name)
  inputs:
    BLACKDUCKSCA_URL: $(BLACKDUCKSCA_URL)
    BLACKDUCKSCA_TOKEN: $(BLACKDUCKSCA_TOKEN)
    BLACKDUCKSCA_SCAN_FULL: true
    # BLACKDUCKSCA_WAITFORSCAN: false   # Used to support the async mode 
    ### Accepts Multiple Values
    #BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES: 'BLOCKER,CRITICAL'
    
    ### Uncomment below configuration to enable automatic fix pull request creation if vulnerabilities are reported
    BLACKDUCKSCA_FIXPR_FILTER_SEVERITIES: "CRITICAL,  HIGH"
    BLACKDUCKSCA_FIXPR_ENABLED: true
    BLACKDUCKSCA_FIXPR_MAXCOUNT: 2
    BLACKDUCKSCA_FIXPR_USEUPGRADEGUIDANCE: 'SHORT_TERM,LONG_TERM'
    AZURE_TOKEN: $(System.AccessToken) # Mandatory when BLACKDUCK_FIXPR_ENABLED is set to 'true'
    
    ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
    # INCLUDE_DIAGNOSTICS: true
    
    ### SARIF report generation 
    BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
    BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH: "$(Build.SourcesDirectory)/sarif/report.sarif.json"
    BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES: "CRITICAL, HIGH, MEDIUM, LOW"
    BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES: true
    
    # NETWORK_AIRGAP: true
    # BRIDGECLI_INSTALL_DIRECTORY: $(BRIDGECLI_INSTALL_DIRECTORY)
    
    ### Uncomment below configuration to specify the project directory
    # PROJECT_DIRECTORY: "$(PROJECT_DIRECTORY)"
    
    ### To enable the use of self-signed certificates
    # NETWORK_SSL_TRUSTALL: true
    
    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'
   
    ### Detect Tool Settings
    # DETECT_SEARCH_DEPTH: 2
    # DETECT_ARGS: '--detect.diagnostic=true'
    # DETECT_CONFIG_PATH: '/Users/tmp/application.properties'
    
    ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
    # continueOnError: true
        
- task: BlackDuckSecurityScan@2
  displayName: 'Black Duck PR Scan'
  condition: eq(variables['Build.Reason'], 'PullRequest')
  ### Use below configuration to set specific detect environment variables
  #env:
    #DETECT_PROJECT_NAME: $(Build.Repository.Name)
  inputs:
    BLACKDUCKSCA_URL: $(BLACKDUCK_URL)
    BLACKDUCKSCA_TOKEN: $(BLACKDUCK_TOKEN)
    BLACKDUCKSCA_SCAN_FULL: false
    
    ### Below configuration is used to enable automatic pull request comment based on Black Duck SCA scan result
    BLACKDUCKSCA_PRCOMMENT_ENABLED: true
    AZURE_TOKEN: $(System.AccessToken) # Mandatory when BLACKDUCKSCA_PRCOMMENT_ENABLED is set to 'true'
    
    ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
    # INCLUDE_DIAGNOSTICS: true
    
    ### Uncomment below configuration to specify the project directory
    # PROJECT_DIRECTORY: $(PROJECT_DIRECTORY)
    
    ### To enable the use of self-signed certificates
    # NETWORK_SSL_TRUSTALL: true
    
    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'
    
    ### Detect Tool Settings
    # DETECT_SEARCH_DEPTH: 2
    # DETECT_ARGS: '--detect.diagnostic=true'
    # DETECT_CONFIG_PATH: '/Users/tmp/application.properties'
    
    ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
    # continueOnError: true
    
    ### Uncomment below configuration to add custom logic based on return status    
    # - task: CmdLine@2
    #   displayName: 'Command Line'
    #   condition: not(eq(variables['BlackDuckSecurityScan.status'], '0'))
    #   inputs:
    #     script: |
    #       echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)      
            
    ### Uncomment below to upload to Advanced security  
    #- task: AdvancedSecurity-Publish@1
    #   inputs:
    #     SarifsInputDirectory: '.bridge/Blackduck SCA SARIF Generator' # When the bridge version is lower than 3.5.0
    #     SarifsInputDirectory: '$(Build.SourcesDirectory)/sarif' # When the bridge version is greater than 3.5.0
```

Note: `continueOnError` is required to use returned status from Black Duck Security Scan Extension in subsequent tasks if `MARK_BUILD_STATUS` is not set or set to FAILED.

**Here is an example using SARIF reports for Black Duck SCA:**

To upload SARIF files to Advanced Security using Black Duck Security Scan, you must configure the `AdvancedSecurity-Publish@1` task with the following input:

- `SarifsInputDirectory`: Use this field to specify the path to the directory containing the SARIF file to be published to Advanced Security. This is a mandatory field.
  - If `BLACKDUCKSCA_REPORTS_SARIF_CREATE` is set to `true`, and `BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH` is not provided, `SarifsInputDirectory` will be the default directory for SARIF creation. You must input the directory path **excluding the file name**.

    For example: `.bridge/Blackduck SCA SARIF
    Generator/report.sarif.json` is the default file path for SARIF creation (when Bridge version is lower than 3.5.0), therefore you must input `.bridge/Blackduck SCA SARIF Generator` to `SarifsInputDirectory`.

    (When Bridge version is greater than 3.5.0, the default file path for SARIF creation is `.blackduck/integrations/blackducksca/sarif/report.sarif.json`.)
  - If `BLACKDUCKSCA_REPORTS_SARIF_CREATE` is set to `true`, and a custom path is provided to `BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH`, then you must provide the same path **excluding the file name** to `SarifsInputDirectory`.

    For example: if `$(Build.SourcesDirectory)/sarif/report.sarif.json` is provided to `BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH`, then you must provide `$(Build.SourcesDirectory)/sarif` to `SarifsInputDirectory`.
  - When using a custom path, if there are multiple SARIF files under the path used in `SarifsInputDirectory`, the Azure task `AdvancedSecurity-Publish@1` will combine all SARIF files and upload them to Advanced Security. Therefore, make sure to keep the relevant SARIF file under this path.
- `Category`: This is an optional field and should be left blank.

Note: For the `AdvancedSecurity-Publish@1` task, only `SarifsInputDirectory` is required. The other input fields are not required or may not be relevant.

Here is a complete example:

```
trigger:
  - master

pool:
  vmImage: ubuntu-latest
  #name: Default

variables:
  - group: Blackduck

steps:
  - task: BlackDuckSecurityScan@2
    displayName: 'Black Duck'
    condition: not(eq(variables['Build.Reason'], 'PullRequest'))

    ### Use below configuration to set specific detect environment variables
    env:
      DETECT_PROJECT_NAME: $(Build.Repository.Name)
    inputs:
      BLACKDUCKSCA_URL: $(BLACKDUCKSCA_URL)
      BLACKDUCKSCA_TOKEN: $(BLACKDUCKSCA_TOKEN)
      BLACKDUCKSCA_SCAN_FULL: false
      AZURE_TOKEN: $(System.AccessToken)  # Mandatory when BLACKDUCKSCA_PRCOMMENT_ENABLED is set to 'true'

      ### Uncomment below configuration if Bridge diagnostic files need to be uploaded
      INCLUDE_DIAGNOSTICS: true

      ### SARIF report generation
      BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
      BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH: "$(Build.SourcesDirectory)/sarif/report.sarif.json"
      BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES: "CRITICAL, HIGH, MEDIUM, LOW"
      BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES: true

  - task: AdvancedSecurity-Publish@1
    inputs:
      SarifsInputDirectory: '$(Build.SourcesDirectory)/sarif'
```

Table 1. List of mandatory and optional parameters for Black Duck® SCA

| **Input parameter** | **Description** | **Mandatory / optional** |
| --- | --- | --- |
| `AZURE_TOKEN` | Azure Access Token  **Example**: `AZURE_TOKEN: $(System.AccessToken)` or `AZURE_TOKEN: $(PAT_TOKEN)` | Mandatory if `BLACKDUCKSCA_PRCOMMENT_ENABLED`or`BLACKDUCKSCA_FIXPR_ENABLED` is set as `true`. |
| `BLACKDUCKSCA_PRCOMMENT_ENABLED` | Option to enable automatic creation pull request comments for new issues found in the pull request.  Baseline full scan results must exist on the server for this feature to work. Note: The merge request from the feature branch to the main branch must exist for this feature to work. **Default**: `false` | Optional |
| `BLACKDUCKSCA_FIXPR_ENABLED` | Enables or disables the automated creation of fix pull request for Black Duck® SCA.  **Default**: false. | Optional |
| `BLACKDUCKSCA_FIXPR_CREATESINGLEPR` | Creates only a single Fix PR if multiple issues are found.  **Accepted values**: `true`, `false`  **Default**: `false`. | Optional |
| `BLACKDUCKSCA_FIXPR_FILTER_SEVERITIES` | Creates Fix PRs only for issues with the severity level specified. If the value is "HIGH", only issues with that severity will have Fix PRs. The value is a comma-separated list.  **Supported severities:** `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`  **Default**: "`CRITICAL, HIGH`" | Optional |
| `BLACKDUCKSCA_FIXPR_MAXCOUNT` | Maximum number of pull requests allowed on a branch when policies are violated. A PR is created for each vulnerable component. | Optional |
| `BLACKDUCKSCA_FIXPR_USEUPGRADEGUIDANCE` | Black Duck® SCA Hub upgrade guidance values.  **Default**: "SHORT_TERM, LONG_TERM" | Optional |
| `DETECT_INSTALL_DIRECTORY` | Installation directory for Detect | Optional |
| `BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES` | Black Duck® SCA scan failure severities used to decide if build should be broken.  **Supported values**: `ALL`, `NONE`, `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`, `OK`, `TRIVIAL`, `UNSPECIFIED`. | Optional |
| `BLACKDUCKSCA_SCAN_FULL` | Specifies whether full scan is required or not.  Must be set to `true` for push events and `false` for pull request events. **Default**: `false` | Optional |
| `BLACKDUCKSCA_TOKEN` | Black Duck® SCA API token | Mandatory |
| `BLACKDUCKSCA_URL` | Black Duck® SCA URL | Mandatory |
| `BLACKDUCKSCA_REPORTS_SARIF_CREATE` | Set this to `true` to generate SARIF report. **Default:**`false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a PR/MR context. | Optional |
| `BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH` | File path (including file name) where SARIF report is created. Only `.sarif` or `.sarif.json` files will be uploaded. All other formats are excluded.  - When the bridge version is lower than 3.5.0, the **default** SARIF file path will be:   - `.bridge/Blackduck SCA SARIF Generator/report.sarif.json` - When the bridge version is greater than 3.5.0, then the **default** SARIF file path will be:   - `.blackduck/integrations/blackducksca/sarif/report.sarif.json` | Optional |
| `BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES` | When set to true, SCA issues are grouped by component. Set this to `false` to list SCA issues by vulnerability. **Default:**`true` | Optional |
| `BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`. **Default:** All severities are included. | Optional |
| `PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `DETECT_SEARCH_DEPTH` | Number indicating the search depth in the source directory. | Optional |
| `DETECT_ARGS` | Additional arguments for Detect. | Optional |
| `DETECT_CONFIG_PATH` | Detect config file path location. | Optional |
| `BLACKDUCKSCA_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |

Table 2. List of network parameters

| **Input parameter** | **Description** | **Mandatory / optional** |
| --- | --- | --- |
| `NETWORK_SSL_TRUSTALL` | Disables SSL certificate verification. Use with caution.  **Default**: false | Optional |

- **Classic Editor**:

  In the Classic Editor SSL Certificates can be configured within the `Network Options` section. Please note only the **Trust All SSL Certificates** options is supported for Black Duck SCA:

  [image: Azure (classic) network options]
