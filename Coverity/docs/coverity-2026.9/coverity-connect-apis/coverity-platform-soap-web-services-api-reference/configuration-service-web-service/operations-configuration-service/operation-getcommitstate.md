---
title: "Operation: getCommitState"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-getcommitstate.html"
content_id: "halo4rMQa9bAH25M1MocsA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:19.777416+00:00"
---

# Operation: getCommitState

## Name

getCommitState

## Description

Find out whether the database will accept new commits of analysis results.

## Output (Literal)

The output of this operation is the argument getCommitStateResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | commitStateDataObj |

## Remarks

See setAcceptingNewCommits().
