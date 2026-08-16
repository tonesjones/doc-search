---
title: "subscriptReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/subscriptreference.html"
content_id: "~U7mAM4KYF0ZHRFvEYqvYw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:49.637077+00:00"
---

# subscriptReference

Matches uses of a subscript to find a value in an array.

This pattern only matches nodes of type `expression`.

## Properties

`subscriptReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `arrayExpression` | `expression` | The array the subscript is being used on |
| `indexExpression` | `expression` | The value inside the brackets ( `[ ]` ) |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches where a variable is used as an index to look up a value in an array:

  
 [image: CXM code follows]   

```
    pattern variableArrayLookup {
        subscriptReference {
            .indexExpression == variableReference
        }
    };
```
