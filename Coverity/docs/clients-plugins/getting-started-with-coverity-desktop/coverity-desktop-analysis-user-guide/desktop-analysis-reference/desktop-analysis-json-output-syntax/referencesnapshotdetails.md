---
title: "ReferenceSnapshotDetails"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencesnapshotdetails.html"
content_id: "~JnWI~MMlvDne0krISIdKA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:10.395895+00:00"
---

# ReferenceSnapshotDetails

This object contains information about the reference snapshot stored on the Coverity
Connect server.

snapshotId: int
:   The numeric snapshot ID.

codeVersionDateTime: string
:   The SCM date/time associated with the version of the code that was analyzed.

description: string
:   The snapshot `description` attribute.

version: string
:   The snapshot `version` attribute.

analysisVersion: string
:   The snapshot's `analysisVersion`. Added in version 3.

analysisVersionOverride: string
:   The `analysisVersionOverride` associated with the reference stream. Added in
    version 3.

target: string
:   The user-provided `target` attribute.
