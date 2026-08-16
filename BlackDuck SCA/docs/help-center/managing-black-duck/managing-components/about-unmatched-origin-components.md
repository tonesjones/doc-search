---
title: "About unmatched origin components"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-unmatched-origin-components.html"
content_id: "SZNEl0DZ_o5LMwIFKz3RXA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:22.109437+00:00"
---

# About unmatched origin components

Components with unmatched origins are components with origin IDs that Black Duck
identified during a package manager scan but could not be mapped to a component version.
You can manually map any given origin ID to a custom component version.

Components with unmatched origins can be found in these locations in Black Duck:

- Scans page: Click the desired scan
  and then click the View BOM Import Log button to view the components with
  unmatched origins specific to this scan.
- Project version BOM page: Click the Unmatched link on the top right
  of the BOM report to view the components with unmatched origins specific to this
  project version.
- Unmatched Origins page:
  Users with the Component Manager role can click the Manage button and then select
  Unmatched Origins.
