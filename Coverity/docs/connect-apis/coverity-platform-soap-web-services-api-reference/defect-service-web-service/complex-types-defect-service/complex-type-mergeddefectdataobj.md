---
title: "Complex type: mergedDefectDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-mergeddefectdataobj.html"
content_id: "nXwWBg2V8mvTcbR7_qMm3w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:36.384583+00:00"
---

# Complex type: mergedDefectDataObj

## Description

Returns data on a CID.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| checkerName | string | Name of the checker that found the software issue associated with the CID. |
| cid | long | CID to which one or more instances of a software issue are associated. |
| componentName | string | Name of the component to which the issue belongs. |
| cwe | int | Common Weakness Enumeration identifier of the type of the issue. |
| defectStateAttributeValues | defectStateAttributeValueDataObj | List of attribute/value pairs associated with the software issue. |
| displayCategory | string | Name of the issue category. |
| displayImpact | string | Probable impact of the issue. |
| displayIssueKind | string | Issue kind. |
| displayType | string | Name of the issue type. |
| domain | string | Domain of the issue. |
| filePathname | string | Path to the file that contains the source file that contains the software issue. |
| firstDetected | dateTime | Date and time when the issue was first detected. |
| firstDetectedBy | string | Value that helps identify the process by which an issue was *initially reported* to Coverity Connect: **COMMIT**(for issues initially reported through a commit process that yields a snapshot; appears as "**Snapshot**" in the UI), **PREVIEW_REPORT** (for issues initially reported through a preview process, which does not produce a snapshot, for example, when Coverity Desktop invokes cov-run-desktop), or **API** (for issues initially reported through a special, rarely used process). In each case, a CID for the issue is created. |
| firstDetectedDescription | string | First description of the snaphot (containing the CID) submitted to the stream. Submitted by using the optional `--description` option of `cov-commit-defects` command. |
| firstDetectedSnapshotId | long | Identifier of the snapshot in which the CID was first detected. |
| firstDetectedStream | string | Stream in which the CID was first detected. |
| firstDetectedTarget | string | Target platform (for example, i386) of the source code in the snapshot in which the CID was first detected. Submitted by using the optional `--target` option of `cov-commit-defects` command. |
| firstDetectedVersion | string | Typically the version of the source code in the snapshot in which the CID was first detected. Submitted by using the optional `--version` option of `cov-commit-defects` command. |
| functionDisplayName | string | Name of the method or function associated with the CID as it appears in the UI. |
| functionMergeName | string |  |
| functionName | string | Name of the method or function that is associated with the CID. |
| issueKind | string | Internal value for issue kind. |
| lastDetected | dateTime | Date and time when the CID was last detected. |
| lastDetectedDescription | string | Last description of the snapshot (containing the issue) submitted to the stream. Submitted by using the optional `--description` option of `cov-commit-defects` command. |
| lastDetectedSnapshotId | long | Identifier of the snapshot in which the CID was last detected. |
| lastDetectedStream | string | Stream in which the CID was last detected. |
| lastDetectedTarget | string | Target platform (for example, i386) of the source code in the snapshot in which the CID was last detected. Submitted by using the optional `--target` option of `cov-commit-defects` command. |
| lastDetectedVersion | string | Typically the version of the source code in the snapshot in which the CID was last detected. Submitted by using the optional `--version` option of `cov-commit-defects` command. |
| lastFixed | dateTime | Date and time when the CID was fixed (no longer occurred in a snapshot). |
| lastTriaged | dateTime | Date and time when the CID was last triaged. |
| mergeKey | string | Internal key used to associate instances of a software issue into a CID. |
| occurrenceCount | int | Number of instances of the software issue that are associated with the CID. |
