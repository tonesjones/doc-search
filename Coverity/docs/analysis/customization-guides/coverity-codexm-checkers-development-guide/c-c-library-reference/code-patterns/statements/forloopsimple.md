---
title: "forLoopSimple"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopsimple.html"
content_id: "8yxrm~_xEz_fM8kuCSt0wg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:59.154852+00:00"
---

# forLoopSimple

Specifically matches only simple `for` loops.

## Properties

`forLoopSimple` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum forLoopKind` | The kind of loop: always `` `simple` ``; see forLoopKind |
| `initializationStatement` | `statement?` | The initialization clause of the `for` loop; `null` if there is none |
| `conditionExpression` | `expression` | The condition that causes the loop to terminate |
| `conditionDeclaration` | `declaration?` | If a variable is declared within the condition (second clause) of the `for` loop, this property contains its name. (This is seldom done; this property is `null` if no such variable is declared.) |
| `updateStatement` | `statement?` | The statement that updates the loop value; frequently something like `i++`. This record is `null` if there is no such statement |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently this is a `blockStatement`. |

**Inherits properties from:**

- astnode
- statement

## Example

The following code:

  
 [image: C/C++ code follows]   

```
for ( int i = 0; i < 42; i++ ) {
    doSomething(i);
};
```

... is matched by `forLoopSimple`, which sets the following properties:

- `.kind` is assigned `` `simple` ``.
- `.initializationStatement` is set to
  the `int i=0` declaration.
- `.conditionExpression` is `i < 42`.
- The `.conditionDeclaration`
  is `null`,
  because the condition doesn't declare anything.
- `.updateStatement` is the increment `i++`.
- `.bodyStatement` is set to
  the `blockStatement` that contains the function call.
