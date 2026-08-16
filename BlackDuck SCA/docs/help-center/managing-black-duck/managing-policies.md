---
title: "Managing policies"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-policies.html"
content_id: "RyW~BfYrh7ATQEyfDBHEkQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:10.912404+00:00"
---

# Managing policies

The Policy Management feature enables you to create rules to govern your use of open
source components. With policy rules, open source usage can be managed on an exception
basis – as long as open source components meet the policy requirements their usage is
allowed. Any open source components/versions that fail to meet your policy rules are
flagged, enabling you to review and determine if the use of the component should be
allowed in the particular application.

Policies in Black Duck SCA are essential for ensuring that your projects
adhere to defined standards regarding components, licenses, and vulnerabilities. This
document outlines how to manage policies effectively across different scanning
scenarios.

Tip: **Want to Learn More?** Check out the
[Black Duck training](https://blackduck.skilljar.com/page/black-duck) courses at
Black Duck Customer Education. You will learn how to implement and
manage policy rules in Black Duck, which can help you reduce
security, license, and operational risks. You will learn which user role is required
to be able to configure policy and how to edit, create, and apply new policies, how
to interpret the results, and how to override policy if necessary.

## About the policy process

To use the policy management feature:

1. Create rules that
   enforce your policies; a user with the Policy Manager role can create and manage policy rules. When creating policy rules determine:
   - Whether to enable the rule. BOMs will not be evaluated until the rule
     is enabled.
   - Whether the rule can be manually overridden.
   - The conditions for this rule.

     Note: Rules can have multiple conditions; *all* conditions must be true for a component to be
     in violation of the rule.
2. View the violations and determine what to do with components that are in
   violation of a rule.

   If you enabled the option, violations can be manually
   overridden.
3. Optionally,
   - Create additional policies and/or edit, delete, or
     disable or enable your existing policies.
   - Select a category for your rule. Black Duck provides these categories
     for a policy rule: component, security, license, operational, and
     uncategorized (default).

     By using categories and filters, you
     can easily find policies (on the Policy Management page) or policy
     violations (on the BOM page) by category.
   - View the
     Project Version report. This report includes policy
     violation information:

     - The `components_date_time.csv`,
       `bom_component_custom_fields_date_time.csv`,
       and`source_date_time.csv`
       files list the policy status and override
       information.
     - The `version_date_time.csv` file
       indicates whether this version of the project has a policy
       violation.

To assist you, Black Duck provides five default policy rules that
you can view, modify, enable, or delete. These policy rules are disabled by
default.

## Policy applicability by scan mode and deployment

The policy engine behaves the same in both Hosted (SaaS) and On-Premises deployments.
There is no difference in how policies are evaluated based on the deployment
model.

How policies are evaluated depends on the scan mode:

| Scan Mode | Policy Evaluation Behavior |
| --- | --- |
| **Detect Full Scan (Online)** | All enabled Full Scan policies are evaluated after the scan is processed by the Black Duck SCA server. Policy violations are stored in the project version, the BOM is updated, and results are available in reports, dashboards, notifications, and the UI. |
| **Detect Offline Scan** | Policies are *not* evaluated while the scan is generated offline. Evaluation occurs only after the scan data is uploaded to a connected Black Duck SCA server and processed — at which point violations are calculated the same as for an online Full Scan. |
| **Detect Rapid Scan** | Only policies enabled for Rapid Scan are evaluated. Rapid Scan returns immediate policy results to the user or CI/CD pipeline but does not create or update a project BOM or project version. Workflows that rely on a persisted BOM (reporting, notifications, dashboards, project history) do not apply. |

Tip: When creating a policy, ensure that it is enabled for the appropriate scan mode
(Full Scan, Rapid Scan, or both), depending on where you want the policy to be
evaluated.

## Viewing policy rules

The Policy Management page lists all your policy rules and indicates whether the rule allows
manual overrides. View this page by clicking [image: image] and selecting
**Policies**:

  
 [image: Policy Management page]   

- The page is filtered to display enabled rules. Modify or clear the filter to
  view disabled rules.
- All rules can be overridden unless noted.
- Click > to view the conditions of this rule and who created and last updated
  it.

From this page, you can view, create, edit, or
delete
policy rules.

## Viewing policy rule violations

When a component is in violation of a policy rule, the Policy Violation icon ( [image: Policy Violation icon] ) appears in the UI on the following pages:

- Source page. Icon appears next to the file name to indicate that a file in a
  component is in violation.
- BOM page. Icon appears next to components in violation.

  In the Tree View of the BOM, [image: Policy violation - child icon] next to the parent component indicates that a child has a policy
  violation.
- Custom dashboards. Icon appears next to the project name to indicate that
  this project has a version which has a policy violation.
- Project Version page. Icon appears next to the version to indicate that it
  has a policy violation.

Hover over the icon to view to view more information:

- On the project level, information such as the following appears:

    
   [image: Policy violations - popup]   

  This information also appears at the component/file level for users who are
  members of projects or have project-group privileges.
- On the component/file level, the following information appears for users with
  the BOM Manager, Global Project Administrator, Global Project Manager,
  Project Manager, and Policy Violation Reviewer roles:

    
   [image: Policy violations - popup]   

  Clicking the icon (when viewing the BOM using the List view) displays the
  Policy Violations dialog box from which you can override the policy
  violation.

## Overriding violations

If a rule was configured to allow manual overrides of violations, then you can override a
disapproved component or file in that project.

When all component violations have been overridden, the Policy Violation Override icon ( [image: Policy Violation Override icon] ) appears in the UI. In the Tree View, [image: Policy violation override - child icon] indicates that a child's policy violation has been overridden; it appears
at the parent level. Click the icon to view more information.

  
 [image: Policy Violation Override Popup]

## Removing policy overrides

If a violation of a policy should not have been overridden, you can remove the
override.
