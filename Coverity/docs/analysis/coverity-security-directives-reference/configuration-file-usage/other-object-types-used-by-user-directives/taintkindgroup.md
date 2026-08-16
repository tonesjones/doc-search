---
title: "TaintKindGroup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/taintkindgroup.html"
content_id: "rfAwJjv8jnYYA9Q5_RY5Nw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:39.765319+00:00"
---

# TaintKindGroup

**Used by these directives:**
`dataflow_checker_name`

A `TaintKindGroup` value describes a set of taint kinds. It consists of a
JSON array of strings, each of which is either a
`TaintKind` string or one of the following special strings
that denotes a set of related taint kinds:

`all_server_taints`
:   (Java, C#, JavaScript) Includes all taint kinds that are
    relevant to server-side Web applications and other server-side
    applications.

`all_jsclient_taints`
:   (JavaScript only) Includes all taint kinds that are relevant to client-side JavaScript code
    (JavaScript that runs in a Web browser).

`all_android_taints`
:   (Java only) Includes all taint kinds that are relevant to Android applications.
