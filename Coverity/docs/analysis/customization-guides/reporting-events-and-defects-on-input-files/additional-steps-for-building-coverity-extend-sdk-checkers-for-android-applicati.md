---
title: "Additional steps for building Coverity Extend SDK checkers for Android applications"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/additional-steps-for-building-coverity-extend-sdk-checkers-for-android-applications.html"
content_id: "1T6hwv4cxpNc7aZ~3Ll6vQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:59.783546+00:00"
---

# Additional steps for building Coverity Extend SDK checkers for Android applications

The general workflow uses `cov-emit-java` to emit the files to the
intermediate directory, then runs the custom checkers on the emitted files. The checkers
iterate over the input files to produce the reports.

1. Emit files, such as AndroidManifest.xml, that your checker
   requires to the intermediate directory. Such files must be associated with an
   APK, for example:

   ```
   cov-emit-java --dir myIntDir --android-apk myAPK.apk --input-file AndroidManifest.xml
   ```

   The `--input-file` option is required and can be specified multiple times. The
   `--android-apk` option is required and can only be specified
   once. Descriptions of these command line options are in the `cov-emit-java`
   command description in the Coverity 2026.6.0 Command Reference.
2. Run your custom checker to analyze the input files.
