---
title: "Disks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/disks.html"
content_id: "m18b5UbblCyk7b87YeWECg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:47.639792+00:00"
---

# Disks

Analysis of large codebases (MLoC) is especially sensitive to the random access speed of disks,
though extra memory can mitigate that issue somewhat by serving as OS disk buffers.
Solid state disks (SSDs) show a clear advantage over mechanical fixed disks ("hard
drives"), and the IOPS rating of an SSD is the best predictor of its performance with
Coverity Analysis (higher is better).
