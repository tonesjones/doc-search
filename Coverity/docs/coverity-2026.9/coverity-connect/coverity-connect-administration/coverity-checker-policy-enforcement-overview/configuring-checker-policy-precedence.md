---
title: "Configuring checker policy precedence"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configuring-checker-policy-precedence.html"
content_id: "hH4C_BNFJT4RZMzZTUEThw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.878920+00:00"
---

# Configuring checker policy precedence

Precedence determines which policy scope takes priority when a global policy and a
project policy both exist and contain conflicting settings.

When Coverity Connect has both a global policy and a project policy for the same
project, it combines them into an effective policy. The precedence setting controls
how conflicts between the two are resolved.

| Precedence | Behavior |
| --- | --- |
| Top Down | Global policy takes precedence over project policy. This is the default. |
| Bottom Up | Project policy takes precedence over global policy. |

If no precedence is configured, Coverity Connect uses Top Down. If only a global
policy exists with no project policy, precedence has no effect.

Note: Requires a user account with the Manage Checker Policies
(`manageCheckerPolicies`) permission. Setting the global
assignment requires a system administrator.

Project-level precedence follows these rules:

- If a global precedence is set, the project cannot set its own precedence;
  attempting to do so returns an error.
- If the global policy has no precedence defined, the project can set a
  precedence.
- If a global policy later adds a precedence, it overrides any project-level
  precedence at run time.

Note:

- When a project is deleted, its related policy assignments are also
  deleted.
- If a policy shared by multiple projects is updated, the API does not update
  the existing policy in place. Instead, it creates a new policy containing
  the updated content and returns the following message: "Policy {0} is
  being shared, a new Policy {1} has been created. Please update project
  assignments." Existing project assignments must be updated manually to
  point to the new policy.

1. Choose the precedence order.

   Use `TOP_DOWN` for global policy precedence or
   `BOTTOM_UP` for project policy precedence.
2. Set the instance-wide default precedence as part of the global policy
   assignment.

   ```
   PUT /api/v2/checkerPolicy/assignments/global?name=policyName&noncomplianceAction=action&precedenceOrder=order
   ```
3. **Optional:** 
   To override the precedence for a specific project, include the
   `precedenceOrder` parameter in the project assignment, then
   verify the result.

   ```
   PUT /api/v2/checkerPolicy/assignments/projects?projectName=projectName&policyName=policyName&precedenceOrder=order
   ```

   ```
   GET /api/v2/checkerPolicy/assignments/projects?projectName=projectName
   ```

   If `precedenceOrder` is not specified, the default is
   `TOP_DOWN`.

   If the global policy assignment already has a `precedenceOrder`
   set, this request returns an error.
