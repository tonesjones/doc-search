---
title: "Complex types: Defect Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-types-defect-service.html"
content_id: "2nQ0RrbZflxG9WYEgsvGsA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:23.061762+00:00"
---

# Complex types: Defect Service

## Description

Defect Service data objects.

## Complex types

| Name | Description |
| --- | --- |
| attributeDefinitionIdDataObj | Identifier for an attribute. |
| attributeDefinitionValueFilterMapDataObj | Filter for one or more attribute values. |
| attributeValueIdDataObj | Identifier for the attribute. |
| componentIdDataObj | Identifier for the component. |
| componentMetricsDataObj | Metrics for a component. |
| CovRemoteServiceException | Error code and message. |
| defectChangeDataObj | Returns data on the CID. |
| defectDetectionHistoryDataObj | Returns detectiion history for a software issue in a snapshot. |
| defectInstanceDataObj | Returns data on an instance of a software issue. |
| defectInstanceIdDataObj | Identifier for an instance of a software issue. |
| defectStateAttributeValueDataObj | Name/value pair for an attribute value. |
| defectStateDataObj | Returns historical triage data on a software issue. |
| defectStateSpecDataObj | Updated attribute values. |
| eventDataObj | Returns data about one or more events that contributed to a software issue. An event is a message associated with a particular line of code that explains some part of a software issue. |
| fieldChangeDataObj | Returns the old and new value of an attribute. |
| fileContentsDataObj | Returns the contents of a source code file. |
| fileIdDataObj | Contents of and path to a source code file. |
| functionInfoDataObj | Returns data on a function or method. |
| localizedValueDataObj | Object containaing a display name and ID for various issue attributes. |
| mergedDefectDataObj | Returns data on a CID. |
| mergedDefectFilterSpecDataObj | Filter on the CIDs to return. |
| mergedDefectIdDataObj | Specification that identifies a software issue. |
| mergedDefectsPageDataObj | Returns data on the requested CIDs. |
| pageSpecDataObj | Specification for the page of records to return. |
| projectIdDataObj | Identifier for a project. |
| projectMetricsDataObj | Triage and source code data on CIDs in a project. |
| projectScopeDefectFilterSpecDataObj | Passes optional filter properties matching the issues to return. |
| projectTrendRecordFilterSpecDataObj | Filter for project trend records to return. |
| propertyDataObj | A key/value pair for a property of an instance of a software issue. |
| propertySpecDataObj | A key/value pair for a property of an instance of a software issue. |
| snapshotScopeDefectFilterSpecDataObj | Filter on the snapshots to return. |
| snapshotScopeSpecDataObj | Specification used for snapshot comparison. |
| standardAttributeIdDataObj | Identifier for a standard attribute. |
| standardAttributeValueFilterMapDataObj | Filter for one or more standard attribute values. |
| standardAttributeValueIdDataObj | Identifier for a standard attribute value. |
| streamDefectDataObj | Returns data on a CID within the context of a stream. |
| streamDefectFilterSpecDataObj | Filter used to return matching software issues within the scope of one or more streams. |
| streamDefectIdDataObj | Identifier for a software issue within the scope of a stream. |
| streamIdDataObj | Identifier for the stream. |
| triageHistoryDataObj | Data object that capture state of triage attributes for a CID at a given point in time. For example, if a developer desginates a new CID as a bug, the triage state changes. |
| triageStoreIdDataObj | Identifier for the triage store. |
