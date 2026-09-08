---
title: "Understanding InfraSec Correlation"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/understanding-infrasec-correlation.html"
content_id: "BtRNk4L2cm9NIPyz49ghPQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:58.716927+00:00"
content_hash: "3b0be4657fda922d8ad70c76691c5d212c78f90ff11521c0beff13422642dd6e"
---

# Understanding InfraSec Correlation

In InfraSec correlation, results with matching Host information may be correlated if the
list of CVEs is an exact match between the available results. Results with differing
host information will be marked with a "do not correlate" flag, which will prevent
correlation by any other process.
