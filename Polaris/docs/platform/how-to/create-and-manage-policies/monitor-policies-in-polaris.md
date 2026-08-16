---
title: "Monitor policies in Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/monitor-policies-in-polaris.html"
content_id: "7q19~8CTuUjjXYSVOSpk6A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:05.852307+00:00"
content_hash: "e3c29833b0cf80f2801eb682627d65b55d2dfbc21a74c555c53f02e7f690d3e0"
---

# Monitor policies in Polaris

You can track policy violations throughout the Polaris user interface.

## Monitor policy on the Portfolio page

When you open the Portfolio page, the quantity of active policy violations in each application appears in the Total Active Policy Violations ( [image: portfolio policy icon] ) column. This is the sum of active policy violations detected in the most recent SAST (default branch only), SCA (default branch only), and DAST tests of projects in each application.

  
 [image: portfolio]   

Open an application to view the policy status of each project (represented by a green [image: policy status green] or red [image: policy status red] shield icon) and the total quantity of violating issues in each SAST (default branch only), SCA (default branch only), and DAST project. Select the info [image: policy total active info icon] icon (in the Total Active Policy Violations column) to view the names of issue and component policies a project violates.

  
 [image: ui application]   

Important: The policy status of each project is based on the most recent test (found in the Latest Completed Test column). Violation quantities can also change as a result of issue and component triage, file and folder exclusions, and automatic component updates.

Note: The quantity of active policy violations doesn't always include overdue issues (issues that are detected after their fix-by date). Overdue issues are only counted as active violations when a policy includes a rule that checks for issues with a Fix-By Status of Overdue. See [Issue policies](issue-policies.md) for more information.

If the same issue or component violates more than one policy (or policy rules), and/or is found in multiple branches, it's only counted once.

When issues found in the latest test violate policies, the shield icon is red. The green shield icon indicates no policy violations were captured in the latest test.

On the Issues tab, a policy status [image: policy status icon] icon appears next to issues that violate issue policies. Hover over the policy status icon to view the names of issue policies an issue violates.

  
 [image: issue policy icon hover]   

On the Components tab, a policy status [image: policy status icon] icon appears next to components that violate component policies. Hover over the policy status icon to view the names of component policies a component violates.

  
 [image: component policy icon hover]

### Issue and component triage

Quantities in the Total Active Policy Violations columns can change when you triage issues or components, but only if:

- An issue policy's rules capture issues with specific Triage Status properties, and/or
- A component policy's rules only capture components that are Included in your software bill of materials (SBOM).

To exclude dismissed issues and excluded components from quantities in the Total Active Policy Violations columns (recommended), make sure your:

- Issue policies' rules capture issues with the To Be Fixed and Not Triaged statuses, and
- Component policies' rules capture components that are Included in your software bill of materials (SBOM).

Note: See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) and Ways to triage components in Polaris for more information on triage.

### File and folder exclusions

Quantities in the Total Active Policy Violations columns can change when you update file and folder exclusion rules. SAST issues that originate in excluded files do not count as violations. See [Exclude files and folders from tests](../exclude-files-and-folders-from-tests.md) for more information.

### Automatic component updates

Quantities in the Total Active Policy Violations columns can change when components are automatically synchronized with the Black Duck KnowledgeBase™. For example, if new issues are added to a component as a result of synchronization, those issues may violate existing policies. See [Automatic component updates from the Black Duck KnowledgeBase](../automatic-component-updates-from-the-black-duck-knowledgebase.md) for more information.

## Monitor policy on the Tests page

The policy status of completed tests is captured on the Tests page, in the Policy Violations column.

  
 [image: ui tests]   

Note: The Policy Violations column also appears on the Tests tab when you open a project.

  
 [image: Project Test Tab]   

Select the info [image: policy total active info icon] icon in the Policy Violations column to view:

- The quantity of policy violations detected in the test.

  Note: The quantity of active policy violations doesn't always include overdue issues (issues that are detected after their fix-by date). Overdue issues are only counted as active violations when a policy includes a rule that checks for issues with a Fix-By Status of Overdue. See [Issue policies](issue-policies.md) for more information.
- The issue and component policies assigned to the branch when the test started, along with links to view issues and components that violate different rules.

Note: Policy information only appears next to completed tests if issue policies were assigned to the branch when the test started.
