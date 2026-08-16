---
title: "Event"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/event.html"
content_id: "kypkzeORzHMlAmjM3YUf0A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:05.861605+00:00"
---

# Event

This object represents an atomic piece of evidence in a defect report. The events in a
defect occurrence form a tree with the defect itself as the root.

covLStrEventDescription: string
:   The event description, represented in a format used internally by
    `cov-run-desktop`.

eventDescription: string
:   The localized event description. Localization may not be available in disconnected mode, in
    which case English is the default language.

eventNumber: int
:   The ordinal number of the event in its parent `event` object.

eventTreePosition: string
:   A dotted hierarchical number (`1.2.3` for instance) that reflects the
    event's position in the defect event tree. The last number is the same as
    `eventNumber`, the next-to-last number is the same as the
    `eventNumber` for this event's parent, and so on. The
    first number is the `eventNumber` of a top-level event.

eventSet: int
:   A non-negative integer that identifies which set of events this particular event is part
    of. In most cases, all events will be in event set 0, the main defect path.
    Some defects, however, have events in multiple event sets.

eventTag: string
:   The event tag. For a path event, the tag is `path`.

filePathname: string
:   The absolute path name of the file containing the event, as it was known on the build
    machine.

strippedFilePathname: string
:   The `filePathname` after path stripping.

lineNumber: int
:   The 1-based line number where the event occurs in its file.

columnNumber: int
:   The number of the column in which the event is shown. Might be absent.

main: boolean
:   True if this is the main event - the event where the ostensible misbehavior happens. Only
    one top-level event will be main, and no lower-level events can be main.

moreInformationId: string
:   An identifier that can be used to find checker documentation. It is absent if the checker
    does not have known documentation.

remediation: boolean
:   Indicates that this event represents remediation advice.

    This attribute was introduced in
    json-output-v2.

events: [Event]
:   If present, this is a non-empty sequence of child events that explain why this event was
    concluded.
