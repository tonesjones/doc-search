---
title: "assignmentOperatorSimple"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperatorsimple.html"
content_id: "9FSzZZJgDAJK0xsGAhBRFQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:41.874276+00:00"
---

# assignmentOperatorSimple

Matches only simple assignments.

CAUTION:

Even though variable declarations look similar to assignment operators, this pattern does not match variable declarations.
See the pattern variableDeclaration.

This pattern is shorthand for the pattern
`` assignmentOperator { .kind == `simple` } ``.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperatorSimple` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignKind` | Always `` `simple` ``; see assignKind |
| `targetExpression` | `expression` | The target of the assignment; typically, a variable receiving a new value, such as what C/C++ refers to as an *lvalue* |
| `sourceExpression` | `expression` | The expression which, when evaluated, is assigned to the target |
| `operator` | `enum` | Always `` `=` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The following C or C++ code assigns a constant value `123` to the variable `x`.
The pattern `assignmentOperatorSimple` matches this simple assignment:

  
 [image: C/C++ code follows]   

```
int x;

x = 123;
```

As mentioned previously, assignment doesn't happen only to variables.
The following CodeXM pattern matches an assignment to the target of a pointer:

  
 [image: CXM code follows]   

```
    pattern assignmentToPointer {
        assignmentOperatorSimple {
            .targetExpression == pointerDereference
        }
    };
```

Assuming the following definition:

  
 [image: C/C++ code follows]   

```
char* chptr;
```

... the `assignmentToPointer` pattern would *not* match the following code:

  
 [image: C/C++ code follows]   

```
chptr = somebuf;
```

... because the target expression is a variable reference (`chptr` itself).

The pattern *would* match the following source:

  
 [image: C/C++ code follows]   

```
*chptr = 42;
```

... because here the target expression dereferences `chptr`.

When a variable is a pointer, the array-like notation is seen as a pointer dereference as well.
That is, `chptr[0]` is equivalent to
`*chptr`,
so `assignmentToPointer` matches it.
This does not hold true for variables defined as arrays:
for `char buf[]`,
the array reference `buf[0]` does not match.
