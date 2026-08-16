---
title: "Multiline logical expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/multiline-logical-expressions.html"
content_id: "Z8uQDRKKZU1wwXueLhU6FQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:02.017305+00:00"
---

# Multiline logical expressions

If a conditional expression is too long to fit on one line, begin a new line with the first subcondition, and indent this line by one level.
If there are further subconditions, put each on its own line.
Begin each new line with the logical operator (such as `&&` or `||`).
Indent each subcondition at the same level as the first.

Here is an example of a multiline logical expression:

[image: CXM code follows]

```
node matches ptn as p where
    p.field1 matches expression
    && p.field2 matches pointerDereference
    && p.field3 matches intType
```
