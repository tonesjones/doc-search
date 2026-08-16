---
title: "Issue policies"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-policies.html"
content_id: "xksQiquDuySuB2qFkyxbog"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:58.307180+00:00"
content_hash: "1c580a27aac4fd2be60dd6dc757d81a5f224afd61801001fec4dcaed9dc38cdd"
---

# Issue policies

Use issue policies to automate actions when issues with specific properties are detected in a test.

## Issue policy overview

Organization Admins and Organization Application Managers can create and manage issue policies on the Policies page. Issue policies are comprised of Rules, Actions, and Fix-by dates.

### Rules

You can add up to five rules to each issue policy. Rules control what actions occur when test results violate a policy (when issues with specific properties are detected in a test). Set up rules to monitor tests for issues with any combination of the following properties:

- New and/or preexisting issues.
- Issues with different fix-by statuses.

  Table 1. Fix-by statuses

  | Fix-by status | Description |
  | --- | --- |
  | Overdue | The issue was not fixed before its fix-by date. |
  | Due Soon | There are 7 or fewer days before the issue must be fixed. |
  | On Track | There are 8 or more days before the issue must be fixed. |
  | Not Set | The issue does not have a fix-by date. |
- Issues captured in SAST, SCA, or DAST scans.
- Exposure of identified vulnerabilities (Reachable and/or Undetermined)
- Issues with specific severities.
- Issues with modified severities.
- Issues with specific triage statuses (including dismissed due to a component being excluded).
- Issues on the CISA KEV list.
- Issues from a particular standard (for example, OWASP® Top 10 API Security Risks 2023).
- Issues with specific Common Weakness Enumeration (CWE™) codes.
- Issues with specific issue risk scores.

### Actions

You can assign the following actions to each rule in an issue policy:

Note: You can add any action to a rule, but actions only function as expected when the prerequisites are met, and only run after a test is complete.

Table 2. Actions and action prerequisites

| Action | Description | Prerequisites |
| --- | --- | --- |
| Send Notification | Send an email notification to Organization Admins when issues with specific properties are found in a test. Each email includes the names of one or more violated issue policies, the violated rules in each policy, the total quantity of violating issues for each rule, and helpful links. Click an issue quantity to view the issues that violate the rule in Polaris. Note: Email notifications for issue and component policies are only sent to Organization Admins. One email is sent each time a test's results violate one or more policies, and each email can include issues that violate more than one of each policy's rules. If a test's results violate issue and component policies, violated issue and component policies are listed in the same email. | Notifications must be enabled for the organization, and your personal notification settings must allow Policy notifications. |
| Attempt Build Break | For tests run via Bridge (including the Black Duck Security Scan Extension for Azure DevOps, the GitHub Action, the GitLab Template, and Black Duck Security Scan Plugin for Jenkins), attempt to break a build after issues with specific properties are found in a test. | The action only affects tests run using Bridge. Additionally, `polaris.waitForScan` must be set to `true` (default) in your pipeline. |
| Create and bundle to 1 external issue tracker ticket | When issues with specific properties are found in a test of a project's default branch, create a ticket. Each ticket includes the name of a violated policy, the violated rules in the policy, and helpful links. Click the name of a violated rule to view the issues that violate the rule in Polaris. Note: Tickets are only created for the default branch of a project. One ticket is created for each violated policy. The links to tickets created by issue policies can be modified. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.  Note: Synchronizing issue triage statuses with Jira ticket statuses is not supported for tickets created by this action. Synchronization only works for individually exported issues with a 1:1 link between a Polaris issue and a Jira ticket. See Create integration options for Jira for more information. | The project must be connected to Azure DevOps or Jira via a issue tracking integration. Note: For more information, see [Issue tracking integrations](../issue-tracking-integrations.md). |

### Fix-by dates

Add fix-by dates to your issue policies to help your developers prioritize issues for remediation, and enforce your organization's security standards across projects and applications. A policy's active fix-by dates are automatically applied to issues based on their severity. Fix-by dates are:

- Optional properties you can add to any issue policy.
- Not dependent on an issue policy's rules.
- Day-based (between 1 and 365 days).
- Severity-specific, so different fix-by dates can be assigned to issues with different severities.
- Shared across branches in your projects.
- Set relative to an issue's earliest first-detection date (on any branch).

Important: A policy will never overwrite a preexisting fix-by date, including fix-by dates set manually, and fix-by dates set by an issue policy.

If an issue with a fix-by date is resolved and later reintroduced (on any branch in the project), the fix-by date is restored. For example:

- A critical severity issue is detected on January 1 at 9:00 AM, and a policy applies a fix-by date of 7 days (January 8 at 9:00 PM).
- On January 5th, the issue is resolved (no longer detected in tests).
- On January 15th, the same issue is reintroduced (detected in a test of the same branch, or a different one).

In this scenario, the issue's fix-by date is restored to January 8 at 9:00 PM.

Note: You can manually set, change, or clear fix-by dates (including fix-by dates set by an issue policy) when you triage issues. When you manually set or change an issue's fix-by date, the fix-by time is set to 5:00 PM in your local timezone. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.

When multiple policies attempt to set an issue's fix-by date, the shortest fix-by date is used.

Fix-by dates don't depend on an issue policy's rules. For example:

- An issue policy is configured to send notifications for new critical severity issues.
- The issue policy includes active fix-by dates for critical, high, and medium severity issues.

In this example, fix-by dates are applied to all critical, high, and medium severity issues captured in tests subject to the policy (that don't already have fix-by dates).

Note: After you add fix-by dates to a policy, the policy's fix-by dates are not automatically applied to issues in your portfolio. Instead, you must re-test the projects that are subject to the policy to apply the policy's fix-by dates.

Note: If the project's Jira integration options include fix-by date synchronization, fix-by dates applied by issue policies are synchronized with the due date on linked Jira tickets. See Create integration options for Jira for more information.

### Multiple rule violations, multiple policy violations

*What happens when a test's results violate more than one rule in a policy?*

- When multiple Send Notification actions are triggered (for multiple rules in the same policy), violating issues are grouped together and sent to Organization Admins in the same email.
- When multiple Create and bundle to 1 external issue tracker ticket actions are triggered (for multiple rules in the same policy), Polaris creates one ticket that includes the names of the violated rules.

*What happens when a test's results violate more than one policy?*

- When Send Notification actions are triggered in different policies, one email is sent to Organization Admins that includes all violated policies.
- When Create and bundle to 1 external issue tracker ticket actions are triggered in different policies, one ticket is created for each violated policy.

*What happens when policies apply different fix-by dates to the same issue?*

- When multiple policies attempt to set an issue's fix-by date, the shortest fix-by date is used.

### Example issue policy

For example, say you create an issue policy with the following fix-by dates:

- Critical: 7 days
- High: 14 days
- Medium: 30 days
- Low or Informational: *Not active*

... and the following rules:

Table 3. Example issue policy

| Rule | Issue properties | Actions |
| --- | --- | --- |
| Rule one | New critical or high severity issues with not triaged or to be fixed triage statuses. | Send Notification and Attempt Build Break |
| Rule two | Existing critical or high severity issues with not triaged or to be fixed triage statuses. | Attempt Build Break |
| Rule three | New critical severity issues with not triaged or to be fixed triage statuses. | Create and bundle to 1 external issue tracker ticket |

In tests subject to this example issue policy:

- If the different action prerequisites are met:
  - Issues that were triaged and dismissed after an earlier test do not trigger actions.
  - For tests run using Bridge, builds will break when new and existing critical or high severity issues are detected.
  - An email notification is sent to Organization Admins when new critical or high severity issues are detected.
  - A ticket is created (in Azure DevOps or Jira, depending on the project's settings) when new critical severity issues are detected in a project's default branch.
- Fix-by dates are applied to critical, high, and medium severity issues that don't already have fix-by dates.

## View an issue policy's details

1. Go to Policies and open the Issue Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select View.

   [image: ui issue policies tab]

## Create an issue policy

Tip: Instead of creating a new issue policy, you can use a preexisting policy as a starting point (and adjust the policy as you wish). Click the options [image: icon polaris options] icon at the end of a policy's row and select Duplicate.

1. Go to Policies and open the Issue Policies tab.
2. Click + Add Policy. The Add Issue Policy screen appears.

   [image: policy issue create]
3. Enter a Policy Name (required) and Short Description (optional).

   Note: Policy names are limited to 255 characters. Policy descriptions are limited to 512 characters.
4. (Optional) Set up the policy's fix-by dates:
   1. Enable fix-by dates for different severities in the Active Status column.
   2. Adjust fix-by dates in the Fix-By column, as required.

      Note: Cells in the Fix-By column accept whole, positive numbers between 1 and 365.
5. (Optional) Set up the policy's rules:
   1. Under Add Rule, select Add More.
   2. Select issue properties that trigger actions with the dropdown in the If... column:

      - Detection Status: Select New, Existing or both.
      - Fix-By Status: Select one or more of Overdue, Due Soon, On Track, or Not Set.

        Note: We recommend you don't use Fix-By Status in conjunction with other properties. Instead, create a separate rule (or a separate issue policy) to automate actions with fix-by statuses.
      - Tool Type: Select either SAST, SCA, and/or DAST.
      - Exposure: Select Reachable and/or Undetermined.
      - Severity: Select one or more of Critical, High, Medium, Low, or Informational.
      - Severity Modified: Select Yes (modified) to match issues with modified severities, or No to match issues with default severities.
      - Triage Status: Select one or more of Not Triaged, To Be Fixed, or Dismissed (including Dismissed False Positive, Dismissed Intentional, Dismissed Other, and/or Dismissed Component Excluded).

        Note: We recommend adding Not Triaged and To Be Fixed properties to most rules. Doing so prevents issues you dismiss from being flagged as violations.
      - On CISA KEV List: Select Yes to match issues that are on the CISA KEV list, or No to match issues that are not on the list.
      - Standard: Select one or more standard issue lists (OWASP Top 10 API Security Risks 2023,OWASP Web Top Ten 2017, OWASP Web Top Ten 2021, 2021 CWE Top 25, PCI DSS 2018, 2022 CWE Top 25, or 2023 CWE Top 25), and then one or more issues from the selected lists.
      - CWE: Set a numerical range for weaknesses found. Separate entries with commas (`256, 5-10, CWE-5, <300, >=400`).
   3. Select the actions to perform when issues with matching properties are detected in a test with the dropdown in the then... column:

      - Send notification
      - Attempt Build Break
      - Create and bundle to 1 external issue tracker ticket
   4. To add additional rules to the policy, repeat these steps.

      Note: You can add up to five rules to each issue policy. You can deactivate rules with the slider in the Status column. Dropdown menus in the If... and then... cannot be empty.
6. Click Save.

The issue policy is saved. To apply it, you can:

- Assign it to specific applications, projects, or branches. See [Change the policies assigned to applications, projects, and branches](change-the-policies-assigned-to-applications-projects-and-branches.md) for more information.
- Add the policy to your organization's default policies (provided you have Organization Admin permissions). See Change your organization's default issue policy for more information.

## Modify an issue policy

1. Go to Policies and open the Issue Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Edit.
3. Modify the policy, as required.
4. Select Save.

## Change your organization's default issue policy

Organization Admins can change your organization's default issue policies. See [Manage your default policies](manage-your-default-policies.md) for more information.

## Delete an issue policy

1. Go to Policies and open the Issue Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Delete.

   A confirmation appears.
3. Click OK to delete the policy.

   CAUTION:

   Policies you delete cannot be recovered. Each issue policy can be assigned to multiple projects and branches.
