---
title: "Adding a C++ model to refine analysis of memory allocation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-c-model-to-refine-analysis-of-memory-allocation.html"
content_id: "VTeNP_Sll0DUtoCU3VrTNg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:37.739981+00:00"
---

# Adding a C++ model to refine analysis of memory allocation

Adding a new C++-language model named `myAllocatorMethod()`.

1. In the <install_dir>/library/ directory, create a
   new file named MyClass.cpp.
2. In the MyClass.cpp file, create a member function named
   `myAllocatorMethod()`.

   Here is the code for the new method:

   ```
   class MyClass {
   public:
       void *myAllocatorMethod(size_t size) {
           return __coverity_alloc__(size);
       }
   };
   ```

   It is possible to create a function model for certain member functions; you
   do not have to create a model that includes all member functions. Member
   functions without explicit models will produce derived models if the source
   code is available.

   This model uses a *modeling primitive,*
   `__coverity_alloc__()`. A primitive is not executable code, but
   when it appears in a model it instructs Coverity Analysis
   how to analyze (or refrain from analyzing) the function being
   modeled.
3. Use the `cov-make-library` command to convert this model
   from its C++ code form into the XML form that the analysis engine
   understands.

   Here is a command line that accomplishes the conversion:

   ```
   > cov-make-library --output-file MyClass MyClass.cpp
   ```

   For more information about creating library files, see
   Adding a C model to emulate memory allocation.
