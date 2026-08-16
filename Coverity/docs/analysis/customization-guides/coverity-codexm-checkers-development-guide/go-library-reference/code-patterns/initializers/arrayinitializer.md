---
title: "arrayInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arrayinitializer.html"
content_id: "h4sWNLnpCxKxWkpNwUGYrg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:55.804915+00:00"
---

# arrayInitializer

Matches the initializations of linear arrays that use a list enclosed in curly braces.

This pattern only matches nodes of type `initializer`.

## Properties

`arrayInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variableInitializerList` | `list<initializer>` | A list of the elements in the curly braces |

**Inherits properties from:**

- astnode
- initializer

## Example

The `arrayInitializer` pattern matches code such as the following array initialization:

  
 [image: Go code follows]   

```
    a []int = {0, 1};
```
