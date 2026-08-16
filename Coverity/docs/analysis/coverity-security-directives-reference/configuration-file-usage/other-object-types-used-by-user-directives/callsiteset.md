---
title: "CallsiteSet"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/callsiteset.html"
content_id: "~PICx23AYWiZsVtK75FAVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:10.237957+00:00"
---

# CallsiteSet

**Used by these directives:**
`csrf_check_needed`, `csrf_validator`,
`dataflow_through_call_site`, `map_read`,
`map_write`, `sensitive_action`

**Used by these objects:**
`ReadableProgramData`, `WritableProgramData`

A `CallsiteSet` identifies a set of function call sites in the source
program. There are a few different ways to specify a `CallsiteSet`. The
different kinds of `CallsiteSet` are supported for different programming
languages. The sections that follow describe the kinds of
`CallsiteSet`:

- callsite_with_static_target
- call_on
- new_on
