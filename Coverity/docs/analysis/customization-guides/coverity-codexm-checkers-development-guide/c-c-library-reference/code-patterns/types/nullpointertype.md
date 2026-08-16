---
title: "nullPointerType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullpointertype.html"
content_id: "j9nIDyme79B2__N5wKIStQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:17.033301+00:00"
---

# nullPointerType

Matches null pointers, including the keyword `nullptr` introduced in C++11.

## Properties

This pattern matches only nodes of type `type`.

`nullPointerType` does not expose any new properties.

**Inherits properties from:**

- astnode

## Example

In the following source code fragment, `nullPointerType` matches the variable `nullVar`:

  
 [image: C/C++ code follows]   

```
#include <cstddef>

std::nullptr_t nullVar = nullptr;
```
