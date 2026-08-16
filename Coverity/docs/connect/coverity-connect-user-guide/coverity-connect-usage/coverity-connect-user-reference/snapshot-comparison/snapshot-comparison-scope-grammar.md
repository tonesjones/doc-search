---
title: "Snapshot comparison scope grammar"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/snapshot-comparison-scope-grammar.html"
content_id: "3l23B2ZQAM4GRTyuHaZZKA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:30.057321+00:00"
---

# Snapshot comparison scope grammar

Coverity Connect provides a grammar that you can use to define the show/comparison scope.
Basically, you can define the scope by one or more snapshot IDs and/or through relative
expressions. The grammar is as follows:

Table 1. Snapshot selection grammar

| Grammar expression | Description |
| --- | --- |
| Snapshot ID | You can specify scope based the number assigned as the snapshot ID. To locate a snapshot ID, go to the Snapshots view type with the Snapshot ID column enabled.  Snapshot IDs should not be specified in selection expressions in views because results will not be returned in projects that do not contain the specified snapshots. |
| `first()` | Represents the first (earliest) snapshot in a stream or set of streams. |
| `last()` | Represents the latest (most recent) snapshot committed to a stream or set of streams. |
| `firstAfter([snapshot ID |expression | date])` | Represents the snapshot that occurs immediately after the specified expression. |
| `lastBefore([snapshot ID | expression | date])` | Represents the snapshot that occurs immediately before the specified expression. |
| date | Either an absolute or relative date:  - **absolute** - in the form of   `yyyy-mm-dd hh:mm:ss`, however you can   exclude the time (hours, minutes, seconds) if desired. If   you specify the time, it must be in 24-hour format. - **relative** - in the form of `N days ago.` For example,   `lastBefore(5 days ago)`.  For date expression behavior, see Grammar for time filter usage. |
| `..` (dot-dot) | Denotes a range of snapshots. For example:  - `20021..20025` - `first()..lastBefore(last())` - `firstAfter(2014-01-02)..firstAfter(2014-01-05)` |
| `,` (comma) | Denotes a set of snapshots. For example, `20021,20022,20025,30031`. |
