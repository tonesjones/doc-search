---
title: "Overriding policy violations"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/overriding-policy-violations.html"
content_id: "ENpVZeJrcN1248UxaHGA5Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:16.249057+00:00"
---

# Overriding policy violations

If a rule was configured to allow manual overrides of violations, then users with the
appropriate role can override
a disapproved component or file in that project.

Note: If you override a file, the component will still be in violation if at least one file in the
component is in violation of a policy.

To override a violation:

1. On the BOM page using the List view, click the Policy Violation icon ( [image: Policy Violation icon] ) of the component you wish to override. The Policy Violations dialog
   box appears.

     
    [image: Policy Violations dialog box]
2. Depending on whether there is one or more policy violation:

   - For one policy violation, click **Override**. Optionally, enter a
     comment and click **Confirm**.

     If you entered a comment, it appears, along with the username of the user
     who overrode the policy violation, in the Policy Violations dialog
     box.

     If you enter a date, the override will expire at that date. When it
     expires it will return to a violation state.
   - For multiple policy violations:

     - Click **Override All** to override all policy violations. The
       Policy Violations dialog box displays the username of the user
       who overrode the policy rule.

       You cannot enter a comment or date when using the **Override All** feature.
     - Click **Override** for each policy violation you want to
       override. Optionally, enter a comment and click
       **Confirm**.

       If you entered a comment, it appears, along with the username of
       the user who overrode the policy violation, in the Policy
       Violations dialog box.
3. Click **Close**.

   The Policy Violation Override icon ( [image: Component Violation Override icon] ) appears next to the component that you overrode if all policy
   violations were overridden. If a component has multiple policy violations and
   not all are overridden, then the Policy Violation icon ( [image: Policy Violation icon] ) will still appear.

Note: Overrides can be removed.
