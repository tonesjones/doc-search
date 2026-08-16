---
title: "TypePattern Superclass"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/typepattern-superclass.html"
content_id: "EcPXhoUvEZgy2pNaFTdDYA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:20.686153+00:00"
---

# TypePattern Superclass

TypePattern matches types. They cannot be used directly in
MATCH or MATCH_TREE (because these functions
match AST nodes) but they can be used as parameters to other patterns, or used directly
on the result of get_type_of_tree. By default, most
TypePatterns remove typedefs and qualifiers before attempting to
match (exceptions are noted). This means for instance, that a pattern
`x_p` defined like this:

```
StructType x("X");
PointerType x_p(x);
```

matches all these types:

```
typedef struct X * X_p; X_p
struct X *
struct X const *
```

TypePattern also has a
match_with_typedefs_and_qualifiers that is analogous to
ExpressionPattern::match_with_casts.
