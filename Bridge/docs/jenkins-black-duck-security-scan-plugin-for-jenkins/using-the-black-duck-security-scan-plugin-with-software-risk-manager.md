---
title: "Using the Black Duck Security Scan Plugin with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-plugin-with-software-risk-manager.html"
content_id: "9sS4cFPWQ6rUm3Qrn1DUeA"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:46.198138+00:00"
---

# Using the Black Duck Security Scan Plugin with Software Risk Manager

The Black Duck Security Scan Plugin can be used with Jenkins Multibranch, Pipeline and Freeestyle projects.

The Jenkins dashboard link and issue count for SRM scans are applicable for push events only. The dashboard link is not shown for pull requests.

## Choose pipeline for use with Software Risk Manager

Use the decision table below to choose a suitable type of Jenkins pipeline and view examples for Software Risk Manager.

| Pipeline type | Use when... | Example |
| --- | --- | --- |
| **Multibranch Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred. - Enterprise applications requiring full feature set. | Multibranch Pipeline |
| **Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred | Pipeline |
| **Freestyle** | - UI based scan configuration. | Freestyle |

Note: By default, Software Risk Manager server URL and access token configured in the Black Duck Security Scan Plugin are used by all Multibranch Pipeline, Pipeline and Freestyle projects. For Multibranch Pipeline and Pipeline projects, these parameters can be overridden in the Jenkinsfile using the `srm_url` and `srm_apikey` parameters. For Jenkins freestyle projects these parameters **cannot** be overridden.

## SRM parameters

| Input parameter | Description | Mandatory / optional |
| --- | --- | --- |
| `srm_url` | The URL for the SRM server. The URL can also be configured in Jenkins **Global Configuration** or passed as an **Environment Variable**. For example, `srm_url: "${env.SRM_URL}"`. | Mandatory (unless configured in Jenkins Global Configuration) |
| `srm_apikey` | The API Key for SRM. The API key can also be configured in Jenkins **Global Configuration** or passed as an **Environment Variable**. For example, `srm_apikey: "${env.SRM_APIKEY}"` | Mandatory (unless configured in Jenkins Global Configuration) |
| `srm_assessment_types` | SRM Assessment Types separated by comma. Accepted values: `SAST` or `SCA` or `SAST, SCA` | Mandatory |
| `srm_project_name` | Project name in SRM Server.  The default value is the name of the repository. | Optional for multibranch pipeline (Mandatory for freestyle and pipeline jobs) |
| `srm_project_id` | Project id in SRM Server. | Optional |
| `srm_branch_name` | Branch name on the SRM Server. The branch is created if it doesn't already exist. | Optional |
| `srm_branch_parent` | Parent Branch name in SRM server. | Optional |
| `detect_execution_path` | Path to the Black Duck Detect jar file to use. | Optional |
| `coverity_execution_path` | Path to Coverity CLI. | Optional |
| `project_directory` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `srm_waitForScan` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |
