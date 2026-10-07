---
title: "integralType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/integraltype.html"
content_id: "C1fRl2fMJsaiclWy2bM4Ng"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.451154+00:00"
---

# integralType

Matches integers of either the `int` or `long` type.

This pattern only matches nodes of type `type`.

## Properties

`integralType` does not expose any new properties.

## Example

The following CodeXM code matches any expression whose type is `int` or `long`:

[image: CXM code follows]

```
    node matches expression as e where e.type matches integralType;
```
