---
title: "Creating a hierarchy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-hierarchy.html"
content_id: "mTSUN3Am4e2BnZ64id4Meg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:03.160546+00:00"
---

# Creating a hierarchy

Before creating a hierarchy, take time to plan. Think about the kind of data that your
Coverity Policy Manager users need to see in the heatmaps and charts. For
guidance, see Planning a hierarchy.

**To create a hierarchy:**

1. Navigate to the Configuration - Hierarchies window by
   selecting Hierarchies from the
   Configuration menu.

   Figure 1. Example: Configuration menu
     
    [image: image]

   Note: If Hierarchies does not appear in this menu, you need
   to get permission to view and manage hierarchies from your Coverity Connect
   administrator (for more details, see Coverity Policy Manager roles and permissions).
2. Use the Add button (in the top-left portion of the
   Configuration - Hierarchies window) to create the
   hierarchy.

   See an example of this window in Figure 1.

   This action opens a pop-up window in which you can type a name and description
   for the hierarchy (recommended), and opt to generate a flat hierarchy that
   contains a single root node with a separate leaf node for each Coverity Connect
   project. If you do not select this option, the new hierarchy will contain a
   single root node.

   You can also select which server you would like the data to be drawn from. Your
   local server will be selected by default, but additional servers will be
   available to Coverity Connect instances that serve as Coordinators to one or
   more Subscribers. See Synchronizing multiple Coverity Connect instances for more
   details.

   Figure 2. Example: Hierarchy Creation window
     
    [image: image]

   The name and description of the hierarchy will appear to end users in the
   Coverity Policy Manager list of hierarchies and in navigation menus. For
   examples, see the figures in Shared navigation and Main Menu tools. The name must be
   unique.

   Note: The following characters are not allowed in the name of a hierarchy:
   `:`
   `\`
   `/`
   `*`
   `'`
   `"`
3. Specify the node tree for the hierarchy:

   1. [Recommended] Change the automatically generated name of the root node
      for the hierarchy (New Hierarchy Node) by typing it into the lower-right
      Name field.

      The name of the root name will appear in Coverity Policy Manager charts
      (see the Sample Company root node in Figure 1). Note that
      the name of the root node can differ from the name of the hierarchy.

      The name of the root often indicates the relationship of the root to the
      children (for examples, see Planning a hierarchy). Note
      that it is not possible to create a sibling of the root node.
   2. Use the buttons at the bottom of the screen to generate nodes (add or
      duplicate) or delete nodes (along with all descendants of the deleted
      node).

      Note that nodes located at the same level in the tree must have different
      names.

      **Node Tree Buttons**

      - Add: Generates a child node for the
        selected node. You can opt to make this child a branch node or a
        leaf node. If you choose to generate a leaf node, you will be
        able to associate it with a project and, if applicable, a
        specific server.

        Figure 3. Example: Node Creation pop-up window
          
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
        with a project.

      Tip: In general, the following limits are recommended:
      - 1-100 child nodes for a single branch node.
      - Upper bound of 2000 nodes for the entire node tree.
      - Node depth of 1-10 levels, where 1 is the level of a child of
        the root node, 2 is a "grandchild" of the root node, and so
        on.

      Drag and Drop functionality
      :   You can move a node to a new location in a hierarchy by
          selecting it, then dragging and dropping it to the desired
          location. Any descendents of a branch node will move along
          with the branch you select.
   3. If you do not want data from a given node to contribute to data values of
      its parent and ancestor nodes, check Exclude from
      rollup for that node.

      Figure 4. Example: exclude node from rollup
        
       [image: image]

      In the example, values from the selected, third
      party node are excluded from rollup.

      This functionality can be useful for excluding data on issues from
      peripheral code bases (perhaps some third-party source) that your
      organization does not need to assess. For example, see With peripheral code
      bases.
   4. Associate your leaf nodes with a project (and any components).

      Figure 5. Example: associating a project and component with a node
        
       [image: image]

      To support any data, a leaf must be associated with a single Coverity
      Connect project. Optionally, a leaf can narrow the scope of the project
      data by specifying a list of components. You can opt to Include or
      Exclude data that is derived from the
      specified components.

      Note: If you add a node to a leaf node, the leaf will become a branch node
      and lose any association with a project (and components). The new node
      will become a leaf to which you can associate a project and any
      components. The leaf will retain its association with a project or
      component even if the name of the project or component changes. If the
      project with which a leaf is associated gets deleted, the leaf will no
      longer have data associated with it. Similarly, if the leaf is
      associated with a single component, and that component gets deleted, the
      leaf will no longer have data associated with it. The UI will indicate
      when a project or a component with which a leaf is associated gets
      deleted.
4. Click the Done button to save your changes.
