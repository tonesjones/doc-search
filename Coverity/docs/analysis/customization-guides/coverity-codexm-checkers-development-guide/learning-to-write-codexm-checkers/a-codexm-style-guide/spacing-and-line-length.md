---
title: "Spacing and line length"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/spacing-and-line-length.html"
content_id: "omKa2yvc99BmONQ~5NsHnA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:03.324454+00:00"
---

# Spacing and line length

Indent using spaces rather than tabs. (Different editing applications can do strangely different things with tab characters.)

- Use 4 spaces for each indentation level.
- Put a single space between an infix (binary) operator and its operands; for example, `a + b` and not `a+b`.
- Always begin a top-level construct, such as `checker` or `pattern`, on a new line.
- Don't write lines longer than 100 characters.
- Don't leave trailing white space at the end of a line.
- End each CXM file with an empty line.
