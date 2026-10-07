---
title: "Using the project landing page"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/using-the-project-landing-page.html"
content_id: "AIz~CjEcVynyxCfTTtAUCA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:32:58.822543+00:00"
---

# Using the project landing page

The Projects page gives you a single place to review the projects you can access and
move into the next level of work.

The Projects page is the first page you see after logging in to Coverity in
the modern UI. It presents all projects you have access to as a card-based view, aligned
with the Black Duck SCA experience. Each project card surfaces key health and activity
information at a glance, and acts as a navigation and action surface.

From the Projects page, you can:

- Scan project cards for recent activity and issue distribution.
- Search for a project by name.
- Sort projects to surface the most relevant items.
- Apply filters to reduce the visible list.
- Switch to the Favorites tab to view projects you have marked as
  favorites.
- Open a project to continue into its Streams View.

## Project cards

Each card represents one project you can access and includes the following
information:

- Project name, as a clickable link to the Streams View.
- Last scan or analysis timestamp.
- Active Streams count.
- Job status indicator (when scan service is enabled).
- Security Risk summary.
- Quality Risk summary.
- Favorite toggle.

## Search, sort, and filter

The toolbar above the project cards provides controls to find and organize
projects:

- **Search** — Finds projects by name using a case-insensitive substring
  match.
- **Sort** — Orders the project list by criteria such as Latest Scan, project name, or
  Active Streams. By default, projects are sorted by Latest Scan, with the most
  recently scanned projects displayed first.
- Add filters — Narrows the list by criteria such as Last Scan and
  Stream Count.

## Favorites

Use the favorite toggle on a project card to mark projects for quick access. The
Favorites tab shows only your favorited projects. Favorite
state persists across page reloads.

Note: The capabilities available in the previous release's Modern UI Projects landing
page are not supported in the latest Projects landing page:

- Project page CSV Export
- Project page XML Export
- Saved Project Views / Custom Project Views

Search, filter, sort, and pagination states are not preserved when navigating
away from the Projects page and returning via the sidebar Projects menu or Projects
breadcrumb.

## Security risk and quality risk cards

Security Risk and Quality Risk cards provide a stream-level summary of findings within a project.

- Each active stream is counted only once and is assigned to its highest
  Security or Quality Risk level.
- The total count across all risk buckets equals the Active Streams
  count shown on the project card when all active streams have the issue
  committed to them.
- The cards are designed to highlight the highest-risk streams by classifying
  each stream according to its highest risk level.
- Clicking either the colored risk bar or the corresponding count opens the
  Streams View with the selected risk filter applied.
- The Security Risk and Quality Risk cards reflect the latest snapshot data of
  the streams.
