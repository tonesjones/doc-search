---
title: "Setting global SCM rules and the SCM user map"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-global-scm-rules-and-the-scm-user-map.html"
content_id: "FeoCwdOvDeYDVjMz8P72rA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:29.943639+00:00"
---

# Setting global SCM rules and the SCM user map

If you have made the decision to enable Coverity tools to assign owners based on SCM
data, the first step is to configure the following globally-defined items:

1. Go to Configuration > System > Automatic Owner Assignment.
2. Choose a global SCM derivation
   rule.
3. Define an SCM
   to Coverity Connect user map file.

Figure 1. SCM system settings for automatic owner assignment
  
 [image: image]

Note: In a Coverity Connect clustered environment, all of these settings are synchronized,
so you can only set them on the coordinator and not on the subscribers. For more
information, see Synchronizing multiple Coverity Connect instances.
