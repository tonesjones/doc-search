---
title: "Decomposing a pattern to match specific properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/decomposing-a-pattern-to-match-specific-properties.html"
content_id: "rQL5DITxVM9aR6qz25pXGA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:39.681654+00:00"
---

# Decomposing a pattern to match specific properties

In the previous section, we learned how to refine our pattern-match search by using the logical `&&` conjunction.
Now let's see how we can further specify the pattern for properties we're interested in, by using a more compact notation known as *pattern decomposition*.

The previous example looked like this:

[image: CXM code follows]

```
    code matches variableDeclaration as decl && (decl.initializer == null)
```

The following CodeXM construct tests for the same condition:

[image: CXM code follows]

```
    code matches variableDeclaration { .initializer == null }
```

In other words, pattern decomposition means breaking a test pattern into one or more constituent
constraints—such as `.initializer == null`.
The decomposed pattern is enclosed in curly brackets.
You can specify more than one constraint within the decomposition.
Separate one constraint from the next by using a semicolon ( `;` ).
When you specify multiple constraints, *all* the constraints must be true in order for the overall pattern to match.

## Variable binding

A decomposition can contain, or be followed by, an `as` clause that defines a new variable. For example:

[image: CXM code follows]

```
    code matches assignmentOperator {
        .sourceExpression == functionCall as call
    } && call.calledFunction.identifier == "fcnID"
```

This pattern defines the new variable `call`.

The following CodeXM code would match the same source code, but would not create the variable:

[image: CXM code follows]

```
    code matches assignmentOperator {
        .sourceExpression == functionCall {
            .calledFunction.identifier == "fcnID"
        }
    }
```

## List-element decomposition

A decomposition of a list or map object can specify an individual element within the list or map. For example:

[image: CXM code follows]

```
    x matches testingElement
        { .x[5] == y }
```

This pattern would test the 6th element of the (zero-based) list `x`.

## Using nested properties

To illustrate another case of pattern decomposition, let's now write a checker that detects calls to a problematic function, `system()`.

**Use case:**
:   Find calls to `system()`.

    Calls to `system()` are "problematic" because they can lead to security breaches.
    This is a function that should be used carefully and sparingly.

To find calls to `system()` we must match `functionCall` patterns.
For each function call, we must then check its `calledFunction` property, which has a subproperty,
`.identifier`, that contains the declared name of the function being called.

Here's an example:

[image: CXM code follows]

```
    for code in globalset allFunctionCode
        where code matches functionCall {
            .calledFunction.identifier == "system"
    }
```

As the sample code shows, a pattern decomposition can use properties that are nested.
Simply use the `.` operator to name them in sequence—rather like the way
you specify a path to a particular file.

Tip:
Nested properties can be tremendously useful, so be sure to check for them, especially when you use a pattern you haven't used before.
For example, if you look at the description of functionCall in the
"C/C++ Library Reference", you see a table of that pattern's properties.
*Always check the property types.*
In the example we have just shown, the `.calledFunction` property,
which we use, has the type `functionSymbol`.
Now, `functionSymbol` is itself a library pattern: one that has a large number of properties—one of which,
`.identfier`, we take advantage of in our example.

Important:
The type of a property is *not necessarily the same* as the type of its parent object.
For example, if your CodeXM code specifies `expr matches assignmentOperator as a`, then
the type of `a.sourceExpression` is a simple expression.
On the other hand, if your CodeXM code specifies `expr matches assignmentOperator { .sourceExpression == functionCall } as a`,
then the type of `a.sourceExpression` is `functionCall`, and you could for example
examine `a.sourceExpression.calledExpression`.
