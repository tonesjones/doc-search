---
title: "Modifying licenses for a component"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/modifying-licenses-for-a-component.html"
content_id: "ROj5aqOHeed375bXiZc1kw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:41.479570+00:00"
---

# Modifying licenses for a component

So that you can successfully manage license risk, you may need to edit the license(s) for
a component version so that it is different from the component version's declared
license identified in Black Duck KB or the license originally selected for
the version of the custom component.

You can modify a single license or include multi-license scenarios, such as "License A
AND License B" or "License A OR License B". This lets you accurately represent the
licenses in Black Duck for the components in your projects.

Note the following:

- Edits made to a license in the BOM are *local* edits. These edits apply to
  this version of the component for this BOM only.
- Edits made to a license from the Black Duck KnowledgeBase component version page or the custom component version page are *global* edits. These edits
  apply to all instances of this version of the component. However, edits made at
  the BOM level will override these edits.

To modify licenses:

1. To modify a single license:

   1. Click [image: Down Arrow icon] located next to the license name and select the license from
      the list of suggestions.
   2. Do one of the following:
      - Click [image: Confirm icon] to confirm this selection.
      - Click [image: Delete icon] to delete this license and the operand.
2. To add a license to the existing license(s):

   1. Click **Add License**. Black Duck adds the following at the root
      level:

        
       [image: Multi-License]   

      For example, when added to a single license, the following appears:

        
       [image: Single License Addition]   
      - To add a license at the original license level, select the
        license by placing the cursor within the parentheses of that
        license.

          
         [image: Single License]   

        Click **Add License**. The licenses is added at the level of
        the original license:

          
         [image: Multi-License Scenario]

      For example, when added to an existing multi-license scenario, the
      following appears:

        
       [image: Multi-License Add License]   
      - To add a license at the same level as the existing
        multi-licenses, select the license by placing the cursor within
        the parentheses of the existing group.

          
         [image: Multi-License]   

        Click **Add License**. The license is added at the same level
        as the existing licenses:

          
         [image: Multi-License Scenario]
   2. Optionally, click [image: image] next to the operand to change it. Possible values are AND or OR.
   3. Click [image: Down Arrow icon] located next to the license name and select the license from
      the list of suggestions.

      - Click [image: Confirm icon] to confirm this selection.
      - Click [image: Delete icon] to delete this license and the operand.
   4. Repeat as necessary.
3. To add a multi-license scenario (for example, License A AND (License B OR License
   C):

   1. Click **Add Group**. Black Duck adds the following at the root
      level:

        
       [image: Multi-License Scenario]   

      When added to a single license, the following appears:

        
       [image: Multi-License Scenario]   
      - To add a group at the original license level, select the license
        by placing the cursor within the parentheses.

          
         [image: Single License]   

        Click **Add Group**. The following appears:

          
         [image: Add Group]

      When added to an existing multi-license scenario, the following
      appears:

        
       [image: Multi-License Scenario]   
      - To add a group at the original license level, select the license
        by placing the cursor within the parentheses:

          
         [image: Add Group]   

        Click **Add group**. The following appears:

          
         [image: Add Group]
   2. Optionally, add additional licenses as described in step 6a.
   3. Optionally, click [image: image] next to the operand to change it. Possible values are AND or OR.
   4. Click [image: Down Arrow icon] located next to the license name and select the license from
      the list of suggestions.

      - Click [image: Confirm icon] to confirm this selection.
      - Click [image: Delete icon] to delete this license and operand.
   5. Repeat as necessary.
4. Optionally:
   - Select **Reset Changes** to display the license(s) that appeared when
     you initially opened this dialog box.
   - Select a group and select **Delete Selected Group** to remove this
     group.
5. Click **Save Changes** if editing the license in the BOM or **Save**.

   The
   assigned license is updated. If the new license carries a different type of
   license risk than the previous one, the license risk
   calculations for the component and for the project version are
   updated in project version BOMs. A [image: Information icon] appears in the table row in the BOM to indicate that a manual
   adjustment was made to this component.

   When viewed in the BOM, the license
   obligations for the revised license(s) will appear when you re-open the
   *Component Name Version* Component License dialog box.

## Reverting BOM-level license edits

If you selected a different license for a component when editing licenses in the BOM,
you can revert the license to its original license as defined in Black Duck KnowledgeBase.

To revert to an original license:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the
   BOM.
4. Select the to open the *Component Name Version* Component License dialog
   box.

     
    [image: Component license dialog box]
5. Select the Edit Mode option to enable editing.

     
    [image: License dialog box]
6. Select **Revert to Original** to revert the license
7. Click **Save Changes**.

   The license is reverted. If the license carries a
   different type of license risk than the previous one, the license risk
   calculations for the component and for the project version are
   updated in the BOM.
