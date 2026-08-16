---
title: "Tree structure of types"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tree-structure-of-types.html"
content_id: "8EOXKuISGMRs40SpAvMtUw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:51.936489+00:00"
---

# Tree structure of types

A given type_t object is actually a tree (or subtree). For example,
the type `int (*)(float, char**)` looks like the following:

```
                    pointer_type_t
                          |
                          |pointed_to
                          V
                    function_type_t
                    /      \        \
        return_type/        \args[0] \args[1]
                  V          V        V
         scalar_type_t  scalar_type_t  pointer_type_t
                |            |              |
                |name        |name          |pointed_to
                |            |              |
              "int"       "float"      pointer_type_t
                                            |
                                            |pointed_to
                                            |
                                       scalar_type_t
                                            |
                                            |name
                                            |
                                         "char"
```

scalar_type_t is a leaf type.

The class_type_t and union_type_t classes are also
leaf types of a sort. Since all recursive types (such as the type of a linked list) must
go through a class or struct or union in order to recurse, you can think of them as
leaves — so that types really are trees, rather than arbitrary graphs. However, this
"leafness" is a property of the code that *uses* the type_t
structure. It's merely a convenient convention. This convention is used by 
`type_recursive_visitor_t`
, among others.
