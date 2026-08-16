---
title: "temporaryConstruction"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/temporaryconstruction.html"
content_id: "N3SWwj6D2Reo07WBnWdVKw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:50.310194+00:00"
---

# temporaryConstruction

Matches all locations where a temporary variable is constructed.

This pattern only matches nodes of type `expression`.

## Properties

`temporaryConstruction` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | How the temporary variable was constructed |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds all assignments from temporary variables:

  
 [image: CXM code follows]   

```
    pattern assignmentFromTemp {
        assignmentOperator {
            sourceExpression == temporaryConstruction
        }
    };
```
