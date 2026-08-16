---
title: "Queries on trees"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/queries-on-trees.html"
content_id: "DyfC0TZOwa5EjF5g2LdwQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:34.489215+00:00"
---

# Queries on trees

These queries return information about the current tree.

- `is_tree_in_macro` — If the current tree is inside a macro,
  returns the macro's name. Otherwise, it returns NULL.
- `get_type_of_tree(tree t)` — Returns the
  `type_t` representing the type of `t`. If
  `t` does not have a type, returns NULL.
- `get_size_of_type(type_t *t)` — Returns the representation
  size in bytes for objects of type `t`.
