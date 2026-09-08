---
title: "Policies Overview"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/policies-overview.html"
content_id: "Cdb~tGzbAGrYGJGz_iyFzw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:23.811979+00:00"
content_hash: "9a21b7df3422b2aff84e9753149cc7613d7aa91f6140859f123f4e0692a2dad3"
---

# Policies Overview

Policies in Software Risk Manager allow you to track compliance to specified
requirements. Once defined, policies can be applied to projects, and policy violations
can be monitored. In this way, polices can be used to prioritize which security issues
need to be addressed, and so on.

Click the Policies icon in the navigation bar to open the Policies page.

[image: image]

The Policies page displays a list of all the currently defined policies, along with the
following information:

- **Policy Name.** Lists the existing policies. Click the policy name to open
  the View Policy window, where you can view or edit the policy definition.
- **Status.** Provides a visual representation of the policy status. There are
  four status icons:
  - Red triangle: Fail (Overdue)
  - Orange hourglass: Warn (Due Soon)
  - Purple hourglass: Pass (On Track)
  - Green checkmark: Pass (No Violations)
- **Findings Violating Policy.** Provides the following statistics:
  - The total number of findings that violate the policy. Clicking the link
    opens the Findings page and lists all the findings violating the
    policy.
  - A color-coded breakdown of findings according to violation status. The
    numbers inside the colored boxes correspond to the number of findings
    for each category: Overdue (red), Due Soon (orange), On Track (purple),
    No Fix-by date (gray). Clicking a box opens the Findings page. Findings
    are sorted according to the corresponding Policy Violations and Policy
    Violation Urgency filters.
  - The number of assigned projects with policy violations. Clicking the
    link opens the Projects modal, which lists the projects using this
    policy.
- **Using This Policy.** Shows the number of projects using the selected
  policy. Clicking the link opens the View Policy Projects window, which lists all
  the projects associated with the policy.

Click the column headers to re-sort the list. You can also use the search field to search
for a specific policy.

## Working with Policies

For more information on policy management, see the following topics:

- Policy Configuration. How to
  view a policy's configuration.
- Creating and Editing Policies.
  How to create or edit a policy's configuration.
- Applying a Policy to a Project.
  How to apply a single policy to a project.
- Applying a Policy
  to Multiple Projects. How to apply a policy to multiple
  projects.
- Monitoring Policy Violations.
  How to track policy violations as they relate to projects, policy, and
  individual findings.
