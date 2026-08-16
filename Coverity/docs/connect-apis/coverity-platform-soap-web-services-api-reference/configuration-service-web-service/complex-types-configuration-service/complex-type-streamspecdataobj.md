---
title: "Complex type: streamSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-streamspecdataobj.html"
content_id: "OH5lIXVMgtfAyQyVPDb4Jg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:04.992265+00:00"
---

# Complex type: streamSpecDataObj

## Description

Specification of a stream.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| analysisVersionOverride | string | Specifies the updated Coverity Analysis version that may retrieve data from this stream. |
| autoDeleteOnExpiry | boolean | Set to *true* if the stream should be deleted after a period of inactivity. The default period is 28 days. (Note that the *stream.expiration.inactivity.days* period is configurable through the *cim.properties* file. The stream will not be deleted unless it contains at least one snapshot.) Defaults to *false* with createStream() and createStreamInProject(). |
| componentMapId | componentMapIdDataObj | Name of the component map with which to associate the stream. Defaults to the *Default Component Map* with createStream() and createStreamInProject(). |
| description | string | Description of the stream. |
| enableDesktopAnalysis | boolean | If true, this stream is able to accept analysis summary information during commit. |
| language | string | The programming language of the source code files associated with the new stream. Required with createStream() and createStreamInProject(). |
| name | string | Name of the new stream. Required with createStream() and createStreamInProject(). |
| outdated | boolean | If true, the filter applies to streams that have been designated as *outdated* and are hidden from the Coverity Connect UI. If false, the filter applies to non-outdated streams. |
| ownerAssignmentOption | string |  |
| pluginVersionOverride | string | Specifies the updated Coverity Desktop plug-in version that may retrieve data from this stream. |
| roleAssignments | roleAssignmentDataObj | Role to associate with the new stream. By default, the username of the stream creator is assigned the *streamOwner* role for the new stream. See getAllRoles(), getRole(), and getAllPermissions. If updating role assignments, respecify any that you want to retain. |
| summaryExpirationDays | int | Specifies the number of days analysis summaries remain in this stream before being automatically removed from their relative snapshot. If you do not want summaries to be deleted, set summaryExpirationDays to 0. This will reset the value to null, and analysis summaries will not expire. |
| triageStoreId | triageStoreIdDataObj | Identifier for the triage store to associate with the new stream. Required with createStream()and createStreamInProject(). Maximum of one triage store name specification allowed. |
| versionMismatchMessage | string | Provides additional instructions to analysis users that are using an incorrect version of Coverity Analysis or the Coverity Desktop plug-in. |
