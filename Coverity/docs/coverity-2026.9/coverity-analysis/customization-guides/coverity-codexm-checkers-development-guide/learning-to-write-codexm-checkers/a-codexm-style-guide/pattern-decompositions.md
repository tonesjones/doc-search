---
title: "Pattern decompositions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/pattern-decompositions.html"
content_id: "wSgMEaApMDqE~2kbjFQJLg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:09.965441+00:00"
---

# Pattern decompositions

The indentation of pattern-decomposition code should parallel the level of nesting it is matching in the target code.

Here is an example:

[image: CXM code follows]

```
pattern assignToHexFortyTwo {
    assignmentOperator {
        .targetExpression == variableReference;
        .sourceExpression == intLiteral {
            .value == 42;
            .base == `hexadecimal`
        }
    }
};
```
