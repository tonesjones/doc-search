---
title: "Assigning Tags to Findings"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/assigning-tags-to-findings.html"
content_id: "kA5r__q46rZsLY4KIGjZ7A"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:01.007881+00:00"
content_hash: "94f3b88c60f1a9d6d717dda4484712e587d2005741e8e96d5243d9d27d1e3b2c"
---

# Assigning Tags to Findings

Tags are part of a project's metadata, which can be configured by users with a "manage"
role. (For more information, see Configuring Project
Metadata.)

Click the Settings icon in the navigation bar and select Tags from the left menu to open
the Tags page.

[image: image]

This page lists all tags (alongside the number of findings to which each tag
has been assigned) that can be assigned to findings.

For more information, see the following topics:

- Viewing existing tags
- Adding a tag
- Renaming a tag
- Deleting a tag

## Viewing Existing Tags

The Tags page shows a list of existing tags and the number of associated
assignments.

**To view a list of existing tags:**

1. Click the Settings icon in the navigation bar and select Tags from the left menu.

   [image: image]
2. Click the column headers to re-sort the list.

## Adding a Tag

**To add a tag:**

1. Click the Settings icon in the navigation bar and select Tags from the left
   menu.

   [image: image]
2. Click Add Tag.

   [image: image]
3. Enter a name for the tag.
4. Click Save.

## Renaming a Tag

Note: If you attempt to rename a tag to a name that already belongs to a tag that has been
assigned to at least one finding, then you will be prompted with a dialog asking you to
confirm the operation. If you confirm the operation, then the tag will be renamed, and
the finding assignments between the involved tags will be merged. Note that the number
of assignments is not necessarily equal to the sum of the finding assignments between
tags once they have been merged, as it is possible for tags to have overlapping finding
assignments. If you do not confirm the operation, then the operation will be
cancelled.

**To rename a tag:**

1. Click the Settings icon in the navigation bar and select Tags from the left
   menu.

   [image: image]
2. Click the dropdown configuration icon to the right of the tag name and select
   Rename.

   [image: image]

   This opens the Rename Tag window.

   [image: image]
3. Enter a new name for the tag.
4. Click Save.

## Deleting a Tag

Note: If you attempt to delete a tag which has been assigned to at least one finding,
then you will be prompted with a dialog asking you to confirm the operation. If you
confirm the operation, then the tag will be deleted and, as a consequence, the tag
will be unassigned from all findings to which the tag had been assigned. If you do
not confirm the operation, the operation will be cancelled.

**To delete a tag:**

1. Click the Settings icon in the navigation bar and select Tags from the left
   menu.

   [image: image]
2. Click the dropdown configuration icon to select Delete.

   [image: image]

   This opens the Delete Tag window.

   [image: image]
3. Click Delete to confirm.
