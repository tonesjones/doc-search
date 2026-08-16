---
title: "View loading - How was the data gathered?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/view-loading-how-was-the-data-gathered-.html"
content_id: "mX9_OM9TLlIuyxfe_6r3YQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:57.540910+00:00"
---

# View loading - How was the data gathered?

The performance data below was gathered using Coverity cloud 2023.9.0 on prem with an
external database with various CPU core configurations.

View Loading responses were calculated by measuring the average loading time over 3 runs
at different concurrencies using medium, large and extra-large sized projects defined by
the total number of issues. The database in question was large (276 GB).
