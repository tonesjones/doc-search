---
title: "booleanType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booleantype.html"
content_id: "E~1~5EqspWG2aQpRAbzwGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:14.596725+00:00"
---

# booleanType

Matches the `bool` type.

This pattern only matches nodes of type `type`.

## Properties

`booleanType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `sizeInBits` | `int` | The size of the Boolean, in bits |
| `sizeInBytes` | `int` | The size of the Boolean, in bytes |

## Example

The following CodeXM pattern matches any expression of the type `bool`:

  
 [image: CXM code follows]   

```
    node matches expression as e where e.type matches booleanType;
```
