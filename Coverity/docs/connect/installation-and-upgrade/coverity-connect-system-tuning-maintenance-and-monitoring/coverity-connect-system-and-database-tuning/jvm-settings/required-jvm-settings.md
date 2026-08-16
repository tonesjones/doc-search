---
title: "Required JVM settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/required-jvm-settings.html"
content_id: "qFhMlnCQ5wrpMcIxQnBPcg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:15.123600+00:00"
---

# Required JVM settings

Table 1. Required JVM settings

| Parameter | Setting and notes |
| --- | --- |
| `-server` | Explicitly set the server runtime (as opposed to the client runtime). There are no additional arguments. |
| `-Xms` | Set the minimum heap size. Example usage: `-Xms512m` |
| `-Xmx` | Set the maximum heap size. Example usage: `-Xmx8g` |
