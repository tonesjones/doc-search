---
title: "Compare default and non-default branches in a project"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/compare-default-and-non-default-branches-in-a-project.html"
content_id: "eR86OnRE4ZaBC2tyOeqYhg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:26.922230+00:00"
content_hash: "bd57c2a844e25b9d2f478d943f454d5754d3b1b4b1cbae61edaade4d3e5225a0"
---

# Compare default and non-default branches in a project

Compare a SAST & SCA project's default and non-default branches to track improvements and keep new issues from reaching the project's default branch.

To find new issues created in a project's non-default branch, or find issues resolved in a project's non-default branch, follow these steps:

1. Go to Portfolio, open an application, open a SAST & SCA project, and open the Issues tab.
2. Select a non-default branch from the pulldown menu at the top of the page.
3. Click the filter [image: A screenshot of the icon used to open the filter panel.] icon.
4. Apply a filter in the Show All Issues... category:

   [image: compare branch filters]

   Note: The Show All Issues... category only appears when you select a non-default branch.

   - In This Branch (default): Show issues found in the default and non-default branches.
   - In This Branch Only: Show issues that are only found in the non-default branch (issues the non-default branch creates).
   - In Default Branch Only: Show issues that are only found in the default branch (issues non-default branch resolves).

   Note: Issue quantities that appear next to the In This Branch Only and In Default Branch Only are static and won't change when you apply other filters.

   Tip: You can find a list of the branches in which an issue exists in the Issue Details tab.
