---
title: "temporaryExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/temporaryexpression.html"
content_id: "CzbzqojH_AtQAqPU2VNsuw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:28.602692+00:00"
---

# temporaryExpression

Matches all locations where a temporary object is constructed.

This pattern only matches nodes of type `expression`.

## Properties

`temporaryExpression` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches temporary constructions of collections:

  
 [image: CXM code follows]   

```
    pattern temporaryCollectionConstruction {
        temporaryExpression {
            .initializer = objectInitializer {
                .memberInitializers == addMemberInitializer
            }
        }
    };
```
