---
title: "Code Sight version 2022.6.1"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.6.1.html"
content_id: "z5A8Eo8w5_0xu9x7j8DjoQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.758828+00:00"
---

# Code Sight version 2022.6.1

Version 2022.6.1 is a hotfix that corrects a critical security bug and a couple of previous known issues.

## Bug fixes

- Fixed an issue where the username and password were being exposed in error messaging and in logs.
  UD-9760, UD-9774
- Fixed a bug where Code Sight would not start up when a proxy configured manually in OS settings was not available.
  UD-9568, UD-9674
- Fixed a bug in Visual Studio and Visual Studio Code where Code Sight sometimes did not start up if either
  (1) the `HTTPS_PROXY` environment variable was set to an invalid value or (2) `HTTPS_PROXY` was
  not set and `HTTP_PROXY` was set to an invalid value.
  UD-9615, UD-9656

## See also

Code Sight Support Matrix

Code Sight Known Issues
