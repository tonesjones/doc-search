---
title: "defaultStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defaultstatement.html"
content_id: "gR~JkosDx2Jb43cVtk6STg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:03.738891+00:00"
---

# defaultStatement

Matches the `default` clause within `switch` statements.

This pattern only matches nodes of type `statement`.

## Properties

`defaultStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The `defaultStatement` pattern matches the statement `default:` in the following source code:

[image: JavaScript code follows]

```
    switch(i) {
        case 0:
            break;
        default:        // defaultStatement
            break;
    };
```

## See also

switchStatement
