---
title: "The let-binding-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-let-binding-expression.html"
content_id: "l~VAv1gaM~qfCGDkP2M_AA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:41.192571+00:00"
---

# The let-binding-expression

With a `let-binding-expression`, you can define a variable that becomes available for use in subsequent expressions.

The `let-binding-expression` is similar to `const-definition`.
Each of these elements defines a variable whose value is constant for the duration of its scope.
The difference is that `const-definition` defines a variable with global scope, which is evaluated (at most) only once
during the life of the checker.
The `let-binding-expression` defines a variable with local scope, whose use is limited to the expression specified
by the `let-binding-expression`, and which is evaluated each time the `let-binding-expression` is evaluated.

## Syntax

The `let` keyword introduces identifier for the local variable, followed by an optional type,
then an equals sign ( `=` ) followed by the expression to evaluate and assign to the variable.
Finally, the `in` keyword introduces the expression during which the identifier will be usable.

  
 [image: Syntax diagram, let-binding-expression]   

```
let-binding-expression ::=
    'let' identifier ( ':' type )?
        '=' value-expression 'in' scope-expression
```

The `value-expression` can be any expression. Its result is assigned to the identifier.

The `scope-expression` can be any expression, and defines the scope within which identifier is available ("in scope").
