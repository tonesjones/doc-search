---
title: "The if-exists-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-if-exists-expression.html"
content_id: "75oM811_a428qSVy2Z1KMg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:37.419953+00:00"
---

# The if-exists-expression

The `if-exists-expression` finds the first member of a set that satisfies some criterion. It returns a result based on that member.

(The `if-exists-expression` differs from the `exists-expression` in the kind of information it provides.
An `exists` expression reports only `true`
or `false` about the existence of a member.
An `if exists` expression actually returns the value of the member being searched for,
or some computation based upon that value.)

## Syntax

The keywords `if exists` introduce an identifier that is used to traverse the set.

The keyword `in` introduces the set itself.
(You can also specify a list to search.)

The keyword `where` can introduce an optional `condition-expression`.

Finally, a colon ( `:` ) introduces a `yields-expression`.
If the member being sought is present in the set or list, and if it satisfies the condition (if one is specified), then
the `yields-expression` is evaluated and becomes the result of the
`if exists` search.

  
 [image: Syntax diagram, if-exists-expression]   

```
if-exists-expression ::=
    'if' 'exists' identifier
    'in' set-producing-expression
    ( 'where' conditional-expression )?
    ':' yields-expression
```
