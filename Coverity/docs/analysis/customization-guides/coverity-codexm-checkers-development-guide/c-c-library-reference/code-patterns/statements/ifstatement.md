---
title: "ifStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ifstatement.html"
content_id: "RweT3NwBNTOwOHySll9JKg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:01.348013+00:00"
---

# ifStatement

Matches entire `if` statements, including their condition expressions
and their `true` and `false` branches.

In C and C++, the consequences of the condition are each a single statement, but that single statement can be a block statement
(that is, any number of statements enclosed by curly braces). This is reflected in the properties of the pattern.

## Properties

`ifStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition that determines whether the `trueStatement` or the `falseStatement` is executed |
| `trueStatement` | `statement` | The "then" statement, which is only executed if `conditionExpression` evaluates to `true` |
| `falseStatement` | `statement?` | The "else" statement, which is only executed if `conditionExpression` evaluates to `false`. If the `if` has no `else` statement, this property is `null`. |
| `conditionDeclaration` | `declaration?` | If a variable is declared in the `conditionExpression`, this property contains its name; otherwise, this property is `null`. |

**Inherits properties from:**

- astnode
- statement

## Example

The `ifStatement` pattern matches an instance such as this target source:

  
 [image: C/C++ code follows]   

```
if ( x == 1 )
    return 0;
else
    CallMyFunction(x);
```

A match returns these values:

- `.conditionExpression` is `x == 1`.
- `.trueStatement` is
  a `returnStatement` that
  contains `return 0;`.
- `.falseStatement` is
  a `simpleStatement` that contains
  `CallMyFunction(x)`.
- `.conditionDeclaration`
  is `null`.

The following use of the `ifStatement` pattern specifically finds
`if` statements that have an `else` clause:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches ifStatement {
            .falseStatement != null
        }
    };
```
