---
title: "Removing policy overrides"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/removing-policy-overrides.html"
content_id: "zhn8qik4AhVO6J59IH~hnQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:16.954101+00:00"
---

# Removing policy overrides

You can remove an override of a component or file that was in violation of a policy rule.
Only users with the appropriate role can override a disapproved component or file in that project.

To remove an override:

1. On the BOM page using the List view, click the Policy Violation Override icon
   ( [image: Policy Violation Override icon] ) located next to the component. The Policy Violations dialog box
   appears.

     
    [image: Policy Violations dialog box]
2. Depending on whether there is one or more policy override to remove:
   - To remove one policy override, click **Undo Override**. Optionally,
     enter a comment and click **Confirm**.

     If you entered a
     comment, it appears, along with the username of the user who removed the
     override, in the Policy Violations dialog box.
   - For multiple policy violations:

     - Click **Undo All Overrides** to remove all policy
       overrides.

       You cannot enter a comment when using the
       **Undo All Overrides** feature.
     - Click **Undo Override** for each policy violation you want to
       override. Optionally, enter a comment and click
       **Confirm**.

       If you entered a comment, it appears,
       along with the username of the user who removed the override, in
       the Policy Violations dialog box.
3. Click **Close**. The BOM appears and the Policy Violation icon ( [image: Policy Violation icon] ) reappears.
