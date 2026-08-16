---
title: "emptyStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/emptystatement.html"
content_id: "O_0Deu6wwk92uD9OKw3SVg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:39.150412+00:00"
---

# emptyStatement

Matches empty statements.

An empty statement might be a non-statement (empty text) terminated by a semicolon, curly braces that do not enclose code,
or it might be an implied branch of an `ifStatement`.

This pattern only matches nodes of type `statement`.

## Properties

`emptyStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The following are examples of Java source code that `emptyStatement` would match:

  
 [image: Java code follows]   

```
    ;   // No code here

    {
        // No code here
    }
                
    if (b) {
        // ...
    }
        // No 'else' branch
```

## See also

blockStatement,
ifStatement
