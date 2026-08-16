---
title: "Data objects: Defect Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/data-objects-defect-service.html"
content_id: "RCtMTTNa_lT69lmenyGPrQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:27.498444+00:00"
---

# Data objects: Defect Service

Change log for data objects in the **Defect Service**. Changes to *fields* are
logged from v6 through the latest version only. Field modifications in earlier versions
are not logged at this time. Note that v7 of the API has changed between Coverity
Connect versions 6.5.1 and 6.6. The v7 values in the table make this distinction by
using *v7 (6.6)* and *v7 (6.5.1)*.

| Data Objects | Introduced | Modified | Removed | Note |
| --- | --- | --- | --- | --- |
| attributeDefinitionDataObj | v4 |  | v5 | REMOVED. |
| attributeDefinitionIdDataObj | v4 |  |  |  |
| attributeDefinitionValueFilterMapDataObj | v4 |  |  |  |
| attributeValueDataObj | v4 |  | v5 | REMOVED. |
| attributeValueIdDataObj | v4 |  |  |  |
| checkerPropertyDataObj | v4 |  | v5 | REMOVED. |
| checkerFilterSpecDataObj | < or = v3 |  | v4 | REMOVED. |
| checkerSubcategoryFilterSpecDataObj | v4 |  | v9 | REMOVED. |
| checkerSubcategoryIdDataObj | v4 |  | v9 | REMOVED. |
| componentIdDataObj | < or = v3 |  |  |  |
| componentMetricsDataObj | < or = v3 | v8 (7.0) |  | v8 (7.0) (removed fields): inspectedCount, resolvedCount |
| defectChangeDataObj | < or = v3 | v6, v7 (6.5.1) |  | v6 (new fields): fixTargetChange v7 (new fields): attributeChanges v7 (removed fields): actionChange, customAttributeChanges, externalReferenceChange, fixTargetChange, ownerChange, severityChange, statusChange |
| defectDetectionHistoryDataObj | v8 (7.0) |  |  |  |
| defectInstanceDataObj | < or = v3 | v9 |  | MODIFIED since introduction: Added checkerSubcategoryIdDataObj. Removed checkerSubcategory. v9 (new fields): category, checkerName, component, cwe, domain, eventSetCaptions, impact, issueKinds, localEffect, longDescription, type |
| defectInstanceIdDataObj | < or = v3 |  |  | v8 (7.5): Do not use this data object. |
| defectStateCustomAttributeValueDataObj | v4 |  | v7 (6.5.1) | REMOVED. |
| defectStateDataObj | < or = v3 |  |  | Modified since introduction. |
| defectStateAttributeValueDataObj | v7 (6.5.1) |  |  | v7 (new fields): attributeDefinitionId, attributeValueId |
| defectStateCustomAttributeValueDataObj | v4 |  | v7 (6.5.1) | v7 (removed fields): attributeDefinitionId, attributeValueId |
| defectStateDataObj | v4 | v6, v7 (6.5.1) |  | v6 (new fields): fixTarget v7 (new fields): defectStateAttributeValues v7 (removed fields): action, classification, comment, externalReference, owner, severity, status, defectStateCustomAttributeValues, fixTarget |
| defectStateSpecDataObj | v4 | v6, v7 (6.5.1) |  | v6 (new fields): fixTarget v7 (new fields): defectStateAttributeValues v7 (removed fields): action, classification, comment, externalReference, owner, severity, status, defectStateCustomAttributeValues, fixTarget |
| eventDataObj | < or = v3 |  |  | Modified since introduction: Added *fileId* (a fileIdDataObj) and *moreInformationId*. Removed *file*. |
| fieldChangeDataObj | < or = v3 |  |  |  |
| fileContentsDataObj | v4 |  |  |  |
| fieldDataObj | v4 |  |  |  |
| functionInfoDataObj | < or = v3 |  |  | Modified since introduction: Removed filePathname. Added fileId (a fileIdDataObj). |
| localizedValueDataObj | v9 |  |  |  |
| mergedDefectDataObj | < or = v3 | v6, v7 (6.5.1), v8 (7.5.1), v9 |  | v6 (new field): ownerName v7 (new field): defectStateAttributeValues v7 (removed fields): action, classification,comment, defectStateCustomAttributeValues, externalReference, fixTarget, owner, ownerName, translatedOwner, severity, status v8 (new field in 7.5.1): firstDetectedBy v9 (new fields):cwe, displayCategory, displayImpact, displayIssueKind, displayType,issueKind v9 (removed field): checkerSubcategory |
| mergedDefectFilterSpecDataObj | < or = v3 | v6, v7(6.5.1), v7 (6.6),v8 (7.0), v9 |  | v6 (new fields): fixTargetNameList v7 (6.5.1) new fields: issueKindList, ownerNamePattern v7 (6.6): legacyNameList v8 (7.0) (removed fields):streamSnapshotFilterSpecIncludeList, streamSnapshotFilterSpecExcludeList, streamSnapshotExcludeAll, streamSnapshotIncludeAll v8 (7.5): Do not use the following fields to this data object: defectPropertyKey, defectPropertyPattern v9 (removed field): checkerSubcategoryFilterSpecList v9 (new fields): checkerCategoryList, checkerList, checkerTypeList, cweList, impactList |
| mergedDefectIdDataObj | v8 (7.0) |  |  | v8 (7.0)**.** Replaces cid parameter to getMergedDefectHistory and cids parameter to getStreamDefects. |
| mergedDefectsPageDataObj | < or = v3 |  |  |  |
| pageSpecDataObj | < or = v3 |  |  |  |
| projectIdDataObj | < or = v3 |  |  |  |
| projectMetricsDataObj | < or = v3 |  |  |  |
| projectScopeDefectFilterSpecDataObj | v8 (7.0) | v8 (7.5.1) |  | v8 (new field in 7.5.1): firstDetectedBy |
| projectTrendRecordFilterSpecDataObj | < or = v3 |  |  |  |
| propertyDataObj | < or = v3 |  |  |  |
| propertySpecDataObj | < or = v3 |  |  | v8 (7.5):Do not use this data object. |
| snapshotIdDataObj | < or = v3 |  | v8 (7.0) | REMOVED from Defect service only. |
| snapshotScopeDefectFilterSpecDataObj |  |  |  |  |
| snapshotScopeSpecDataObj |  |  |  |  |
| standardAttributeIdDataObj | v9 |  |  |  |
| standardAttributeValueFilterMapDataObj | v9 |  |  |  |
| standardAttributeValueIdDataObj | v9 |  |  |  |
| streamDefectDataObj | < or = v3 | v6, v7 (6.5.1), v9 |  | v6 (new fields): fixTarget v7 (new fields): defectStateAttributeValues v7 (removed fields): action, classification,comment, externalReference, owner, severity, status, defectStateCustomAttributeValues, fixTarget v9 (removed field): checkerSubcategoryId v9 (new fields): checkerName, domain |
| streamDefectFilterSpecDataObj | < or = v3 |  |  |  |
| streamDefectIdDataObj | < or = v3 |  |  |  |
| streamFunctionDataObj | v6 |  |  |  |
| streamFunctionPageDataObj | v6 |  |  |  |
| streamIdDataObj | < or = v3 |  |  |  |
| streamSnapshotFilterSpecDataObj | v4 |  | v8 (7.0) | REMOVED. |
| triageStoreIdDataObj | v6 |  |  |  |
