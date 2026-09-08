---
title: "Built-In Open Source Dependency Scanners"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/built-in-open-source-dependency-scanners.html"
content_id: "oK05Ir4_GxEKfKzm1nj9Aw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:36.859353+00:00"
content_hash: "7903a4bddd2f78b94a7d920ba27f2de0fcbc1fc7470ab9cf48ea23aaa56db60d"
---

# Built-In Open Source Dependency Scanners

Software Risk Manager also scans input to check for dependencies with known
vulnerabilities.

The following dependencies are checked:

- **Java:**
  `.jar` and `.war` files in Java projects.
- **.NET:**
  `.exe` and `.dll` files in .NET projects.
- **JavaScript** files are checked by name or a hash of the file (minified
  JavaScript incorporated into a different source file will not be checked).
