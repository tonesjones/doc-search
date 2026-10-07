---
title: "Assigning a checker policy to a project"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/assigning-a-checker-policy-to-a-project.html"
content_id: "QrbKBFrBmHhGupRTNU04mA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.837703+00:00"
---

# Assigning a checker policy to a project

Assign an uploaded checker policy to a project to apply project-level requirements
in addition to or in place of the global policy.

Project and global policies are selected from policies already in the policy library on
Coverity Connect. When both a global policy and a project policy exist, Coverity
Connect combines them into an effective policy based on the configured precedence.
See Configuring checker policy precedence.

To create and upload a policy file first, see Creating a checker policy and Setting the global checker policy.

Note: Requires a user account with the Manage Checker Policies
(`manageCheckerPolicies`) permission.

1. Confirm that the policy exists in the policy library. If it does not exist,
   upload it first.

   ```
   POST /api/v2/checkerPolicy/policies
   Content-Type: multipart/form-data

   file=@policy_file
   ```
2. Assign the policy to the project.

   ```
   PUT /api/v2/checkerPolicy/assignments/projects?projectName=projectName&policyName=policyName
   ```

   Add `&precedenceOrder=TOP_DOWN` or
   `&precedenceOrder=BOTTOM_UP` only when this project
   must override the instance-wide precedence setting. If omitted, the global
   precedence applies.
3. Verify the project assignment.

   ```
   GET /api/v2/checkerPolicy/assignments/projects?projectName=projectName
   ```

   Project-level assignments do not include a
   `noncomplianceAction` setting. That setting is inherited
   from the global assignment.

   The selected policy is applied as the project policy.
