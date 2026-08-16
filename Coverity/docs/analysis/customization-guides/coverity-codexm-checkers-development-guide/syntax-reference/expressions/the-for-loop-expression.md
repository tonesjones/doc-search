---
title: "The for-loop-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-for-loop-expression.html"
content_id: "cnU3znXrMi~xjTjPdipYWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:33.236999+00:00"
---

# The for-loop-expression

A `for-loop-expression` traverses a set or a list.

Frequently a `for` loop is at the heart of a CodeXM checker, since analyzing code involves traversing
the abstract syntax tree (AST) nodes of the target code, or a calling tree of functions in that code.

## Syntax

The keyword `for` introduces the loop variable.
The loop variable will be assigned, in turn, each of the values in the set being examined.
The set itself is introduced by the keyword `in`, followed by the variable or expression that represents
the set.

If the set to examine is of the type globalset, then the `for-loop-expression`
must include the keyword `globalset`, immediately following the keyword `in`.

To filter the set to only those members that meet a specific criterion, you can use the `where` keyword followed by a
`condition-expression` that describes the criterion.
(If you omit the filter condition, the loop visits every member of the set: It is as if the `condition-expression` were simply the value
`true`.)

Finally, a colon ( `:` ) introduces the `result-expression`.

The variable named by `identifier` is within scope, and can be referred to, in both the
`condition-expression` and the `result-expression`.

  
 [image: Syntax diagram, for-loop-expression]   

```
for-loop-expression ::=
    'for' identifier 'in' ( 'globalset' )? set-producing-expression
        ( 'where' condition-expression )? ':' result-expression
```

The `set-producing-expression` must result in a set or a list.

The `condition-expression` describes a condition (criterion) and the
`result-expression` is evaluated for each member of the set that meets that condition.
