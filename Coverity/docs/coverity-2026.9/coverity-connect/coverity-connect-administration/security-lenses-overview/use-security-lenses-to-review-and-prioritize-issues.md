---
title: "Use Security Lenses to review and prioritize issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/use-security-lenses-to-review-and-prioritize-issues.html"
content_id: "6xVGwdHcLxv5gwOeoUzFKw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.000596+00:00"
---

# Use Security Lenses to review and prioritize issues

Use Security Lenses to identify, review, and prioritize issues based on **Security
Impact** classifications.

Security Impact classifications must be available for the
issues you want to review. Issues that are not associated with a supported security
context are assigned a value of **None**.

1. Click **View** and open a view that contains the issues you want to
   review.
2. Select the **Issues** view.
3. To review issues by Security Impact, do the following:
   1. Click **Settings**.
   2. Click the **Columns** tab.
   3. Select the **Security Impact** checkbox.
   4. Click **OK**.
4. To sort issues by Security Impact, click the **Security Impact** column
   heading.

   Click the column heading again to reverse the sort order. In ascending order,
   issues are sorted from **None** to **Very High**. In descending order,
   issues are sorted from **Very High** to **None**.
5. To group issues by a specific **Security Impact** value, do the
   following:
   1. Click **Settings**.
   2. On the **Filters** tab, from the **Group by** drop-down menu,
      select **Security Impact**.
   3. Click **OK**.
   4. In the new group pane on the left, select the value you want to review,
      such as **Very High**.

      Issues with a **Very High** Security Impact classification
      are displayed.
6. (Optional) If you are using **Modern UI**, review and filter issues by
   Security Impact:
   1. Open the **Projects** view and select the project that contains the
      issues you want to review.
   2. Click **Streams**.

      You are redirected to the Issues view.
   3. Click **Add Filter** and select **Security Impact**.
   4. Select one or more Security Impact values and apply the filter.

      Issues that match the selected Security Impact classifications
      are displayed.
