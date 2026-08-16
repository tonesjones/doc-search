---
title: "'switch' expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switch-expressions.html"
content_id: "DWP2eJLAjXdWIep45exFDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:03.983614+00:00"
---

# 'switch' expressions

Put the `switch` keyword, the argument,
and the opening brace ( `{` ) on the same line.

- Indent the cases by one level.
- Introduce each case, *including* the first, with the vertical separator `|`.
- Put the `->` arrow on the same line as the case itself, unless the case requires more than one line.
- Put the closing brace ( `}` ) on a line of its own, aligned with the `switch` keyword.

The following sample code illustrates all of these conventions:

[image: CXM code follows]

```
switch (a) {
    | case1 ->
        let b = someFunction(a) in
            {
                field1 = /* ... */;
                field2 = /* ... */;
            }
    | pattern {
        binaryOperator {
            .lhsExpression == variableReference
        }
      } ->
        let b = someFunction(a) in
            {
                field1 = /* ... */;
                field2 = /* ... */;
            }
    | default -> null
}
```
