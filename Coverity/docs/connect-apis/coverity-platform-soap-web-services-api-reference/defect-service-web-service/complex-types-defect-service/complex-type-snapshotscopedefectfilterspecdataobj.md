---
title: "Complex type: snapshotScopeDefectFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-snapshotscopedefectfilterspecdataobj.html"
content_id: "psJLtPLazB2mgcBMFAdc_w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:43.895413+00:00"
---

# Complex type: snapshotScopeDefectFilterSpecDataObj

## Description

Filter on the snapshots to return.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| actionNameList | string | Name/value pairs for a list of attributes. |
| attributeDefinitionValueFilterMap | attributeDefinitionValueFilterMap​DataObj | Specification of an attribute value. |
| checkerCategoryList | string | List of checker categories. |
| checkerList | string | List of checkers. |
| checkerTypeList | string | List of checker types. |
| cidList | long | List of CIDs. |
| classificationNameList | string | Classification of the CID. Multiple classifications allowed. |
| componentIdExclude | boolean | If one or more component name filters is specified, set to true to exclude matching results from the specified components. Defaults to false, including the matches from the components in the results. |
| componentIdList | componentIdDataObj | Name of a component that contains the CID. Multiple components allowed. |
| cweList | long | Common Weakness Enumeration identifier of the type of issue found by the checker. Zero or more identifiers allowed. |
| externalReference | string | An external reference for a CID that is used by your company to identify the software issue. Corresponds to a field in the Coverity Connect triage pane. |
| fileName | string | A file name. Example: /test.c |
| firstDetectedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the First Detected date of a CID.Example1: 2013-03-18T12:42:19.384-07:00Example2: 2013-03-18 |
| firstDetectedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the First Detected date of a CID. For an example, see firstDetectedEndDate. |
| fixTargetNameList | string | Fix target for the CID; a triage value for the CID. Multiple fix targets allowed. |
| functionMergeName | string | Internal function name used as one of the criteria for merging separate occurrences of the same software issue, with the result that they are identified by the same CID. |
| functionName | string | Name of the function or method. |
| impactNameList | string | Probable impact (High, Medium, or Low) of the issue found by the checker. Zero or more impact levels allowed. |
| issueComparison | string | If set to *PRESENT*, returns overlapping CIDs in a snapshot comparison, that is, CIDs found in snapshot(s) to which both the showSelector and *compareSelector* values of the *snaphotScope* parameter (snapshotScopeSpecDataObj) apply. If set to *ABSENT*, returns CIDs that are present in the snapshot(s) to which the *showSelector* value applies but absent from those to which the compareSelector value applies. If not set, values are *PRESENT* and *ABSENT*. |
| issueKindList | string | Issue kind. Multiple issue kinds allowed. |
| lastDetectedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the Last Detected date of a CID.For an example, see firstDetectedEndDate. |
| lastDetectedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the Last Detected date of a CID.For an example, see firstDetectedEndDate. |
| legacyNameList | string | Legacy designation for the CID (true or false), a triage value for the CID. Built-in attribute. Defaults to false. |
| maxOccurrenceCount | int | Maximum number of instances of software issues associated with a given CID.See minOccurrenceCount. |
| mergeExtra | string | Internal property used as one of the criteria for merging occurrences of an issue. |
| mergeKey | string | Internal signature used to merge separate occurrences of the same software issue and identify them all by the same CID. |
| minOccurrenceCount | int | Minimum number of instances of software issues associated with a given CID.See maxOccurrenceCount. |
| ownerNameList | string | Owner of the CID. |
| ownerNamePattern | string | Glob pattern matching the first or last name of the owner of a CID. |
| severityNameList | string | Severity of the CID; a triage value for the CID. Multiple severities allowed. |
| statusNameList | string | Status of the CID. Multiple statuses allowed. |
| streamExcludeNameList | streamIdDataObj | Identifier for a stream to exclude. Multiple streams are allowed. See streamExcludeQualifier. |
| streamExcludeQualifier | string | If set to *ANY*, the filter will exclude from the results CIDs found in each of the streams listed in the *streamExcludeNameList* field. If set to ALL, the filter will only exclude a CID if it is found in all listed streams. Valid values are *ANY* or *ALL*. Defaults to *ANY*. |
| streamIncludeNameList | streamIdDataObj | Identifier for a stream to include. Multiple streams are allowed. See *streamIncludeQualifier*. |
| streamIncludeQualifier | string | If set to *ANY*, the filter will return CIDs found in each of the streams listed in the *streamIncludeNameList* field. If set to ALL, the filter will only return a CID if it is found in all listed streams. Valid values are *ANY* or *ALL*. Defaults to *ANY*. |
