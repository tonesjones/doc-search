---
title: "'for' loops"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/for-loops.html"
content_id: "AvrsKvBeHEAVNmENuVlsfg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:09.722601+00:00"
---

# 'for' loops

Where possible, put a `for` loop on a single line.
If the loop needs more than one line, indent the subsequent lines by one level.
Put a space before the colon ( `:` ) that ends the condition

Here are examples:

[image: CXM code follows]

```
for n in globalset allFunctionCode where n matches binaryOperator : // ...
```

[image: CXM code follows]

```
for n in globalset allFunctionCode
    where n matches binaryOperator as o
    && o.lhsExpression matches variableReference as v :
        // ...
```
