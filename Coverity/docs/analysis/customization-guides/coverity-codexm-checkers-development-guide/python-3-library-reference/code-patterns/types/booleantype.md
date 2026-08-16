---
title: "booleanType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booleantype.html"
content_id: "1Eyl1_CkGApHVV1vu~4pFA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:33.555673+00:00"
---

# booleanType

Matches the `boolean` type.

This pattern only matches nodes of type `type`.

## Properties

`booleanType` does not expose any new properties.

## Example

The following CodeXM code matches any expression of the type `boolean`:

[image: CXM code follows]

```
    node matches expression as e where e.type matches booleanType;
```
