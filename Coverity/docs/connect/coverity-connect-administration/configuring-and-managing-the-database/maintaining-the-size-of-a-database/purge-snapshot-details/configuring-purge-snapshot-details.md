---
title: "Configuring purge snapshot details"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-purge-snapshot-details.html"
content_id: "Jx12JQ0LD3tRRQZUFPt1xw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:17.364167+00:00"
---

# Configuring purge snapshot details

This section describes purging snapshot details throughout the Coverity Connect adminstration
configuration menu.

Note: Observe the following recommendations:

- For considerations when purging snapshots during or after an upgrade, see Important upgrade notes.
- Back up and restore your database after the purge process completes.

To configure snapshot detail purging, define the following:

Scope:
:   Allows you to designate the purge snapshot details process based on their age
    (in days) AND identifies the number of snapshots within a stream that will
    not be removed. Coverity Connect will not remove snapshot details for the
    most recently committed snapshot, so the value to designate the number of
    snapshots per stream must be one or greater.

    If you chose to enable automatic snapshot details deletion during your
    Coverity Connect installation process, the scope is set for snapshots that
    are older than 120 days and to keep snapshot details for 5 snapshots per
    stream. These settings can be changed at any time.

Schedule:
:   Allows you to choose the days and time of day that the snapshot purge process
    will run. If you chose to enable automatic purging during your Coverity
    Connect installation process, the snapshot purging schedule is set for every
    day at 5:00 AM. The time value is set in 24-hour notation.

- The purge snapshot details feature removes the following snapshot data (and not
  the entire snapshot itself):

  - out-of-date source code
  - source code symbol references (xrefs)
  - function metrics and instances

  Because the Purge Snapshot Details feature does not remove the entire snapshot,
  you can still view some information for a CID that occurred in a "purged"
  snapshot. For example, if you view a CID that is in the FIXED state that
  belonged to a snapshot that has been cleaned, you can still see some of the
  basic information (such as triage states). However, you are not able to see the
  source code in which the issue occurred or any function data.
- The snapshot purging process is global to all streams within a given Coverity
  Connect instance. If you have an enterprise
  cluster deployment, the snapshot purging configuration for a given
  Coverity Connect instance is not shared with other Coverity Connect instances
  within the cluster.
- This feature removes rows from the database table. It purges snapshot details in
  order to reduce the rate at which the database grows.
- In Coverity Policy Manager, if you have changed the configuration and it needs to
  fetch the existing history (and the history includes purged snapshots) of a
  stream, the following information is not available (and thus not displayed in
  Coverity Policy Manager):

  - Code coverage numbers (they will be set to 0)
  - Function count
  - CCM information
