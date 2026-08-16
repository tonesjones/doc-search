---
title: "Modifying licenses in a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/modifying-licenses-in-a-bom.html"
content_id: "simSXnXYy7H4Gpz2ORErPw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:40.785000+00:00"
---

# Modifying licenses in a BOM

So that you can successfully manage license risk, you may need to edit the license(s) for
a component version used in a BOM so that it is different from the component's declared
license identified in Black Duck KB.

You can modify a single license or include multi-license scenarios, such as "License A
AND License B" or "License A OR License B". This lets you accurately represent the
licenses in Black Duck for the components in your projects

If you have modified a license, you can select to revert it back to the license as
defined by Black Duck KnowledgeBase.

Note: License adjustments can be made at both the project and project version levels. This
behavior is controlled by the **Component Adjustments** project setting, which also
governs other component adjustments.

To modify licenses:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the BOM.
4. Select the single license or multi-license to open the *Component Name
   Version* Component License dialog box.

     
    [image: Component license dialog box]
5. Select the Edit Mode option to enable editing.

     
    [image: Component License dialog box]
6. Edit the license as described here.
