---
title: "Building with Bazel"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/building-with-bazel.html"
content_id: "jsxpzQagFU18qvEE1rqG2g"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.941756+00:00"
---

# Building with Bazel

If you run Coverity 2024.3.0 or a newer version, you can use the Bazel build tool.

Before you begin to configure Bazel, please see the
["requirements and limitations"](https://documentation.blackduck.com/bundle/coverity-docs/page/coverity-analysis/topics/building_with_bazel.html#ariaid-title2) for Coverity and Bazel.

**To enable the Coverity-Bazel integration:**

1. Follow the steps in the Coverity documentation:
   See ["Building with Bazel"](https://documentation.blackduck.com/bundle/coverity-docs/page/coverity-analysis/topics/building_with_bazel.html) in the
   *Coverity Analysis User and Administrator Guide*.

   You will need to modify the Bazel build file and either the workspace file or the module file.
   More steps are needed if you use Bazel 7 or a newer version.
2. Add a configuration file to the root of your project (for coverity.conf) or your working directory
   (for a CLI-based configuration file) and configure it for Bazel support.

   Here is an example of such a configuration file, in JSON format:

   ```
   {
       "type": "Coverity configuration",
       "format_version": 1,
       "format_minor_version": 7,
       "settings": {
           "cov_run_desktop": {
               "build_options": [
                   "--bazel"
               ],
               "build_cmd": [
                   "bazel",
                   "build",
                   "--registry=file:///<myLocn>/../../cov-registry",
                   "--registry=http://<myURL>/../packages/bazel/central-registry",
                   ":coverity_build"
               ]
           },
           "ide": {
               "build_strategy": "CUSTOM"
           }
       }
   }
   ```

   If you already have a project-specific coverity.conf file, add the `"settings"`
   fields to it.
