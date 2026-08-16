---
title: "Editing a custom license"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/editing-a-custom-license.html"
content_id: "ExrLziOgHJdL5HcBZd8rDQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:43.823989+00:00"
---

# Editing a custom license

Custom licenses can be edited by users with the License Manager role and by users with
the BOM Manager, or Project Manager role:

- License Managers can make *global* edits to custom licenses. The License
  Manager can edit any of the custom license settings.

  These edits are propagated to BOMs with components using the custom license as
  described below.
- BOM Managers and Project Managers can only make *local* edits to the license
  text of a custom license used in a BOM.

  These edits only apply to the version of the custom license used in the BOM.

When the License Manager edits a custom license:

- Edits to the license family and license name are always propagated to the custom
  licenses used in BOMs.
- Edits to the license text *may or may not* be propagated to the custom licenses
  used in BOMs:
  - If the BOM Manager or Project Manager *edited the license text*, the
    edits made by the License Manager *are not* propagated to the
    version of the custom license used in the BOM.
  - If the BOM Manager or Project Manager *did not edit* the license
    text, the edits made by the License Manager *are* propagated to the
    custom license used in the BOM.

To edit a custom license:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

     
    [image: License Management page]
3. Select the license name to display the *License Name*
   **Settings** tab.

     
    [image: image]
4. Modify the information shown for this custom license.

   - **Name**: License name. You can modify a custom license name.
   - **License Family**: Use the drop-down selector to choose the license
     family.
   - **Status**: Use the drop-down selector to choose the license
     status.
   - **Notes**: You can type any text in this field. Use this for
     additional information or helpful notes.
   - **Expiration Date**: Use the calendar tool to set the expiration
     date.
   - **License Text**: The actual license as found in the component.
5. Click **Save**.
   - The username of the user who edited this license appears in the
     **User** column and the time the license was modified appears in
     the **Last Updated** column in the License Management page.
   - Edit information also appears in the *Component/Subproject Name
     Version* Component License dialog box.

       
      [image: image]
