---
title: "Replace a built-in model in order to reduce the number of defect reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/replace-a-built-in-model-in-order-to-reduce-the-number-of-defect-reports.html"
content_id: "WTCiL7JQXGBKLqUwNpMINA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:33.153940+00:00"
---

# Replace a built-in model in order to reduce the number of defect reports

Adding a model to the Coverity Analysis configuration can also be a
way to reduce the number of defect reports; in particular, false positive reports.

To continue with the memory-management example introduced in Adding a C model to emulate memory allocation, suppose that the C-library
method `free()` has been overridden and is now part of a special allocation
scheme. You no longer want calls to `free()` to be reported; instead, you
want the function `free()` to have no influence on the analysis.

Here is an update to my_free.c that accomplishes this:

```
void free(void* x) {
    // Do nothing.
}

void my_free(void* x) {
    __coverity_free__(x);
}
```

The model source has changed in two ways:

1. We implemented a model of `free()` that does nothing.

   User models always
   override any configuration shipped by Coverity and any models that are
   automatically derived during interprocedural analysis. Thus, adding this model
   definition suppresses the default analysis of `free()`.

   As a
   consequence, all associated use-after-`free()` defect reports are
   suppressed as well.
2. We also updated the definition of `my_free()`. The original implementation of
   `my_free()` depended on the standard C-library
   `free()` implementation and Coverity's analysis of it (see
   Adding a C model to emulate memory allocation). Because we have now
   removed that behavior for the model of `free()`, we use instead the
   modeling primitive `__coverity_free__()`. This particular primitive
   indicates that its argument, *`x`,* must not be dereferenced
   after the primitive has been called.

You can regenerate the model library, my_free, by invoking
`cov-make-library`, as shown in Adding a C model to emulate memory allocation or Adding a C++ model to refine analysis of memory allocation.
