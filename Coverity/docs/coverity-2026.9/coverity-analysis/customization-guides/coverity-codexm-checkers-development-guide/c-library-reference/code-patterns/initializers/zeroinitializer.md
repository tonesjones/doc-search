---
title: "zeroInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/zeroinitializer.html"
content_id: "WX3qgporvfhyN3nocmtYzg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:30.736715+00:00"
---

# zeroInitializer

Matches initializations where no value is provided.

This pattern only matches nodes of type `initializer`.

## Properties

`zeroInitializer` does not expose any new properties.

**Inherits properties from:**

- astnode
- initializer

## Example

For a C# class declared as follows:

  
 [image: C# code follows]   

```
    class Example {
        private int a;
    };
```

... the initialization of the field `` `a` `` will match `zeroInitializer`.
