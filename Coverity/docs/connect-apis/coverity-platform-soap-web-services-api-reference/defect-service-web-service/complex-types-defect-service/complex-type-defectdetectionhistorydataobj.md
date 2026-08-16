---
title: "Complex type: defectDetectionHistoryDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-defectdetectionhistorydataobj.html"
content_id: "MUw_Mz9pQ6kBEEVfyph80w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:28.309601+00:00"
---

# Complex type: defectDetectionHistoryDataObj

## Description

Returns detectiion history for a software issue in a snapshot.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| defectDetection | string | Detection status of the CI FIRST_DETECTED or LAST_DETECTED. Note that this field might be omitted if neither value applies, for example, in the case that a software issue appears and disppears from the analysis results several times. |
| detection | dateTime | Date and time that the issue was detected. |
| inCurrentSnapshot | boolean | True if the issue is in the current snapshot, false if not. |
| snapshotId | long | Identifier for the snapshot. Note that this field does not appear if inCurrentSnapshot is *true*. |
| streams | streamIdDataObj | Name of a stream. |
| userName | string | The username of the person who committed the analysis results to Coverity Connect. |
