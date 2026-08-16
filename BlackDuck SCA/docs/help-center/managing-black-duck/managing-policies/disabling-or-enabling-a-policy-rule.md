---
title: "Disabling or enabling a policy rule"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/disabling-or-enabling-a-policy-rule.html"
content_id: "_oEhqzMrIkBiy8gpXifhqA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:15.513740+00:00"
---

# Disabling or enabling a policy rule

Users with the Policy Manager role can
disable or enable policy rules.

- When a rule is disabled, violations are removed for any component that was in
  violation of the policy rule (if the rule was previously enabled).
- When a rule is enabled, existing BOMs are immediately evaluated to determine if
  they are in violation of this rule.

To disable or enable a policy:

1. Click [image: image] > **Policies**.

   The Policy Management page appears.
2. Click [image: Options] in the row of the policy rule that you want to enable or disable and
   select **Edit**.
3. Do one of the following:
   - Clear the **Enabled** option to disable the rule.
   - Select the **Enabled** option to enable the rule.
4. Click **Update**.
