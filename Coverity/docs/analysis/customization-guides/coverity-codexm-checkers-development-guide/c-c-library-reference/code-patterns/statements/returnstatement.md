---
title: "returnStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/returnstatement.html"
content_id: "RfHENhBhojAM3fr6NqAX8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:02.864291+00:00"
---

# returnStatement

Matches both simple, void `return` statements,
and `return <expression>` returns.

## Properties

`returnStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isVoid` | `bool` | Equal to `true` if the function is a `void` function that uses a simple `return` statement and does not return a value. |
| `returnedExpression` | `expression?` | If the type of the function is *not* `void`, this property contains the expression that the function returns; otherwise, it is `null`. |

**Inherits properties from:**

- astnode
- statement

## Example

Consider the following C or C++ source:

  
 [image: C/C++ code follows]   

```
int func( int i ) {
    return i;
}
```

The `returnStatement` CodeXM pattern matches the
`return` statement found within that function code.
In this example, the pattern's `.isVoid` property is
`false`,
and the `.returnedExpression` is `i`.

The following pattern matches instances of `return`
where the expression being returned is an integer literal that appears
directly in the source code
(as opposed to one that was expanded from a preprocessor macro):

  
 [image: CXM code follows]   

```
    pattern literalIntReturn {
        returnStatement {
            .returnedExpression == intLiteral {  // An integer
                .macrosExpandedFrom.length == 0
            }                                    // Not expanded from macro
        }
    };
```

In other words, this matches `return 42;`
but it does not match `return ERROR_CODE;`,
where `ERROR_CODE` is defined to be an integer.
