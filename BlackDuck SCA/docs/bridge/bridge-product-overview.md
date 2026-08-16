---
title: "Bridge product overview"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-product-overview.html"
content_id: "iQXSk~S0hNK2YPe60lwDgw"
version: "latest"
section: "Bridge product overview"
scraped_at: "2026-08-08T23:46:48.492565+00:00"
---

# Bridge product overview

Bridge includes Bridge CLI, Black Duck Security App and Black Duck Security Scan for integrating Black Duck security testing into CI/CD workflows.

Bridge provides a unified way to integrate Black Duck security testing tools into CI/CD workflows. It enables teams to run scans as part of a single automated pipeline job using a consistent interface.

[image: Bridge Overview]

At its core, Bridge automates security testing for Black Duck® SCA, Coverity, Polaris and Software Risk Manager by invoking the appropriate scanning tools through a standardized workflow.

Black Duck provides CI native wrappers to support major source control and build platforms, including: GitHub Actions, GitLab templates, Azure DevOps extensions, Jenkins plugins and Bitbucket pipes.

For environments where CI native wrappers are not yet available, the Bridge CLI can be downloaded and used directly within pipelines, making it possible to automate Black Duck security tests on virtually any platform.

Apps are available for GitHub and Bitbucket to streamline on-boarding by generating and deploying workflow configurations to selected repositories, ensuring that Black Duck scans can be adopted across an organization with minimal configuration.

The table below illustrates the security assessments supported by each Black Duck product:

| Product | Assessment |
| --- | --- |
| Black Duck SCA | SCA |
| Coverity | SAST |
| Polaris | SCA, SAST, SCA and SAST, DAST |
| SRM | SCA, SAST |

## Building a bridge to enhanced application security

By acting as a bridge between source control platforms and a Black Duck security platform, Bridge enables organizations to implement security scanning as integral parts of the development process. This proactive approach identifies and addresses vulnerabilities early and creates a culture of security awareness among developers.

The workflow below illustrates the process for integrating Black Duck security scanning into development pipelines, enabling teams to identify and address vulnerabilities in source code and dependencies effectively through baseline scans, Pull Request scans and scans triggered by merges into monitored branches.

[image: Bridge workflow]

Bridge CLI uploads source code artifacts to the Black Duck server (Black Duck, Coverity, Polaris or Software Risk Manager) for scanning and analysis.

Scan results are collated and used to perform post scan operations:

- Inject Pull Request comments.
- Raise Fix Pull Requests.
- Create and upload SARIF reports to integrate with third party tools such as GitHub Advanced Security or GitLab Vulnerability reports. SARIF reports are generated after a full scan has been performed on a monitored branch, in response to a push event or via a Pull Request merge.
- Create issues in source code repository.
- Break the build for policy violations.

**Black Duck scan workflow**

1. **Baseline scan**: An initial baseline security scan is run in response to push events on monitored branches, such as main, develop, staging and release. A baseline scan establishes a reference point for comparing subsequent scans on a branch and enables Bridge to identify new issues introduced in a Pull Request. SARIF reports and repository issues can be created from baseline scan findings.
2. **Pull request scans**: A baseline scan must be run for the target branch before a Pull Request scan is run. Without a baseline scan on the target branch the PR is merging into the PR scan will fail. Pull Request scans report new issues introduced on a feature branch that are not present in the baseline scan, providing immediate feedback to developers before merging.

   Note: A Pull Request scan does not upload issues to the Black Duck platform
3. **Merge pull request**: Approved Pull Requests merged into a monitored branch, trigger a full scan of the code-base, with security issues uploaded to the integrated Black Duck platform, e.g. Black Duck SCA, Coverity, Polaris or Software Risk Manager. SARIF reports and repository issues can be created from scan findings when a Pull Request is merged into a monitored branch.

## What features does Bridge offer?

Use the feature matrices below to assist with choosing the Black Duck platform that aligns with the security testing objectives of your organization.

**Universal features**

| Platform | Supported assessments | Break build | Sync and async scans |
| --- | --- | --- | --- |
| Black Duck® SCA | SCA | ✅ | ✅ |
| Coverity | SAST | ✅ | ✅ |
| Polaris | DAST, SAST and SCA | ✅ | ✅ |
| Software Risk Manager | SAST and SCA | ✅ | ✅ |

**Baseline branch scan features**

| Platform | SARIF reports | Repository issues |
| --- | --- | --- |
| Black Duck® SCA | ✅ | ✅ |
| Coverity | ❌ | ❌ |
| Polaris | ✅ | ✅ |
| Software Risk Manager | ❌ | ❌ |

**Pull request scan features**

| Platform | Pull request scans | Pull request comments | Raise dependency fix pull requests |
| --- | --- | --- | --- |
| Black Duck® SCA | ✅ | ✅ | ✅ |
| Coverity | ✅ | ✅ | ❌ |
| Polaris | ✅ | ✅ | ✅ |
| Software Risk Manager | ❌ | ❌ | ❌ |

## Choose how to run Bridge

The Bridge ecosystem follows a stacked deployment model where the Bridge CLI delivers the core scanning capabilities, Bridge Security Scan wraps and automates those capabilities for CI/CD pipelines and the Bridge Security App provides the highest-level interface for configuring and managing those pipelines to selected repositories within an organization.

[image: Bridge product model]

- **Bridge CLI**: A command-line interface that serves as the foundation utility for both the Bridge Security App and Bridge Security Scan. The Bridge CLI can be used to script testing with any of the Black Duck platforms on virtually any testing platform. Bridge CLI is an ideal solution wherever there is a need to automate Black Duck Software products and the Bridge Security Scan or Bridge Security App is not supported for the Source Control Management platform. A full bundle or thin client is available for download.

  | Download | When To Use |
  | --- | --- |
  | [Bridge CLI Bundle](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) | Suitable for offline use, e.g. air-gapped environments. |
  | [Bridge CLI Thin Client](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-thin-client/latest/) | Suitable for use in cloud CI/CD environments. |

  Visit the Bridge download page for full download and installation information.
- **Bridge Security Scan**: Bridge Security Scan acts as a wrapper interface for the Bridge CLI, transforming configured parameters into CLI commands, allowing users to run tests within their CI/CD pipeline jobs. Compatible with Azure DevOps, Bitbucket, GitHub, GitLab and Jenkins CI/CD platforms. Automating security tests with Bridge Security Scan is the recommended solution, with facilitated access to new features and a standard interface to all Black Duck platforms.

  | Black Duck | Platform |
  | --- | --- |
  | Black Duck Security Scan Extension | Azure DevOps |
  | Black Duck Security Scan Pipe | Bitbucket |
  | Black Duck Security Scan Action | GitHub |
  | Black Duck Security Scan Template | GitLab |
  | Black Duck Security Scan Plugin | Jenkins |
- **Bridge Security App**: Web application that simplifies the configuration of a Black Duck CI/CD pipeline by modifying the pipeline configuration file dynamically depending upon which security scan options and Black Duck platform are configured. Repositories can be on-boarded from organizations or from within personal workspace, facilitating management and deployment of security scans. Bridge Security App is currently available for Azure DevOps, GitHub, GitLab and Bitbucket.

## What does Bridge cost?

Bridge is available for free for all Black Duck customers.

**Related Links**  

- Central Integrations release notes
- Bridge CLI product overview
- Bridge support matrix
