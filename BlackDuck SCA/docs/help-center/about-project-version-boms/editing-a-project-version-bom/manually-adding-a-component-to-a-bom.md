---
title: "Manually adding a component to a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/manually-adding-a-component-to-a-bom.html"
content_id: "SpCvlxzKExbLrzXR_QWwoA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:33.543379+00:00"
---

# Manually adding a component to a BOM

Once you have mapped a component scan to a project version, the scan results
automatically populate the project version's BOM with the discovered components.
Although the BOM contains all the components discovered in the mapped scan, there may be
other components that you are using in that version of your project that either were not
discovered in one of the mapped scans or were not scanned.

You can manually add components to the project version's BOM so that they are included in
all project version information and risk calculations. You must manually add the
component to the BOM of each version of the project in which you use it. You cannot
manually add a component to the BOMs of multiple versions of a project at once.

Note: If a subsequent component scan automatically updates the project version's BOM to reflect
the discovered OSS components that are included in the BOM, any OSS components that you
have manually added to the BOM will be unaffected by that update. Components that are
added to the BOM manually can only be deleted from the BOM manually.

To manually add a component to a BOM:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab.  
    [image: BOM page]
4. Click **Add** and select **Component** to open the Add Component dialog
   box.
5. Enter the name of the component that you want to add. The search results will
   attempt to return possible matches based on this priority ranking:

   - Exact string matches regardless of component origin i.e. "apache
     log4j"
   - Custom components with fuzzy match
   - Fuzzy KnowledgeBase component match used in this or other projects
   - Other fuzzy match KnowledgeBase components

   Note below, when searching for "apache log4", the “Apache Log4” component appears first as
   this is a exact string match and is a custom component. It is then followed by
   Apache Log4j, the KnowledgeBase component match.

     
    [image: Add Component modal]
6. Optionally, enter or select a version and an origin ID.
7. Optionally, select **Advanced Attributes** and do the following:
   - Enter the purpose for adding this component.
   - Select **Modification** if you modified this component and optionally,
     enter information regarding the modification.
8. Click **Save**.

   - Black Duck adds the component to the project
     version's BOM. An [image: image] icon appears in
     the row of the manually added component If you entered a purpose or you
     specified that you modified the component and entered information
     regarding the modification.
   - The **Match Type** column indicates that the component was added to
     the project version's BOM manually (**Manually Added**).
   - All vulnerability data, license information, version age information, and
     project development activity information for the component that you
     added to the BOM is pulled from Black Duck KB and used to
     update the security, license, and operational risks for this version of
     your project.
