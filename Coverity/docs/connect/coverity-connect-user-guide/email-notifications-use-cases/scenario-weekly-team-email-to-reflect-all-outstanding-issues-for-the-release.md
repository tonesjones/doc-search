---
title: "Scenario: Weekly team Email to reflect all outstanding issues for the release"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-weekly-team-email-to-reflect-all-outstanding-issues-for-the-release.html"
content_id: "604b072vNy_f3JgG7Ebm3g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:34.062026+00:00"
---

# Scenario: Weekly team Email to reflect all outstanding issues for the release

**Goal:** To send a team-wide email notification once a week highlighting any issues
that have been introduced since the last software release.

**Basic configuration:** In this scenario, the team lead creates a view that filters
on:

- Status = New or
  Triaged
- First Detected date is after last release
  date

The team lead then adds a notification scheduled for once a week, and adds each
team member individually or adds a group including the team members to the list of
recipients.
