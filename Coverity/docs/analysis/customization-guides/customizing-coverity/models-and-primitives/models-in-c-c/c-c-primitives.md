---
title: "C/C++ primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-primitives.html"
content_id: "xbEUEGQutfJV_jtbYBqDpQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:39.723654+00:00"
---

# C/C++ primitives

These sections describe the modeling primitives available to C and C++ source
code.

The <install_dir>/library/ directory contains the source
for the models shipped with Coverity Analysis. You can alter these
models and recompile them with the `cov-make-library` command. To
add new models, create a file with stub functions that represent the behavior of the
functions you wish to model.

Note: Do not use the files in the <install_dir>/library/
directory as arguments to the `cov-make-library` command. Instead,
create your own files for models.

A model can employ either Coverity primitives or existing library functions (for example,
`malloc()`, `calloc()`, and `fopen()`).
You can find the files referenced as examples in
<install_dir>/library/generic/common/.
