---
title: "Verification of modules"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/verification-of-modules.html"
content_id: "MSsBc9OQDbAXR6AYesXNDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:48.423516+00:00"
---

# Verification of modules

When the `-ancmpl` option is in effect each module which is analyzed but
not referenced is reported. All public module variables which are not referenced, not
defined, not allocated or not associated will be listed. All public constants and public
derived types which are not referenced are listed.

If the `-anref` option is also in effect the call tree will be traversed
to detect modules with unsaved public data which are not referenced in the root of
referencing program units. See also Analysis of the reference structure.
