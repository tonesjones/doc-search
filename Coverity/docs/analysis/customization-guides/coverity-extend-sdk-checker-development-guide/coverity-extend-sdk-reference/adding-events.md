---
title: "Adding events"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-events.html"
content_id: "XGRwxerPSaX~vLLDXWdAqw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:42.994508+00:00"
---

# Adding events

A defect report (error) from a checker consists of a nonempty sequence of events. An
event is a pair consisting of two strings: a tag, and a description. A typical checker
creates an event each time it updates its store, and a final event when it outputs an
defect report. Event tags are short, single-word strings. Typically, a checker has one
tag for each major kind of event that it creates.

You can suppress defect reports by adding source code annotations as described in Customizing Coverity. The event tag named is in the annotation.

Event descriptions are arbitrary strings that describe what is happening and what the
defect is to the user.

The main way to create a defect report is to use `ADD_EVENT` and `COMMIT_ERROR`. However, using
`OUTPUT_ERROR(desc)` outputs a single-event defect report
immediately, bypassing the store entirely. Input file macros are also used for producing
events and errors (see Reporting events and defects on input files).

Outputting a defect does not necessarily mean it will ultimately be put into the final
list of defects, due to two pass checking, which is explained in Two-pass checking.
