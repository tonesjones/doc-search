---
title: "CID"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cid.html"
content_id: "oWpF34Wy~Trf556LICSAXg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:12.686863+00:00"
---

# CID

Unique identifier (Coverity ID) for one or more instances (occurrences) of a
given software issue. The API often uses *MergedDefect* to refer to a
CID.

Issue instances, both within a snapshot and across snapshots (even in different streams), are grouped together
according to similarity, with the intent that two issues are "similar" if
the same source code change would fix them both. Such instances share the
same CID. Coverity Connect associates triage data, such as classification,
action, and severity, with the CID (rather than with an individual issue).
