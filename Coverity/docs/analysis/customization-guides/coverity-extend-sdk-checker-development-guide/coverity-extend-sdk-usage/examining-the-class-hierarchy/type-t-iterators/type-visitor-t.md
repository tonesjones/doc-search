---
title: "type_visitor_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/type_visitor_t.html"
content_id: "zn7e2f3QyTF8NeoqJoAFMw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:55.238214+00:00"
---

# type_visitor_t

The type_visitor_t is an interface that clients can implement. The
handlers, such as on_function or on_class, react
to the various kinds of type_t nodes. Invoking its
operator() on a type.t object invokes the
appropriate handler for the dynamic type of that object.
