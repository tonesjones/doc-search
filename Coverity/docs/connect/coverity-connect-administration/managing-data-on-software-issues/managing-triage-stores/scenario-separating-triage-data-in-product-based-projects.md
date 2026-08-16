---
title: "Scenario: Separating triage data in product-based projects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-separating-triage-data-in-product-based-projects.html"
content_id: "vtwC3qtyJ06aSgbtvDSK8Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:24.115936+00:00"
---

# Scenario: Separating triage data in product-based projects

A company might keep the streams for each product in a separate project. Figure 1 illustrates such a
case. Each stream in a project is for issues from a separate branch (here, rel_1.0_* and
rel_2.0_* streams) of the code base for a given product (here, *_p1 or *_p2). Streams
for the active branch of the code base (here, rel_2.0_* streams) for all products share
the Main triage store, while streams for the maintenance branch (here, rel_1.0_*
streams) share the Maintenance triage store. As in Scenario: Separating triage data by code branch, when triaging a CID in a
project, users (with the appropriate permissions) can triage the CID in all triage
stores (the default) or only in a subset of them by selecting triage stores.

Figure 1. Example: Updating triage value, multiple stores, product-based projects
  
 [image: image]

**To complete the scenario:**

1. Use the procedure in Scenario: Separating triage data by code branch as a guide.

   The only difference to keep in mind is that streams for each release branch
   (rather than for each product) are in separate projects. Nevertheless, both
   scenarios use triage stores in the same way.
2. Click Done to save your changes and exit.
