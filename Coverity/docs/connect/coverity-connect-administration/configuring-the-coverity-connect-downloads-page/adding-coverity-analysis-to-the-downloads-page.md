---
title: "Adding Coverity Analysis to the Downloads page"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-coverity-analysis-to-the-downloads-page.html"
content_id: "YhdV9aROnrplKX1~9QkBqw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:57.778757+00:00"
---

# Adding Coverity Analysis to the Downloads page

Coverity Connect allows you to add Coverity Analysis product packages and license files
to the Downloads page, so that Coverity Desktop users can obtain
and install Coverity Analysis from a central location:

1. Obtain the Coverity Analysis packages (.exe for Windows
   systems or .sh for Unix) that you want to make available to
   your users.
2. Copy the Coverity Analysis installer packages into the
   <install_dir>/server/base/webapps/downloads
   directory.
3. Optionally copy the Coverity Analysis license (license.dat)
   file into same directory.

Users with proper sign-in credentials and permissions can now download the Coverity
Analysis package and install it on their system.

Note: Make sure the Coverity Analysis package version is compatible with the
Coverity Connect version. Version mismatches can cause
runtime failures. For more information, see Compatibility between Coverity product components in the Coverity 2026.6.0 Installation and Upgrade Guide.
