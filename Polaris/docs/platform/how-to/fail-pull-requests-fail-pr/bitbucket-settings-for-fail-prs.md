---
title: "Bitbucket Settings for Fail PRs"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/bitbucket-settings-for-fail-prs.html"
content_id: "OnBzeagJ~NQgeGeuTCb2QQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:41.059681+00:00"
content_hash: "e54e14877e65502a83e12919c878a371e31965751edaa1ca8f0fd4474ae20e79"
---

# Bitbucket Settings for Fail PRs

To block merge requests, enable Merge Checks and Merge Conditions in Bitbucket and enable the Fail Pull/Merge Request action and block settings in Polaris. For Polaris instructions, see [Fail Pull Requests (Fail PR)](../fail-pull-requests-fail-pr.md).

Note: Block PR is only supported for Premium and not for Free/Standard plans.

Enable Merge Checks at the repository level in Bitbucket.

This setting is configured per repository, not at the workspace or project level. In Bitbucket, go to Repository Settings > Merge checks and enable the required build or check condition for Polaris.   
 [image: Bitbucket settings showing the merge checks options]
