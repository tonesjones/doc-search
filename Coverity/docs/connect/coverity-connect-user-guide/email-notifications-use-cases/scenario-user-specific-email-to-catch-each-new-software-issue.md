---
title: "Scenario: User specific Email to catch each new software issue"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-user-specific-email-to-catch-each-new-software-issue.html"
content_id: "WFrvb4SL5~P~zavZKHp8JQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:34.695805+00:00"
---

# Scenario: User specific Email to catch each new software issue

**Goal:** To notify any member of a team when a new issue is detected in the code for
which they are personally responsible.

**Basic configuration:** In this scenario, the team lead creates a view that filters
on:

- First Detected in the last day
- Owner = <User> (for relative user)

The team lead then adds a notification scheduled for every night at midnight, with
each team member or group included in the list of recipients.
