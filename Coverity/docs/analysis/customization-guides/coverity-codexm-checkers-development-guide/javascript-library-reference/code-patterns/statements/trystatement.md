---
title: "tryStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/trystatement.html"
content_id: "AiUHYWML2~1pf4Xnu8w55Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:14.451638+00:00"
---

# tryStatement

Matches `try ... catch ... finally` statements.

This pattern only matches nodes of type `statement`.

## Properties

`tryStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statements in the body of the `try` statement |
| `catchBlockList` | `list<record>` | The list of catch blocks |
| `finallyStatement` | `statement?` | The `finally` statement; `null` if there isn’t one |

**Inherits properties from:**

- astnode
- statement

## Example

The `tryStatement` pattern matches the following case:

[image: JavaScript code follows]

```
    try {         // Case 1
        f1(0);
    } catch(e) {
        // ...
    } finally {
        f2();
    }
                
    try {         // Case 2
        f1(0);
    } catch(e) {
        // ...
    };
```

In the first case, the `.bodyStatement` property is the
blockStatement `{f1(0);}`,
the `.catchBlockList` property is a list with one element, and
the `.finallyStatement` property is the\
blockStatement `{f2();}`.

In the second case, the `.finallyStatement` property is `null`.
