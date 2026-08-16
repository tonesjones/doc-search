---
title: "PICC compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/picc-compiler.html"
content_id: "uSROmFtIowUxlQCtTpLuZA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:46.250399+00:00"
---

# PICC compiler

The compiler executable name is `pic1` and the ID is `picc`.
Note the following:

- Coverity cannot compile PICC programs in which "@" occurs in either comments or quoted
  strings.
- PICC allows an extension of binary literals specified by a leading 0b, for example
  0b00011111. This is supported by passing the
  `--allow_0b_binary_literals` flag to `cov-emit`
  whenever `cov-configure` is given `--comptype picc`
  or `--compiler picl`.
