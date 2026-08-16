---
title: "expressionInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressioninitializer.html"
content_id: "U6zN89Yvvolg09QKf__8pw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:56.874793+00:00"
---

# expressionInitializer

Matches simple expressions used to initialize scalar objects.

## Properties

`expressionInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression that evaluates to a value used to initialize the object |

**Inherits properties from:**

- astnode
- initializer

## Example

In the following target code:

  
 [image: C/C++ code follows]   

```
int x = y + z;
```

... `expressionInitializer` matches the right-hand-side of the initialization
and captures it via the property `.expression`.

The unqualified CodeXM pattern matches any initializer.
To match a specific type of initializer—for example, the type of initializer represented by
the binary operator (as in the example above)—you could use the following pattern:

  
 [image: CXM code follows]   

```
    node matches expressionInitializer {
        .expression == binaryOperator
    };
```
