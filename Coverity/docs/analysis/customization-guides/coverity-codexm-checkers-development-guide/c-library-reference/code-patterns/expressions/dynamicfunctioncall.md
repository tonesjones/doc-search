---
title: "dynamicFunctionCall"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dynamicfunctioncall.html"
content_id: "yKRjxHg7r9z4PMo3U7G2tA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:34.513562+00:00"
---

# dynamicFunctionCall

Matches dynamic function calls.

This pattern only matches nodes of type `expression`.

## Properties

`dynamicFunctionCall` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `callKind` | `DynamicFuncKind` | One of `` `DFK_METHOD` ``, `` `DFK_INVOKE` ``, `` `DFK_PROPERTY` ``, `` `DFK_INDEXER` ``, `` `DFK_OPERATOR` ``, or `` `DFK_CONVERSION` `` |
| `name` | `string` | The name of the function |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches calls to the dynamic function named `example()`:

  
 [image: CXM code follows]   

```
    pattern dynamicExampleCall {
        dynamicFunctionCall {
            .name == "example"
        }
    };
```
