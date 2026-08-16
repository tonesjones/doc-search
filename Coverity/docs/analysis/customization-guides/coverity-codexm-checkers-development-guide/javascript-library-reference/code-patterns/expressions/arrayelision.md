---
title: "arrayElision"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arrayelision.html"
content_id: "P0gO~_VOypyQQ6dFSr8lKQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:25.769764+00:00"
---

# arrayElision

Matches elisions in arrays.

An elision is the "hole" created when using commas within an array literal.

The elision is specified in ECMAScript 2015, 12.2.5.1.

This pattern only matches nodes of type `expression`.

## Properties

`arrayElision` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The `arrayElision` pattern matches the elements between the trailing commas
in the following array literal:

[image: JavaScript code follows]

```
    ["a", "b", , ,];
```

## See also

arrayLiteral
