---
title: "Simple type: deleteSnapshotJobStatus"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/simple-type-deletesnapshotjobstatus.html"
content_id: "22NqBNJ5aIptd7GonFJeHA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:12.221614+00:00"
---

# Simple type: deleteSnapshotJobStatus

## Description

Returns the status of a preceeding deleteSnaphot() request.

## Derived by

Restricting string

## Enumeration

| Value | Description |
| --- | --- |
| QUEUED | Queued for deletion. |
| RUNNING | Deletion in progress. |
| SUCCEEDED | Deleted successfully. |
| FAILED | Deletion failed. |

## Remarks

See getDeleteSnapshotJobInfo().
