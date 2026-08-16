---
title: "IssueOccurrence"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/issueoccurrence.html"
content_id: "O1jkxVJEtOt1LOXR_ZsD~Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:05.203450+00:00"
---

# IssueOccurrence

This object represents a single issue occurrence produced by the analysis. It contains
the following elements for describing the occurrence:

mergeKey: string
:   A 32 character hexadecimal string representing the hash of several issue
    details.

occurrenceCountForMK: int
:   The number of occurrences in the parent CoverityIssues object that have the same
    `mergeKey` value.

occurrenceNumberInMK: int
:   A number between 1 and `occurrenceCountForMK`, unique for
    this merge key.

referenceOccurrenceCountForMK: int
:   The number of occurrences in the reference snapshot for containing
    CoverityIssues objects that have the same mergeKey value. The number of
    occurrences in the reference snapshot may be different than the number of
    occurrences in the local analysis reported in
    occurrenceCountForMK. Added in version 5.

checkerName: string
:   The name of the checker that produced the issue.

subcategory: string
:   The checker-specific subcategory which indicates the kind of issue found in
    this occurrence.

type: string
:   The kind of issue, corresponding roughly to the checker. Added in version
    7.

subtype: string
:   A subdivision of `type`, denoting a sub-type of the issue
    type. Added in version 7.

code-language: string
:   Represents the programming language of the source file. Added in version 7.

extra: string
:   A checker-specific merging discriminator.

domain: string
:   The analysis "domain," as carried in the defect XML.

language: string
:   The name of the programming language containing the main event of the
    occurrence. Added in version 4.

mainEventFilePathname: string
:   The absolute path name of the file containing the main event, reflecting
    its physical location on the machine where the build was performed.

strippedMainEventFilePathname: string
:   The `mainEventFilePathname` after path stripping. Path
    stripping will not change the value of
    `mainEventFilePathname`.

mainEventLineNumber: int
:   The 1-based line number of the occurrence's main event.

mainEventColumnNumber: int
:   The number of the column in which the main event is shown. Might be absent.

properties: [string]
:   A set of key/value pairs for general properties of the issue.

functionDisplayName: string
:   The display name of the function where the main event occurs. The display
    name usually follows the syntax of the programming language to uniquely
    denote the function. This may be absent if the main event is not in a
    function or if the analysis does not know or report the function.

functionMangledName: string
:   A unique string generated to identify the function where the main event
    occurs. This will be absent only when `functionDisplayName`
    is also absent.

functionHtmlDisplayName: string
:   The same name as `functionDisplayName`, but with HTML tags
    included. If absent, this field is replaced by the
    `functionDisplayName` value. If that is not available,
    the field is replaced by a version of `functionMangledName`
    that has been automatically unmangled.

functionSimpleName: string
:   The short function name from the actual source code. If the function is
    anonymous, this field is empty. If absent, this field is replaced by the
    `functionDisplayName` value. If that is not available,
    the field is replaced by a version of `functionMangledName`
    that has been automatically unmangled.

functionSearchName: string
:   The long function name. This might have been spelled out by the programmer.
    If absent, this field is replaced by the
    `functionDisplayName` value. If that is not available,
    the field is replaced by a version of `functionMangledName`
    that has been automatically unmangled.

ordered: boolean
:   When `true`, the sequence of events in
    `events[]` and their children is significant.
    Specifically, the events are in chronological order along a particular code
    path that the analysis believes would misbehave. When false, the event tree
    is not in a meaningful order.

events: [Event]
:   A list of top-level events in this issue report, each of which has several
    attributes described in the Event section. The
    events are ordered chronologically, relative to their specific event set.

stateOnServer: StateOnServer
:   A list of attribute values for the issue as they exist on the Coverity
    Connect server. These values are described in the StateOnServer section. This object is
    `null` in disconnected mode.

checkerProperties: [CheckerProperties]
:   A list of property values for the checker that discovered the issue. These
    values are described in the CheckerProperties section. This information is retrieved from
    Coverity Connect, so may be absent in disconnected mode if not previously
    stored.

localStatus: string?
:   The string localStatus represents the local status with respect to
    reference status. Used when `--include-missing-locally true`
    is provided. The values are currently:

    - "local": the defect is reported by local analysis but is not present in reference
      snapshot.
    - "missing": the defect is found the reference snapshot, but not in local analysis.
    - "present": the defect is both in the reference snapshot and local analysis.

    When `--include-missing-locally` is
    `false` (default), this field is always null. Added in
    version 5.
