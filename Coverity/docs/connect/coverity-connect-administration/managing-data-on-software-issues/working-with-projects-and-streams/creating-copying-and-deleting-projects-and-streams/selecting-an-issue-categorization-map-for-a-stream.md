---
title: "Selecting an issue categorization map for a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/selecting-an-issue-categorization-map-for-a-stream.html"
content_id: "5LGGwrZFmzL1MXL2AKHBfw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:03.319917+00:00"
---

# Selecting an issue categorization map for a stream

Checkers automatically categorize issues and assign an impact level (High, Medium, Low,
and Audit). For example, in the Coverity categorization, a C/C++
FORWARD_NULL checker can report a number of medium priority issues, one of which is an
unchecked dynamic_cast.

Custom categorizations can be imported through Configuration > System > Issue Categorization, and applied to individual streams.

**To select an issue categorization map:**

1. Select Configuration > Projects & Streams.
2. Select the stream with which you want to associate an issue categorization
   map.
3. In Stream Details, click
   Edit.
4. Use the Issue Categorization drop-down to select your
   preferred issue category map.
5. Click OK to save your changes and exit.

Note: Note that the issue categorization map is applied to defect instances at commit time.
Changes to issue category mapping will only take effect for future snapshots, and will
not get applied to existing defects.
