---
title: "Complex type: streamDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-streamdataobj.html"
content_id: "f_icOd7IF2r6yd5orgqJBw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:02.970809+00:00"
---

# Complex type: streamDataObj

## Description

Stream data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| autoDeleteOnExpiry | boolean | A value of *true* if the stream should be deleted after a period of inactivity; otherwise, *false*. The default inactivity period is 28 days. (Note that the *stream.expiration.inactivity.days* period is configurable through the *cim.properties* file. The stream will not be deleted unless it contains at least one snapshot.) |
| componentMapId | componentMapIdDataObj | Name of the component map with which the stream is associated. Same as the map for the copied stream. |
| description | string | Description of the stream. Same as description of the copied stream. |
| id | streamIdDataObj | Identifier for the stream. Automatically generated when you use copyStream(): *[copied_stream_name] copy [#]* |
| language | string | Programming language of the stream. Same as the language of the copied stream. |
| outdated | boolean | If true, the stream has been designated as *outdated* and is hidden from the Coverity Connect UI. |
| primaryProjectId | projectIdDataObj | Name of the project with which the stream is associated. The copy is automatically associated with the same primary project as the source stream. This field is not returned when copying a stream. |
| triageStoreId | triageStoreIdDataObj | Identifier for the triage store with which the stream is associated. |
| roleAssignments | roleAssignmentDataObj | Set of roles associated with the new stream. The copy is assigned the same roles that are assigned to the source stream. This field is not returned when copying a stream. |
| analysisVersionOverride | string | If necessary, specifies the updated Coverity Analysis version that may retrieve data from this stream. |
| summaryExpirationDays | int | Specifies the number of days analysis summaries remain in this stream before being automatically removed from their relative snapshots. If null, summaries do not expire, except in cases of snapshot deletion or skeletonization. |
| pluginVersionOverride | string | If necessary, specifies the updated Coverity Desktop plug-in version that may retrieve data from this stream. |
| versionMismatchMessage | string | Provides additional instructions to analysis users that are using an incorrect version of Coverity Analysis or the Coverity Desktop plug-in. |
| enableDesktopAnalysis | boolean | If true, this stream is able to accept analysis summaries during commit. |
| ownerAssignmentOption | string |  |
