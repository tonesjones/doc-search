---
title: "Sorting issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sorting-issues.html"
content_id: "wuDlxnERGt20EpXqh6AY2g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:37.150369+00:00"
---

# Sorting issues

Central analysis results are listed in the Issues view and
can be sorted by any of the default columns. Right-click on a CID, then use
Show Columns and Sort By to
display and sort on the following columns:

Impact
:   Issue impact as determined by Coverity Connect: High, Medium,
    Low, or Audit.

    The Impact value is displayed in the first column, and is represented by a
    colored icon (a blue 'down' arrow for Low impact, a yellow dash for Medium,
    and a red 'up' arrow for High) - illustrated in Issues view.

CID
:   The numeric identifier that groups similar issues that are found in
    several analysis snapshots.

Checker
:   The checker that reported the issue.

Owner
:   The user assigned to resolve the issue. You can change the owner that is
    assigned to the issue in the Details view.

Classification
:   Indicates the state of an issue. The classifications are
    Unclassified, Pending, False Positive, Intentional and Bug. You can change
    the level assignment in the Details view.

Severity
:   Indicates an issue's magnitude of potential risk. The severity levels
    are Unspecified, Major, Moderate, and Minor. You can change the severity
    level in the Details
    view.

Action
:   Indicates how an issue is to be handled. The categories are
    Undecided, Fix Required, Fix Submitted, Modeling Required, and Ignore. You
    can change the action in the Details view.

Fix Target
:   The targeted time frame in which the issue should be fixed.

Ext. Reference
:   An identifier (such as an issue number in a different database) specified by
    your company.

Legacy
:   Displays True if the CID is a Legacy Issue, otherwise
    False.

Component
:   The name of the component in which the issue was discovered.

Function
:   The name of the function that contains the issue. This column is not sortable.

File
:   The file path that contains the issue. If the file is not located, the path
    displays in red text. If red text is displayed, go to the 
    File Path Mapping dialog, and make sure
    that you have the proper definitions for stripping the remote path prefix
    and for adding the proper local path to search (if needed). The displayed
    path is the path known to Coverity Connect, the tooltip will
    display the local file path if the file is found locally.

Occurrences
:   The number of issues that have this CID.

First Detected
:   The date of the analysis in which the issue was first detected.

Last Detected
:   The date of the analysis in which the issue was last detected.

Last Triaged
:   The date of the last analysis in which a change was made to the issue's
    triage data.
