---
title: "Editing a KnowledgeBase license"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/editing-a-knowledgebase-license.html"
content_id: "WjUdqGg3WL8D1EBRnMpSCQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:00.808676+00:00"
---

# Editing a KnowledgeBase license

KnowledgeBase
licenses can be edited by users with the License Manager role and by users with the BOM
Manager, or Project Manager role:

- License Managers can make *global* edits to KnowledgeBase licenses. The
  License Manager can edit the license family, license text, and other license
  settings. License Managers can also edit the license terms. The
  license name *cannot* be changed.

  These edits are propagated to BOMs with components using the KnowledgeBase
  license.
- BOM Managers and Project Managers can only make *local* edits to the license
  text of a KnowledgeBase license used in a BOM.

  These edits only apply to the version of the KnowledgeBase license used in the
  BOM.

When the License Manager edits a KnowledgeBase license:

- Edits to the license family and license terms are always propagated to the
  KnowledgeBase licenses used in BOMs.
- Edits to the license text *may or may not* be propagated to the KnowledgeBase
  licenses used in BOMs:
  - If the BOM Manager/Project Manager *edited the license text*, the
    edits made by the License Manager *are not* propagated to the
    version of the KnowledgeBase license used in the BOM.
  - If the BOM Manager/Project Manager *did not edit* the license text,
    the edits made by the License Manager *are* propagated to the
    KnowledgeBase license used in the BOM.

Note: KnowledgeBase updates may modify existing KnowledgeBase licenses. However, if a
KnowledgeBase license has been edited by a License Manager or BOM Manager, then
modifications to a KnowledgeBase license due to KnowledgeBase updates are not propagated
globally (if the License Manager has edited this license) or to the edited local version
(if the BOM Manager has modified this license).

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

     
    [image: License Management page]
3. Select the KnowledgeBase license name to display the *License Name*
   **Settings** tab.

     
    [image: image]
4. Modify the information:

   - **Name**: License name. Note that this field is read-only.
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

   In the License Management page, the source for this license changes to
   **Modified KnowledgeBase** with the username of the user who edited this
   license listed in the **User** column and the time the license was modified
   listed in the **Last Updated** column.

KnowledgeBase licenses can be restored to their original values.
