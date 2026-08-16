---
title: "Adding a C model to emulate memory allocation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-c-model-to-emulate-memory-allocation.html"
content_id: "nR_AE~pta9QsTPIMRsHLbw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:32.496333+00:00"
---

# Adding a C model to emulate memory allocation

Adding a new C-language model named `my_free()`.

1. In the <install_dir>/library/ directory, create a
   new file named my_free.c.
2. In this new source file, create a stub C function that uses the standard
   C-library function `free()` to emulate the behavior of the new
   deallocation function.

   Here is the code for the model:

   ```
   void free(void*);
       
   void my_free(void* x) {
       free(x);
   }
   ```
3. Use the `cov-make-library` command to convert this model
   from its C-code form into the XML form that the analysis engine
   understands.

   Here is a command line that accomplishes the conversion:

   ```
   > cov-make-library --output-file my_free my_free.c
   ```

   The `cov-make-library` command creates a new library
   file whose name and path are specified by the `--output-file` option.
   This file contains the library form of the model, which specifies that
   `my_free()` will deallocate its only argument,
   `x`.

   If you do not use the `--output-file` (or
   `-of`) option, the default output name is
   user_models.xmldb in the config/ directory. If
   user_models already exists, or a file of the
   name you specify already exists, `cov-make-library`
   appends the new model or models to the existing library; otherwise, it
   creates a new library file of the appropriate name.

   Remember:
   When you run `cov-make-library`, you can change the
   directories for temporary storage and for the generated configuration file.
   If you change these directories, you must also specify the location of these
   files when you run `cov-analyze`, so that the analysis
   engine can find the new configuration files.
