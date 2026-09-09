---
title: "Findings View"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/findings-view.html"
content_id: "fd8dSEQRvlU5zDUUjV9q4A"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:05:55.850644+00:00"
content_hash: "9b5c76217e3411bb7822bd0c14e671baf60ece0150c5018785f0f43f80014a85"
---

# Findings View

This view displays the findings from the selected project. There are three sections: the
findings table, the summary area, and a toolbar.

  
 [image: image]   

The table has columns for many of the finding properties such as:

- Severity (shown using severity icons)
- ID
- Tool
- Rule
- CWE
- Codebase Locations
- Status

The table can be sorted by any of these columns except the Tool column. Right-clicking on
a row provides a context menu for performing actions on the selected finding.

The summary area is located above the table. It provides the project name, the total
number of findings, and the number of findings for each severity category.

  
 [image: image]   

The toolbar buttons include (from left to right) the ability to switch Code Dx projects,
show details of a finding, show remote source code residing on the Code Dx server, show
only findings assigned to you, filter by status, change status, synchronize the Eclipse
Package Explorer view with the table contents, and refresh the table.

  
 [image: image]

## Switching Code Dx Projects

The table of findings can easily be changed to show the results of different Code Dx
projects. This is done using the following toolbar button:

  
 [image: image]   

A dialog is displayed after you click the *Select a Project* button. Note that
only the projects accessible to your user credentials (provided during
configuration) will be shown in this dialog.

  
 [image: image]

## Showing Source Code for a Finding

You can view and edit the local source code for a finding by double-clicking on it,
or by right-clicking on the selected finding and choosing *Show Finding* in the
context menu. The editor view will open with the associated source code. If there is
a line number for the finding, the editor will automatically scroll to that
location.

  
 [image: image]

## Showing Finding Details

The details of a finding can be viewed by selecting a row in the table and either
using the toolbar button or the context menu of the row.

  
 [image: image]

## Showing Remote Source

It is sometimes useful to see the current version of a source file on the Code Dx
server. For example, if the code local to eclipse is different from the remote code.
This can be done by selecting a row in the table and either using the toolbar button
or the context menu of the row.

  
 [image: image]   

The file will be downloaded from the Code Dx server and displayed in a read-only
editor.

  
 [image: image]   

The title of the editor will be marked with a `[Code Dx]` label before
the filename so that it can be distinguished from local source.

## Filtering Findings

The table can be filtered to show only the findings that are assigned to you (left
button) and to hide findings that have a status of `Ignored`,
`False Positive`,`Fixed`, `Gone`
and `Mitigated` (right button).

  
 [image: image]

## Changing the Status of Findings

You can change the status of a single finding or a group of findings. First select
the finding(s) then use either the *Change Status* dropdown located on the
toolbar or the *Status* option in the context menu.

  
 [image: image]

## Sync and Refresh

The *Sync* button is situated to the immediate right of the *Change Status*
dropdown and is used in conjunction with the Package Explorer view and editors. With
the button enabled, just click a file in the Package Explorer and the table will
display only those findings associated with the selected file. Selecting an editor
window of an open file will do the same.

The *Refresh* button is located to the right of the *Sync* button. It is
used to refresh the table with the findings on the Code Dx server.

  
 [image: image]
