---
title: "Bazel support"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/bazel-support.html"
content_id: "MyM_e1XN0f5hpetd4DZEFA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:24.443838+00:00"
---

# Bazel support

The Coverity CLI supports capture of builds using the Bazel build tool.
Bazel capture is enabled using the capture.build.bazel configuration option for the
`coverity capture` and `coverity scan` commands.

For example, you might start a scan that uses Bazel by entering a command line such as the following:

```
coverity scan -o capture.build.bazel=true -- bazel build :myproject
```

Important:
You can set configuration options in the configuration file: They don't need to appear on the command line.

For example, if the configuration file contains `capture.build.bazel=true`, then the following
command line would have the same effect as the previous example:

```
coverity scan -- bazel build :myproject
```

General information is presented in "Building with Bazel" in the Coverity Analysis 2026.6.0 User and Administrator Guide.
The following requirements and limitations, also described in Coverity Analysis 2026.6.0 User and Administrator Guide apply:

- Certain limitations apply to Bazel capture for Coverity tools.
  In particular, building with Bazel does not support caching.

  For details, please see "Requirements and limitations".
- The build command supplied to the Coverity CLI must follow the same format as described in
  "Performing the build".

If you provide your own compiler configuration, either via
capture.compiler-configuration.file or via
capture.compiler-configuration.cov-configure, then you may need
to include compiler configurations for Bazel wrappers such as
compiler_wrapper.sh and cc_wrapper.sh,
depending on your project and the platform on which you are running.
