---
title: "Sigma checkers introduced; legacy checkers retired"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sigma-checkers-introduced-legacy-checkers-retired.html"
content_id: "i4SfXa9R4CGMFHRMoDrWFw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:21.681733+00:00"
---

# Sigma checkers introduced; legacy checkers retired

With the release of Coverity 2021.9.0, the Sigma analysis engine is integrated into
Coverity Analysis. With this integration, a number of legacy Coverity Analysis checkers
have been replaced by Sigma (SIGMA.*) checkers and a number have been removed and not
replaced.

The following list summarizes these changes:

- All OpenAPI (OPENAPI.*) checkers have been replaced by Sigma checkers.
- A number of Coverity Analysis Swift checkers have been replaced by Sigma Swift
  checkers. See Replaced Swift checkers for the complete list.
- All Coverity Analysis Swift checkers not replaced by Sigma checkers have been
  removed (and not replaced). The removed Swift checkers include the parse warning,
  quality, and taint-flow checkers. See Removed Swift checkers for
  the complete list.
- Some Java, Javascript, Typescript, and configuration-file security checkers have
  been replaced by Sigma checkers. See Replaced Java, JavaScript, and TypeScript checkers for the complete
  list.

For more information about Sigma checkers, see the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html).
