---
title: "GitLab Settings for Fail PRs"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-settings-for-fail-prs.html"
content_id: "oGAo1N1lqEbDvs5Wsz4JoQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:40.256850+00:00"
content_hash: "7462e7888c1d4c342017f165acf45f91f33d896f513449af3d5619041a3a1f57"
---

# GitLab Settings for Fail PRs

To block merge requests based on pipeline or build job failures, enable Pipeline must succeed in GitLab and enable the Fail Pull/Merge Request action and block settings in Polaris. For Polaris instructions, see [Fail Pull Requests (Fail PR)](../fail-pull-requests-fail-pr.md).

Note: Available only for GitLab SaaS (Premium).

Enable the Pipeline must succeed setting at the repository level in GitLab.

This setting is not available at the organization level. GitLab does not support target branch level configurations.   
 [image: GitLab repository settings showing the Pipeline must succeed option]
