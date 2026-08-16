---
title: "Create a Fail Pull Request (Fail PR - Warn or Block)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-a-fail-pull-request-fail-pr-warn-or-block-.html"
content_id: "w2RDUs14qaD98Qp2jEzntA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:39.330029+00:00"
content_hash: "0eb73c4113df0ba47d73ff332caf110e2e9a7570c28455b44b145c2c6201abbb"
---

# Create a Fail Pull Request (Fail PR - Warn or Block)

For overview, prerequisites, and inheritance, see [Fail Pull Requests (Fail PR)](../fail-pull-requests-fail-pr.md).

1. Configure a PR policy with the Fail action.

   Add the Fail Pull/Merge Request action within a Pull/Merge Request policy rule (see [Pull/merge request policies](../create-and-manage-policies/pull-merge-request-policies.md)). This tells Polaris which vulnerabilities should cause a PR scan to be considered a failure and automatically issues a warning or blocks a PR. Policies are rule-based and can be scoped by security risk level.

   Note: A scan that fails due to an error (not just a policy violation) is also treated as a PR scan failure. This prevents incomplete scans from creating a gap in your security enforcement.
2. Assign the Fail PR policy.

   Once created, a policy can be applied in the following ways:
   - **Organization level:** Via Pull/Merge Request Policies, where an existing policy can be selected and applied to the whole organization.
   - **Application level:** Via Pull/Merge Request Policies, where an existing policy can be selected and applied to the application directly.
   - **Bulk onboarding:** A Pull/Merge Request policy can be attached during import and applied across multiple projects simultaneously.

   Note: At this point, if an assigned policy is violated, a warning is issued. To block merges, complete the following step.
3. Decide whether to warn or block.

   After setting up the Fail Pull/Merge Request action in your policy, decide what happens at the organization or application level when a PR scan fails.

   | Option | Behavior | Developer Can Merge? |
   | --- | --- | --- |
   | Warn (default) | Polaris posts a warning comment on the PR indicating the scan failed. No merge restriction is applied. | Yes — at their own risk |
   | Block | Polaris instructs the SCM to prevent the PR from being merged until issues are resolved or the setting is changed. | No — blocked until resolved |
4. Configure the Block setting (optional).

   This setting is available at two levels. The most specific level takes precedence:
   - **Organization level:** Applies to all projects unless overridden.
   - **Application level:** Overrides the organization-level setting for that application.

   1. Navigate to the Analysis page for the organization or application level and edit the SCM Event-based Test Automation settings.
   2. Enable Block merge when policy fails pull/merge request.
   3. Select Default branches only or All branches.
   4. Save your changes.
5. Verify the developer workflow.

   Once the feature is configured, developers will experience the following when a PR is created or edited:
   - A SAST or SCA scan is automatically triggered.
   - The developer cannot merge the PR until the scan completes, regardless of whether Block is configured.
   - A notification or status check in the SCM indicates that a scan is in progress.
   - Polaris passes the scan status twice: once on PR creation with a running status, and again after the scan completes with a success, failure, cancelled, or skipped status.After the scan completes, one of two outcomes occurs:
   - **Scan passes:** The PR status check in the SCM is updated to passing and the developer can merge normally.
   - **Scan fails:** Polaris posts a PR comment listing the issues found and guidance on how to resolve them. If the policy is set to warn, the developer may still merge. If the project is configured to block, the developer cannot merge until the issues are addressed.

   Note: Developers do not need to log into Polaris to view the issues. All relevant information is available in the PR comment posted by Polaris.
6. Unblock a PR (for security admins).

   If a PR has been blocked, there are two ways to unblock it:
   - **Change the configuration to Warn:** Navigate to the organization or application SCM Event-based Test Automation settings on the Analysis page and deselect Block merge when policy fails pull/merge request. This immediately unblocks all open PRs with a failed policy check.
   - **Resolve the vulnerabilities:** The developer fixes the issues identified in the PR comment and pushes new commits, triggering a new scan. If the updated code no longer violates the policy, the block is lifted automatically.

   Note: Developers cannot unblock a PR themselves unless they have sufficient SCM-level permissions. To allow developers to merge without resolving issues, use Warn rather than Block.
