---
title: "The exists-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-exists-expression.html"
content_id: "qzRFcbAVWXFT5U7~WZWgcQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:30.300098+00:00"
---

# The exists-expression

The `exists-expression` answers the question,
"Is there at least one value in a set that meets a specified condition?"
Its result, therefore, is simply either `true` or `false`.

## Syntax

The expression is introduced by the keyword `exists`,
followed by an identifier that is used to traverse the set.

The keyword `in` introduces the set itself.
(You can also specify a list to search.)
It is followed optionally by the keyword `globalset`
(which is necessary if the set in question is a globalset type)
and then by an expression that evaluates to the set.

The keyword `where` introduces
a `condition-expression`, presumably expressed in terms of the identifier, that describes
the object of the search.

  
 [image: Syntax diagram, exists-expression]   

```
exists-expression ::=
    'exists' identifier
    'in' ( 'globalset' )? set-producing-expression
    'where' conditional-expression
```

## Details

The `exists-expression` shown in the following code:

[image: CXM code follows]

```
    exists x in someSet where cond // ...
```

... can be considered shorthand for the following lengthier (and less readable) CodeXM pattern:

[image: CXM code follows]

```
    ! (for x in someSet where cond: x).empty
```

If the keyword `globalset` is present,
the `condition-expression` cannot reference local variables that were defined outside of the loop.
See The globalset-type for more information.
