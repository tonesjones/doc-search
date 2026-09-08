---
title: "Monitoring Policy Violations"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/monitoring-policy-violations.html"
content_id: "ItYfnrnWe0WYEcYFScnwDw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:28.087338+00:00"
content_hash: "bf9231369e15072b6b36416b2a49aff7c3575d8e179141c7e6995c3868eaaacb"
---

# Monitoring Policy Violations

Once a policy has been defined and applied to a project, Software Risk Manager will track
policy violations and provide violation status in a variety of ways. Policy information
and violation status appears on the following pages:

- Projects page
- Findings page
- Policies page

Note: Email notifications for changes to policy violation status can be configured on the
user configuration page. For more information, see User Configuration
Settings. For information on customizing the policy email template, see Customizing the Policy Email Template.

## Understanding Policy Violation Parameters

You can set the "duration" or number of days before a policy is violated when you
create policy rules. Time-based violations are based on calendar days. Polices can
be set to preselected periods, that is, 1 day, 7 days, 14 days, etc. The "fix-by"
date is calculated based on the day the finding was created. For example, if a rule
has been set to 7 days, the policy will show a violation 7 days after the finding
was created.

Tickets will be created whenever a finding violates the `findings
matching` condition; nevertheless, the threshold or fix-by date doesn't
need to be reached. Consider the following example:

```
If > 100 findings matching Only Critical and Highs, fix by 14 days and Create
      Tickets
```

If your project only has one new critical or high finding,
a ticket will be created for that finding even though the policy itself is still
passing because it hasn't hit the threshold and hasn't gone over the fix-by date

When using the Policy filters, note the following range definitions:

- Due Soon is 0–7 days.
- On Track is anything over 7 days.
- Overdue occurs when the fix-by date has passed by at least one day.

## Monitoring Policy Violations for Projects

Click the Projects icon in the navigation bar to view a summary of policy issues
related to a specific project.

[image: image]

This page shows the number of policy violations for each project along with links to
additional information. Policy information is displayed in the second and third
columns to the right of the total number of findings for that project. The total
number of policy violations for a specific project is broken out by policy violation
status, shown in color-coded boxes. Clicking a box takes you to the Findings page,
where the findings have been filtered according to that status.

[image: image]

Policy violations are defined as follows:

- Red: Overdue
- Orange: Due soon
- Purple: On track
- Gray: Unspecified "fix-by"

The third column shows the number of policies associated with that project. Clicking
the link displays the policies associated with that project.

## Monitoring Policy Violations for Findings

Policy violations for a single finding can be found on the Findings page. Click the
Findings icon from the navigation bar to open the Findings page, then mouse over the
shield icon next to the finding ID to see a summary of policy violations for that
finding. The number of days specified to fix the issue is displayed in the "Fix By"
column.

You can also use filters to sort findings based on policy violations. For more
information, see Working with
Filters.

[image: image]
