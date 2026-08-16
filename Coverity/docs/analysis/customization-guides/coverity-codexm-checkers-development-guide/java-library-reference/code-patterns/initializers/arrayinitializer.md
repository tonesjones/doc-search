---
title: "arrayInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arrayinitializer.html"
content_id: "eXlaso_AW1_qA4AGBU0EAg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:26.615335+00:00"
---

# arrayInitializer

Matches array initialization that uses curly braces.

This pattern only matches nodes of type `initializer`.

## Properties

`arrayInitiializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variableInitializerList` | `list<initializer>` | A list of the elements within the curly braces |

**Inherits properties from:**

- astnode
- initializer

## Example

`arrayInitializer` would match an array initialization that used this format:

  
 [image: Java code follows]   

```
int[] a = {0, 1};
```
