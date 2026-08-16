---
title: "The include-directive"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-include-directive.html"
content_id: "dcvl_~vFlN_GRp3kdOVaDw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:18.005264+00:00"
---

# The include-directive

The `include-directive` performs two functions.
First, it incorporates the contents of the specified CodeXM file, as if it were present in the current file.
Second, if an `enum-literal-expression` is present, and it indicates a language library,
the expression ensures that the contents of this CodeXM file are applied only to code of the same language.

Including another CodeXM file permits you to write common support functionality and make it available to many different checkers,
or to aggregate many checkers (separated for reasons of maintainability) into a single file that you can specify
on the `cov-analyze` command line.

For example, if your file contains the following line:

[image: CXM code follows]

```
include `C/C++`;
```

... this causes the checkers declared in your file to be applied only to C or C++ code.

## Syntax

The directive is introduced by the `include` keyword, followed by either of the following:

- A string literal that contains the path (relative to the present file) and name of the file to include
- An enum literal that names a built-in include file

  
 [image: Syntax diagram, include-directive]   

```
include-directive ::=
    'include' ( string-literal-expression
              | enum-literal-expression )
```
