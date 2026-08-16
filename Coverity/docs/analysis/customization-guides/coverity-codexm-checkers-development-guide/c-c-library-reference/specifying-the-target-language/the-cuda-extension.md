---
title: "The CUDA extension"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-cuda-extension.html"
content_id: "PdID3QJzEf78Gc5wonVyrQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:26.737682+00:00"
---

# The CUDA extension

In Coverity 2020.12, the C/C++ library introduced support for the CUDA® parallel computing platform.

CUDA support includes additional property fields for the
globalVariableSymbol,
localVariableSymbol, and
variableSymbol patterns.
It also includes a new pattern, kernelCall,
which matches calls to launch CUDA kernels.

To use `kernelCall` patterns in your CodeXM program, you need to replace the declaration that includes
`` `C/C++` `` with an include of `` `CUDA` ``; for example:
`` include `CUDA` ``.

If you don't include the library named `` `CUDA` ``, your program can still use the CUDA-specific
property fields, but it won't recognize the `kernelCall` pattern.
