---
title: "Security scores, severity mappings, and assurance levels"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-scores-severity-mappings-and-assurance-levels.html"
content_id: "UH6MFLNUk_Xv3guDvs9ILg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:16.866471+00:00"
---

# Security scores, severity mappings, and assurance levels

The Security Report application analyzes the issues returned by Coverity Connect and
calculates a Security Score, based on the severity mapping selected when you configure
the report. The Security Report Generator compares this value to the required **Assurance Level** and determines if the Security Score passes
or fails. For more information, see the next section.

When you configure the report generator, you select the **Assurance
Level**. There are four Assurance Levels, representing Security Scores of greater
than or equal to 60, 70, 80, and 90. When choosing the Assurance Level, consider the
potential for damage to life, property, or reputation. An application with high damage
potential should have a high Assurance Level.
