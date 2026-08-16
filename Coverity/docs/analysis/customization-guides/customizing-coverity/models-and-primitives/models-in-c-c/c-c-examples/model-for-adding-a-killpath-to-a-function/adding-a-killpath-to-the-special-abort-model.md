---
title: "Adding a killpath to the 'special_abort()' model"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-killpath-to-the-special_abort-model.html"
content_id: "tmW0PY4Vz1g9cyshGfS0zg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:35.099833+00:00"
---

# Adding a killpath to the 'special_abort()' model

These steps show how to add a new killpath to a function model named
`special_abort()`.

1. In the source file kill.c, create a model named
   `special_abort()`.

   Here is the code for the new model:

   ```
   void special_abort(const char* msg) {
       __coverity_panic__();
   }
   ```
2. Generate a new model for `special_abort()`.

   The new model is to suppress the `RESOURCE_LEAK` defect in
   the following test case, where without the override Coverity would report a
   leak at the assignment of the pointer `*p`:

   ```
   void test() {
       int *p = (int*)malloc(10);
       *p = 0;                    // No defect due to overridden malloc
       special_abort("we are done - no leak");
   }
   ```
3. Use `cov-make-library` to generate the models for the new
   function.

   Use the following command line to build the models from both
   kill.c and
   my_memory_allocators.c:

   ```
   > cov-make-library kill.c my_memory_allocators.c
   ```

   (The my_memory_allocators library is discussed in Example: Override a default C model)
4. Analyze the example and verify there are no defects.

   The following command line performs the analysis:

   ```
   > cov-analyze --dir /tmp/tmp-intermediate
   ```
5. Verify that there are no defects produced by Coverity Analysis
   in any of the *.errors.xml files generated in the current
   directory.

   Important: To add a macro to the library that aborts, you must first tell the
   Coverity compiler to change that macro into a function call. See the
   description of the Coverity compiler directive `#nodef` in
   "Suppressing macro expansion to improve modeling"
   in the Coverity Analysis 2026.6.0 User and Administrator Guide. Alternatively, you can use
   function annotations to specify that all paths through a function are
   killpaths. See Analysis annotations.
