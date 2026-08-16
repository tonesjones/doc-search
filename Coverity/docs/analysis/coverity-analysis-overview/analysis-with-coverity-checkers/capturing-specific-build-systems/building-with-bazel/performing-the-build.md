---
title: "Performing the build"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/performing-the-build.html"
content_id: "wKlaIV0OriOj0UaKjKMZOQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:40.115980+00:00"
---

# Performing the build

The build can be captured by running the `cov-build` command with the
`--bazel` flag. The invocation will look something like this:

```
cov-build --dir /path/to/idir --bazel bazel build //my-bazel-target
```

Notice the --bazel option. Wrapping your Bazel build with cov-build
--bazel causes your build to be run with a Bazel aspect that generates a
JSON description of each target given in your Bazel command instead of performing the
original build, and then replays the compilations in those files for analysis by
Coverity. By default, this uses the -j auto option. You can set a
specific count value by using -j <count> when you invoke the
cov-build command. When running cov-build --bazel, bazel will
not produce all of the original build artifacts; this is intentional, as most build
artifacts are not required for analysis, and not producing artifacts that the
analysis does not depend on will speed up capture of the build. If the original
build artifacts are necessary for later use, the original bazel command must be run
without involvement of cov-build, either before or after running cov-build.

In the `bazel build` command:

- `bazel` can be the name of any Bazel executable, but must be the first
  argument that follows the --bazel option.
- Whatever arguments are normally given as startup arguments (between `bazel`
  and `build`) or build arguments (after `build`, other
  than targets) that are normally given for the native build should also be included
  in this `bazel build` command.
