---
title: "variableDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variabledeclaration.html"
content_id: "dPTeKI9dYq9W~BfOPoCWqw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:08.037927+00:00"
---

# variableDeclaration

Matches variable declarations, regardless of their location.

For example, this pattern matches both the simple declarations found at the top of function code,
and the scoped declarations that are found in various flow-of-control statements.

## Properties

`variableDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum variableDeclarationKind` (see below) | Variables can be declared in a variety of locations. This property indicates the scope of the declaration. |
| `variable` | `symbol` | The identifier of the variable being declared |
| `initializer` | `initializer?` | The expression evaluated to determine the initial value; `null` if there is no such expression |

These are the possible values for the `kind` property
(see also variableDeclarationKind):

`` `simple` ``
:   A local variable declaration

`` `global` ``
:   A variable declaration with global scope

`` `for` ``
:   A variable declared within the conditional expression
    of a `for` loop

`` `while` ``
:   A variable declared within the conditional expression
    of a `while` loop

`` `if` ``
:   A variable declared within the conditional expression
    of an `if` statement

`` `switch` ``
:   A variable declared within the conditional expression
    of a `switch` statement

**Inherits properties from:**

- astnode
- declaration

## Declarations in Conditional Expressions

- A variable declared within a conditional expression is always initialized.
- A variable declared within a conditional expression is in scope for the remainder
  of the conditional, and within the body of the flow-of-control statement
  where it was declared.

For example, a variable declared in the conditional expression of an
`if` statement is in scope for the rest of the conditional, and also
within the statement's `then`
and `else` clauses.

## Example

The `variableDeclaration` pattern matches source code such as the following:

  
 [image: C/C++ code follows]   

```
int num;
int count = 1;
```

In the first instance, `.variable` refers to `num`,
and the property `.initializer` is
`null`.

In the second instance, `.variable` refers to `count`,
and `.initializer` is set to an
`expressionInitializer` whose value is
an `intLiteral` equal to `1`.

The following CodeXM pattern matches uninitialized variable declarations:

  
 [image: CXM code follows]   

```
    pattern variableDeclarationUninitialized {
        variableDeclaration {
            .initializer == null
        }
    };
```
