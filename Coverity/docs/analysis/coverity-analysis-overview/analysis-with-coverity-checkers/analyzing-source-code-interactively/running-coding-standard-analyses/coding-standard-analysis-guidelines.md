---
title: "Coding-standard analysis guidelines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coding-standard-analysis-guidelines.html"
content_id: "TQHgmX_rFe7XwiPVQeqhRA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:11.745464+00:00"
---

# Coding-standard analysis guidelines

To avoid problems, follow these guidelines in running coding-standard analyses:

- If you want to run both coding-standard and non-coding-standard analysis on the same source,
  we recommend that you perform separate analyses that you commit to separate streams.
  Follow these steps:
  1. Run `cov-build` once.
  2. Run `cov-analyze` and `cov-commit-defects`
     for the non-coding-standard analysis.
  3. Run `cov-analyze` again with the `--force`
     option for the coding standard analysis, followed by
     `cov-commit-defects` to the coding standard
     stream.
- For coding standard analysis only, use the `--emit-complementary-info`
  option to the `cov-build` command. Otherwise,
  `cov-analyze` will silently run the build again to capture the
  additional information it needs.
- Coding standard analysis can report an overwhelming number of issues. We
  recommend you apply Mandatory rules first, then apply Required rules, and then
  Advisory rules. These categories and the rules are listed in one of the
  following directories:
  - <install_dir>/config/coding-standards/misracpp2023
  - <install_dir>/config/coding-standards/misrac2023
  - <install_dir>/config/coding-standards/misrac2004
  - <install_dir>/config/coding-standards/misrac2012
  - <install_dir>/config/coding-standards/misracpp2008
  - <install_dir>/config/coding-standards/autosarcpp14
  - <install_dir>/config/coding-standards/cert-c
  - <install_dir>/config/coding-standards/cert-cpp
  - <install_dir>/config/coding-standards/cert-c-recommendation
  - <install_dir>/config/coding-standards/cert-java
  - <install_dir>/config/coding-standards/hyundai-c
  - <install_dir>/config/coding-standards/hyundai-cpp
  - <install_dir>/config/coding-standards/hyundai-java
  - <install_dir>/config/coding-standards/iso-ts17961
