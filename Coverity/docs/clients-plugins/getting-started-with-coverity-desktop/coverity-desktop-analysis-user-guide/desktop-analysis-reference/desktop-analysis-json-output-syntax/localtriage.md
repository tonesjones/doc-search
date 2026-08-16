---
title: "LocalTriage"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/localtriage.html"
content_id: "moQ2MCQDS3YqqBMKpBQ~ng"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:09.080471+00:00"
---

# LocalTriage

LocalTriage is an optional object that is specified by code annotations, rather than at the
server level. (For more information on code annotations, see Annotations in C/C++ in the Coverity Customization guide.)

classification: string
:   The possible values for "classification" are the same as for the "classification" field in
    Triage.

    When filtering or sorting on
    "classification", the field that is used is the one from the server, if that
    is present. Otherwise, if the local "classification" field is present, this
    is used instead.

comment?: string
:   An optional comment string, obtained from deviation pragmas.
