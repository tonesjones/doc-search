---
title: "Creating legacy issues after upgrading Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-legacy-issues-after-upgrading-coverity-analysis.html"
content_id: "AgZrgE1uTX_ZvdgvOrMnhw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:27.227449+00:00"
---

# Creating legacy issues after upgrading Coverity Analysis

When a company upgrades to a newer version of Coverity Analysis, improvements in Coverity
checkers may reveal additional issues that existed in the company's code base prior to
upgrading. To mark these newly revealed issues as legacy issues, complete the following
steps:

1. Run an analysis on your code base using the original Coverity Analysis version,
   and commit the results.
2. Complete the upgrade to the newer Coverity Analysis version.
3. Run the analysis again, and commit the results. Any issues introduced in this
   step are the cause of improvements in the Coverity checkers.
4. Use the following command to mark the issues found after upgrade as legacy
   issues:

   ```
   > cov-manage-im --mode defects --stream streamName --update --newest --set legacy:True
   ```

   The `--newest` option makes sure that only the issues introduced
   in the most recent snapshot (after the upgrade) are marked as legacy issues.

   Note: An optional `[snapshotId]` parameter can be added after
   the `--newest` option to compare the newest snapshot directly
   against the specified older snapshot. In the following example, all issues
   that are present in the latest snapshot but not present in snapshot 10001
   will be marked as Legacy issues.

   ```
   > cov-manage-im --mode defects --stream streamname --update --newest 10001 --set legacy:True
   ```
