---
title: "Other deployment models and features"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/other-deployment-models-and-features.html"
content_id: "Ftai68pMleAJ5G5jdO8elg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:44.632927+00:00"
---

# Other deployment models and features

The following diagram represents additional (and optimal) deployment considerations that
can add value to the developers and administrator of your system.

[image: image]

**The flow is as follows:** 

1. The developer fixes issues after being notified by Coverity Connect
2. The developer checks the fixes into the build.
3. Coverity analysis tools run on the code base.
4. Before the results are committed to Coverity Connect, the build administrator
   creates the Preview Report to make
   sure that the code is clean before checking it in.
5. After the code is checked in, results of a passing or failing build is  reported in Jenkins.
6. An issue report is exported in XML format
   and integrated into the organization's third party plug-in.
