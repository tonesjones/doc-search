---
title: "Complex type: eventDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-eventdataobj.html"
content_id: "VNh06Xk6UpFHp9d7r1qG1w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:32.331560+00:00"
---

# Complex type: eventDataObj

## Description

Returns data about one or more events that contributed to a software issue. An event
is a message associated with a particular line of code that explains some part of a
software issue.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| events | eventDataObj | Container for event data. Multiple events for a single CID are possible. |
| eventDescription | string | Description of the event. |
| eventKind | string | The event kind. |
| eventNumber | int | Internal 1-based sequence number for ordering path events. Path events show the flow of control through a method or function along a path where the sofware issue occurs. |
| eventSet | int | Internal integer that is non-zero for multi-event displays of software issues. |
| eventTag | string | Short identifier for an occurrence (instance) of a software issue. Used in the UI. |
| fileId | fileIdDataObj | Identifier for the file that contains the software issue. |
| id | long | Identifier for the software issue. |
| lineNumber | int | Line number on which the software issue occurs in the source file. |
| main | boolean | Value of *true* for the main event of a software issue. In the unlikely event that no event is designated as the main one, use the last event in the sequence as the main event. |
| moreInformationId | string | Internal. ID to documentation that provides background on a potential security vulnerability or other software issue. The link to this information appears in the UI. |
| pathCondition | string | Internal. Text of a condition tested in the code. Relates to the flow of control through a function along a path where a software issue occurs. |
| polarity | boolean | Internal. |
