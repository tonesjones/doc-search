---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "tUBUXWVLZY9qNKPuaDlorQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:32.204171+00:00"
---

# Examples

This section provides examples of show and comparison scope expressions as well as
examples of creating views to filter on a desired set of defects. Some of the examples
reference the illustration below.

The following figure represents a Coverity Connect project containing three streams, each
of which are represented by snapshot ID and the date of commit.

Figure 1. Snapshot comparison example
  
 [image: image]

Comparing the last snapshot with its predecessor to determine new issues
:   The following are basic examples of comparing the most recent snapshot with
    the snapshot that occurs just before it. When the scope is applied and the
    list of CIDs are displayed, a CID that is absent in the preceding (compared
    to) snapshot implies that the issue was just introduced.

    - **Relative expressions:**

      ```
      Show: last()
      Compared to: lastBefore(last())
      ```

      This scope will compare the union of snapshots 10015, 20025, 30035 to
      the union of snapshots 10014, 20024, 30034. Those CIDs with a
      Comparison column value of absent will be the newly introduced
      issues.
    - **Snapshot ID:**

      ```
      Show:10015
      Compared to:10014
      ```

      The preceding example compares two snapshots in Stream 1. To specify
      snapshots in multiple streams, use:

      ```
      Show: 10015,20025,30035
      Compared to: 10014,20024,30034
      ```

Comparing snapshots in separate streams
:   Snapshot comparison is not limited to snapshots that are adjacent or
    sequential, nor are the limited to comparison within the same stream. You
    can compare snapshots that exist in different streams.

    - **Snapshot ID:**

      ```
      Show: 10015
      Compared to: 30034
      ```

      The preceding example compares snapshot 10015 from Stream 1 to
      snapshot 30034 from Stream 3. In addition, you can specify a group
      of multiple snapshots or series of snapshots from one stream and
      compare them to a group or series in different snapshot. For example
      (series):

      ```
      Show: 10012..10014
      Compared to: 30033..30035
      ```

Outstanding issues since the last release
:   This example shows a comparison scope intending to show all outstanding
    (unfixed) issues since the last release of a product (assume Stream 1
    represents the product code base). The release is represented by a
    particular date, so in Stream 1, assume that the release date was 01/02/14
    (represented by snapshot 10012).

    - **Relative expressions:**

      ```
      Show: last()
      Compared to: firstAfter(2014-01-01)
      ```

Fixed issues since the last release
:   This example shows a show/comparison intending to display all fixed issues
    since the last release of a product (assume Stream 1 represents the product
    code base). The release is represented by a particular date, so in Stream 1,
    assume that the release date was 01/02/14 (represented by snapshot
    10012).

    - **Relative expressions:**

      ```
      Show: firstAfter(2014-01-01)
      Compared to: last()
      ```

      An issue that is absent indicates that the issue was fixed or
      dismissed in the specified time frame.
