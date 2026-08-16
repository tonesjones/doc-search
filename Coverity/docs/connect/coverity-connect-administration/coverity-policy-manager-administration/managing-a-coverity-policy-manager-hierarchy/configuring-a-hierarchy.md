---
title: "Configuring a hierarchy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-a-hierarchy.html"
content_id: "bmEBtSBcUPR5RFNkjLufOQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:02.211145+00:00"
---

# Configuring a hierarchy

In Coverity Policy Manager, a hierarchy
specifies an ordered tree data structure (a node tree) for heatmaps and charts. You can create and maintain
hierarchies through the Coverity Policy Manager UI or through a JSON file (see Importing/exporting a Coverity Policy Manager hierarchy). The JSON
import/export feature is preferred for large hierarchies or large-scale changes. The UI
is preferred when creating smaller hierarchies or when making small-scale modifications
to existing hierarchies.

Figure 1. Example: Hierarchy Configuration window
  
 [image: image]

As shown in Figure 1, the
Name column (top-left portion of the window) lists all
hierarchies that have been created. Selecting a name in this list allows you to use the
edit settings fields for the hierarchy.

**Hierarchy buttons**

- Add: Generates a new hierarchy. See Creating a hierarchy. Note the other Add button (located at the
  bottom of the screen) is for the node tree (see Node Tree
  Buttons).
- Duplicate: Creates a copy of the selected hierarchy that
  is identical except for the name. For example, a duplicate of C and
  C++ is named C and C++ Copy.
- Delete: Deletes the hierarchy along with its node
  tree.
- Import: Uploads a hierarchy configuration to Coverity
  Policy Manager. See Importing/exporting a Coverity Policy Manager hierarchy.
- Export: Downloads a hierarchy configuration to a JSON
  file. This file is convenient for large-scale hierarchy configurations in which
  you edit this file and then import it back to Coverity Policy Manager instead of
  using the node configuration functionality in the UI. See Importing/exporting a Coverity Policy Manager hierarchy.
