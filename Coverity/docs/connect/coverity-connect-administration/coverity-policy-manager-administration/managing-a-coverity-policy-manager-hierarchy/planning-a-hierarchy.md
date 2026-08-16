---
title: "Planning a hierarchy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/planning-a-hierarchy.html"
content_id: "MOn2X7ASoZLjVBaAzWYwpw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:01.395674+00:00"
---

# Planning a hierarchy

Before you attempt to create or modify a hierarchy, it is important to understand the needs of your Coverity Policy
Manager users so that you can determine a useful way of organizing the data that the
hierarchy will support. Though it is possible to create a hierarchy that simply
organizes each Coverity Connect project into a
separate node in the hierarchy, Coverity Policy Manager users are likely to require a
different structure. As a basic goal, your hierarchy should allow Coverity Policy
Manager users to see data that matters to them.

It helps to start by thinking of your development organization from the top down, rather
than from the bottom up. For example, a vice president of engineering might want to see
information on all products. A manager who reports to the vice president might need to
check data that is aggregated from all the teams that build one of the products. A team
lead primarily needs to get the status of code managed by that group. Most likely, the
vice president and managers also need to be able to navigate to the areas of the code
base that concern them. So it would be helpful to build one or more hierarchies that
could support such views.

**Coverity Policy Manager Use Case**

Scenario
:   Assume that a company has used Coverity products for several years. Twenty
    project managers oversee a total of sixty software development projects,
    some of which are separate Coverity Connect projects, while others (about half) are components of a single Coverity
    Connect project.

    The director who is in charge of this project management team wants to see
    charts (Status Reports and Trend Reports) that organize data on software
    issues (for example, impact, count, density, and so on) by project
    manager:

    1. You need to set up a hierarchy in which the analyzed source code
       files than contain issues from the company's software projects are
       associated with the appropriate project manager.

       1. You create a separate branch node for each project manager
          (for example, the node might name the project
          manager).
       2. For each branch that represents a separate project manager,
          you create one or more leaf nodes, and associate the leaves
          with the project or component for which each project manager
          is responsible.

          In the case that a given project manager is reponsible for
          managing all software issues in a given Coverity Connect
          project, you can associate the leaf with the entire
          project.

          In the case that the project manager is responsible for
          managing software issues from a subset of source files from
          a Coverity Connect project, you can associate the leaf with
          a component. If the components do not exist, a Coverity
          Connect administrator will need to set them up for you (see
          Using components).

       The following figure represents a portion of the node tree for the
       hierarchy described in this step.

       Figure 1. Example: organizing a hierarchy by management personnel
         
        [image: image]

       For guidance, see Configuring a hierarchy. For
       additional node tree examples, see the figures below.
    2. You need to assign a Coverity Connect role to the director (or to a
       Coverity Connect user group to which the director belongs) that
       allows the director access to the Coverity Policy Manager user
       interface (see Coverity Policy Manager roles and permissions).

       The director can then use the Coverity Policy Manager heatmap and
       charts that are supported by the hierarchy to view and compare data
       on issues associated with each project manager.

       The Coverity Policy Manager charts (heatmaps and reports) allow users
       to navigate to data that is associated with the entire set of
       project managers, with an individual project manager, and with
       individual project or component data that is associated with a leaf
       node. For example, the director can configure the heatmap to show
       policy violations on defect density. A trend chart might show
       changes to issues over time (for example, how many issues are
       introduced and resolved each day). A status report might show the
       number outstanding issues that are of high impact.

Other ways of organizing data are possible. Coverity Policy Manager users might need to
see data organized in any of the following ways:

**By geography**

- A company might have engineering groups in the United States, India, and Japan.
  In such a case, the root node of the hierarchy could be called *Worldwide*,
  and child nodes could be called *U.S.*, *India*, *Japan*. Further
  subdivisions might identify the various cities where the development takes
  place. In this way, an executive in charge of worldwide development and managers
  in charge of the various regions could get the status of all code bases in
  aggregate or broken down by country or city.

  Figure 2 divides the hierarchy
  by geography. The leaf nodes of this hierarchy contain Coverity Connect projects
  and components that are associated with the cities.

  Figure 2. Example: organizing a hierarchy by geographical regions
    
   [image: image]

**By functionality**

- A company might divide its code base into functional units such as front end,
  back end, and so on. In such a case, the children of the root node could be
  named according to those functional divisions, and, if needed, their children
  could be named according to subdivisions of those functional units.

  Figure 3 divides the
  hierarchy into functional units. The leaf nodes of this hierarchy contain
  Coverity Connect projects and components that are associated with them.

  Figure 3. Example: organizing a hierarchy by functionality
    
   [image: image]

**By product or project**

- A company might build multiple products. In such a case, the children of the root
  node could be named according to product name then subdivided further by product
  modules and, if needed, by submodules.

  Figure 4 divides the hierarchy by
  product. The leaf nodes of this hierarchy contain Coverity Connect projects and
  components that are associated with the product modules.

  Figure 4. Example: organizing a hierarchy by product
    
   [image: image]

**By company department or division**

- A company might have engineering teams that span multiple departments or
  corporate divisions. In such a case, the children of the root node could be
  named according those departments or divisions. Each department could be made up
  of further subdivisions, such as teams.

  Figure 5 divides the hierarchy
  by department. The leaf nodes of this hierarchy contain Coverity Connect
  projects and components that are associated with the teams in each
  department.

  Figure 5. Example: organizing a hierarchy by department
    
   [image: image]

**By a hybrid structure**

- A company might have separate front end and back end teams for different
  products. In such a case, the children of the root node could represent each
  product, and the subdivisions of each product could identify the functional
  units of the product. Alternatively, the children of the root could be the front
  end and back end nodes, and the subdivisions of these functional units could
  identify the products. The leaf nodes of this hierarchy could contain Coverity
  Connect projects and components that are associated with submodules of each
  product or with subdivisions of the functional units.

  Figure 6 divides the hierarchy
  first by function, then by product.

  Figure 6. Example 1: organizing a hierarchy by a hybrid structure
    
   [image: image]

  Figure 7 divides the hierarchy
  first by product, then by function.

  Figure 7. Example 2: organizing a hierarchy by a hybrid structure
    
   [image: image]

**By Coverity Connect instance**

- A company might host multiple instances of Coverity Connect that pass data to
  Coverity Policy Manager. In this case, the hierarchy could get data from
  projects and components in each Coverity Connect instance. Though the children
  of the root node could identify each Coverity Connect instance, they need not do
  so. The children could represent any other organizational structure that makes
  sense for the company.

  For example, assume a case in which one instance of Coverity Connect contains
  projects for a set of front end modules that are used by multiple products.
  Assume another instance contains projects for back end modules used by those
  products. A third instance might contain other modules for these and other
  products. In this case, the hierarchy could divide the code base by product and
  then break down each product by module and submodule. The leaf nodes could
  contain Coverity Policy Manager projects and components that are associated with
  the submodules of each product.

  A simpler example, Figure 8,
  explicitly divides the hierarchy by Coverity Connect instance.

  Figure 8. Example: organizing a hierarchy explicitly by Coverity Connect instance
    
   [image: image]

  Figure 9 incorporates projects and
  components from multiple Coverity Connect instances without explicitly
  identifying the instances. Note that this figure includes the same projects and
  components that Figure 8
  includes.

  Figure 9. Example: organizing a hierarchy implicitly by Coverity Connect instance
    
   [image: image]

**With peripheral code bases**

- Perhaps a company uses common libraries, third party code, or legacy code that
  managers want to examine separately from the primary code base. It is possible
  to create separate, high-level nodes in the hierarchy that are just for these
  items. In this case, one of the children of the root could be called
  *Peripheral*, and its children could be called *Libraries*,
  *Third Party*, and *Legacy*. The leaf nodes could then contain the
  projects and components that make up the divisions of the peripheral code
  bases.

  A simpler example, Figure 10,
  contains all the peripheral code in a single, high-level node.

  Figure 10. Example: configuring peripheral code bases in a hierarchy
    
   [image: image]

  Note that if users do not need to get status of some or all of the peripheral
  code base, Coverity Connect projects and components for that code can be omitted
  from the hierarchy. It is also possible to specify peripheral code bases within
  subnodes that use the Exclude from rollup feature; for
  instance, see the Libraries node in Figure 1.

**With new or modified code bases**

- Perhaps a company has added a product or an engineering group. It is possible to
  add nodes for them to an existing hierarchy. It is also possible to delete or
  reorganize existing nodes in the hierarchy.

For procedures on specifying one or more hierarchies, see Configuring a hierarchy.
