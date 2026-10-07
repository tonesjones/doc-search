---
title: "Inheritance"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/inheritance.html"
content_id: "yKSHWc0fx~sggm1m6xT8Ng"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:55.416517+00:00"
---

# Inheritance

Given a `class_type_t`, the inheritance hierarchy can be examined using,
for example, the following:

```
class_type_t *c = ...;
defined_class_type_t d = c->load_definition();
if(d) {
    d->get_parents();
}
```

This returns a vector of the immediate ancestors.

To iterate over all parents, including those that are inherited, use:

```
class_type_t *c = ...;
defined_class_type_t d = c->load_definition();
if(d) {
    d->get_all_parents();
}
```
