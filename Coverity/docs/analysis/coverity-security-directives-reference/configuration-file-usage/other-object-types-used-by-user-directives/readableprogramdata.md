---
title: "ReadableProgramData"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/readableprogramdata.html"
content_id: "jWRVnrx~pfhuXxvjDuI_MA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:32.292183+00:00"
---

# ReadableProgramData

**Used by these directives:**
`data_has_tag`, `tainted_data`

A `ReadableProgramData` object identifies the location of a readable
value: either for the purpose of noticing *reads* from that location, or to
indicate that something is read from that location. You can specify a
`ReadableProgramData` object by using one of the following field
names:

- from_callsite
- read_from_object_with_tag
- read_path_off_global
- read_off_any
- read_from_js_require
- read_from_HANA_library_import
