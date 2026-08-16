---
title: "Mapping from variables to their class/type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/mapping-from-variables-to-their-class/type.html"
content_id: "u6l4AZGN4VHUqBygjXb71g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:51.280638+00:00"
---

# Mapping from variables to their class/type

To obtain the type of an expression or variable, match it with a pattern that inherits
from TypedExpr (such as Expr), and then use the
TypedExpr::get_type_t() method.

This returns a pointer to a types::type_t (hereafter referred to as
type_t) object, which is the root of a C++ class hierarchy for
representing types.

The type_t class has a number of methods for querying the actual type.
For example, type_t::as_class_p() returns a pointer to a
class_type_t if that type_t is a class_type_t,
otherwise it returns NULL.

The following is an Coverity Extend SDK checker fragment that checks for the
current expression being a pointer to a class:

```
Expr e;
if (MATCH(e)) {
  if (type_t *t = e.get_type_t()) {
    if (class_type_t *ct = t->as_class_p()) {
      // now 'ct' is the class_type_t representing the type
      // of the expression matched by 'e'
    }
  }
}
```
