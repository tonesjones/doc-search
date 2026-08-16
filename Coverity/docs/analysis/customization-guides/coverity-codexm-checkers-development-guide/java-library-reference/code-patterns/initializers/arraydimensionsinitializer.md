---
title: "arrayDimensionsInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arraydimensionsinitializer.html"
content_id: "GFumWTlAg_1x3xL1mOFpVg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:25.881669+00:00"
---

# arrayDimensionsInitializer

Matches multidimensional array initialization.

This pattern only matches nodes of type `initializer`.

## Properties

`arrayDimensionsInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `dimensions` | `list<expression>` | List of dimensions |

**Inherits properties from:**

- astnode
- initializer

## Example

`arrayDimensionsInitializer` would match an array initialization that used this format:

  
 [image: Java code follows]   

```
int a[][][] = new int[3][][];
```
