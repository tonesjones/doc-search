---
title: "type_visitor_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/type_visitor_t.html"
content_id: "zn7e2f3QyTF8NeoqJoAFMw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:55.530521+00:00"
---

# type_visitor_t

The type_visitor_t is an interface that clients can implement. The
handlers, such as on_function or on_class, react
to the various kinds of type_t nodes. Invoking its
operator() on a type.t object invokes the
appropriate handler for the dynamic type of that object.
