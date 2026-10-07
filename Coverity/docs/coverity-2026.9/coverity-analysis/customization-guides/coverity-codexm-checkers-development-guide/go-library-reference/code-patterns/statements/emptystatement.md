---
title: "emptyStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/emptystatement.html"
content_id: "wc6dzCO5QLypPJv2RbkPFw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:33.740375+00:00"
---

# emptyStatement

Matches empty statements.

The following are examples of `emptyStatement` situations:

  
 [image: Go code follows]   

```
    ;    // No code here

    {
        // No code here
    }

    if (b) {
        // ...
    }
        // No 'else' branch
```

This pattern only matches nodes of type `statement`.

## Properties

`emptyStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## See also

blockStatement,
ifStatement
