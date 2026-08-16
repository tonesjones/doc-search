---
title: "Assigning RBAC roles on a synchronized Coverity Connect cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assigning-rbac-roles-on-a-synchronized-coverity-connect-cluster.html"
content_id: "hGXzL~~mDrxxoj_RguZj~Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:49.009225+00:00"
---

# Assigning RBAC roles on a synchronized Coverity Connect cluster

If you are using a Coordinator to synchronize multiple Coverity Connect instances, the
global, triage store, and component level roles must be set on the Coordinator. Any of
these roles that are set on the Coordinator are shared with each Subscriber within the
enterprise. Roles for the project and stream levels, however, can be set on and are
local to each Subscriber instance. If you are using Coverity Connect as a standalone
instance, roles can be set for each level on that Coverity Connect instance. Please note
that *in order for a developer to be able to triage issues,* the developer must
have the appropriate roles set at the triage store, component, stream, and component map
levels. For an example, see Scenario: Granting triage permissions on a synchronized Coverity Connect enterprise cluster.

Figure 1. RBAC roles on a Coverity Connect cluster
  
 [image: image]

For more information about Coverity Connect synchronization, see Synchronizing multiple Coverity Connect instances.
