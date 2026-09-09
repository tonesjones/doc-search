---
title: "Managing Tags"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/managing-tags.html"
content_id: "AxFMPg_tuJ6YQFuH8KM3wQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:10.612129+00:00"
content_hash: "d787e532384612110bad5e14e9035e22e24ea4f6188dabebd57c09e9b5443c86"
---

# Managing Tags

The *Manage Tags* button opens the *Manage Tags* dialog. The *Manage Tags*
dialog enables users to assign tags to findings or unassign tags from findings in bulk.
The dialog is composed of three sections, each of which will be described in sequence.
Note that no operations will be applied until the OK button in the footer of the dialog
is clicked. (Clicking the Cancel will discard all dialog activity.)

[image: image]

## Current Assignments

The *Current Assignments* section presents a sequence of tags that have been assigned to at
least one of the selected findings. Each tag in the sequence is paired with the
number of selected findings to which that tag has been assigned (provided in
parentheses next to the tag).

[image: image]

## Bulk Assign

The *Bulk Assign* section allows users to select tags that should be assigned to all
selected findings. The dropdown select menu (which will appear as soon as you begin
typing the name of a tag) will be populated with tags that are available for
assignment, including tags that have already been assigned to some of the selected
findings. Admins can create tags inline if they attempt to assign a tag that does
not exist.

[image: image]

The number of tags that will be attempted to be assigned once the OK button is
clicked is shown in the footer of the dialog.

[image: image]

## Bulk Unassign

The *Bulk Unassign* section allows users to select tags that should be unassigned from all
selected findings. The dropdown select menu (which will appear as soon as you begin
typing the name of a tag) will be populated with tags that appear in the *Current
Assignments* section of the dialog.

[image: image]

The number of tags that will be attempted to be unassigned once the OK button is
clicked is shown in the footer of the dialog.

[image: image]
