---
title: "Example: Expressions used as if-statement conditions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-expressions-used-as-if-statement-conditions.html"
content_id: "HrIkTf43TGtR3cOO6RgO_A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:22.969388+00:00"
---

# Example: Expressions used as if-statement conditions

The condition of an `if` statement is an expression.
How complex the expression is, can have an effect on which CodeXM patterns will match the condition.

In the following snippet of target JavaScript code:

[image: C/C++ code follows]

```
if ( my_boolean ) {
    if ( getPropertyValue(a) == v) {
        // ... Do something.
    }
};
```

... we see a pair of `if` statements.
As described in the previous section, the `ifStatement` pattern detects either instance.

But each statement has a condition: namely, the part enclosed by the parentheses that follow the keyword `if`.
Both conditions in this example are expressions.
The first is simply a variable reference.
The second is more complicated: It is made up of a binary operator (specifically, the equality operator) with operands
(which are themselves expressions) appearing on either side.
The left-hand operand is a function call, and the right-hand operand is a variable reference.

You could match the first of these conditions by using the expression pattern `variableReference`
(which also matches the right-hand side of the second condition),
and you could match the second of these conditions by using the expression pattern `binaryOperator`.

To inspect a complete condition expression, look at the `.conditionExpression` property
of the ifStatement pattern.
