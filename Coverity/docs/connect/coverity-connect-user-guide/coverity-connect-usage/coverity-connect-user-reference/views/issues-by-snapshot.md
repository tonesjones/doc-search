---
title: "Issues: By Snapshot"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/issues-by-snapshot.html"
content_id: "dvk3cl4_U5Gouz0qNHlJuw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:12.495573+00:00"
---

# Issues: By Snapshot

See also Status values.

Use Issues: By Snapshot views to review issues that need to be
triaged and addressed in current versions of your source code. Use the snapshot scope to
refine the time frame of the issues shown.

- This view type allows you to see CIDs in one (or more) snapshot. It also allows
  you to view all occurrences of an issue. This view type is designed for users
  whose primary tasks fall under the Coverity Connect "developer workflow". By default, the
  views in this view type display the filtered CIDs that occurred in the most
  recent snapshot -- and typically, developers are interested in the state of CIDs
  in the most recent snapshot.

  Note: It is possible to change the scope to show and/or compare a series of
  snapshots, snapshots that occur in different streams, and so forth. For more
  information, see Snapshot comparison.

  Coverity Connect provides the following Issues: By
  Snapshot views:

  - High Impact Outstanding: Classification is set to
    Unclassified, Pending,
    Bug, untested AND the
    High Impact Outstanding: 
    Impact
     filter is set to High.
  - My Outstanding: 
    Status
     filter is set to New and
    Triaged, and the Owner
    is set to your user name.
  - Outstanding Issues: 
    Issue Kind
     filter is set to Quality, and the 
    Status
     filter is set to New and
    Triaged.
  - Outstanding Untriaged: 
    Status
     filter is set to New.
  - Unsaved view: While this view is not a default
    view "out of the box", it is the view that is displayed by default from
    a view type (other than Issues: By Snapshot) from which you derive a
    list of issues. For example, when you select a component from a
    Components view, the Unsaved
    view displays the issues in that component. To create a
    new view from an unsaved view, select the Save as
    Copy option and rename, apply filters, and save the
    copied view.

**You can also view issue information in occurrences mode**. An
*occurrence* is an instance of an issue, and the issue itself represents a set
of occurences of the same defect. Multiple occurrences might happen when there are
multiple findings of an issue in the same file, or when a project that uses multiple
streams/triage stores has an occurrence of a merged defect for each stream despite it
being the same issue. In the latter case, it is possible for any of the triage columns'
cells to contain a variety of values. In this case, the string "Various" will be
displayed in issues mode, but will display the correct line number in occurrences
mode.

There are times when you need to look at a specific occurrence. An occurrence is
associated with a file, a line number, and a triage comment. Note that column values are
exactly the same in both Issues mode and Occurrences mode for both a merged defect and
its occurrences for every column except line number.

To view snaphot issues in **Occurences** mode:

1. Click on the settings (gear) icon.
2. In the **Filters**, **Columns**, or
   **Snapshot Scope** tab of the **Settings** dialog box, click the box **Show
   Occurrences**, and click **OK**.

With the occurences view enabled, the **Issues: By Snapshot**
display will show all occurrences of a defect. As a result the issues grid will display
one row for each occurrence; occurrences belonging to the same merged defect/issue will
have the same CID. Because triage cannot be changed for occurences, the Triage panel
will be read-only in this mode.

- **Line number**, to display the line number of the
  occurrence in the source file.
- **Last triage comment**, to display the last triage comment
  for the issue that aggregates this occurrence.
