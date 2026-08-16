---
title: "Find issues captured after a test"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/find-issues-captured-after-a-test.html"
content_id: "3pqhJJ7ZuWZkM_lsop2YWA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:32.673037+00:00"
content_hash: "2a60e0499a9cf7bd8ea479f0e039523b5ac38e5aeb0ac228fa6b14d95f97449b"
---

# Find issues captured after a test

After you open a completed test's results, you can apply filters to find issues that were added to your projects after tests completed. Follow these steps:

1. Go to Tests and select the See Results [image: tests icon see results] icon next to a completed test.

   The Detected Issues tab opens.
2. Select the filter [image: A screenshot of the icon used to open the filter panel.] icon.

   The Filters panel opens.
3. Under Show All Issues..., select the Found post-test filter.

   This filter only returns issues that were added to the project after testing was completed, and includes:
   - Issues associated with components (or component origins) that were added to the branch manually.
   - Issues that were automatically added to the project as a result of automatic synchronization with the Black Duck KnowledgeBase™.

     Note: This happens automatically when the issues linked to a component or component origin change in the Black Duck KnowledgeBase™.
