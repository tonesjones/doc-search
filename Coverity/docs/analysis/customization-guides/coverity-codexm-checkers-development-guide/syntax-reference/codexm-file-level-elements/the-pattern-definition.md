---
title: "The pattern-definition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-pattern-definition.html"
content_id: "PJn7t2YOBeuEBObrZXeJLg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:18.735932+00:00"
---

# The pattern-definition

A `pattern-definition` lets you define code patterns that can be more complex than the predefined patterns
provided by a language library.

Custom patterns can be built using other patterns that have already been defined (either library patterns or other custom patterns in
your own CodeXM project).

A pattern can be recursive, but to implement this, you need to define a function;
also see Defining CodeXM functions.

## Syntax

  
 [image: Syntax diagram, pattern-definition]   

```
pattern-definition ::=
    'pattern' pattern-name '{' match-list '}'
```
