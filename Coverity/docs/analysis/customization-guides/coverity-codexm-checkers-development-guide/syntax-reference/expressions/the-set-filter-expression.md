---
title: "The set-filter-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-set-filter-expression.html"
content_id: "BLv0K8sWL015vvqhdcwFNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:55.368057+00:00"
---

# The set-filter-expression

The `set-filter-expression` filters members of a set or a list.
It returns the members that meet the filtering criterion.

If you pass it a set, the `set-filter-expression` returns a set.
If you pass it a list, it returns a list.

Note:
In releases before Coverity 2019.09, `set-filter-expression` returned a set regardless of whether it was passed
a set or a list. This was a source of confusion.
Legacy code need not change: The update is backward compatible because it has always been possible to treat a list as a set.

## Syntax

  
 [image: Syntax diagram, set-filter-expression]   

```
set-filter-expression ::=
    set-producing-expression '%' pattern-producing-expression
```

The `set-producing-expression` specifies a set or a list that has already been declared.

The `pattern-producing-expression` is simply an expression that produces a pattern.
Typically this will be an identifier that names a pattern you have already created.

## Details

Set filtering is essentially a syntactic shorthand for the longer notation shown here:

[image: CXM code follows]

```
    for x in myThings where x matches something as y :
        // ...
```

Remember:
If you use the same variable name before and after the `matches`
clause—that is, `x matches something as x`—then the
original `x` and the `x` that is the result are two different variables that happen to
have the same name. This is known as *shadowing:* The first value is shadowed by the second one, and the original `x`
value is no longer accessible.

**Mnemonics:**

- In many languages the `%` operator is the modulo (remainder from division) operator.
  With that in mind, you can think of the `set-filter-expression` `%` operator as removing those members
  that do not match the pattern stated, leaving only those that do.
- This expression is also known as the *which are* operator: So you might read the code above,
  or its shorter form using `%`, as
  "`myThings` *which are* `something`".
