---
title: "Enhancing Single-File Scans with Central Scan Results"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/enhancing-single-file-scans-with-central-scan-results.html"
content_id: "pKrF3qXIZQlemW0iJacpVQ"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.889841+00:00"
---

# Enhancing Single-File Scans with Central Scan Results

When performing a **single-file scan with Coverity**, you can
significantly improve result accuracy by **referencing a previously run full central
scan**. This approach allows your local scan to leverage the analysis context from
the central scan.

Important: This enhancement requires that a full scan has already been run on
the server for the stream or project you reference.

## Configuration Options

Add one of the following Coverity
configuration files at the root of your repository (working
directory):

- **Using a Coverity YAML/JSON Configuration**

  - **Compatible with:**
    Coverity Connect
  - **File type:**
    `coverity.yaml` or `coverity.json`
  - **Configuration:** Specify the stream from the central scan
  - **Performance impact:** Downloads analysis summaries only
  - **Benefit:** Improves single-file scan accuracy while minimizing
    network traffic
- **Using a Coverity CONF Configuration**

  - **Compatible with:**
    Coverity Connect and Coverity on
    Polaris
  - **File type:**
    `coverity.conf`
  - **Configuration:** Specify the stream (Connect) or project
    (Coverity on Polaris) from the central scan
  - **Performance impact:** Downloads both analysis settings and
    summaries
  - **Benefit:** Provides the highest fidelity for single-file
    scans

## Benefits of Synchronizing with Central Scan Results

- **Improved Accuracy:** Single-file scans use the same configuration and
  context as the full scan
- **Time Efficiency:** Avoids running a full local scan for single-file
  analysis
- **Result Consistency:** Local findings align more closely with central
  scan results
