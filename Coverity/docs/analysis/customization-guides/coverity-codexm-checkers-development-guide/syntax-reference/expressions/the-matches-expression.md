---
title: "The matches-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-matches-expression.html"
content_id: "Le5axEsU9_wfHIz7IoL95A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:49.459199+00:00"
---

# The matches-expression

Much of the power of CodeXM relies on pattern matching: comparing code (or other things) to a pattern to find which match that pattern.

The `matches-expression` is a *predicate* in the logical sense; that is, a statement that is true or false,
depending on whether the condition it describes has been satisfied or not.
In the context of CodeXM, the `matches-expression` compares an expression to a pattern.
If the two do match, the `matches-expression` is successful.
It can optionally define an appropriately typed variable that describes the results of that match.

## Syntax

The expression to match is followed by the keyword `matches`, and then by an expression to represent the pattern.

  
 [image: Syntax diagram, matches-expression]   

```
matches-expression ::=
    expression 'matches' pattern-producing-expression
    ( 'as' identifier )?
```

The `pattern-producing-expression` is simply an expression that produces a
pattern.
Typically this will be an identifier that names a pattern you have already created.

You have the option of using the keyword `as` to define a variable whose
value is defined by the initial match and whose scope
is the remainder of the `matches-expression`.

Most often you would define such a variable to further refine the match, as in the following commented code snippet:

[image: CXM code follows]

```
//                                defined
//                                |   and
//                                |        used
//                                |        |
node matches variableReference as v   &&   v.name == something
```

CAUTION:

You cannot use the logical OR ( `||` ) in an expression of this sort, because OR implies that the expression to its right will be
evaluated even when the match has failed.
This is not logical, and indeed if the match fails, the value of the new variable `v` is undefined.

## Type handling in a matches-expression

When a `matches-expression` includes a decomposition to specify a field, and the matches condition evaluates to `true`,
then the type of the field *is not necessarily the same* as the type of its parent object.

The following code is a typical use of `matches`:

[image: CXM code follows]

```
    expr matches assignmentOperator {
        .sourceExpression == functionCall
    } as a
```

After evaluating the preceding example, `a.sourceExpression` has the type `functionCall`, and you could for example
use `a.sourceExpression.calledExpression` in further CodeXM code.

By contrast, when you use `matches` without a decomposition, as in the following example:

[image: CXM code follows]

```
    expr matches assignmentOperator as a
```

... then no type change occurs, and `a.sourceExpression` would be just a simple expression.
