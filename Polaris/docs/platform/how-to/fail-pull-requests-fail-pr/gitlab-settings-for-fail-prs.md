---
title: "GitLab Settings for Fail PRs"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-settings-for-fail-prs.html"
content_id: "oGAo1N1lqEbDvs5Wsz4JoQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:19.379223+00:00"
content_hash: "27a23ac6e8aa9348f7c93c4f3e23382f4d993401d79973cf4c409ac3ecc90593"
---

# GitLab Settings for Fail PRs

To block merge requests based on pipeline or build job failures, you must enable Pipeline must succeed in GitLab and enable the Fail Pull/Merge Request action and block settings in Polaris. For Polaris instructions, see [Fail Pull Requests (Fail PR)](../fail-pull-requests-fail-pr.md).

Important:

If the Pipeline must succeed setting is not enabled, Polaris will still deliver commit statuses (`running`, then `success` or `failed`), but GitLab will not block the merge on failure.

Enabling the setting blocks merges for any pipeline failure, not just Polaris; to override this, disable the setting temporarily.

Enable the Pipeline must succeed setting at the repository level in GitLab.

This setting is not available at the group level. GitLab does not support target branch level configurations.   
 [image: GitLab repository settings showing the Pipeline must succeed option]
