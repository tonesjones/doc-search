---
title: "The comparand-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-comparand-expression.html"
content_id: "e5kjloGDKQq22GXp6jccSQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:28.713589+00:00"
---

# The comparand-expression

The `comparand-expression` specifies a literal value or a pattern to either match or not match.

## Syntax

  
 [image: Syntax diagram, comparand-expression]   

```
comparand-expression ::= ( literal-expression | pattern-expression ) ( 'as' identifier )?
```

Each `comparand-expression` should evaluate to one of the following:

- A specific value to compare (as in the example shown in the "Details" section that follows),
  using the same comparison semantics as normal equality or inequality.
- A pattern expression, meaning that the named property must (or must not) match that pattern.
  If the pattern does match, the property is assigned the value of the expression that the matched pattern yields.

The `comparand-expression` can also include a *variable-binding* stipulation.

## Variable binding

If the expression ends with the keyword `as` and then a previously unused variable name,
this creates a new variable of that name, bound to the result of the expression.

For example, consider the following decomposition:

[image: CXM code follows]

```
    x matches testingBind
        { .x == y as b }
```

This would create the variable `b`, whose value would equal the result of `y`.

The `comparand-expression` can include more than one `as`-clause; for example:

[image: CXM code follows]

```
    x matches testingBind
        { .x == y as b } as c
```

... where the new variable's field `c.x` now has the same value as `b`.

## Details

Suppose your checker uses a pattern, `intLiteral`, that matches integer literals in the target code.

The `intLiteral` pattern has a property named `value`.
The `value` property represents the numeric value of the integer literal.

If you use the pattern with no qualifications, as in the following code:

[image: CXM code follows]

```
    x matches intLiteral
```

... then your checker matches *any* integer literal it finds in the code it is inspecting.

By comparison, if you use a property to qualify the pattern, as the following example shows:

[image: CXM code follows]

```
    x matches intLiteral { .value == 42 }
```

... then your checker matches only instances of integer literals whose value equals 42.
