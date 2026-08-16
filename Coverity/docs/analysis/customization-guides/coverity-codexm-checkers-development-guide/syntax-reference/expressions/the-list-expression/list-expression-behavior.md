---
title: "list-expression behavior"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/list-expression-behavior.html"
content_id: "UjLhLAS3DyjhwsuQg3S1hw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:43.261794+00:00"
---

# list-expression behavior

Each `expression` in the list is evaluated when the list is created.
The order of items in the list is the order in which they are specified in the source code.

Elements do not have to be unique: More than one element can have the same value.

To access elements in a list, you can use either a for-loop-expression
or an element-access-expression.
You can also retrieve members of a list by using the set-filter-expression.
