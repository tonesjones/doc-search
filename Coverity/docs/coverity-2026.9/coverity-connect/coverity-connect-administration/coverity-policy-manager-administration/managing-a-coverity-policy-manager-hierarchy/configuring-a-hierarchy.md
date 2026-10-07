---
title: "Configuring a hierarchy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configuring-a-hierarchy.html"
content_id: "bmEBtSBcUPR5RFNkjLufOQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.309344+00:00"
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

- Add: Generates a new hierarchy. See Creating a hierarchy. Note the other Add button (located at the bottom of the screen) is for the
  node tree (see
  - Add: Generates a child node for the
    selected node. You can opt to make this child a branch node or a
    leaf node. If you choose to generate a leaf node, you will be
    able to associate it with a project and, if applicable, a
    specific server.

    Figure 2. Example: Node Creation pop-up window
      
     [image: image]
  - Duplicate: Generates a sibling node that
    is identical to the selected node except for the name. For
    example, a duplicate of Front End is
    named Front End Copy. This sibling will
    contain copies of any descendants of the duplicated node.

    It is not possible to create a duplicate of the root
    node.
  - Delete: Deletes a node from the selected
    hierarchy. Deleting a node also deletes any descendents of that
    node. However, it is not possible to delete the root node.

    If you delete all the descendents of a given branch node, the
    node will have no data associated with it until you associate it
    with a project or create a leaf node for it that is associated
    with a project.).
- Duplicate: Creates a copy of the selected hierarchy that
  is identical except for the name. For example, a duplicate of C and
  C++ is named C and C++ Copy.
- Delete: Deletes the hierarchy along with its node tree.

  Figure 3. Example: Node tree for a Hierarchy
    
   [image: image]
- Import: Uploads a hierarchy configuration to Coverity
  Policy Manager. See Importing/exporting a Coverity Policy Manager hierarchy.
- Export: Downloads a hierarchy configuration to a JSON file. This file is
  convenient for large-scale hierarchy configurations in which you edit this file
  and then import it back to Coverity Policy Manager instead of
  using the node configuration functionality in the UI. See Importing/exporting a Coverity Policy Manager hierarchy.
