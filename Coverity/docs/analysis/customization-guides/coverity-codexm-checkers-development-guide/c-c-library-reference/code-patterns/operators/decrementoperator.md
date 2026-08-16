---
title: "decrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/decrementoperator.html"
content_id: "Kngx0VH85mGn_Mn65q2eJQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:49.380122+00:00"
---

# decrementOperator

Matches the decrement operators, detecting both prefix (as in `--i`)
and postfix (`i--`) variants.

This pattern only matches nodes of type `expression`.

## Properties

`decrementOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being decremented |
| `kind` | `enum` | `` `prefix` `` or `` `postfix` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The `decrementOperator` pattern matches the instance on both lines of the following source code:

  
 [image: C/C++ code follows]   

```
    m--;
--m;
```

In both instances, `.operandExpression` refers to the variable `m`.
The `.kind` property is `` `postfix` `` in the first instance and `` `prefix` `` in the second.

The following CodeXM pattern matches any postfix decrement operator:

  
 [image: CXM code follows]   

```
    pattern postfixDecrement {
        decrementOperator {
            .kind == `postfix`
        }
    };
```
