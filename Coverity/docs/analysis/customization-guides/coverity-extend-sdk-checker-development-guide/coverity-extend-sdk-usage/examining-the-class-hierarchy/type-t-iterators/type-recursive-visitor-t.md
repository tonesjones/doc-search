---
title: "type_recursive_visitor_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/type_recursive_visitor_t.html"
content_id: "drlPQXgx7a3S1uyaF4jKcA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:56.544738+00:00"
---

# type_recursive_visitor_t

The previous two interfaces are combined to form the
type_recursive_visitor_t, which is both an interface and a tree
traversal mechanism. To use this class, inherit from it, and then implement the
appropriate on_XXX methods. By default, these methods recursively
traverse their sub types (hence the `recursive` in the name of the
visitor), except for classes and unions. That is, they visit the tree structure
described in Tree structure of types. If you
override one of the methods other than on_class or
on_union, you must call the superclass method if you want
recursive traversal to proceed below the overridden point.
