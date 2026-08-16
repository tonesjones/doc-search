---
title: "assignmentOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperator.html"
content_id: "EFFdWC6fjZxxm6gDe1VYvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:40.287978+00:00"
---

# assignmentOperator

Matches all forms of the assignment operator in expressions, or the cases where a variable takes on a new value.

This pattern *does not* match variable declarations, which are distinct and are matched by their own pattern,
variableDeclaration.

This general pattern matches both simple assignments such as `x = 10`
and the compound forms such as `x += 10`.
(The patterns `assignmentOperatorSimple` and
`assignmentOperatorCompound` make the distinction by matching only one of these forms of assignment or the other.)

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignKind` | Either `` `simple` `` or `` `compound` ``, to indicate which form of assignment has matched; see assignKind |
| `targetExpression` | `expression` | The target of the assignment; typically, a variable receiving a new value, such as what C/C++ refers to as an *lvalue* |
| `sourceExpression` | `expression` | The expression which, when evaluated, is assigned to the target |
| `operator` | `enum` | The assignment operator, either `` `=` `` or one of the many compound forms, such as `` `+=` `` or `` `*=` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The `assignmentOperator` pattern matches source such as the assignment shown here:

  
 [image: C/C++ code follows]   

```
int num;

num = 1;
```

In this match, the `.operator` is described as `` `=` ``
and its `.kind` is `` `simple` ``.
Unsurprisingly, the `.sourceExpression` is an `intLiteral`;
specifically, the literal `1`.

What might be surprising is that there is a property named `.targetExpression`.
You might expect this to be named "`.targetVariable`",
but consider that not every assignment is directly to a named variable.
For example, an assignment can also be made to an address pointed to by a pointer, or to a member of an array.

In this particular example, however, `.targetExpression` is a
`variableReference`,
which is always the case when a variable is being assigned.

Consider the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern embeddedAssignment {
        assignmentOperator {
            .parent != simpleStatement
        }
    };
```

Statements and expressions in your code can be visualized as a tree structure.
We saw this in the Code patterns section, and we draw upon that example here.
Remember that the following C/C++ source code:

  
 [image: C/C++ code follows]   

```
x = y*2 + 1;
```

... is expressed by the following syntax tree:

[image: Code expressed as a tree of nodes]

We see that the `simpleStatement` pattern matches the expression
`x = y*2 + 1`,
which is an assignment of `y*2 + 1` to
the variable `x`.

The pattern `embeddedAssignment` shown above matches any instance of an assignment operator
that is not immediately under a simple statement.
In other words, `embeddedAssignment` finds assignments that occur within a larger expression
(because the parent would be another expression)
or within an `if`, `while`, or other statement
(because the parent would be another kind of statement).

Consequently, this pattern would detect the assignment of `y` in the following source code:

  
 [image: C/C++ code follows]   

```
x = 4 * (y = 42) + z;
```

... as well as the assignment of `x` in the following C/C++ source:

  
 [image: C/C++ code follows]   

```
if (x = 42) {
    // ...
};
```
