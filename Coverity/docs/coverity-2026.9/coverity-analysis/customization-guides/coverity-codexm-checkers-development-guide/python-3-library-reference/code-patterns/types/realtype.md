---
title: "realType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/realtype.html"
content_id: "2TAxfZPuo5zm9ih19xDXkA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.491346+00:00"
---

# realType

Matches real numbers of the `real`, `complex`, or `float` type.

This pattern only matches nodes of type `type`.

## Properties

`realType` does not expose any new properties.

## Example

The following CodeXM code matches any expression whose type is `real`, `complex`, or `float`:

[image: CXM code follows]

```
    node matches expression as e where e.type matches realType;
```
