---
title: "Editing license text in the BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/editing-license-text-in-the-bom.html"
content_id: "i6VpEZ0iv~rKYX4J0VGdIw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:43.298833+00:00"
---

# Editing license text in the BOM

You may notice that the license text for some components is incomplete as the Black Duck KB may not have the full license text for some components. Since
most attribution clauses in licenses usually require at a minimum that the license text
be provided in any redistributions, you may need to edit the existing license text.

Note the following:

- Edits to license text only apply to the license text for that component version:
  edits do not apply to other components with the same license.
- If you selected to make edits persistent then edits to license text apply to all
  existing versions of a project and will also be carried forward as additional
  scans are completed for the same code or Docker image.
- There is an option to revert to the original license text.
- The dialog box displays the first and last name and date or time the license text
  was edited above the license text.

    
   [image: username and date or time the license text was edited]   

  This message appears for local or global edits
  (made by the License Manager).
- If you edited the original license, saved the changes, selected a different
  license, and then select the original license, your edited version of the
  license will appear.
- Edits made globally to
  licenses by the License Manager will propagate to the version used in
  the BOM unless the BOM Manager or Project Manager has edited the license,

To edit license text:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the BOM.
4. Select the license name to open the *Component Name Version* Component
   License dialog box.

     
    [image: image]
5. Select the license you wish to edit.

   The dialog box expands to show the obligations and license text for the selected
   license.
6. Edit the text directly in the field.
7. Click **Save Changes**.

To revert to the original license text:

1. Open the *Component Name Version* Component License dialog box as described
   above.
2. Click [image: Option icon] located above the license text and select **Revert to Original License
   Text**.

     
    [image: Revert to Original License Text]
