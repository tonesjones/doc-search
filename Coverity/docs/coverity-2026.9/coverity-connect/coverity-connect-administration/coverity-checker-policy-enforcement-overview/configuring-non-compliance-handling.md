---
title: "Configuring non-compliance handling"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configuring-non-compliance-handling.html"
content_id: "TdcTfZnIg6T~I50iJMsQ9w"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.918707+00:00"
---

# Configuring non-compliance handling

Non-compliance handling determines what Coverity Connect does when a scan does not
satisfy the effective checker policy at commit time.

When a scan is committed to Coverity Connect, Coverity Connect checks the scan
configuration against the effective policy. If the scan does not comply, Coverity
Connect responds based on the configured handling option.

| Option | Behavior |
| --- | --- |
| Reject | The commit is rejected and Coverity Connect returns an error identifying which setting failed and why. The scan must be rerun with a compliant configuration before results can be committed. This is the default. |
| Warn and Accept | The commit is accepted. Coverity Connect returns a warning identifying the non-compliant setting. The results are committed despite the non-compliance. |

Note: Non-compliance handling is configured at the global level and applies to all projects in
the Coverity Connect instance. Requires a user account with the Manage Checker
Policies (`manageCheckerPolicies`) permission. Setting the global
assignment requires a system administrator.

Tip: If no global or project assignment exists, no policy is enforced. To
remove the global assignment, call `DELETE
/api/v2/checkerPolicy/assignments/global`. To remove a project
assignment, call `DELETE /api/v2/checkerPolicy/assignments/projects`
with the projectName query parameter.

1. Choose the non-compliance action.

   Use `REJECT` to block non-compliant commits, or
   `WARN_AND_ACCEPT` to allow the commit while returning a
   warning.
2. Configure the action on the global assignment.

   ```
   PUT /api/v2/checkerPolicy/assignments/global?name=policyName&noncomplianceAction=action&precedenceOrder=order
   ```
3. Verify the configured action.

   ```
   GET /api/v2/checkerPolicy/assignments/global
   ```
