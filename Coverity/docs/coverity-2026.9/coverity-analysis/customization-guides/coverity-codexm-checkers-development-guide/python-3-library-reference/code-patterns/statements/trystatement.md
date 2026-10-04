---
title: "tryStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/trystatement.html"
content_id: "YNWHBDhH6UlI0ok7MhdBMQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:49.942519+00:00"
---

# tryStatement

Matches `try` statements, including
any `except`, `finally`,
or `else` blocks.

This pattern only matches nodes of type `statement`.

## Properties

`tryStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `elseBlock` | `list<statement>?` | The statements in the `else` block; `null` if there is no `else` |
| `exceptHandlers` | `list<statement>` | The statements in the `except` block |
| `finallyBlock` | `statement?` | The statement in the `finally` block; `null` if there is no `finally` |
| `tryBlock` | `statement` | The statement in the `try` block |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `try` statements
that contain both `finally` and `else` blocks:

[image: CXM code follows]

```
    pattern hasElseAndFinally {
        tryStatement {
            .elseBlock == NonNull;
            .finallyBlock == NonNull
        }
    };
```
