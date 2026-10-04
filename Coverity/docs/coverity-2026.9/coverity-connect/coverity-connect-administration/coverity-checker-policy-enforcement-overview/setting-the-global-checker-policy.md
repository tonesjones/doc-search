---
title: "Setting the global checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/setting-the-global-checker-policy.html"
content_id: "LwmfHy6_cyN_pk0Tf7bGoQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.798794+00:00"
---

# Setting the global checker policy

Upload a checker policy file to Coverity Connect to apply it as the global policy
for all projects in the instance.

The global policy defines the organization-wide baseline requirements that all scans
must satisfy. Coverity Connect validates the policy file at upload time. If the file
contains syntax errors or unsupported settings, Coverity Connect reports the errors
so you can correct and re-upload the file.

To create the policy file, see Creating a checker policy.

Note: Uploading a policy requires a user account with the Manage Checker Policies
(`manageCheckerPolicies`) permission. Setting the global
assignment requires a system administrator.

1. Upload the policy file to the policy library.

   ```
   POST /api/v2/checkerPolicy/policies
   Content-Type: multipart/form-data

   file=@policy_file
   ```

   Note the policy name returned in the response. You need it in the next
   step.
2. Assign the policy as the global policy and set the enforcement defaults.

   ```
   PUT /api/v2/checkerPolicy/assignments/global?name=policyName&noncomplianceAction=REJECT&precedenceOrder=TOP_DOWN
   ```

   Use `WARN_AND_ACCEPT` instead of `REJECT` when
   non-compliant commits should be accepted with a warning. Use
   `BOTTOM_UP` instead of `TOP_DOWN` when
   project policies should take precedence over the global policy.
3. Verify the active global assignment.

   ```
   GET /api/v2/checkerPolicy/assignments/global
   ```

   Confirm that the response shows the expected `name`,
   `noncomplianceAction`, and
   `precedenceOrder`.
