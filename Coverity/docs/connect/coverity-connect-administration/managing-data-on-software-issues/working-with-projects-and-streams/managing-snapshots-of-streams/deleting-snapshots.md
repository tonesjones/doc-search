---
title: "Deleting snapshots"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deleting-snapshots.html"
content_id: "EI_eFtuwV3r6PKUNnDn5GQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:08.971968+00:00"
---

# Deleting snapshots

Coverity Connect allows you to delete snapshots from a specified stream. Deleting a
snapshot reverses the effects of a commit and can be used to undo a commit of mistaken,
erroneous, or experimental analysis results.

When you delete the most recent snapshot in a stream, Coverity Connect removes all the
data that comprises the snapshot (including issue states and file states) from the
stream. For example, if you commit a snapshot and then immediately delete that snapshot,
Coverity Connect will be in a state equivalent to the state it was in before the
snapshot was committed.

When you delete an older snapshot, Coverity Connect updates its history as if the
snapshot had never occurred. For example, assume that you have committed snapshot1,
snapshot2, and snapshot3 (in order). Then you delete snapshot2. Coverity Connect's
history now appears as if you only committed snapshot1 and snapshot3.

Deleting a snapshot affects other aspects of the system. The following important notes
outline things you should consider before you delete a snapshot:

Trends and metrics
:   Trends and metrics are not automatically recalculated after a snapshot is
    deleted. If you delete a snapshot before the nightly metrics and trends data
    is collected, the data for the deleted snapshot will not be recorded as part
    of the trend and metrics data for that stream or issue. If you delete an
    older snapshot (one that has already been factored into trends and metrics
    data), you must manually recompute the data. For more information on
    recomputing trend records, see Managing daily trend records at the project level.

Defect Manager run deletion vs. Coverity Connect snapshot deletion
:   Coverity Defect Manager had the ability to delete runs. This is a very
    different mechanism than the ability in Coverity Connect to delete
    snapshots. If you are accustomed to using Defect Manager and are new to
    Coverity Connect, it is important to note the distinction.

    Deleting a run in Defect Manager deleted some of the information from a run
    but retained all of the triage information. Basically, it archived the run
    that was used to save space in the database while retaining the most
    important state information from a run. It worked on the assumption that a
    run was valid, but that you no longer needed to keep the additional data
    around and wanted to aggregate the information.

    In Coverity Connect, you use snapshot deletion when a snapshot is not valid.
    This feature is used to correct mistakes. A snapshot should be deleted only
    if it was a mistake or otherwise invalid.

    Do not use snapshot deletion to save space, as it will alter the history of
    your issues. See Important upgrade notes for the proper
    procedure.

**To delete a snapshot:**

1. Navigate to Configuration > Projects & Streams, and select a Project.
2. Click the corresponding triangle icon to open the project, and select a stream
   name under the project.
3. In the Snapshots tab, select a snapshot to
   delete.
4. Click Delete.
5. In the confirmation window, click Delete.

Note: Snapshot deletion may not be an instantaneous process. To indicate that a deletion
operation has been queued for a given snapshot, a yellow, rounded square icon will
appear in the snapshot ID column.
