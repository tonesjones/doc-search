---
title: "arrayDimensionsInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arraydimensionsinitializer.html"
content_id: "JRRVe54rr6fyEDCCGBufyg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:16.671106+00:00"
---

# arrayDimensionsInitializer

Matches multidimensional array initializations.

This pattern only matches nodes of type `initializer`.

## Properties

`arrayDimensionsInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `dimensions` | `list<expression>` | A list of the dimensions |

**Inherits properties from:**

- astnode
- initializer

## Example

The CodeXM pattern `arrayDimensionsInitializer` matches code such as the following array initialization in C# code:

  
 [image: C# code follows]   

```
    int a[][][] = new int[3][][];
```
