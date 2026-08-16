---
title: "How was Commit data gathered?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/how-was-commit-data-gathered-.html"
content_id: "GfXiJ2JNpi6RNj3xZJMTFg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:53.452621+00:00"
---

# How was Commit data gathered?

The performance data below was gathered using Coverity cloud 2023.9.0 on-prem with an
external database.

Commit throughput was calculated by measuring the average commit time over three runs
with high concurrency (the number of commitPoolThreads or greater)
using the medium, large and extra-large IDIRs. Commits were performed at high
concurrency and to different streams to avoid stream locking.

## Medium IDIR (2.6 GB): MONGO V3.0.7

Analysis summary report:

- Files analyzed : 2945 Total

  - C : 329
  - C++ : 2616
- Total LoC input to cov-analyze : 879778
- Functions analyzed : 144039
- Classes/structs analyzed : 31193
- Paths analyzed : 5734303
- Time taken by analysis : 00:08:04
- Defect occurrences found : 11592 Total

## Large IDIR (12 GB): Open office (OOO)

Analysis summary report:

- Files analyzed : 26233 Total

  - C : 613
  - C++ : 25620
- Total LoC input to cov-analyze : 6770079
- Functions analyzed : 495677
- Classes/structs analyzed : 74844
- Paths analyzed : 69082579
- Time taken by analysis : 00:54:46
- Defect occurrences found : 11960 Total

## Largest IDIR (36 GB): Merged IDIRS

Analysis summary report:

- Files analyzed : 93946 Total

  - C : 13840
  - C++ : 80106
- Total LoC input to cov-analyze : 25821156
- Functions analyzed : 1863515
- Classes/structs analyzed : 269824
- Paths analyzed : 194371624
- Time taken by analysis : 03:03:38
- Defect occurrences found : 49491 Total
