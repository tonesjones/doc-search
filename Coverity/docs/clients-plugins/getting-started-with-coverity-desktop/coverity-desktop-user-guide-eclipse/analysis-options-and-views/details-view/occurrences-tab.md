---
title: "Occurrences tab"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/occurrences-tab.html"
content_id: "xvfE4~GqdFa3LQ6WleqoKw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:00.901004+00:00"
---

# Occurrences tab

The Occurrences tab shows the stream in which the occurrence of
the issue is located, lists the name of the event(s) that lead to the issue for each
category, and the filename and line number where this event was detected. Click the
event name to go to the event in the source editor.

You can also browse through the next/previous occurrence of the CID (if more than one
occurrence exists) by using the arrow controls labeled Occurrence 1 of
n.

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
| [image: image] | Path event. |
