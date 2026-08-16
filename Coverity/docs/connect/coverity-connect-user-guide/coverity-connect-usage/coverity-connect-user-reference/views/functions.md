---
title: "Functions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functions.html"
content_id: "H912LKFXe8UprkVeE_r5Pg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:14.861035+00:00"
---

# Functions

Use Function views to look at the functions and methods in the selected
project. Click through different values on the top right of the
Triage panel to view specific issues associated with a
function.

As of the 2025.9.0 release, the Functions view presents all
versions of functions across all streams within a project. The previous
Function view presented one function per unique version of
source code across all streams. Given this more complete presentation of data, you might
see higher row counts, especially for projects with many streams.

By default, Coverity Connect provides the following Functions views:

- High CCM (>15): The CCM filter is set to `>15`.
- In Latest Snapshot: This view is not filtered.
- With Outstanding Issues: The 
  Outstanding filter is set to
  `>0`.

When you select a function from the list of functions, the function opens in the Source
browser. The right pane displays the number of (and a link to) the outstanding issues in
that function, as well as the metrics for the function, including HIS (Hersteller
Initiative Software) metrics, if these values are present.

Figure 1. HIS function metrics in the Coverity Connect interface
  
 [image: HIS function metrics display]

## About the With Outstanding Issues view

The Functions: With Outstanding Issues
view is similar to the Functions: In Latest
Snapshot view, except that With Outstanding
Issues displays only functions that have at least one outstanding
issue. It does this using the filter 
Outstanding
`>0`.

An administrator creates the Functions: With
Outstanding Issues view and shares the view with all other users.
When shared by the administrator, other users can only view the content as
configured by the administrator. Users can still modify the original view and create
their own custom views with different names.

Note: With Outstanding Issues is a shared admin view. Shared admin
views always display the admin user's language. If a non-admin user has a different
language than the admin user, this view will not display the non-admin user's chosen
language.
