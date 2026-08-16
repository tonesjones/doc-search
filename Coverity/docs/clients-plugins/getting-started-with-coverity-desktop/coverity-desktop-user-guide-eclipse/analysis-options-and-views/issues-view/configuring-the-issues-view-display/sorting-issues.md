---
title: "Sorting issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sorting-issues.html"
content_id: "yUChEZm0TKQyuLJZuhew3A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:55.306207+00:00"
---

# Sorting issues

Use the Sort by menu to sort the list of issues based on the
following default categories:

Impact
:   Issue impact as determined by Coverity Connect: High, Medium,
    Low, or Audit.

CID
:   A numeric identifier for the essential characteristics of a defect that are
    unlikely to change from snapshot to snapshot. When two occurrences have the
    same CID, it is likely that both would be fixed by the same source code
    change. Triage is associated with the CID rather than any particular
    occurrence.

MergeKey
:   Internal signature used to merge separate occurrences of the same software
    issue and identify them all by the same CID.

Checker
:   The checker that reported the issue.

Owner
:   The user assigned to resolve the issue. You can change the owner that is
    assigned to the issue in the Details view.

Classification
:   Indicates the state of an issue. The available classifications are
    Unclassified, Pending, False Positive, Intentional and Bug. You can change
    the level assignment in the Details view.

Severity
:   Indicates an issue's magnitude of potential risk. The default severity levels
    are Unspecified, Major, Moderate, and Minor. You can change the severity
    level in the Details
    view.

Action
:   Indicates how an issue is to be handled. The default categories are
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
:   The name of the function that contains the issue.

File
:   The file path that contains the issue. If the file is not located, the path
    displays in red text. If red text is displayed, go to the 
    File Path Mapping dialog, and make sure
    that you have the proper definitions for stripping the remote path prefix
    and for adding the proper local path to search (if needed). The displayed
    path is the path known to Coverity Connect, the tooltip will
    display the local file path if the file is found locally.

Occurrences
:   The number of defect occurrences that all have the same CID.

First Detected
:   The date of the analysis in which the issue was first detected.

Last Detected
:   The date of the analysis in which the issue was last detected.

    Sortable in Remote Issues mode only.

Last Triaged
:   The date of the last analysis in which a change was made to the issue's
    triage data.

    Sortable in Remote Issues mode only.

Category
:   Short description of the nature of the software issue.

Type
:   Issue type. For example, *Resource leak, Out-of-bounds write*.

Present in Reference
:   Indicates whether a CID is present in your reference stream.

    Sortable in Local Issues mode only.

Language
:   Programming language associated with the issue.

Custom attribute (text)
:   Appears if a custom attribute that accepts a text field exists in Coverity Connect. Sorting is done alphabetically.

Custom attribute (picklist)
:   Appears if a custom attribute with an ordered set of pick-list values exists
    in Coverity Connect. Sorting is according to the index of the
    pick-list element. That is, it is only ordered alphabetically if the list is
    ordered alphabetically in the Coverity Connect
    configuration.
