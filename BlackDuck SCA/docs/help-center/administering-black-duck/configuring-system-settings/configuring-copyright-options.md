---
title: "Configuring copyright options"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-copyright-options.html"
content_id: "177FenvDBBXRscnd3flU3w"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:20.825298+00:00"
---

# Configuring copyright options

You can configure options to improve copyright lists, which are used in SBOM and Notices
File reports.

To configure copyright options:

1. Log in to Black Duck as a System Administrator.
2. Click [image: Admin button] and select **System Settings**.
3. Select **Copyrights** from the lefthand menu.
4. Check the checkbox for any of the following options:

   - **Normalize Copyright Entries from the KnowledgeBase**. Standardize
     the format of copyright entries, applying the transformations described
     below. This option must be enabled to apply any of these
     transformations.

     Warning: By enabling any of these options, you are modifying the fundamental
     characteristics of copyrights obtained from the KnowledgeBase copyright
     inventory, and these may now deviate from how they appeared in the
     identifying source code.

     - **Merge Copyrights**. Enabling this option will merge identical
       copyrights with different date ranges. If a component has multiple
       copyright entries for different years, they will be combined into one
       entry displaying the range of years.

       For example, the following copyrights would be combined into one merged
       copyright:

       ```
       Copyright 2021 Component Corporation
       Copyright 2022 Component Corporation
       Copyright 2023 Component Corporation
       Copyright 2024 Component Corporation
       ```

       The resulting merger displays `Copyright 2021-2024 Component
       Corporation`.
     - **Remove Copyrights Without Dates**. Enabling this option will remove
       any copyrights that do not have a date.

       For example the following copyright would be removed from validated
       copyright lists:

       ```
       Copyright Component Corporation
       ```
     - **Standard Copyright Tag**. Selecting one of options below will modify
       all copyrights to use the desired tag.

       - None, use existing string
       - Copyright ©
       - Copyright (C)
       - Copyright (c)
       - ©
       - (C)
       - (c)
   - **Truncate Long Copyright Entries**. Truncates long copyrights to the
     first 200 characters. This transformation does not require **Normalize
     Copyright Entries from the KnowledgeBase** to be enabled to
     function. However, if that setting is enabled, **Truncate Long
     Copyright Entries** will automatically be enabled and cannot be
     disabled.

## Transformations when normalizing copyright entries

When enabling **Normalize Copyright Entries from the KnowledgeBase**, the
following changes will be applied to copyright entries from the KnowledgeBase. Text
normalization is case insensitive.

- Escaped character markers like \n and \u003c are replaced with real
  characters.
- HTML copyright markers, &#169; and &copy; are replaced with ©.
- Comment markers /*, *, */, //, and # are removed.
- All sequences of white space, like \n, \r, \t and spaces are replaced with a
  single space.
- Copyright entries are truncated to 200 characters.
- All text after "all rights reserved" is removed.
- Copyright entries which do not include the word copyright, start with (C) or
  have (c) or © without a valid date (19dd or 20dd) are rejected.
- Copyright entries with no text (numbers are not text) after the copyright
  marker are rejected.
- Copyright entries shorter than 15 characters with no valid date are
  rejected.
- When copyrights are normalized duplicate entries are removed in reports.

Note: Rejected entries are truncated to 200 characters, but otherwise remain
unedited.
