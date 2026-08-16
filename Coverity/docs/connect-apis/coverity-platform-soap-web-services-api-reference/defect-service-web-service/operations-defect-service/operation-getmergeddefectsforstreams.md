---
title: "Operation: getMergedDefectsForStreams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getmergeddefectsforstreams.html"
content_id: "PuedbrUHBnBWJXyTaEaNtg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:18.388651+00:00"
---

# Operation: getMergedDefectsForStreams

## Name

getMergedDefectsForStreams

## Description

Retrieve the current attributes and other properties of CIDs (filtered or unfiltered)
in a specified stream.

## Parameters

streamIds
:   **Type:** 
    streamIdDataObj

    Identifier for a stream.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the stream. You can specify one or more instances of streamIdDataObj. See the example. |

filterSpec
:   **Type:** 
    mergedDefectFilterSpecDataObj

    Optional filter properties used to match CIDs to return from the
    specified stream.

    | Field name | Type | Description |
    | --- | --- | --- |
    | cidList | long | A CID. Multiple CIDs allowed. |
    | filenamePatternList | string | Filename pattern for source code files that containing software issues associated with the CIDs. Up to 20 patterns allowed. |
    | componentIdList | componentIdDataObj | Name of a component that contains the CID. Multiple components allowed. |
    | statusNameList | string | Status of the CID. Multiple statuses allowed. |
    | classificationNameList | string | Classification of the CID; a triage value for the CID. Multiple classifications allowed. |
    | actionNameList | string | Name/value pairs for a list of attributes. |
    | fixTargetNameList | string | Fix target for the CID; a triage value for the CID. Multiple fix targets allowed. |
    | severityNameList | string | Severity of the CID; a triage value for the CID. Multiple severities allowed. |
    | legacyNameList | string | Legacy designation for the CID (*true* or *false*); a triage value for the CID. Built-in attribute. Defaults to *false*. |
    | ownerNameList | string | Owner of the CID. |
    | checkerList | string | List of checkers. |
    | cweList | int | Common Weakness Enumeration identifier of the type of issue. |
    | checkerCategoryList | string | List of checker categories. |
    | checkerTypeList | string | List of checker types. |
    | impactList | string | List of values for issue impact. |
    | issueKindList | string | Kind of issue identified by the CID. |
    | attributeDefinitionValueFilter​Map | attributeDefinitionValueFilter​MapDataObj | Specification of an attribute value. |
    | componentIdExclude | boolean | If one or more component name filters is specified, set to *true* to exclude matching results from the specified components. Defaults to *false*, including the matches from the components in the results. |
    | defectPropertyKey | string | Do not use this field. The API does not process these values. |
    | defectPropertyPattern | string | Do not use this field. The API does not process these values. |
    | externalReferencePattern | string | Glob pattern matching the value of an Ext. Reference attribute value. |
    | firstDetectedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the First Detected date of a CID. **Example1**: 2013-03-18T12:42:19.384-07:00 **Example2**: 2013-03-18 |
    | firstDetectedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the First Detected date of a CID. For an example, see firstDetectedEndDate. |
    | functionNamePattern | string | Glob pattern matching the name of the function (or method) associated with a CID. |
    | lastDetectedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the Last Detected date of a CID. For an example, see firstDetectedEndDate. |
    | lastDetectedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the Last Detected date of a CID. For an example, see firstDetectedEndDate. |
    | lastFixedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the Last Fixed date of a CID. For an example, see firstDetectedEndDate. |
    | lastFixedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the Last Fixed date of a CID. For an example, see firstDetectedEndDate. |
    | lastTriagedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the Last Triaged date of a CID. For an example, see firstDetectedEndDate. |
    | lastTriagedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the Last Triaged date of a CID. For an example, see firstDetectedEndDate. |
    | maxCid | long | Upper numeric bound of CIDs to retrieve. For example, no greater than CID 25000. See minCid. |
    | maxOccurrenceCount | int | Maximum number of instances of software issues associated with a given CID. See minOccurrenceCount. |
    | mergedDefectIdDataObjs | mergedDefectIdDataObj | Identifier for a software issue. Multiple specifications are allowed, up to a limit of 100. |
    | minCid | long | Lower numeric bound of CIDs to retrieve. For example, no smaller than CID 24500. See maxCid. |
    | minOccurrenceCount | int | Minimum number of instances of software issues associated with a given CID. See maxOccurrenceCount. |
    | ownerNamePattern | string | Glob pattern matching the first or last name of the owner of a CID. |
    | snapshotComparisonField | string | Specifies the snapshot used for comparison filtering. |
    | standardAttributeValueFilter​MapList | standardAttributeValueFilterMap​DataObj | Specification of a standard attribute. |
    | streamExcludeNameList | streamIdDataObj | Identifier for a stream to exclude. Multiple streams are allowed. |
    | streamExcludeQualifier | string | Specifies whether the filter works for 'ANY' or 'ALL' of the excluded streams. |
    | streamIncludeNameList | streamIdDataObj | Identifier for a stream to include. Multiple streams are allowed. |
    | streamIncludeQualifier | string | Specifies whether the filter works for 'ANY' or 'ALL' of the included streams. |

pageSpec
:   **Type:** 
    pageSpecDataObj

    Specification for the page of results to return. The pageSize field is
    required.

    | Field name | Type | Description |
    | --- | --- | --- |
    | pageSize | int | Required. Up to 5000 records per page. |
    | sortAscending | boolean | Set to *false* to return records in reverse alphabetical or numerical order. Defaults to *true*. |
    | sortField | string | Name of the field to use for sorting results. Not all fields are supported. However, you can typically sort by a field that returns numeric results, such as cid and the date fields. |
    | startIndex | int | Zero-based index of records to return. Defaults to *0*. |

snapshotScope
:   **Type:** 
    snapshotScopeSpecDataObj

    Optional parameter for adjusting the snapshot scope.

    | Field name | Type | Description |
    | --- | --- | --- |
    | compareOutdatedStreams | boolean | If set to *true*, includes outdated streams found in snapshots specified by *compareSelector*. If *false*, the default, only non-outdated streams are included. See the note in *showOutdatedStreams*. |
    | compareSelector | string | Snapshot ID or snapshot grammar value that is used to set the scope of snapshots to compare with the *showSelector* snapshot scope. For more information, see "Snapshot comparison" in the Coverity Platform 2026.6.0 User and Administrator Guide. |
    | showOutdatedStreams | boolean | If set to *true*, includes outdated streams found in snapshots specified by show*Selector*. If *false*, the default, only non-outdated streams are included. Note that a user with proper RBAC permissions at the stream level can designate a stream as *outdated* to exclude the stream from Coverity Connect processes. |
    | showSelector | string | Require Snapshot ID or snapshot grammar value that is used to set the scope of snapshots Default: *last()*which iincludes the latest snapshot of each stream in the project. See the Coverity Platform Administration Guide for details on the snapshot grammar. |

## Output (literal)

The output of this operation is the argument getMergedDefectsForStreamsResponse
having the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | mergedDefectsPageDataObj |
