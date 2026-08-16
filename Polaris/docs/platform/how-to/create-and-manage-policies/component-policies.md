---
title: "Component policies"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/component-policies.html"
content_id: "WEH9WFyQ3kk89_Am_VWQ2w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:00.081307+00:00"
content_hash: "5c27fe2c00dbdcf467250157eef37dc8e4d2c93551c816cfc57609cf96686231"
---

# Component policies

Use component policies to automate actions when components with specific properties are detected in an SCA test.

## Component policy overview

Organization Admins and Organization Application Managers can create and manage component policies on the Policies page. Component policies are comprised of Rules and Actions.

### Rules

You can add up to five rules to each component policy. Rules control what actions occur when test results violate a policy (when components with specific properties are detected in an SCA test). Set up rules to monitor tests for components with any combination of the following properties:

- Included or excluded from your SBOM.
- Exposure of identified vulnerabilities in components (Reachable and/or Undetermined).
- Declared and/or deep licenses. All or specify license families.

  Note: Deep license data, which is disabled by default, must be enabled for it to be included in violations.
- License status
- Direct or transitive dependencies.
- Different security risks.
- Components that contain issues on the CISA KEV list.
- Subject to specific licenses.
- Specific names of components.
- Specific match scores.

### Actions

You can assign the following actions to each rule in a component policy:

Note: You can add any action to a rule, but actions only function as expected when the prerequisites are met, and only run after a test is complete.

Table 1. Actions and action prerequisites

| Action | Description | Prerequisites |
| --- | --- | --- |
| Send Notification | Send an email notification to Organization Admins when components with specific properties are found in a test. Each email includes the names of one or more violated component policies, the violated rules in each policy, the total quantity of violating components for each rule, and helpful links. Click a component quantity to view the components that violate the rule in Polaris. Note: Email notifications for issue and component policies are only sent to Organization Admins. One email is sent each time a test's results violate one or more policies, and each email can include components that violate more than one of each policy's rules. If a test's results violate issue and component policies, violated issue and component policies are listed in the same email. | Notifications must be enabled for the organization, and your personal notification settings must allow Policy notifications. |
| Attempt Build Break | For SCA tests run via Bridge (including the Black Duck Security Scan Extension for Azure DevOps, the GitHub Action, the GitLab Template, and Black Duck Security Scan Plugin for Jenkins), attempt to break a build after components with specific properties are found in a SCA test. | The action only affects SCA tests run using Bridge CLI Bundle 3.2.0 or later, or Bridge CLI Thin Client 3.0.16 or later. Additionally, `polaris.waitForScan` must be set to `true` (default) in your pipeline. |
| Create a fix pull request (for direct deps. with vulnerabilities) | Automatically create a fix pull request (Fix PR) for components with direct dependency vulnerabilities detected by the SCA scan of SCM-integrated projects based on assignment of this policy and customizable Fix PR settings. | See [Fix Pull Requests (Fix PR)](../fix-pull-requests-fix-pr.md) for prerequisites. |

### Example component policy

For example, say you create a component policy with the following rule:

Table 2. Example component policy

| Rule | Component properties | Actions |
| --- | --- | --- |
| Rule one | Components with Permissive, AGPL, or Unknown licenses with a Security Risk of Critical or High. | Send Notification |

In tests subject to this example component policy:

- An email notification is sent to Organization Admins when critical or high-risk components with permissive, AGPL, or unknown licenses are detected in a test.

## View a component policy's details

1. Go to Policies and open the Component Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select View.

   [image: ui component policies tab]

## Create a component policy

Tip: Instead of creating a new component policy, you can use a preexisting policy as a starting point (and adjust the policy as you wish). Click the options [image: icon polaris options] icon at the end of a policy's row and select Duplicate.

1. Go to Policies and open the Component Policies tab.
2. Click + Add Policy. The Add Component Policy screen appears.

   [image: policy component create]
3. Enter a Policy Name (required) and Short Description (optional).

   Note: Policy names are limited to 255 characters. Policy descriptions are limited to 512 characters.
4. (Optional) Set up the policy's rules:
   1. Under Add Rule, select Add More.
   2. Select issue properties that trigger notifications with the dropdown in the If... column:

      - SBOM: Select Included, Excluded or both.
      - Exposure (matches SCA only): Select Reachable and/or Undetermined.
      - License Family: Select one or more of Permissive, Reciprocal, AGPL, Restricted Third Party Proprietary, Unknown, or Weak Reciprocal.
      - License Status: Select one or more of Unreviewed, In Review, Reviewed, Approved, Limited Approval, Rejected, Deprecated.
      - Match Type: Select Direct Dependency, Transitive Dependency or both.
      - Contains issues that are on the CISA KEV list: Select Yes to match components that contain issues on the CISA KEV list, or No to match components that do not.
      - Security Risk: Select one or more of Critical, High, Medium, or Low.
      - License: Select one or more licenses.

        Note: This field accepts partial matches and is case-sensitive. After you enter a license name, select licenses with the checkboxes. Up to 20 licenses appear at a time.
      - Component: Find a specific component by name (for example, `Apache Log4j 1.2.17`).

        Note: This field is limited to 100 characters, does not accept fuzzy or partial matches, and only allows a single component.
      - Match Score: Set a numerical range for component match scores. Separate entries with commas (`5-10, <=70`).

        Note: Precise match scores only appear for components identified in signature analysis tests; the match score for a component identified in a package manager test will always be 100%. This field is limited to 100 characters.
   3. Select the actions to perform when components with matching properties are detected in a test with the dropdown in the then... column:

      - Send notification
      - Attempt Build Break
      - Create a fix pull request (for direct deps. with vulnerabilities)
   4. To add additional rules to the policy, repeat these steps.

      Note: You can add up to five rules to each component policy. You can deactivate rules with the slider in the Status column. Dropdown menus in the If... and then... cannot be empty.
5. Click Save.

The component policy is saved. To apply it, you can:

- Assign it to specific applications, projects, or branches. See [Change the policies assigned to applications, projects, and branches](change-the-policies-assigned-to-applications-projects-and-branches.md) for more information.
- Add the policy to your organization's default policies (provided you have Organization Admin permissions). See Change your organization's default component policy for more information.

## Modify a component policy

1. Go to Policies and open the Component Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Edit.
3. Modify the policy, as required.
4. Select Save.

## Change your organization's default component policy

Organization Admins can change your organization's default component policies. See [Manage your default policies](manage-your-default-policies.md) for more information.

## Delete a component policy

1. Go to Policies and open the Component Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Delete.

   A confirmation appears.
3. Click OK to delete the policy.

   CAUTION:

   Policies you delete cannot be recovered. Each component policy can be assigned to multiple projects and branches.
