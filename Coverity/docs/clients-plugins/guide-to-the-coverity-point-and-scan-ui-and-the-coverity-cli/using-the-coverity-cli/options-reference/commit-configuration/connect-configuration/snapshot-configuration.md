---
title: "Snapshot configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/snapshot-configuration.html"
content_id: "iT0LyfWGfRkmesr4nibePg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:18.545329+00:00"
---

# Snapshot configuration

Each of these options specifies a snapshot to use for the comparison report. *Only one
at a time* must be present in a particular Coverity CLI configuration.

| Key | Type | Description |
| --- | --- | --- |
| `date` | string | The date and time of a snapshot to use for the comparison report. This value should have the form `"YYYY-MM-DDThh:mm:ss"`, where the date and time are separated by a `"T"` character, and the time is optionally followed by a time-zone specification. If a time zone is specified, it should consist of either a `"Z"` to denote UTC, or a `"+"` or `"-"` sign followed by colon-separated hours and minutes east of UTC; for example, `"2023-12-27T13:21:05-08:00"`.  If no time zone is specified, the local time zone is assumed. |
| `id` | integer | The ID of a snapshot to use for the comparison report. |
| `reference` | string | One of `"idir"`, `"latest"`, or `"scm"`. "idir"  Uses the snapshot created closest to, but not after, the creation date of the intermediate directory.  "latest"  Uses the snapshot with the latest code-version date in the specified stream.  "scm"  Queries the SCM to find the version that was most recently checked out or updated, and then uses the snapshot closest to that time. |
