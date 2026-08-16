---
title: "'let' bindings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/let-bindings.html"
content_id: "9hEom7C53Kfew~96oihZiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:01.363649+00:00"
---

# 'let' bindings

If a `let` expression fits on a single line, end the line with the `in` keyword. Indent the lines that follow by one more level.

Here is an example:

[image: CXM code follows]

```
let x = x + y in
    // ...
```

If the `let` expression is too long to fit on one line, then use multiple lines
and align the `in` keyword with the opening `let`.

Here is an example of a multiline `let` expression:

[image: CXM code follows]

```
let b =
    switch(a) {
        | binaryoperator as o -> o.lhsExpression
        | unaryoperator as o  -> o.operandExpression
        | default             -> null
    }
in
    // ...
```
