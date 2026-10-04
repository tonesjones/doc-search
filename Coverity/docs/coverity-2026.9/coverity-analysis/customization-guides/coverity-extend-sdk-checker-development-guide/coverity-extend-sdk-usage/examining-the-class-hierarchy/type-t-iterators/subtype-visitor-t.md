---
title: "subtype_visitor_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/subtype_visitor_t.html"
content_id: "JWIvxSl_evFzYFBQ8PoZtQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:55.570610+00:00"
---

# subtype_visitor_t

The subtype_visitor_t is another interface. When a type object's
iter_subtypes method is invoked, the type object invokes the
passed subtype_visitor_t::operator() on each of its component or
"sub" types. For example, the fields of a class are considered sub types, as is the
pointed_to element of a pointer_type_t.
