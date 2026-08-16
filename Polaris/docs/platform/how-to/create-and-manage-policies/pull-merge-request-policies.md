---
title: "Pull/merge request policies"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/pull/merge-request-policies.html"
content_id: "KbFY26G77gxRLYd04Jve~A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:59.176843+00:00"
content_hash: "1d2a3117420d332f1fa450ba6675e7f42d7cb60f5589854fd2321a9ae9c41097"
---

# Pull/merge request policies

Use pull/merge request policies to enable pull request comments.

Organization Admins and Organization Application Managers can define when a pull request comment should be added to the relevant pull/merge request when a new issue is introduced.

Important: If you assign a pull/merge request policy to an application, project or branch that isn't connected to an SCM repository and does not fill the prerequisites below, it will not function as expected.

## Pull/merge request policy overview

When using Event-Based Test Automation, this policy allows you to turn on pull request comments at the application, project or branch level.

Note: Pull request comments are also available with integration via the Bridge. This information is for pull request comments from SCM Integrations via Polaris.

### Prerequisites

The following prerequisites must be met to use pull/merge request policies:

- Using Azure Repos, Bitbucket Cloud (Premium), GitHub, GitHub Enterprise, or GitLab SaaS (Premium or Ultimate).
- Onboarded to Polaris using SCM Integrations and Event-Based Test Automation has been enabled. See [Event-Based Test Automation in Polaris for SCM Integrations](../event-based-test-automation-in-polaris-for-scm-integrations.md).
- “A new pull request is created or updated” has been selected (either default or non-IDE branches) in your test automation.
- For Fail PRs:
  - Correct configuration of your SCM Integration, see [Fix Pull Requests (Fix PR)](../fix-pull-requests-fix-pr.md)
  - For Block PR, organization or application settings under Event-Based Test Automation must include block setting.

Note: For the first test, or when you run a full analysis after a rapid scan, expect a high number of pull request comments.

### Rules

You can add up to five rules to each pull/merge request policy. Rules control what actions occur when test results match the filter (when issues with specific properties are detected in a test). Set up rules to monitor tests for issues with any combination of the following properties:

- Issues with different fix-by statuses.

  Table 1. Fix-by statuses

  | Fix-by status | Description |
  | --- | --- |
  | Overdue | The issue was not fixed before its fix-by date. |
  | Due Soon | There are 7 or fewer days before the issue must be fixed. |
  | On Track | There are 8 or more days before the issue must be fixed. |
  | Not Set | The issue does not have a fix-by date. |
- Issues captured in SAST or SCA scans.
- Issues with specific severities.
- Issues with specific triage statuses (including dismissed due to a component being excluded).
- Issues on the CISA KEV list.
- Issues from a particular standard (for example, OWASP® Top 10 API Security Risks 2023).
- Issues with specific Common Weakness Enumeration (CWE™) codes.
- Issues with reachable vulnerabilities.

### Action

If your rule is matched, then a pull request comment or Fail PR is created.

Note: You can add any action to a rule, but actions only function as expected when the prerequisites are met, and only run after a test is complete.

## View a pull/merge request policy's details

1. Go to Policies and open the Pull/Merge Request Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select View.

   [image: ui pr policies tab]

## Create a pull/merge request policy

1. Go to Policies and open the Pull/Merge Request Policies tab.
2. Click + Add Policy. The Add Pull/Merge Request Policies screen appears.

   [image: pr policy create]   

   Tip: Instead of creating a new policy, you can use an existing policy as a starting point (and adjust the policy as you wish). Click the icon at the end of a policy's row and select Duplicate.
3. Enter a Policy Name (required) and Short Description (optional).

   Note: Policy names are limited to 255 characters. Policy descriptions are limited to 512 characters.
4. Set up the policy's rules:
   1. Under Add Rule, select Add More.
   2. Select issue properties that trigger actions with the dropdown in the If... column:

      - Fix-By Status: Select one or more of Overdue, Due Soon, On Track, or Not Set.

        Note: We recommend you don't use Fix-By Status in conjunction with other properties. Instead, create a separate rule (or a separate issue policy) to automate actions with fix-by statuses.
      - Tool Type: Select either SAST and/or SCA.

        Note: Pull/Merge Request policies only work for SCM Integration SAST and SCA scans. If the tool type DAST is selected, no pull request comments will be created.
      - Exposure: Select Reachable and/or Undetermined.
      - Severity: Select one or more of Critical, High, Medium, Low, or Informational.
      - Triage Status: Select one or more of Not Triaged, To Be Fixed, or Dismissed (including Dismissed False Positive, Dismissed Intentional, Dismissed Other, and/or Dismissed Component Excluded).

        Note: We recommend adding Not Triaged and To Be Fixed properties to most rules. Doing so prevents issues you dismiss from being flagged as violations.
      - On CISA KEV List: Select Yes to match issues that are on the CISA KEV list, or No to match issues that are not on the list.
      - Standard: Select one or more standard issue lists (OWASP Top 10 API Security Risks 2023,OWASP Web Top Ten 2017, OWASP Web Top Ten 2021, 2021 CWE Top 25, PCI DSS 2018, 2022 CWE Top 25, or 2023 CWE Top 25), and then one or more issues from the selected lists.
      - CWE: Set a numerical range for weaknesses found. Separate entries with commas (`256, 5-10, CWE-5, <300, >=400`).
   3. Select the actions to perform when issues with matching properties are detected in a test with the dropdown in the then... column:

      - Create pull request comments.
      - Fail pull/merge request.
   4. To add additional rules to the policy, repeat these steps.

      Note: You can add up to five rules to each pull/merge request policy. You can deactivate rules with the slider in the Status column. Dropdown menus in the If... and then... cannot be empty.
5. Click Save.

The pull/merge request policy is saved. To apply it, you can:

- Assign it to specific applications, projects, or branches. See [Change the policies assigned to applications, projects, and branches](change-the-policies-assigned-to-applications-projects-and-branches.md) for more information.
- Add the policy to your organization's default policies (provided you have Organization Admin permissions). See Change your organization's default pull/merge request policy for more information.

## Modify a pull/merge request policy

1. Go to Policies and open the Pull/Merge Request Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Edit.
3. Modify the policy, as required.
4. Select Save.

## Change your organization's default pull/merge request policy

Organization Admins can change your organization's default pull/merge request policies. See [Manage your default policies](manage-your-default-policies.md) for more information.

## Delete a pull/merge request policy

1. Go to Policies and open the Pull/Merge Request Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Delete.

   A confirmation appears.
3. Click OK to delete the policy.

   CAUTION:

   Policies you delete cannot be recovered.
