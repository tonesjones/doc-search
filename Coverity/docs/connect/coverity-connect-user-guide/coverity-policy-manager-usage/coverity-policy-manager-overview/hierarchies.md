---
title: "Hierarchies"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/hierarchies.html"
content_id: "i68zqnUKVv~Y~h9vqUvwjQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:52.832027+00:00"
---

# Hierarchies

Coverity Policy Manager administrators specify one or more hierarchies through the
Hierarchies configuration screen. For details, see Configuring a hierarchy.

A hierarchy is a tree data structure (a **node tree**) that
underlies one or more Coverity Policy Manager heatmaps or reports. Each node
in a hierarchy represents some part of your code base that has been analyzed and
committed to an instance of Coverity Connect that shares data with Coverity Policy
Manager.

Figure 1. Example: Node tree for a Hierarchy
  
 [image: image]

The terminal (leaf) nodes in a hierarchy are the source of data for the higher level
nodes, which aggregate data from lower level nodes. This aggregation allows you to
examine the code base at increasingly inclusive levels, as described in the Coverity Policy Manager Use Case in
Managing a Coverity Policy Manager hierarchy.

Leaf nodes are associated with a Coverity Connect project. Coverity Policy Manager Administrators can limit the scope of data
for a leaf node to one or more Coverity Connect components that are associated with the selected project.
