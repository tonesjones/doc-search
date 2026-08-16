---
title: "Creating a custom triage attribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-custom-triage-attribute.html"
content_id: "8nUKpM1rtU9dmeBtYXMUXg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:12.516671+00:00"
---

# Creating a custom triage attribute

You can create up to 10 custom attributes and specify their attribute values.

**To create a custom attribute:**

1. Select Configuration > Attributes.
2. Click the Add button that is below the list of built-in
   and custom attributes.

   A screen displays with a name similar to New Attribute Definition
   108.
3. Type a name and description for the attribute.
4. Indicate whether to display this attribute in the Triage panel so that developers
   can use it to triage issues.

   This panel appears in Projects > 
   a project
    > 
   a CID
    > Source tab.
5. For Type, select a value.

   1. Select the value type:

      - Text: Allows developers to type a value of
        their choice when triaging the issue.
      - Pick list: Allows developers to select a
        value from a list of pre-specified values when triaging the
        issue.
   2. If you selected Pick list:

      1. Click +.
      2. Type a name for the value.
      3. Select whether the value is the Default
         value for the pick list, and/or if it is
         Deprecated.
6. Click Create to save your changes and exit.
