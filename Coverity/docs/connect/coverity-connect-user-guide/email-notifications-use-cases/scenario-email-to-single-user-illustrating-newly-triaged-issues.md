---
title: "Scenario: Email to single user illustrating newly triaged issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-email-to-single-user-illustrating-newly-triaged-issues.html"
content_id: "ZFEauMZj6R8E8_4JfY6KjA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:35.338539+00:00"
---

# Scenario: Email to single user illustrating newly triaged issues

**Goal:** To notify a single developer of all issues triaged in the last 24 hours for
a specific project (Project Y).

**Basic configuration:** In this scenario, a developer creates a view that filters on:

- Last Triaged in the last day
- Only in projects = Project
  Y

The developer then sets the view's columns to all triage values (Classification,
Severity, Action, Owner, Fix Target, Ext. Reference) and adds a notification scheduled
for every night at midnight, with no additional recipients configured.
