---
title: "Complex type: mergedDefectFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-mergeddefectfilterspecdataobj.html"
content_id: "N_YrS0qeAQmQi0_sqNcpgA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:37.125830+00:00"
---

# Complex type: mergedDefectFilterSpecDataObj

## Description

Filter on the CIDs to return.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| cidList | long | A CID. Multiple CIDs allowed. |
| filenamePatternList | string | Filename pattern for source code files that containing software issues associated with the CIDs. Up to 20 patterns allowed. |
| componentIdList | componentIdDataObj | Name of a component that contains the CID. Multiple components allowed. |
| statusNameList | string | Status of the CID. Multiple statuses allowed. By default, CID information is returned for the status types New, Triaged, and Dismissed. |
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
| attributeDefinitionValueFilterMap | attributeDefinitionValueFilterMap​DataObj | Specification of an attribute value. |
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
| streamExcludeNameList | streamIdDataObj | Identifier for a stream to exclude. Multiple streams are allowed. |
| streamExcludeQualifier | string | Specifies whether the filter works for 'ANY' or 'ALL' of the excluded streams. |
| streamIncludeNameList | streamIdDataObj | Identifier for a stream to include. Multiple streams are allowed. |
| streamIncludeQualifier | string | Specifies whether the filter works for 'ANY' or 'ALL' of the included streams. |
