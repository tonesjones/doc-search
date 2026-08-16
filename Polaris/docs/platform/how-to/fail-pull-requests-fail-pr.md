---
title: "Fail Pull Requests (Fail PR)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/fail-pull-requests-fail-pr-.html"
content_id: "VFjnK3oWpnq20ERG3uyaYA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:38.676429+00:00"
content_hash: "e0ecf5a8b7583adfc0200b75e061c8763d11b9a68acb3d8ef84ad294d7a15b9a"
---

# Fail Pull Requests (Fail PR)

Polaris supports Fail PR for source code management (SCM) integrations with event-based test automation.

When a pull request matches the criteria of an assigned pull/merge request policy with a fail PR action, Polaris sends a warning. If you also have an event-based test automation setting (in the organization or application analysis sections) enabled blocking on either all or default branches, the merge will be blocked.

## Prerequisites

- Your SCM integration supports PR blocking.
- Supported SCM:
  - Azure (Basic, and Basic + Test plans)
  - Bitbucket (Premium)
  - GitHub Standard (public repositories only)
  - GitHub Enterprise
  - GitLab SaaS (Premium and Ultimate)
- SCM integration has been configured to support event-based testing automation (see [Event-Based Test Automation in Polaris for SCM Integrations](event-based-test-automation-in-polaris-for-scm-integrations.md)).
- Additional settings are required in SCM to support block for the following:
  - Bitbucket
  - GitLab

Note: The PR blocking feature is not available for all SCM integrations. Polaris displays a notification in the PR policy configuration and organization and application settings to indicate which SCMs support this functionality. If your SCM does not support blocking, you can still use the Fail PR policy to notify developers of failed scans.

## Roles

To manage policies and settings:

- You have a Polaris account with appropriate permissions (organization, application, or project admin).
- You have appropriate permissions in your SCM.

## Known Limitations

- Branch and project level configuration of warn/block is not currently available. Branch (default or all) is configurable at the application level and applied to all projects in the application.
- Not all SCM integrations support PR blocking at this time.
- Fix PR interaction: When a Fix PR is created on a branch that already has an open PR, it is treated as a PR edit and triggers a new scan.

## Overview

Fail PR uses the following components:

PR Policy (required)
:   The rule created in Pull/Merge Request Policies must include the Fail Pull/Merge Request action. By default, a warning is issued and the developer can merge unless the Block PR setting is enabled.

Block PR Setting (optional)
:   Configured at the organization or application level under Analysis >  SCM Event-based Test Automation. You can enable blocking and select default or all branches. If the block setting is not enabled, a warning is sent by default.

Note: There is no project-level or branch-level customization. Both PR Policy and Block PR Settings are available at the organization and application levels only.

## Example End-to-End Workflow

1. An organization is bulk onboarded, applying a pull request policy set to the Fail Pull/Merge Request action and an organization-level SCM Event-based Test Automation setting with block PR enabled across three repositories.
2. A pull request is created on a test branch containing both SAST and SCA vulnerabilities.
3. As soon as the PR is created, the merge button is blocked with a pending status.
4. Once the SAST and SCA scans complete, PR comments are automatically posted to the SCM interface.
5. The PR remains blocked with a message indicating a policy violation, along with a link to the specific scan results. This allows developers to identify and fix vulnerabilities directly from their SCM without logging into Polaris.
6. Within Polaris, issues can be filtered by Pull/Merge Request policy and other criteria to view details. Failed PRs can also be found in audit logs.

Note: Users with the correct access in the SCM can bypass the block and merge a failed PR. Regular users cannot merge a blocked PR.

## Fail PR Inheritance

Fail PR settings can be customized at the organization or application level. Organization-level settings serve as defaults for all applications and projects in your portfolio. Settings at lower levels take precedence:

- An application's settings override organization-level settings for that application.

To check the active Fail PR settings at each level:

- **Organization:** My Organization > Analysis (under Event-based Automatic Test)
- **Application:** Portfolio > select an application > Settings > Analysis

## Settings Status

At the top of the Event-based Automatic Test Settings panel, the settings status is shown as one of the following:

Inherited
:   The settings that apply to the application are inherited from the organization level.

Modified
:   The settings have been edited at this level. Selecting Reset returns them to Inherited.

## Rulesets

GitLab and Bitbucket require additional settings before rulesets can be configured. For more information, see:

- GitLab Settings for Fail PRs
- Bitbucket Settings for Fail PRs

For GitHub and Azure, Polaris automatically generates the required ruleset in the SCM when a pull/merge request policy with a Fail PR action and block settings are enabled. Rulesets are created for all repositories in the organization once bulk onboarding begins. Customers do not need to manually create rulesets in their SCM repositories.

Consider the following ruleset behavior:

- During bulk onboarding, if the block setting is enabled at the organization level, rulesets are automatically created for all new applications as they are onboarded.
- If the block setting was not enabled during bulk onboarding, no ruleset is created. The setting can be enabled at the application level afterward, which creates the ruleset at that point.
- If an application inherits organization settings and the organization-level setting is updated, the ruleset change cascades to all inheriting applications.
- If an application setting has been manually modified, it will not be affected by subsequent organization-level changes.

## How PR Scanning Works Before Merging

A PR scan must complete before a PR is eligible to be merged. Once the scan finishes, one of three outcomes determines whether the merge button is enabled:

- PR scan passes — Merge button is enabled.
- PR scan fails; project allows merging despite failures — Merge button is enabled.
- PR scan fails; project is configured to block merging — Merge button is disabled.

## Behavior Summary

The following table summarizes merge behavior based on configuration and scan state:

| Scenario | Policy Has Fail Action | Policy Has No Fail Action |
| --- | --- | --- |
| Scan is running — Block is configured | Developer cannot merge until scan completes | Developer cannot merge until scan completes |
| Scan is running — Block is NOT configured | Developer can merge while scan is running | Developer can merge while scan is running |
| Scan complete, policy violated — Block configured | Developer cannot merge | Developer can merge |
| Scan complete, policy violated — Block NOT configured | Developer can merge (with warning) | Developer can merge |

## PR Status Values

Polaris sends one of four statuses to the SCM for each pull request event:

Pending
:   Displayed as a yellow indicator while the test is being created or is queued. The PR cannot be merged during this state.

Success
:   Displayed when all tests complete with no policy violations. The PR can be merged.

Failed
:   Displayed when a policy with the Fail PR action is attached to the project and a policy violation is detected. The PR is blocked from merging. The SCM displays the reason, for example: "Policy evaluation has failed."

Error
:   Displayed when an issue occurs on the Polaris side, such as the test not being created, the test entering pending review, the user cancelling the test, or a policy failing to evaluate due to an internal error. The PR is blocked.

Note: A direct link to the Polaris test is provided in the SCM so users can check what was violated. If the test has been deleted, the link returns a 401.

## Fail-Fast Behavior with Multiple Test Types

When multiple test types are configured (for example, both SAST and SCA), Polaris applies fail-fast logic:

- If any test fails or returns an error before the others complete, Polaris immediately blocks the PR without waiting for remaining tests to finish.
- If a test completes with no violation, Polaris waits for all other configured tests to complete before sending a success status.
- A success status is only sent when all tests have completed without violations.

Note: PR comments are still populated for all tests regardless of fail-fast behavior, but only one blocking status is sent to the SCM once a failure or error is detected.

## Audit Logs

The following actions are recorded in Polaris audit logs for compliance and traceability:

| Audit Event | Description |
| --- | --- |
| PR policy created / changed / deleted | Captures any changes to the PR policy configuration. |
| PR failure action added / changed / removed | Captures changes to the warn/block configuration at the organization, application, or project level. |
| PR scan marked as failure | Recorded when a scan result triggers a policy failure. |
| PR blocked or warned | Noted as part of the PR scan audit event. |

## Frequently Asked Questions

Can a developer unblock their own PR?
:   Only if the developer has sufficient SCM-level permissions to override the block. In most configurations, only a security admin can unblock a PR by changing the setting from Block to Warn.

What happens if the scan cannot complete due to an error?
:   A scan error is treated as a failure. An incomplete scan cannot confirm whether vulnerabilities exist, so allowing a merge could allow vulnerable code through. The developer will see the failure in the SCM status check and a comment will be posted.

Do developers need access to Polaris to fix their PR?
:   No. All information needed to resolve the failing issues is included in the PR comment posted by Polaris. Developers can work entirely within their SCM interface.

Does this feature work with the Fix PR workflow?
:   When a Fix PR is created on a branch that already has an open PR, it is treated as a PR edit and triggers a new scan. The standard Fail PR and blocking behavior applies to that scan.
