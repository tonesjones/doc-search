---
title: "Control how default policies are applied to branches"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/control-how-default-policies-are-applied-to-branches.html"
content_id: "6_0Zvo1nP_ZrJjedn1O8xQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:02.857192+00:00"
content_hash: "9f246eef48bf55b9a5e975854ec4cbf4b0c8cc9d2ac3afa4230d07972fb28f70"
---

# Control how default policies are applied to branches

Organization Admins can control how default policies are applied to branches. Your default policies can be applied to default branches, non-default branches, all branches, or you can choose to not apply default policies automatically.

The branch inheritance table determines which branches receive default policies automatically. You can apply default policies to default branches, non-default branches, all branches, or none.

Note: Only Organization Admins can complete these steps.

1. Go to My Organization > Policies.

   A table that shows how your default policies are applied to branches appears under Default values for new branches.
2. To make changes, select Edit (next to Default values for new branches).
3. Use the checkboxes in the Default branches and Non-default branches columns to select the branches different default policies will be applied to.
4. Select Save.

Now, when you create new branches (or new branches are imported into Polaris), new branches of the selected type inherit default policies automatically.

Important: Changes you make do not affect branches that have already been customized.
