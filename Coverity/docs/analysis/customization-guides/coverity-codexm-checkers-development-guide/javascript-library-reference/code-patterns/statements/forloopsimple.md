---
title: "forLoopSimple"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopsimple.html"
content_id: "XEx4FVtsjH9RrEzxMzY6FQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:08.481272+00:00"
---

# forLoopSimple

Matches simple `for` loops of the form `for (int i = 0; i < 10; ++i)`.

This pattern only matches nodes of type `statement`.

## Properties

`forLoopSimple` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently, this is a blockStatement. |
| `conditionExpression` | `expression` | The condition that causes the loop to terminate |
| `initializationStatement` | `statement` | Initialization clause of the for loop |
| kind | `enum` | Always `` `simple` `` |
| `updateStatement` | `statement` | The expression statement to update the loop value (frequently something like `i++`) |

**Inherits properties from:**

- astnode
- statement

## Example

The `forLoopSimple` pattern matches the following `for` loop:

[image: JavaScript code follows]

```
    for (let i = 0; i < 10; ++i) {
        // ...
    };
```

## See also

forLoopIn,
forLoopOf
