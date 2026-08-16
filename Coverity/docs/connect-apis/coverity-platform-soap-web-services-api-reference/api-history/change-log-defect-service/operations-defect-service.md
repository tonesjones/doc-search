---
title: "Operations: Defect Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operations-defect-service.html"
content_id: "RgIONEfE_Sl62WU2ESD5Ag"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:26.719034+00:00"
---

# Operations: Defect Service

Change log for operations in the **Defect Service**. Changes
to *fields* are logged as noted at this time. Also note that v7 of the API has
changed between Coverity Connect versions 6.5.1 and 6.6. The v7 values in the table
make this distinction by using *v7 (6.6)* and *v7 (6.5.1)*.

| Operations | Introduced | Modified | Removed | Note |
| --- | --- | --- | --- | --- |
| copyStreamDefectStates | v4 |  | v5 | REMOVED. |
| getCheckerSubcategoriesForProject | v4 |  | v9 | REMOVED. |
| getCheckerSubcategoriesForStreams | v4 |  | v9 | REMOVED. |
| getCIDsForProject | < or = v3 |  | v8 (7.0) | REMOVED. |
| getCIDsForStreams | < or = v3 |  | v8 (7.0) | REMOVED. |
| getComponentMetricsForProject | < or = v3 |  |  |  |
| getFileContents | < or = v3 |  |  |  |
| getMergedDefectHistory | < or = v3 | Yes (some version info not available at this time), v8 (7.0) |  | *Changed fields since introduction:* scopePattern removed. streamIdDataObj.name added. *Changed response since introduction:*mergedDefectDataObj v8 (7.0) changes: Passes v8 snapshotScopeSpecDataObj. Now returns getMergedDefectsForStreams, streamExcludeQualifier, streamIncludeNameList, and streamIncludeQualifier. |
| getMergedDefectDetectionHistory | v8 (7.0) |  |  | New in v8 (7.0).Passes v8 mergedDefectIdDataObj. |
| getMergedDefectsForProject | < or = v3 |  | v8 (7.0) | REMOVED. Replaced by getMergedDefectsForProjectScope. |
| getMergedDefectsForProjectScope | v8 (7.0) |  |  | New in v8 (7.0).Replaces getMergedDefectsForProject. |
| getMergedDefectsForSnapshotScope | v8 (7.0) |  |  | New in v8 (7.0).Passes v8 snapshotScopeDefectFilterSpecDataObj and snapshotScopeSpecDataObj. |
| getMergedDefectsForStreams | < or = v3 |  |  |  |
| getStreamDefects | < or = v3 | Yes (version information not available at this time) |  | *Changed fields since introduction:*streamDefectFilterSpecDataObj.streamIdList added scopePattern removed |
| getTrendRecordsForProject | < or = v3 |  |  |  |
| updateDefectInstanceProperties | < or = v3 |  |  | **v8 (7.5):** Do not use this operation. |
| updateStreamDefects | < or = v3 |  |  |  |
| updateTriageForCIDsInTriageStore | v6 | v8 (7.0) |  | v8 (7.0) changes: Passes v8 mergedDefectIdDataObj |
| getTriageHistory | v8 (7.0) |  |  | New in v8 (7.0).Passes v8 mergedDefectIdDataObj. |
