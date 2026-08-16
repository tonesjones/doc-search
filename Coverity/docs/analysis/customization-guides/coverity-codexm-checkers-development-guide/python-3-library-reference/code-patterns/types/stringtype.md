---
title: "stringType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stringtype.html"
content_id: "v0GDUDCK1ciGMIE0fi6ZsA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:36.852104+00:00"
---

# stringType

Matches the `string` type.

This pattern only matches nodes of type `type`.

## Properties

`stringType` does not expose any new properties.

## Example

The following CodeXM code matches any expression whose type is `string`:

[image: CXM code follows]

```
    node matches expression as e where e.type matches stringType;
```
