---
title: "zeroInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/zeroinitializer.html"
content_id: "MEzePPPu4dmoixBObOVIpg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:42.656393+00:00"
---

# zeroInitializer

Matches initializations where no value is given.

This pattern only matches nodes of type `initializer`.

## Properties

`zeroInitializer` does not expose any new properties.

**Inherits properties from:**

- astnode
- initializer

## Example

For the following Java class:

  
 [image: Java code follows]   

```
Example {
    private int a;
};
```

... the initialization of the field `a` will be a `zeroInitializer`
