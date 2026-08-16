---
title: "CheckerSettings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkersettings.html"
content_id: "UZI8SVRmNCSCtDI4lTlhdQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:28.960244+00:00"
---

# CheckerSettings

The `CheckerSettings` class allows users to configure specific checker
settings during the `cov-run-desktop` analysis.

When merging two Settings objects, the checkers and extend_checkers objects are merged.

- The enabled property of the higher-priority `CheckerConfiguration` is applied
- The 
  `CheckerOptions`
   objects are merged on a per-property basis, with values assigned to
  individual properties of the higher-priority Settings object replacing the
  corresponding values of the lower-priority Settings object
  (including string[] properties)

The `CheckerSettings` class has the following attributes:

enabled?: bool
:   If `true`, then enable the checker. If `false`, then disable
    the checker. If unspecified, the checker is enabled according to the settings in
    the reference snapshot.

options?: CheckerOptions
:   `CheckerOptions`
     objects which define the specific options to configure the checker.
