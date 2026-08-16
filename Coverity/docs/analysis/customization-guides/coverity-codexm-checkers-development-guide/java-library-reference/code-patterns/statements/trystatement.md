---
title: "tryStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/trystatement.html"
content_id: "lRwacYnWc8U4gnuPNW4XLQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:48.282226+00:00"
---

# tryStatement

Matches `try` statements, including `catch` blocks and the `finally` block.

This pattern only matches nodes of type `statement`.

## Properties

`tryStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the `try` block |
| `catchBlockList` | `list<handler>` | The Java handlers |
| `finallyStatement` | `statement>` | The body of the `finally` block, it if exists; `null` if it does not |
| `resourcesList` | `list<declaration>` | A list of resources declared in a try-with-resource `try` |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches handlers for `Exception`.
This pattern uses `tryStatement`,
which has the field `.catchBlockList`, a list of handlers:

  
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
