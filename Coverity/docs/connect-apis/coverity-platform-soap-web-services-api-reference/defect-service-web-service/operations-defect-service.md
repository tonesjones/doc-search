---
title: "Operations: Defect Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operations-defect-service.html"
content_id: "r1PseLj99U1fqdilW9yFFA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:13.514591+00:00"
---

# Operations: Defect Service

## Operations

| Name | Description |
| --- | --- |
| getComponentMetricsForProject | Retrieve metrics on components associated with streams in a specified project. |
| getFileContents | Retrieve the Base64-encoded value of the zlib-compressed contents of a file that contains an instance of a CID. |
| getMergedDefectDetectionHistory | Retrieves detection history for a software issue. The return data is similar to the Detection History information in the Coverity Connect UI. |
| getMergedDefectHistory | Retrieve a date and time stamped list of changes to attributes used to triage a specified CID. |
| getMergedDefectsForProjectScope | Retrieve CIDs (filtered or unfiltered) that are in a specified project. |
| getMergedDefectsForSnapshotScope | Retrieve CIDs (filtered or unfiltered) that are in the current or specified snapshots. Optionally, perform snapshot comparisons. |
| getMergedDefectsForStreams | Retrieve the current attributes and other properties of CIDs (filtered or unfiltered) in a specified stream. |
| getStreamDefects | Retrieve instances of software issues for one or more CIDs. |
| getTrendRecordsForProject | Retrieve daily records on CIDs and source code in a project. |
| getTriageHistory | Retrieve the triage history for a software issue. |
| updateDefectInstanceProperties | Do not use this operation. |
| updateStreamDefects | Update the one or more attribute values for *all* instances of a CID found in a given stream. Note that this update will apply to all instances of the CID in all streams that share the same triage store. |
| updateTriageForCIDsInTriageStore | Update one or more attribute values for a CID in a specified triage store. |
