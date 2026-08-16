---
title: "Viewing heatmap data"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-heatmap-data.html"
content_id: "8Ut8zf3ZVrKnDL4Vqk_kIA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:32.897667+00:00"
---

# Viewing heatmap data

The Black Duck Heatmap provides an intuitive and powerful solution to capture, present,
analyze, distribute, and automate data analysis, problem detection, problem
identification, and applying limited solutions that are mapped to known problems.
Statistical data from Black Duck is represented in a matrix with hour of day as one axis
and day (or date) of month as the other axis.

The heatmaps are color coded to display the minimum and maximum value in the dataset and
to calculate percentages for each value relative to the minimum and maximum. The
smallest number is 0% (green color) and the largest is 100% (red color). We then use
this percentage to determine the exact color value to use in the heatmap.

[image: image]

Note: Red values in the heatmap does not indicate an error. It is the maximum boundary when
determining the amount of scans conducted in the last 30 days.

To view a UI representation of the heatmap:

1. Log in to Black Duck with one of the following roles:

   - Global Code Scanner
   - Global Notification Viewer
   - Global Project Administrator
   - Global Project Manager
   - Global Project Viewer
2. Click [image: image] .
3. Select **Heatmaps** in the **Diagnostics** section of the Admin menu.

Note: Heatmap data is populated when the scan is completed and becomes read-only afterwards.
Changes made to the projects are not synced with heatmap data.

## Filtering the heatmap

You can filter the data displayed in the heatmap by clicking the blue **+ Filter**
button on the top right of the page and then using any of the following options.
Multiple filters can be added simultaneously to further refine the results:

- **Code Location ID**: Select one or many code location IDs.
- **Code Location Name**: Select one or many code location names.
- **Project Name**: Select one or many project names.
- **Scan Date**: Select a start and end date.
- **Scan Status**: Select from Success, Started, and/or Failure.
- **Scan Type**: Select from the available scan types.
- **Version Name**: Select any version names.

You can edit filters by clicking on an existing filter and adding additional
criteria. You can remove an active filter by clicking the [image: image]
button to the right of the filter.
