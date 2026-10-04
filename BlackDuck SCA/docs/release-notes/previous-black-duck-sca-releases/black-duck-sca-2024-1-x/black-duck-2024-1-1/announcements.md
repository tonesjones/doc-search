---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "F4O_AQh42xXXo2~2LrRo5w"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:30.867324+00:00"
content_hash: "df8056aa8703fda24194d3f2dbd463ba79e756fa4fbdbe4ef6eceaa536616a10"
---

# Announcements

## Black Duck 2024.1.0 Job runner issue (HUB-41654)

A high impact bug (HUB-41654) was identified in 2024.1.0 which affects the Black Duck Job runner and KnowledgeBase Update Check job. This bug causes the Update KnowledgeBase Data job to fail to apply updates to BOMs with new or modified vulnerabilities. This issue will only occur when specific vulnerability conditions apply and is likely to only impact a small number of customer BOMs. We recommend customers running 2024.1.0 upgrade to 2024.1.1 as soon as possible to resolve this issue.

This issue only impacts customers running 2024.1.0. For further details, please see the [Community announcement](https://community.blackduck.com/s/question/0D5Uh000006fsSZKAY/black-duck-202410-jobrunner-issue) regarding this issue.
