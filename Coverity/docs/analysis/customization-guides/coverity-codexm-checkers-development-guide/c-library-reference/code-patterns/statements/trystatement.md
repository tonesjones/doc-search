---
title: "tryStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/trystatement.html"
content_id: "cTYo55KTZ~c9zkzkswD~Ww"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:08.027657+00:00"
---

# tryStatement

Matches `try` statements, including their initial block, `catch` blocks, and `finally` block (if present).

This pattern only matches nodes of type `statement`.

## Properties

`tryStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the initial `try` block |
| `catchBlockList` | `list<handler>` | The bodies of the `catch` blocks |
| `finallyStatement` | `statement?` | The body of the `finally` block, it if exists; `null`, otherwise |
| `resourcesList` | `list<declaration>` | A list of resources declared in a try-with-resource `try`. |

**Inherits properties from:**

- astnode
- statement

## Example

The following pattern matches handlers for `Exception`. It uses the `tryStatement` pattern's `catchBlockList` property, which provides a list of handlers:

  
 [image: CXM code follows]   

```
    pattern exceptionHandle {
        tryStatement as t where
            exists h in t.catchBlockList where
                h.variable.type matches classType { .simpleName == "Exception" }
    };
```

## See also

declaration,
handler
