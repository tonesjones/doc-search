---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "MB7LqCtCGjdZL9ReWbXZ2A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:02.688647+00:00"
---

# Announcements

## Updated automatic project version deletion feature

Black Duck 2023.1.0 updated the automatic project version deletion feature (formerly
known as Automatic Data Removal). This feature is now enabled by default upon
upgrading to 2023.1.0 and any upcoming future releases.

Automatic project version deletion allows the automatic removal of old project
versions within Black Duck. The default settings will remove project versions which
have not been updated or scanned within 90 days. Upon upgrading to 2023.1.x, any old
project versions which have not been updated or re-scanned in 45 days will be
deleted 45 days after upgrade assuming they are not re-scanned or updated post
upgrade. These settings can be changed under the system administrator data retention
settings page.
