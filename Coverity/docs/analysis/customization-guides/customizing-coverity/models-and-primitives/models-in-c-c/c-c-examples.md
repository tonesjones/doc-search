---
title: "C/C++ examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-examples.html"
content_id: "4bk2OptoiNk4KL2mk2ySlQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:31.185139+00:00"
---

# C/C++ examples

The following sections describe use cases that apply to C source, C++ source, or to both languages.

In Coverity Analysis terminology, adding a new function to the Coverity Analysis configuration is called *adding a model*.
You can rewrite the model for a function in the standard library so that it more accurately reflects the function's behavior.
Adding a model to the configuration can improve the accuracy of analysis.

The following sections present examples of implementing such models in C and in C++.
Most examples apply to both languages. The exceptions are models that use classes, virtual functions, or templates:
These apply only to C++.

Important:
Unlike C, C++ allows overloading. Because of this, the steps to add a model differ between these two languages.
Specifically, for C++ code, you must make sure that the mangled name of the function in the library matches the mangled name of the function in the actual source code.
The type signatures must match by name. For further information, see Adding a C++ model.
