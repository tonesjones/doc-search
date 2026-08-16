---
title: "defaultStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defaultstatement.html"
content_id: "50g8n~jI33a2I2liwEOU5Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:53.864342+00:00"
---

# defaultStatement

Matches the `default` case in `switch` statements.

This pattern only matches nodes of type `statement`.

## Properties

`defaultStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `switch` statements that have a `default` clause:

  
 [image: CXM code follows]   

```
    pattern switchWithDefault {
        switchStatement as sw where
            exists stmt in sw.caseList where
                stmt matches defaultStatement
    };
```

## See also

caseStatement,
switchStatement
