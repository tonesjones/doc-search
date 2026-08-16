---
title: "The CodeXM-File"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-codexm-file.html"
content_id: "pky4RBqyjmb1mlxjKGLchg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:11.551458+00:00"
---

# The CodeXM-File

A CodeXM file consists of checker definitions and the declarations that support them.

## Syntax

The source file contains any number of declarations. Each declaration is terminated by a semicolon ( `;` ).
Declarations can appear in any order, except that a definition or declaration needs to appear before the first time a reference to it appears;
in other words, the rule is *Declare it before you use it*.

Each of these definitions is described in greater detail below.

  
 [image: Syntax diagram, the CodeXM-file]   

```
CodeXM-file ::=
    (
        (   checker-definition
          | const-definition
          | forward-declaration
          | function-definition
          | function-property-definition
          | include-directive
          | pattern-definition
          | type-definition
        )
        ';'
    )*
```
