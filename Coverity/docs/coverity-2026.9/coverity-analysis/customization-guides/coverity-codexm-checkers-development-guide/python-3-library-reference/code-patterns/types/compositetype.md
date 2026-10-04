---
title: "compositeType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/compositetype.html"
content_id: "0kWy2Y~pytSwiB7jaB2N~w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.358020+00:00"
---

# compositeType

Matches composite objects such as sequences, sets, and dictionaries.

This pattern only matches nodes of type `type`.

## Properties

`compositeType` does not expose any new properties.

## Example

The following CodeXM code matches any expression that has a composite type:

[image: CXM code follows]

```
    node matches expression as e where e.type matches compositeType;
```
