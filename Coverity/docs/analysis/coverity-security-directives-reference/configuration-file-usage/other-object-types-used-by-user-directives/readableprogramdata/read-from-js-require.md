---
title: "read_from_js_require"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/read_from_js_require.html"
content_id: "9gbW~1ORWYWQixA_BgaRwA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:35.508177+00:00"
---

# read_from_js_require

**Languages: JavaScript**

A `read_from_js_require ReadableProgramData` value identifies a readable
value along an access path that is relative to a JavaScript module value returned from a
`require` call site. Calling `require` with the name
of a module is a common approach to using modules, such as in Node.js programs.

## Fields

The `read_from_js_require` object has the following fields:

`read_from_js_require`
:   A string value that names the JavaScript module specified in the
    `require` call site.

`path`
:   (Optional) A non-empty array of AccessPathElement values
    for `read_from_js_require` to use.

## Examples

For examples that use this `ReadableProgramData`, see tainted_data
and new_on.
