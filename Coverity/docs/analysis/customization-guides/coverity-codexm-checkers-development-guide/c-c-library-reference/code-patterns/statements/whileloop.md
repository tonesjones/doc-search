---
title: "whileLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/whileloop.html"
content_id: "M9WjjO2YXJ5VmPkbdk1MpQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:05.854989+00:00"
---

# whileLoop

Matches only standard `while` loops
(as opposed to `do ... while` loops or `for` loops).

The match includes the body statement that the `while` loop contains.

This pattern only matches nodes of type `statement`.

## Properties

`whileLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition that causes the loop to terminate |
| `conditionDeclaration` | `declaration?` | If a variable is declared within the condition of the `while` loop, this property contains its name. (This is seldom done; this property is `null` if no such variable is declared.) |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently this is a `blockStatement`. |

**Inherits properties from:**

- astnode
- statement

## Example

The following C/C++ fragment matches a `whileLoop` CodeXM pattern, which sets the following properties:

- `.conditionExpression` is the condition expressed in parentheses;
  namely,
  `int cachedResult = SomeFunction()`.
- `.conditionDeclaration` describes the variable `cachedResult`.
- `.bodyStatement` is
  the `DoSomethingWith()` call inside the loop.

  
 [image: C/C++ code follows]   

```
while ( int cachedResult = SomeFunction() ) {
    DoSomethingWith( cachedResult );
};
```

## See also

Matching a loop whose condition is always true
