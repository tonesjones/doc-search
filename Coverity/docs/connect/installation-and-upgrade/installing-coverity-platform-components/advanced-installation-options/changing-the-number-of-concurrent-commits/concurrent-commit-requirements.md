---
title: "Concurrent commit requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/concurrent-commit-requirements.html"
content_id: "pvYB2yicBZW_o38zJmzdVg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:01.363641+00:00"
---

# Concurrent commit requirements

Concurrent commits require additional RAM. Given projects with the following characteristics:

- Files analyzed: ~3000
- Total lines of code input to `cov-analyze`: ~3 million
- Functions analyzed: ~90,000
- Paths analyzed: ~7.5 million
- Defect occurrences found: ~4,000

The amount of memory required is as follows:

- 2 concurrent commits - 8Gb
- 5 concurrent commits - 16Gb (default `commitPoolThreads`
  value)
- 8 concurrent commits - 24Gb

Ideally, you should have 1 CPU core per concurrent commit.
