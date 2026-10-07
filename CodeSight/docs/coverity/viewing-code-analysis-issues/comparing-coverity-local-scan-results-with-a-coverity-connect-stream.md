---
title: "Comparing Coverity Local Scan Results with a Coverity Connect Stream"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/comparing-coverity-local-scan-results-with-a-coverity-connect-stream.html"
content_id: "V~R12WoBqnD2hXL_z_px8g"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.536828+00:00"
---

# Comparing Coverity Local Scan Results with a Coverity Connect Stream

Compare local Coverity scan results in the Local View against a Coverity Connect stream to distinguish newly introduced issues from existing server issues.

## IDEs Supported

- Visual Studio
- VS Code

## Selecting a Target Stream for Comparison

1. In your IDE, open the **Local View**.
2. In the toolbar, click **Compare with**.

   *Note: The **Compare with** option is only available after a local Coverity scan has completed.*
3. Select the target **Coverity Connect Project** and **Stream**.

   The Local View refreshes with comparison results.
4. To change the baseline stream, click **Compare with** again and select a different project and stream.

## Filtering Issues by Comparison Status

After selecting a target stream, use the filter buttons in the Local View toolbar to narrow displayed issues:

- **All** (default): Displays all local scan results.
- **New** (red editor marker): Displays only issues introduced locally that do not exist in the server snapshot.
- **Existing** (blue editor marker): Displays only issues that already exist in the server snapshot.

Note: If no target stream is selected, issues display with purple editor markers and no comparison labels.

Note: Code Sight generates comparison results on demand against the latest server snapshot when you select a stream or switch filter options.

## Scan Configuration Isolation

Comparison settings (target stream and active filter) are saved per scan configuration:

- Each scan configuration maintains its own **Compare with** target and filter state.
- Scanning with another configuration loads the comparison state saved for that configuration.
- New scan configurations default to the **All** filter with no stream selected.
