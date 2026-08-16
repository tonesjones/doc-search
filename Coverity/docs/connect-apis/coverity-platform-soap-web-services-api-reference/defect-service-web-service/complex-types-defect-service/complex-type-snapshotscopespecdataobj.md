---
title: "Complex type: snapshotScopeSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-snapshotscopespecdataobj.html"
content_id: "lldLPF5xM1Ny3pApWumZvQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:44.558260+00:00"
---

# Complex type: snapshotScopeSpecDataObj

## Description

Specification used for snapshot comparison.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| compareOutdatedStreams | boolean | If set to *true*, includes outdated streams found in snapshots specified by *compareSelector*. If *false*, the default, only non-outdated streams are included. See the note in *showOutdatedStreams*. |
| compareSelector | string | Snapshot ID or snapshot grammar value that is used to set the scope of snapshots to compare with the *showSelector* snapshot scope. For more information, see "Snapshot comparison" in the Coverity Platform 2026.6.0 User and Administrator Guide. |
| showOutdatedStreams | boolean | If set to *true*, includes outdated streams found in snapshots specified by show*Selector*. If *false*, the default, only non-outdated streams are included. Note that a user with proper RBAC permissions at the stream level can designate a stream as *outdated* to exclude the stream from Coverity Connect processes. |
| showSelector | string | Require Snapshot ID or snapshot grammar value that is used to set the scope of snapshots Default: *last()* which iincludes the latest snapshot of each stream in the project. See the Coverity Platform Administration Guide for details on the snapshot grammar. |
