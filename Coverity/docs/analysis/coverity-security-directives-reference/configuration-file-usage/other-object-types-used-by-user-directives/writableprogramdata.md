---
title: "WritableProgramData"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/writableprogramdata.html"
content_id: "9mwNhotGDqxRCQx5OW18WA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:42.377993+00:00"
---

# WritableProgramData

**Used by these directives:**
`async_method`, `local_callback`,
`sanitizer_for_checker`, `sink_for_checker`

A `WritableProgramData` value identifies the location of a writable value:
either for the purpose of noticing writes to that location, or to indicate that
something is written to that location. You can specify a
`ReadableProgramData` object by using one of the following field
names:

- to_callsite
- write_to_object_with_tag
- write_path_off_global
- write_off_any
