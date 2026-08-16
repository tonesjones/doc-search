---
title: "Adding a C++ model"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-c-model.html"
content_id: "WYWMMY9uO2LsNl5qeaEfpQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:36.434416+00:00"
---

# Adding a C++ model

A major concern when adding a C++ model is to make sure that the mangled name of the function in the library matches the mangled name of the function in
the actual source code

For example, if one of the arguments to the function that you are attempting to override
is a structure pointer, you must either include the definition for that structure in
your library file, or make a dummy structure whose name exactly matches the name in your
library file. Mangled names include type names (for example, `struct factoidStruct`), but they do not include the structure's
contents.
