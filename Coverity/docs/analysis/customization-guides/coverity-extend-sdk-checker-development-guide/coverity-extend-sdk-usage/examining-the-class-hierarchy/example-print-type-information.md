---
title: "Example: print type information"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-print-type-information.html"
content_id: "J9W1nopC8ZqCUvxJdB9ssQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:57.839359+00:00"
---

# Example: print type information

The PRINT_TYPES checker example (see also,
<install_dir>/sdk/samples/print_types/print_types.cpp)
demonstrates some of the type_t API. The checker itself simply
matches declarations and uses the declared types as a root set in a recursive
exploration of the program's type hierarchy. It also prints out the name and type of
those declarations. The bulk of the work is done by the
ClassTypeVisitor, which inherits from
type_recursive_visitor_t. Its on_class method
prints out the base classes and (non-static) fields of each class that can be reached
from the root set of types. It keeps a set of class names so it can avoid printing
information about the same class twice. Note that, as explained previously, you cannot
keep a set of class_type_t pointers.
