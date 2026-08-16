---
title: "Examining the class hierarchy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examining-the-class-hierarchy.html"
content_id: "ogvVjdhHvkjgs9d_Qo_CiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:50.622238+00:00"
---

# Examining the class hierarchy

You can use the Coverity Extend SDK to examine the class hierarchy of C++, C#,
or java programs. This capability consists of an in-memory representation of the
hierarchy and an API to query that representation.

The representation and API are declared in
<install_dir>/sdk/headers/types/extend-types.hpp. The
comments in that header file are the definitive documentation for individual methods.
This section describes how to use the API at a high level, and Types explains it at an intermediate level of
detail.
