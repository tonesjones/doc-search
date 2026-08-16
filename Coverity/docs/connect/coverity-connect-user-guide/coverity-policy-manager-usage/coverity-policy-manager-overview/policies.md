---
title: "Policies"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/policies.html"
content_id: "2wi9rlyt7JKX0PWDyvHS1Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:57.265295+00:00"
---

# Policies

Coverity Policy Manager policies are thresholds you set in heatmaps so that you can evaluate the
integrity of your code base, and so that you can check other information, such as
Coverity Connect activity levels. In Coverity Policy Manager, a policy is expressed as a
simple formula that, when applied to report data, determines whether a given data point
is compliant (displayed in green), at risk (displayed in yellow), or in violation
(displayed in red) of your standards. For example, an Issue Density report might display
in a yellow band the data points that fall within 1.0-1.8 software issues per thousand
lines of code (issues/KLOC) and show in a red band the data points that exceed 1.8
issues/KLOC. Data points below 1.0 issues/KLOC would appear in a green band. Coverity
Policy Manager permits one policy per heatmap.

For an example that shows how to set a policy for a heatmap, see Figure 1.
