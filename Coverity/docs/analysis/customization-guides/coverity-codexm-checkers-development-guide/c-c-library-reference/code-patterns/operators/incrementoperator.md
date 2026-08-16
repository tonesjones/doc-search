---
title: "incrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incrementoperator.html"
content_id: "BiCa59hkarm9jN0q_f7wcw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:50.964235+00:00"
---

# incrementOperator

Matches the increment operators, detecting both prefix (as in `++i`)
and postfix (`i++`) variants.

This pattern only matches nodes of type `expression`.

## Properties

`incrementOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being incremented |
| `kind` | `enum` | `` `prefix` `` or `` `postfix` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The `incrementOperator` pattern matches both of the following two lines of C/C++ code:

  
 [image: C/C++ code follows]   

```
    m++;
    ++m;
```

In both instances, `.operandExpression` refers to the variable `m`.
The `.kind` property is `` `postfix` `` in the first instance and `` `prefix` `` in the second.

The following custom CodeXM pattern detects when post-incrementation is used in the update statement
of a `for` loop:

  
 [image: CXM code follows]   

```
    pattern forLoopPostIncrement {
        forLoopSimple {
            .updateStatement == NonNull
        }
        as forIncr where forIncr.updateStatement
            matches simpleStatement {
                .expression == incrementOperator {
                    .kind == `postfix`
                }
            }
    };
```

In particular, the `forLoopPostIncrement` pattern matches the following C/C++ code,

  
 [image: C/C++ code follows]   

```
    for ( int i = 0; i < 99; i++ ) {
        // Do something.
    };
```

... but it does not match the comparable pre-incrementation:

  
 [image: C/C++ code follows]   

```
    for ( int i = 0; i < 99; ++i ) {
        // Do something.
};
```
