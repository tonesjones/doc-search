---
title: "Using Reachability Analysis"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/using-reachability-analysis.html"
content_id: "D_margwjeCZ_YbktijIeHw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:41.712602+00:00"
content_hash: "11225f3a7545a47a125ed2707620c7dc28adfa55c89f60323cd4f2eeb6575690"
---

# Using Reachability Analysis

Reachability Analysis is incorporated into Polaris SCA testing to determine whether identified component vulnerabilities are actively reachable from source code, providing precise remediation guidance.

Reachability Analysis makes SCA results more actionable by reducing false positives and focusing upgrade efforts on actively exploitable vulnerabilities.

Note: Reachability analysis is disabled by default. When enabled, it may increase package manager scan time.

Reachability analysis:

- Applies to SCA package manager scans only.
- Can be enabled or disabled by Organization Admins at the organization level.
- Is available for scans via Source or SCM.
- Reports results for vulnerabilities called through direct dependencies.
- Provides reachability evidence for vulnerabilities, including file and method signatures, showing where and how vulnerabilities are reachable in the code.
- For supported languages, see SCA Reachability Analysis Supported Languages.

## Reachability Analysis Settings

Reachability analysis is disabled by default. An Organization Admin must enable it at the organization level before it can be enabled at lower levels. Enabling it at the organization level does not automatically enable it for any application, project, or branch — each must be configured individually.

Project Admins can enable reachability analysis for individual applications, projects, and branches, balancing the tradeoff between scan performance and reachability coverage.

If an Organization Admin disables reachability at the organization level (for example, because it is slowing SCA scans) it is turned off across all applications, projects, and branches. This does not erase configurations at lower levels. When re-enabled at the organization level, all lower-level settings return to their previous state.

## Setting Inheritance

Organization-level reachability analysis settings control whether reachability analysis is available across your portfolio. Unlike other settings in Polaris, application-level settings are not inherited from the organization. Each application must be configured individually. Projects and branches inherit from their parent application, but project- and branch-level settings take precedence.

Inheritance rules:

- For reachability analysis to be available at any level, it must be enabled at the organization level.
- Applications do not inherit the organization setting. If the organization is enabled, each application remains disabled until the application-level setting is enabled.
- A project's settings inherit application-level settings but can be modified to override the application settings for that project.
- A branch's settings inherit application-level and project-level settings but can be modified to override the application and project settings for that branch.

To check active reachability analysis settings, open the Analysis tab in Settings at the relevant level:

- **Organization:** My Organization > Analysis
- **Application:** Portfolio > select an application > Settings > Analysis
- **Project:** Portfolio > select an application > select a project > Settings > Analysis
- **Branch:** Portfolio > select an application > select a project > select a branch > SCA Analysis

At the top of the Reachability Analysis panel, the settings status displays as one of the following:

Inherited
:   Settings are inherited from a parent level. For projects, inherited from the application. For branches, inherited from the application or project.

Modified
:   Settings have been edited at this level. Select Reset to return to Inherited.

## How to View and Manage Reachability Analysis

Note: If reachability filters are not visible in the Issues, Components, Policy, Reporting, or Dashboards screens, reachability analysis has not been enabled at the organization level.

| Where | Summary | Details |
| --- | --- | --- |
| Portfolio > select an application > select a project > Issues tab, select an issue > Exposure tab. | View reachability exposure for an individual issue. |  |
| Portfolio > select an application > select a project > Issues tab > Filter | View or triage all issues with exposure of identified vulnerabilities for a project. | Filter Exposure by Reachable and/or Undetermined. |
| Portfolio > select an application > select a project > Components tab, select a component > Security Details tab | View reachability information for an individual component. | A Reachable label appears next to the Security Details tab where applicable. The Details tab lists all issues aggregated from all component origins matched to that component version. |
| Dashboards | View exposure across all included applications, projects, and branches. | Filter Exposure by Reachable and/or Undetermined for selected applications, projects, and branches. By default, both are selected. Results are exportable. Dashboards that include reachability:  - Issue Summary Dashboard - Portfolio ROI Dashboards - Table - Component Search |
| Reporting | View exposure across all included applications, projects, and branches. | By default, both Reachable and Undetermined exposures are selected. Reports that include reachability information:  - Issue Summary Report - Standard Compliance - Standard Compliance Detail Report - Security Audit Report - Issue Overview Report - Developer Detail SCA Report - SBOM |
| Policies | Set rules based on exposure to trigger an action. | Filter Exposure by Reachable and/or Undetermined. Available for:  - Issue Policies - Pull/Merge Policies - Component Policies |

**Related tasks**  

- Enable reachability analysis at the organization level
- Enable reachability analysis at the application level
- Enable reachability analysis at the project level
- Enable reachability analysis at the branch level
