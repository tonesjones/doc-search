---
title: "Snapshot scope"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/snapshot-scope.html"
content_id: "a2aeIBiPZY9hXDur52bDeA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:24.233698+00:00"
---

# Snapshot scope

You use the snapshot scope to specify one or more snapshots that you can then use to
create a view of the issues you want to display:

Show
:   The scope designated in this field determines the snapshots whose issues will
    be listed after filters are applied.

    The scope field(s) can be referenced by a combination of snapshot IDs and a
    relative statements constructed with a specialized snapshot selection
    grammar.

    This field is only editable in views of the 
    Issues: By Snapshot
     and 
    Snapshots
     view types.

Compared to
:   This optional field defines the scope of snapshots that will be compared to
    in the Show scope. It determines the value of the
    Comparison column; whether an issue is present or
    absent from the comparison scope. For more information, see Snapshot comparison.

    This field is only editable in 
    Issues: By Snapshot
    .

    The scope field(s) can be referenced by a combination of snapshot IDs and a
    relative statements constructed with a specialized snapshot selection
    grammar.

Show Matches
:   Displays the snapshots that match the snapshot selection grammar expression
    that you entered (if any) per field. If the statement is not formatted
    correctly, Coverity Connect will alert you.

Include outdated streams
:   Allows Coverity Connect to process the data contained in streams that have
    been designated as "outdated".

    A user with proper RBAC permissions at the stream level can designate a
    stream to be "outdated" to exclude the stream from Coverity Connect
    processes. This designation is performed in the Project and Streams
    configuration window. For more information, see Setting up streams.
