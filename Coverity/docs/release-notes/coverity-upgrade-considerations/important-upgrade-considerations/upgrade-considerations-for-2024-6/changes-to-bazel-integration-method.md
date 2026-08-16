---
title: "Changes to Bazel integration method"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changes-to-bazel-integration-method.html"
content_id: "CAWf2Tre9k~yUYrd08JxFw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:56.058063+00:00"
---

# Changes to Bazel integration method

The rule-based method of integrating Coverity Analysis with Bazel has been dropped in
favor of a simpler method. To continue capturing Bazel projects, you must make the
following changes:

1. Remove all references to the Coverity integration from your Bazel
   `BUILD` files, but not from your `WORKSPACE` or
   `MODULE.bazel` files. Your `BUILD` file should
   currently have targets similar to the following:

   ```
   cov_gen_script(name="my-coverity-target", deps=["//my-bazel-target", "//my-second-bazel-target"])
   ```

   Remove
   all such targets. These targets are now non-functional and will generate an error
   directing you to the documentation.
2. Replace the `cov_gen_script` target in the Bazel command you pass to
   `cov-build` with the actual targets that normally build the code
   you want to capture. You will change the `cov-build` command from
   something like `cov-build <...> --bazel bazel build
   :my-coverity-target` to something like `cov-build <...>
   --bazel build //my-bazel-target //my-second-bazel-target`.

**Example**

The following example illustrates the changes you would make for an existing project.
Let's assume the existing project has the following WORKSPACE file, BUILD file, and
capture (`cov-build`) command:

**Existing WORKSPACE file**

```
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name="rules_coverity",
    urls=["file:///path/to/coverity/installation/bazel/rules_coverity.tar.gz"]
)
load("@rules_coverity//coverity:repositories.bzl", "rules_coverity_toolchains")
rules_coverity_toolchains(register_empty_cpp_toolchain=False)
```

**Existing BUILD file**

```
load("@rules_cc//cc:defs.bzl", "cc_binary")
cc_binary(name="main", srcs=["main.c"])

load("@rules_coverity//coverity:defs.bzl", "cov_gen_script")
cov_gen_script(name="coverity_target", deps=[":main"])
```

**Existing capture (`cov-build`) command**

```
cov-build --dir /path/to/idir --bazel bazel build :coverity_target
```

**Changes**

The changes you would have to make to this project are as follows:

1. Leave the WORKSPACE file as is.
2. Update the BUILD file to read as
   follows:

   ```
   load("@rules_cc//cc:defs.bzl", "cc_binary")
   cc_binary(name="main", srcs=["main.c"])
   ```
3. Update the capture (`cov-build`) command to read as
   follows:

   ```
   cov-build --dir /path/to/idir --bazel bazel build :main
   ```
