---
title: "Using the Black Duck Security Scan Plugin with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-plugin-with-coverity.html"
content_id: "d9GyXZQD6xmHZ9UncmbR0w"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:43.424547+00:00"
---

# Using the Black Duck Security Scan Plugin with Coverity

The Black Duck Security Scan Plugin can be used with Jenkins Multibranch, Pipeline and Freestyle projects.

Note: The Jenkins dashboard link and issue count for Coverity scans is applicable for push events only. The dashboard link is not shown for Pull Requests.

Coverity scans is applicable for push events only. The dashboard link is not shown for Pull Requests.

## Choose pipeline for use with Coverity

Use the decision table below to choose a suitable type of Jenkins pipeline and view examples for Coverity.

| Pipeline type | Use when... | Example |
| --- | --- | --- |
| **Multibranch Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred. - Enterprise applications requiring full feature set. - PR Comments are required. | Multibranch Pipeline |
| **Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred. - Push/merge scans only needed for protected branches. - PR Comments not required. | Pipeline |
| **Freestyle** | Simplest method:   - UI based scan configuration. - Push/merge scans only needed for protected branches. - PR Comments not required. | Freestyle |

Note: By default, Coverity server URL, user and password parameters configured in the Black Duck Security Scan Plugin are used by all Multibranch Pipeline, Pipeline and Freestyle projects. For Multibranch and Pipeline projects these parameters can be overridden in the Jenkinsfile using the `coverity_url`, `coverity_passphrase` and `coverity_user` parameters. For Jenkins freestyle projects these parameters **cannot** be overriden.

## Test connection configuration for committer role in Coverity instance

Users with Committer role must have the Access web services permission to test the connection with Coverity instance and this permission needs to be enabled if it is not enabled already.

Steps to enable Access web services permission for Committer role:

1. Login with an Admin user
2. Go to Configuration → Roles
3. Select Committer Role and click on Edit button
4. Enable Permission Access web services
5. Click OK → Done

## Coverity scan parameters

| Input parameter | Description | Mandatory / optional |
| --- | --- | --- |
| `bitbucket_token` | Applies to Bitbucket users. The token can be configured in Jenkins global configurations or can be passed as environment variable. This is required if `prcomment` is set to true. Example: `bitbucket_token: "${env.BITBUCKET_TOKEN}"` | Optional (mandatory for PR comment when used for bitbucket) |
| `github_token` | Applies to GitHub users. The token can be configured in Jenkins global configurations or can be passed as environment variable. Example, `github_token: "${env.GITHUB_TOKEN}"` | Optional (mandatory for pr comment) |
| `gitlab_token` | Applies to GitLab users. The token can be configured in Jenkins global configurations or can be passed as environment variable. Example, `gitlab_token: "${env.GITLAB_TOKEN}"`. | Optional |
| `coverity_prComment_enabled` | When set to `true`, pull request comments are created automatically for new issues found in the pull request. This feature requires a full scan to exist on the server prior to use. Once you have completed a full scan, it will serve as a baseline, and then you may set `coverity_prComment_enabled=true`.  Additionally, the merge request from your feature branch to your main branch must exist for this feature to work.  **Default:**`false`  Note: When both `coverity_prComment_enabled` and `coverity_policy_view` are configured for a Coverity PR scan, the `coverity_policy_view` setting will be ignored and PR comments will be generated only for new issues that match the specified impact filter (`coverity_prComment_impacts`). Further details can be found here. | Optional |
| `coverity_prComment_impacts` | Comma-separated list of impacts that will cause Pull Request scans to fail.  Issues detected in the Pull Request that match any of the listed impact levels will be uploaded to Coverity, added as Pull Request comments and trigger build failure.    Valid impacts are: `High`, `Medium`, `Low` and `Audit`.    **Default**: `High` | Optional |
| `coverity_install_directory` | The directory path used to install Coverity. | Optional |
| `coverity_local` | Used to support local analysis. Supported values are `true` and `false`. | Optional |
| `coverity_passphrase` | The password for Coverity. | Mandatory (unless configured in Jenkins Global Configuration) |
| `coverity_policy_view` | The ID number/Name of a saved view to apply as a "break the build" policy. If any defects are found within this view when applied to the project, the build will fail with an exit code. For example, `coverity_policy_view: '100001'` or `coverity_policy_view: 'Outstanding Issues'`. | Optional |
| `coverity_project_name` | Coverity project name.  The default value is the name of the repository. | Optional for multibranch (Mandatory for freestyle and pipeline jobs) |
| `coverity_stream_name` | Coverity stream name.  Default value in non PR context is set as **REPOSITORY_NAME-BRANCH_NAME**  Default value in PR context is set as **REPOSITORY_NAME-CHANGE_TARGET** | Optional for multibranch (Mandatory for freestyle and pipeline jobs) |
| `coverity_url` | The URL for the Coverity server. | Mandatory (unless configured in Jenkins Global Configuration) |
| `coverity_user` | The username for Coverity. | Mandatory (unless configured in Jenkins Global Configuration) |
| `coverity_version` | Download the specified Coverity version rather than downloading the default latest version. | Optional |
| `product` | Name of the Black Duck security product. Example: `product: "COVERITY"` | Mandatory |
| `project_directory` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `coverity_build_command` | Build command for Coverity. | Optional |
| `coverity_clean_command` | Clean command for Coverity. | Optional |
| `coverity_config_path` | Coverity config file path location. | Optional |
| `coverity_args` | Additional arguments for Coverity. | Optional |
| `coverity_waitForScan` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |

### Network parameters

| **Input parameter** | Description |
| --- | --- |
| `network_ssl_cert_file` | Path to a file that includes one or more trusted CA certificates. Supported formats: PEM, CRT.  Example: `network_ssl_cert_file: 'path/to/cert/cert.pem'` |
| `network_ssl_trustAll` | Disables SSL certificate verification. Use with caution.  Example: `network_ssl_trustAll: true` |

Note:

1. Network parameters are for use with Coverity Connect. These parameters are not supported on Coverity CNC.
2. `network_ssl_trustAll=true` and `network_ssl_cert_file=<file path>`cannot be passed at the same time.
