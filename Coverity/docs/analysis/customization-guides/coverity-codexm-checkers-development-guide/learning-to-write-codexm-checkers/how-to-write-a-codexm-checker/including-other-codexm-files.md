---
title: "Including other CodeXM files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/including-other-codexm-files.html"
content_id: "MU1uyDbe_zbWHou79hkbVw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:49.069290+00:00"
---

# Including other CodeXM files

With CodeXM, you can include other CodeXM files by using the `include` directive.

When you include another file, the patterns, functions, and other definitions kept in that file become available to the current CodeXM file.
This allows you to define a collection of useful tools in one place, and share them among many checker files.

To do this, use the following syntax in your checker file:

[image: CXM code follows]

```
include "../path/to/codexm/file.cxm";
```

Attention:
Unlike other instances of include mentioned in this document, the code that follows the `include` keyword is a (quote-enclosed) string,
not a (backtick-enclosed) enumeration member. When quotes are used, this tells CodeXM to look for a file on your file system.
In contrast, the enum-based include directives cause predefined libraries installed with cov-analyze to be included.

Relative paths used with the quoted-string variant are relative to the location of the CodeXM file.
