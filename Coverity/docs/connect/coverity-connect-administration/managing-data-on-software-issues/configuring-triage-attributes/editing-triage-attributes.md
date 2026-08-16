---
title: "Editing triage attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/editing-triage-attributes.html"
content_id: "qFZWGqNuJvjW0sWNLBiXdg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:14.438818+00:00"
---

# Editing triage attributes

You can modify Custom attributes, Built In
(only Action, Severity, and Fix
Target) attributes, and their values.

Note: You cannot change or delete the Classification or
Ext. Reference attributes.

**To edit an attribute:**

1. Select Configuration > Attributes.
2. Select an editable attribute.
3. Click Edit to modify the attribute, as needed:

   **To change the name or description of an attribute:**

   - Type a new name or description for the attribute.

   **To display or hide an attribute from the Coverity
   Connect Triage panel:**

   - Set Display.

     On means that the attribute will appear the panel.
     Off means that it will not appear in the
     panel.

   **To add a new value to an attribute:**

   - Click + to show the Values
     field.

     You can create one or more predefined values or a text box into which
     developers can enter the value.
4. Modify any attribute values, as needed:

   **To change the name or description of an attribute value:**

   - Type a new name or description for the value.

     Note that CIDs associated with an old attribute *value* name will
     still refer to the old name.

   **To delete an attribute value:**

   - Select the value, and click - to remove it.

     Note: You cannot delete an attribute value if an issue is using it.

     Note that you can deprecate an
     attribute value if you do not want to delete it.

   **To deprecate an attribute value:**

   - Click the Deprecated check box that is associated
     with the value.

     This action strikes through the name of the value. Developers cannot
     triage a deprecated issue. You can un-deprecate the value at a later
     date, if necessary.

     Note that you can delete an
     attribute value if you do not need it anymore.

   **To reorder triage attribute values:**

   - Select the value that you want to move, and then click
     Up or Down to change
     the position of the selected attribute value.

     The order that you specify affects the order in which the values appear
     in lists and the order used when sorting on its column in tables
     throughout Coverity Connect.

   **To select a default value for an attribute:**

   - Click the Default check box that is associated
     with the value that you want to set as the default.
5. Click OK to save your changes and exit.
