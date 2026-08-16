---
title: "Using the Black Duck Security Scan Action with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-action-with-coverity.html"
content_id: "dPEl2ehUTaTVSXGo76rtPg"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:47.356723+00:00"
---

# Using the Black Duck Security Scan Action with Coverity

On push events, a full Coverity scan will be run and results are committed to the Coverity server database.

On pull request events, comments are added to pull requests for new issues found by the scan if `coverity_prComment_enabled` is set to `true` (see example below). New issues detected by the scan are uploaded to the Coverity server (CNC and Connect) as preview commits.

When adding pull request comments, you must have a baseline scan on your main branch. When another branch is merged with your main, a scan will be triggered. While pull request comments are turned on, they will be triggered by the scan if the branch introduces a new vulnerability.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments

Before running the pipeline with Black Duck Security Scan Action, make sure the specified project and stream exist in your Coverity server environment.

Below is an example of a `workflow.yml` file configured for Coverity Cloud Deployment.

```
name: CI-Coverity-Basic
on:
  push:
    branches: [ main, master, develop, stage, release ]
  pull_request:
    branches: [ main, master, develop, stage, release ]
  workflow_dispatch: 

jobs:
  build:
    runs-on: [ ubuntu-latest ]
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5
      - name: Coverity Scan
        uses: blackduck-inc/black-duck-security-scan@v2
        with:
          ### SCANNING: Required fields
          coverity_url: ${{ vars.COVERITY_URL }}
          coverity_user: ${{ secrets.COVERITY_USER }}
          coverity_passphrase: ${{ secrets.COVERITY_PASSPHRASE }}
                            
          ### Coverity Connect users - Uncomment below
          # coverity_local: true
          
          ### POLICY ENFORCEMENT: Uncomment to break build on policy
          # coverity_policy_view: 'Outstanding Issues'
          
          ### PULL REQUEST COMMENTS:
          coverity_prComment_enabled: true
          ## Use the parameter below to add comments for issues filtered
          ## by impact. Default is High if unset
          ## NOTE: Issues matching coverity_policy_view are ignored if set
          # coverity_prComment_impacts: 'High,Medium,Low,Audit'
          github_token: ${{ secrets.GITHUB_TOKEN }} # Required when PR comments is enabled 
                            
          ### Mark build status if policy violating issues are found
          # mark_build_status: 'success'
                            
      ### Uncomment below configuration to add custom logic based on return status
      # - name: cmdLine
      #   id: cmdLine
      #   run: |
      #     EXIT_CODE=${{ steps.black-duck-security-scan.outputs.status }}
      #     echo "Black Duck Security Scan exit status - $EXIT_CODE"

      - name: Save Logs
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: bridge-logs
          path: ${{ github.workspace }}/.bridge
          include-hidden-files: true
```

Note: If you are using Coverity Connect, you need to uncomment `coverity_local: true` in the example below.

What follows is a more detailed example of a `workflow.yml` file configured for Coverity for more advanced users.

```
name: CI-Coverity-Basic
on:
  push:
    branches: [ main, master, develop, stage, release ]
  pull_request:
    branches: [ main, master, develop, stage, release ]
  workflow_dispatch: 

jobs:
  build:
    runs-on: [ ubuntu-latest ]
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5
      - name: Coverity Scan
        uses: blackduck-inc/black-duck-security-scan@v2.1.0
        with:
          coverity_url: ${{ vars.COVERITY_URL }}
          coverity_user: ${{ secrets.COVERITY_USER }}
          coverity_passphrase: ${{ secrets.COVERITY_PASSPHRASE }}
          coverity_project_name: ${{ github.event.repository.name }}
          coverity_stream_name: ${{ github.event.repository.name }}-${{ github.ref_name }}
          coverity_policy_view: 'Outstanding Issues'
          # coverity_waitForScan: false   # Used to support the async mode
          
          ### PULL REQUEST COMMENTS:
          coverity_prComment_enabled: true
          ## Use the parameter below to add comments for issues filtered 
          ## by impact. Default is High if unset
          ## NOTE: Issues matching coverity_policy_view are ignored if set
          # coverity_prComment_impacts: 'High,Medium,Low,Audit'
          github_token: ${{ secrets.GITHUB_TOKEN }} # Required when PR comments is enabled
          
          ### Arbitrary product-related CL arguments
          # coverity_build_command: mvn clean install
          # coverity_clean_command: mvn clean
          # coverity_config_path: /Users/Config/coverity.yml
          # coverity_args: -c /Users/Config/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install
        
          # project_directory: ${{ vars.PROJECT_DIRECTORY }}
        
          ### Coverity Connect users - Uncomment below
          # coverity_local: true
          
          ### POLICY ENFORCEMENT: Uncomment to break build on policy
          # coverity_policy_view: 'Outstanding Issues' 
          
          ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
          # include_diagnostics: true 
          
          ### Mark build status if policy violating issues are found
          # mark_build_status: 'success'
                      
      ### Uncomment below configuration to add custom logic based on return status
      # - name: cmdLine
      #   id: cmdLine
      #   run: |
      #     EXIT_CODE=${{ steps.black-duck-security-scan.outputs.status }}
      #     echo "Black Duck Security Scan exit status - $EXIT_CODE"

      - name: Save Logs
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: bridge-logs
          path: ${{ github.workspace }}/.bridge
          include-hidden-files: true
```

Table 1. **List of mandatory and optional parameters for Coverity**

| Input Parameter | Description | Mandatory / Optional |
| --- | --- | --- |
| `coverity_prComment_enabled` | Option to enable automatic creation pull request comments for new issues found in the pull request.    Baseline full scan results must exist on the server for this feature to work.    **Note**: The merge request from the feature branch to the main branch must exist for this feature to work.   **Default**: `false`   **Note**: When both `coverity_prComment_enabled` and `coverity_prComment_impacts` are configured for a Coverity PR scan, the `coverity_policy_view` setting will be ignored, and PR comments will be generated only for new issues that match the specified impact filter (`coverity_prComment_impacts`). Further details can be found here. | Optional |
| `coverity_prComment_impacts` | Comma-separated list of impacts that will cause Pull Request scans to fail.  Issues detected in the Pull Request that match any of the listed impact levels will be uploaded to Coverity, added as Pull Request comments and trigger build failure.    Valid impacts are: `High`, `Medium`, `Low` and `Audit`.    **Default**: `High` | Optional |
| `coverity_install_directory` | Installation directory of Coverity. | Optional |
| `coverity_local` | Set to `false` if you are using Coverity cloud deployment. Black Duck Security Scan Action will install Coverity Thin Client as necessary. Set to `true` if using on-premises Coverity Connect. When set to `true`, Black Duck Security Scan Action will install Coverity Analysis on the local system in order to execute the scan.  **Default**: `false`.  **Example:** `coverity_local: true`  Note: You can use an existing installation of Coverity tools by setting the `coverity_install_directory` option. | Optional |
| `coverity_passphrase` | Coverity passphrase. | Mandatory |
| `coverity_policy_view` | ID or name of policy view to be used to enforce the “break the build” policy.  If issues are found in the specified view, then the build will fail.  **Examples**: `coverity_policy_view: '100001'` or `coverity_policy_view: 'Outstanding Issues'` | Optional |
| `coverity_project_name` | Coverity project name.  Default value is the name of the repository, which includes repository name.  Tip: Many customers prefer to set their Coverity project and stream names to match the GitHub repository name. | Optional |
| `coverity_stream_name` | Coverity stream name. Default value in non PR context is set as `GITHUB_REPOSITORY-GITHUB_REF_NAME`.  Default value in PR context is set as `GITHUB_REPOSITORY-GITHUB_BASE_REF`. | Optional |
| `coverity_url` | Coverity URL. | Mandatory |
| `coverity_user` | Coverity username. | Mandatory |
| `coverity_version` | The version of Coverity to use. **Example**: `coverity_version: '2023.6.0'` | Optional |
| `github_token` | GitHub Access Token.  **Example**: `github_token: ${{ secrets.GITHUB_TOKEN }}` | Mandatory if `coverity_prComment_enabled` is set as `true` |
| `coverity_build_command` | Build command for Coverity. | Optional |
| `coverity_clean_command` | Clean command for Coverity. | Optional |
| `coverity_config_path` | Coverity config file path location. | Optional |
| `coverity_args` | Additional arguments for Coverity | Optional |
| `project_directory` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `coverity_waitForScan` | Specifies whether the workflow should wait for the analysis to complete or not. Supported values: `true` or `false`  **Default**: `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |

Table 2. **Network parameters**

| **Input Parameter** | Description | Mandatory / Optional |
| --- | --- | --- |
| `network_ssl_trustAll` | Disables SSL certificate verification. Use with caution. **Deafult:**`false` | Optional |
| `network_ssl_cert_file` | File path to configure the Http Calls to accept a self-signed certificate. | Optional |

Note:

1. Network parameters are for use with Coverity Connect. These parameters are not supported on Coverity CNC.
2. `network_ssl_trustAll=true` and `network_ssl_cert_file=<file
   path>` cannot be passed at the same time.
