---
title: "numberKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/numberkind.html"
content_id: "4EnBHFVmgvicjpEje00x~w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:16.032484+00:00"
---

# numberKind

The type of a numeric value.

`numberKind` defines the following values:

| Name | Description |
| --- | --- |
| `` `boolean` `` | A Boolean value (`true` or `false`) |
| `` `complex` `` | A complex value. Complex numbers are represented by a pair of machine-level double-precision floating-point values. |
| `` `int` `` | A 32-bit integer value |
| `` `long` `` | An integer value of arbitrary length. The possible length is limited by the available virtual memory. |
| `` `real` `` | A machine-level double-precision floating-point value |

Note:
The discrete types `int` and `long`
are indistinguishable to the Python library.
The same is true of the continuous types `real` and `complex`,
although you *can* search for the imaginary component of a complex value:
see imaginaryLiteral.
