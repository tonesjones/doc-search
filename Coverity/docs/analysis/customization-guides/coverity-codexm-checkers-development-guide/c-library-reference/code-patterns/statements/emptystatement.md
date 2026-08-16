---
title: "emptyStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/emptystatement.html"
content_id: "FqgaFgGRCnFCnyuUl7ORCg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:55.370804+00:00"
---

# emptyStatement

Matches empty statements.

An empty statement can be a line with no executable code that is terminated by a semicolon,
non-executable code enclosed by curly braces, or an implied branch of an `if` statement.

This pattern only matches nodes of type `statement`.

## Properties

`emptyStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The following are examples of `emptyStatement` situations:

  
 [image: C# code follows]   

```
    ;   // No code here

    {
        // No code here
    }

    if (b) {
        // ...
    }
    // No else branch
```

## See also

blockStatement,
ifStatement
