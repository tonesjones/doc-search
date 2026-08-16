---
title: "Model for resource leaks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/model-for-resource-leaks.html"
content_id: "LbeX7oiHIIGbqn13vMCVeg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:57.332197+00:00"
---

# Model for resource leaks

To model a resource leak, you can use the `open()` and
`close()` methods of the `Resource_LeakPrimitives`
class.

The following steps show how to add models for detecting resource leaks to a class called
`MyResource`.

1. Import the `Resource_LeakPrimitives` class into your user model
   source file, and create the custom ("user") models for the resources
   that need to be tracked during the analysis.

   For example, you might use the
   following code:

   ```
   import com.coverity.primitives.Resource_LeakPrimitives;
   public class MyResource {

       public MyResource() {
           com.coverity.primitives.Resource_LeakPrimitives.open(this);
       }
       
       public void close() {
           com.coverity.primitives.Resource_LeakPrimitives.close(this);
       }

   }
   ```
2. Generate the model file.

   For example, if this is to be a quality checker, the
   following command line would generate the model file correctly:

   ```
   > cov-make-library --output-file user_models --disable-default --quality MyResource.java
   ```

   Note: The combination of the `--disable-default` and
   `--quality` options limits the generation of models to those
   used by quality checkers.

   The user_models library can now analyze other packages
   for `MyResource` leaks.
3. Use the new model during analysis.

   For example, the following command line
   launches such an analysis:

   ```
   > cov-analyze --dir <intermediate_directory> --user-model-file user_models
   ```

For more information about modeling resource leaks, see the descriptions in the Coverity 2026.6.0 Checker Reference of models to use with the "USE_AFTER_FREE"
and "RESOURCE_LEAK" checkers.
