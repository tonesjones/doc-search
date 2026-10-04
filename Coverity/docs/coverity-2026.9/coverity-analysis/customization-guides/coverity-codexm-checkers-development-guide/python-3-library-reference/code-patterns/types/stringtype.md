---
title: "stringType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/stringtype.html"
content_id: "v0GDUDCK1ciGMIE0fi6ZsA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.532081+00:00"
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
