---
title: "Finding Search"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/finding-search.html"
content_id: "3aVzTM~GjFXDae0rvOgjWQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:31.087731+00:00"
content_hash: "88726af37fbcb0700195b02a4d8a42ae983f5576b654315019230f61d7ee9895"
---

# Finding Search

On the *Findings Page*, the *Search* area lets you filter findings based on
metadata fields from their results, specifically, "Evidence" on the *Details Page*.
The fields presented in the *Search* dropdown are the intersection of the set of
fields present in that project and the set of fields present in a "for display"
whitelist. The "for display" whitelist can be augmented via configuration:

- `additional-values.extra-for-display` [default: N/A] - a
  comma-separated list of result metadata fields that you want to appear in the
  *Search* dropdown. Leading and trailing spaces around each entry in the
  list will be trimmed. For example, `Field 1, Field 2 , Field 3`
  will be interpreted as a 3-item list; `Field 1`, `Field
  2`, and `Field 3`.

**Note:** When searching based on a result metadata field, you must enter the full
case-sensitive value of the metadata to get a match. For example, searching by
`Field 1` for `abc` will not match a `Field
1` with a value of `abc123`or `ABC`.
