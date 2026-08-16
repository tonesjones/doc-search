---
title: "Event-Based Test Automation in Polaris for SCM Integrations"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/event-based-test-automation-in-polaris-for-scm-integrations.html"
content_id: "1h4tAFLTrhhOgs_enTTArg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:14.209487+00:00"
content_hash: "c865ffff3f9de75ec0ec7e683592ed712499e196287236c00ca8f2bb246e53a7"
---

# Event-Based Test Automation in Polaris for SCM Integrations

## Overview

Event-based test automation allows you to manage testing with your onboarded SCM repositories. If selected, testing in Polaris will be triggered by merge events in your SCM environment. This can be turned on or off at the organization, application, project, and branch levels in the Polaris UI.

Note: Organization Admins can monitor event-based testing activity in audit logs (My Organization > Audit Logs).

### Prerequisites

- Only available for Azure Repos, Bitbucket Cloud (Premium), GitHub, GitHub Enterprise, or GitLab SaaS (Premium or Ultimate).
- An SCM integration that supports event-based testing automation (see [Connect a Polaris project to a repository in your SCM](connect-a-polaris-project-to-a-repository-in-your-scm.md) or Connect Polaris to Multiple SCM Repositories).
- The access token used for integration must fit token requirements .
  - Azure Tokens for SCM Bulk Integration and/or Monitoring
  - Bitbucket Tokens for SCM Bulk Integration and/or Monitoring
  - GitHub Tokens for SCM Bulk Integration and/or Monitoring
  - GitLab Tokens for SCM Bulk Integration and/or Monitoring
- If you plan on using PR comments:
  - For pull request comments, create or assign a pull/merge request policy (see [Pull/merge request policies](create-and-manage-policies/pull-merge-request-policies.md)) and enable "A new pull request is created or updated" in your test automation.
  - For Fix PRs, see [Fix Pull Requests (Fix PR)](fix-pull-requests-fix-pr.md)
  - For Fail PRs, see [Fail Pull Requests (Fail PR)](fail-pull-requests-fail-pr.md)

### Setting inheritance

Event-based test automation settings set at the organization-level serve as defaults for all the applications, projects, and branches in your portfolio. However, test automation settings assigned to applications, projects, and branches take precedence:

- An application's settings override organization-level test automation settings.
- A project's settings override both application and organization-level test automation settings.
- A branch's settings override project, application, and organization-level test automation settings.

To check the active event-based test automation settings for an application or project, open the Analysis tab.

- For an application, go to Portfolio > select an application > Settings > Analysis.
- For a project, go to Portfolio > select an application > select a project > Settings > Analysis.

When Inherited appears at the top of the SCM Event-based Test Automation panel, the automation settings that apply to the application (example below) or project are inherited.

[image: Screenshot of the Event-based Test Automation panel for an application.]

To check the active event-based test automation settings for a branch, go to Portfolio > select an application > select a project > Branches > select a branch. When Inherited appears near Test Automation, the automation settings that apply to the branch are inherited.

[image: Screenshot of the Event-based Test Automation settings for a branch.]

## Update organization-level event-based test automation settings

Changing the settings will cause all appslications and projects that are inheriting the settings to get new settings. To manage organization-level test automation settings:

Note: Only Organization Administrators can manage organization-level test automation settings.

1. Go to My Organization > Analysis.
2. Select Edit next to SCM Event-based Test Automation.
3. Modify your organization's event-based test automation settings, as required.
   1. Select the events that trigger a test: A new pull request is created or updated, A pull request is merged, or both.

      These options are available for both default and non-default branches.

      To enable pull request comments, enable A new pull request is created or updated and assign a pull/merge request policy (see [Pull/merge request policies](create-and-manage-policies/pull-merge-request-policies.md)).
   2. Select if tests are SAST (Full or Rapid), SCA, or both test types.

      Note: Rapid Scan Static tests provide quick results, whereas full SAST tests provide more in-depth but time-consuming analysis. The initial test should be full. Rapid scans are recommended for new pull requests, and full analysis for merges. Before a rapid scan, if the system detects no full analysis has run on the project with the same tool version, it converts the scan to full. Subsequent scans for that tool version run as rapid scans.
   3. Option to select Block merge when policy fails pull/merge then select Default branches only or All branches. It requires a fail pull/merge request policy. See [Fail Pull Requests (Fail PR)](fail-pull-requests-fail-pr.md)
4. Select Save.

## Update application-level event-based test automation settings

To manage application-level test automation settings, follow these steps:

Note: Organization Administrators, Organization Application Managers, and other users with permissions to manage application settings can manage application-level test automation settings.

1. Go to Portfolio and open an application.
2. Go to Settings > Analysis.
3. Select Edit next to SCM Event-based Test Automation.
4. Modify the application's test automation settings, as required.

   You can enable SAST (Full and/or Rapid) and SCA tests when, for default and non-default branches, A new pull request is created or updated and/or A pull request is merged.

   Note: Rapid Scan Static tests provide quick results, whereas full SAST tests provides more in-depth but time-consuming analysis. The initial test should be full. Rapid scans are recommended for new pull requests, and full analysis for merges. Before a rapid scan, if the system detects no full analysis has run on the project with the same tool version, it converts the scan to full. Subsequent scans for that tool version run as rapid scans.

   Note: For pull request comments, create or assign a pull/merge request policy (see [Pull/merge request policies](create-and-manage-policies/pull-merge-request-policies.md)) and enable "A new pull request is created or updated" in your test automation.
5. Select Save.

## Update project-level event-based test automation settings

To manage project-level test automation settings, follow these steps:

Note: Organization Administrators, Organization Application Managers, Application Administrators, and other users with permissions to manage project settings can manage project-level test automation settings.

1. Go to Portfolio, open an application, and open a project.
2. Go to Settings > Analysis.
3. Select Edit next to SCM Event-based Test Automation.
4. Modify the project's test automation settings, as required.

   You can enable SAST (Full and/or Rapid) and SCA tests when, for default and non-default branches, A new pull request is created or updated and/or A pull request is merged.

   Note: Rapid Scan Static tests provide quick results, whereas full SAST tests provides more in-depth but time-consuming analysis. The initial test should be full. Rapid scans are recommended for new pull requests, and full analysis for merges. Before a rapid scan, if the system detects no full analysis has run on the project with the same tool version, it converts the scan to full. Subsequent scans for that tool version run as rapid scans.

   Note: For pull request comments, create or assign a pull/merge request policy (see [Pull/merge request policies](create-and-manage-policies/pull-merge-request-policies.md)) and enable "A new pull request is created or updated" in your test automation.
5. Select Save.

## Update branch-level event-based test automation settings

To manage branch-level test automation settings, follow these steps:

Note: Organization Administrators, Organization Application Managers, Application Administrators, and other users with permissions to manage branch settings can manage branch-level test automation settings.

1. Go to Portfolio, open an application, and open a project.
2. Go to Branches.
3. Select the branch you wish to modify.
4. Modify the branch's test automation settings (under Test Automation), as required.

   You can enable SAST (Full and/or Rapid) and SCA tests when A new pull request is created or updated and/or A pull request is merged.

   Note: Rapid Scan Static tests provide quick results, whereas full SAST tests provides more in-depth but time-consuming analysis. The initial test should be full. Rapid scans are recommended for new pull requests, and full analysis for merges. Before a rapid scan, if the system detects no full analysis has run on the project with the same tool version, it converts the scan to full. Subsequent scans for that tool version run as rapid scans.

   Note: For pull request comments, create or assign a pull/merge request policy (see [Pull/merge request policies](create-and-manage-policies/pull-merge-request-policies.md)) and enable "A new pull request is created or updated" in your test automation.
5. Select Save.

## Reset event-based test automation settings

After you customize application, project, or branch-level test automation settings, you can select Reset to revert changes. When you reset an application's test automation settings, the application will inherit your organization-level test automation settings. When you reset a project's test automation settings, the project will inherit application (if set) or organization-level test automation settings. When you reset a branch's test automation settings, the branch will inherit project (if set), application (if set), or organization-level test automation settings.

1. Open the application, project, or branch's settings:
   - For an application, go to Portfolio > select an application > Settings > Analysis.
   - For a project, go to Portfolio > select an application > select a project > Settings > Analysis.
   - For a branch, go to Portfolio > select an application > select a project > Branches > select a branch.
2. Select Reset.

   After you reset branch-level test automation settings, select Save.
