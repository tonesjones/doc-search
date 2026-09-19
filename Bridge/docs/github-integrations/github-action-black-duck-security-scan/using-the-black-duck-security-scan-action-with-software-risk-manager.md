---
title: "Using the Black Duck Security Scan Action with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-action-with-software-risk-manager.html"
content_id: "GtOc_csY7NqtdUYPDS8MIQ"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:48.960748+00:00"
---

# Using the Black Duck Security Scan Action with Software Risk Manager

As a Software Risk Manager (SRM) customer, you can use GitHub Action to automate SCA and
SAST scanning in your CI pipeline.

Add the following code block to your existing `workflow.yml` file
in your `.github/workflows` directory.

Below is a simplified example of a `workflow.yml` file
configured for SRM.

```
name: CI-SRM-Basic 
on:
  push:
    branches: [ main, master, develop, stage, release ]
  workflow_dispatch:
jobs:
  build:
    runs-on: [ ubuntu-latest ]
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5
      - name: SRM Scan
        uses: blackduck-inc/black-duck-security-scan@v2
        with:
          ### SCANNING: Required fields
          srm_url: ${{ vars.SRM_URL }}
          srm_apikey: ${{ secrets.SRM_API_KEY }}
          srm_assessment_types: "SCA,SAST" 
          
          ### Mark build status if policy violating issues are found
          # mark_build_status: 'success'
          
          ### Uncomment below configuration to add custom logic based on return status
          # - name: cmdLine
          # id: cmdLine
          # run: |
          # EXIT_CODE=${{ steps.black-duck-security-scan.outputs.status }}
          # echo "Black Duck Security Scan exit status - $EXIT_CODE"
```

What follows is a more detailed example of a
`workflow.yml` file configured for SRM for more
advanced users.

```
name: CI-SRM
on:
  push:
    branches: [ main, master, develop, stage, release ]
  workflow_dispatch:
jobs:
  build:
    runs-on: [ ubuntu-latest ]
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5
      - name: SRM Scan
        uses: blackduck-inc/black-duck-security-scan@v2
        with:
          ### SCANNING: Required fields
          srm_url: ${{ vars.SRM_URL }}
          srm_apikey: ${{ secrets.SRM_API_KEY }}
          srm_assessment_types: "SCA,SAST"

          ### SCANNING: Optional fields
          # srm_project_name: ${{ vars.PROJECT_NAME }}
          # srm_project_id: ${{ vars.PROJECT_ID }}
          # srm_branch_name: ${{ vars.BRANCH_NAME }}
          # srm_branch_parent: ${{ vars.BRANCH_PARENT }}
          # srm_waitForScan: false   # Used to support the async mode 
          # detect_execution_path: ${{ vars.DETECT_EXECUTION_PATH }}
          # coverity_execution_path: ${{ vars.COVERITY_EXECUTION_PATH }}    
          # project_directory: ${{ vars.PROJECT_DIRECTORY }}
          
          ### Uncomment below to add arbitrary CL parameters
          # detect_search_depth: 2
          # detect_args: '--detect.diagnostic=true'
          # detect_config_path: '/Users/Config/application.properties'
          # coverity_build_command: mvn clean install
          # coverity_clean_command: mvn clean
          # coverity_config_path: /Users/Config/coverity.yml
          # coverity_args: --config-override capture.build.build-command=mvn install
```

Table 1. List of mandatory and optional parameters for SRM

| **Input Parameter** | Description | **Mandatory / Optional** |
| --- | --- | --- |
| `srm_url` | SRM Server URL. | Mandatory |
| `srm_apikey` | SRM API Key. | Mandatory |
| `srm_assessment_types` | SRM Assessment Types separated by comma. Accepted values:  `SAST` or `SCA` or`SAST`, `SCA`. | Mandatory |
| `srm_project_name` | Project name in SRM Server. The Default Value is `$(Build.Repository.Name)` | Optional |
| `srm_project_id` | Project id in SRM Server | Optional |
| `srm_branch_name` | Branch name on the SRM Server. The branch is created if it doesn't already exist. If a new branch name is passed to `srm_branch_name` parameter, `srm_branch_parent` should also be passed. otherwise error message will be displayed to the user. If an existing branch name is passed to `srm_branch_name`, `srm_branch_parent` is not required. | Optional |
| `srm_branch_parent` | Parent Branch name in SRM server. | Optional |
| `detect_execution_path` | Path to the Black Duck Detect jar  file to use. | Optional |
| `coverity_execution_path` | Path to Coverity CLI. | Optional |
| `project_directory` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `srm_waitForScan` | Specifies whether the workflow should wait for the analysis to complete or not. Supported values: `true` or `false`  **Default**: `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |
