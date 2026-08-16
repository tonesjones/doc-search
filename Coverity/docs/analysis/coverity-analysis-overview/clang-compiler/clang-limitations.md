---
title: "Clang Limitations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/clang-limitations.html"
content_id: "hUx_8ADbsViNd3_nZhX03A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:38.935317+00:00"
---

# Clang Limitations

Clang compilers have various use limitations with Coverity products. These limitations
are described in this section.

Language limitations
:   The following language extensions are not supported. Functions and variable initializers
    that use these features will not be analyzed. However, other functions and
    variable initializers within the same translation unit will still be analyzed.

    - Altivec vector types and expressions
    - CUDA language extensions
    - OpenMP language extensions
    - OpenCL language extensions

Compiler driver limitations
:   - Clang driver invocations that specify the `-cc1` option are not
      supported.
    - Clang driver invocations that specify multiple `-arch
      <architecture>` options are not supported.
