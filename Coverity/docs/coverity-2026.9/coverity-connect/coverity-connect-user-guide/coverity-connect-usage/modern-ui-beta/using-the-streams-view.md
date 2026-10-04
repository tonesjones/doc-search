---
title: "Using the Streams View"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/using-the-streams-view.html"
content_id: "QL~Jfzpb99Xo~S6U6QCq~w"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:32:58.975228+00:00"
---

# Using the Streams View

The Streams View gives you a centralized place to review, navigate, and manage the streams within a project.

After selecting a project from the Projects page, you enter the Streams View. Each stream is displayed as a card that summarizes key metrics, including issue counts broken down by security and quality impact.

From the Streams View, you can:

- Browse streams and review their health status at a glance.
- Search for a stream by name.
- Sort streams by name, lastest scan, or open issues.
- Apply filters to focus on streams with specific characteristics.
- Select a stream to navigate into the Issues View for that stream.
- Activate and deactivate streams (requires admin permission).

Navigation hierarchy: Projects page → Streams View → Issues View.

## Stream cards

Each card represents one stream and includes the following information:

- Stream name.
- Last scan
- Open Issues (clickable — Total number of issues with applied filter New and
  Triaged)
- Security issues breakdown by impact (Very High, High, Moderate, Low, Very Low,
  None).
- Quality issues breakdown by impact (High, Medium, and Low).
- Administrative actions — Toggle active status — are visible only to users with
  the appropriate stream admin permissions.

When you click an issue count on a stream card, the Issues View opens with the corresponding view and stream filter applied. The view label shows (modified) to indicate that a filter has been added.

## Navigation and breadcrumbs

After entering the Issues View for a stream, the page header displays the stream name in a breadcrumb combobox. You can use this combobox to switch to a different stream without returning to the Streams View.

## Permissions

The Streams View displays only the streams you have permission to access. Administrative actions — create, edit, delete, and toggle active status — are visible only to users with the appropriate stream admin permissions.
