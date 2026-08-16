---
title: "The decomposing-pattern-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-decomposing-pattern-expression.html"
content_id: "2c_R8zqWgB0oJgilSksXGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:27.904265+00:00"
---

# The decomposing-pattern-expression

With the `decomposing-pattern-expression`, your checker can match not only a particular pattern,
but the value of specified properties of that pattern. Decomposition is a way to narrow a search.

## Syntax

Pattern decomposition is expressed by a list enclosed by curly braces
( `{` and `}` ).
Each item in the list consists of a property prefixed by a dot ( `.` ),
an equals ( `==` ) or not-equals ( `!=` ) assertion,
and then an expression that specifies the value of the property to match or to not match.

  
 [image: Syntax diagram, decomposing-pattern-expression]   

```
decomposing-pattern-expression ::=
    expression '{'      ( '.' property-name ( '[' element-expression ']' )* )+
                        ( '==' | '!=' ) comparand-expression
                  ( ';' ( '.' property-name ( '[' element-expression ']' )* )+
                        ( '==' | '!=' ) comparand-expression )*
    '}'
```

Each `property-name` is an identifier
that names a property of the pattern.
Each `comparand-expression` specifies the value or values to match.

Properties can nest, so the `property-name` can be a *path* to a property.
In other words, `.calledFunction.identifier == something` is legal syntax.
Properties with a nullable type along the path are handled correctly.

If the left-hand side of the comparison, the `property-name`, is a list or a map, the expression can specify individual elements.

## List-element decomposition

For example, the following decomposition compares the first element of the list `x` to the value of `y`:

[image: CXM code follows]

```
    x matches testingElement
        { .x[0] == y }
```

There can be more than one `element-expression`. This depends on how many dimensions the array has.

CAUTION:

The following decomposition changes the type of `x`
(see The matches-expression):
[image: CXM code follows]

```
    { .x == y }
```

... but the following decomposition:

[image: CXM code follows]

```
    { .x[0] == y }
```

... (or any other `element-expression` in brackets)
*does not change* the type of `x`.
