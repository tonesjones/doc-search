---
title: "Occurrences tab"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/occurrences-tab.html"
content_id: "6e9p~J7Eju25FQf7djoOgg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:43.076592+00:00"
---

# Occurrences tab

The Occurrences tab shows the stream in which the occurrence of
the issue is located, lists the name of the event(s) that lead to the issue for each
category, and the filename and line number where this event was detected. Click the
event name to go to the event in the source editor.

Coverity Desktop provides tags that highlight the line where the event
appears in the code. Tags that are associated with red markers indicate events and
messages that are directly related to the issue. Tags that are associated with green
markers indicate conditional branches and the programmatic decisions necessary for this
issue to occur. When you double click a marker, the source editor focuses on the section
of code in which the event occurs. Coverity Desktop provides the
following markers:

Table 1. Issue markers

| Marker | Description |
| --- | --- |
| [image: image] | Issue main event. |
| [image: image] | Issue event. |
| [image: image] | Multiple issue events that occur on the same line. |
| [image: image] | Path event (True branch). |
| [image: image] | Path event (False branch). |

Coverity Analysis can produce issue events that are grouped in multiple sets
(sometimes referred to as multi-event issues). For multi-event issues, events
are visually separated into different sets and are displayed in an
expandable/collapsible tree. Each event set is distinguished by a checker
property.
