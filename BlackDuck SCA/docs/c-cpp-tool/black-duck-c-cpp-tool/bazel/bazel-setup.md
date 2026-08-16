---
title: "Bazel setup"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/bazel-setup.html"
content_id: "KUsit7e57btUfByP7lW10g"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:57.628549+00:00"
---

# Bazel setup

## Modify the WORKSPACE file

Like other Bazel integrations, the Coverity integration has an archive of rules to be
used by the build.

The Black Duck C/CPP tool will attempt to automatically update this file as required
if it hasn't already been modified by the user. If the automatic update fails, the
failure will be logged and the user will need to complete the following steps
manually.

The WORKSPACE (or WORKSPACE.bazel) file defines the root of the Bazel project, and it
needs to be modified to reference the Coverity integration. If you are supplying
your own Coverity installation, the Coverity integration can be found in the
Coverity Analysis installation at:

```
<Coverity Analysis installation path>/bazel/rules_coverity.tar.gz
```

If you are using the mini package provided by Black Duck C/CPP, then by default the
Coverity integration can be found in the Coverity Analysis installation at:

```
<User home>/.blackduck/blackduck-c-cpp/cov-build-capture/bazel/rules_coverity.tar.gz
```

You can remove it from the installation and host it anywhere convenient.

Assuming the integration archive is available on a network share at
`/mnt/network-share/rules_coverity.tar.gz,` append the following
snippet onto your WORKSPACE file:

```
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name="rules_coverity",
    urls=["file:///mnt/network-share/rules_coverity.tar.gz"],
)
  
  
load("@rules_coverity//coverity:repositories.bzl", "rules_coverity_toolchains")
rules_coverity_toolchains()
```

You can use different URLs, depending on whether the integration archive is available
locally, on a file share, or through HTTP. The only part of the kit that is
necessary for this is the integration archive, so it can be placed wherever needed,
independently of the rest of the kit. Bazel can fetch from "file://", "http://" and
"https://" URLs. The "urls" field is a list - multiple URLs can be specified, and
fetching the integration from them will be attempted in order.

## Modify the BUILD file

Unlike the WORKSPACE file, Black Duck C/CPP can't update the BUILD file
automatically. This must be completed by the user.

Bazel uses the BUILD (or BUILD.bazel) file to do the following:

- Mark a package boundary
- Declare what targets can be built in that package
- Specify how to build those targets

The Coverity-Bazel integration needs a new target added that depends on existing
targets to generate a "build description" of all the build commands that would have
been executed in the building of those targets. If you had, for example, a build
with two separate targets that you wanted to capture, the BUILD file would start out
looking something like this:

```
load("@rules_cc//cc:defs.bzl", "cc_binary")​
cc_binary(name="foo", srcs=["foo.cc"])
cc_binary(name="bar", srcs=["bar.cc"])
```

To capture the files (including link files) used in the building of the targets :foo
and :bar (foo.cc and bar.cc, respectively), you would modify the BUILD file to be
something like this:

```
load("@rules_cc//cc:defs.bzl", "cc_binary")
cc_binary(name="foo", srcs=["foo.cc"])
cc_binary(name="bar", srcs=["bar.cc"])
 
load("@rules_coverity//coverity:defs.bzl", "cov_enable_link", "cov_gen_script")
cov_enable_link(
    name = "enable_link",
    build_setting_default = True,
)
cov_gen_script(name="coverity-target", deps=[":foo", ":bar"], enable_link = ":enable_link",)
```

Here is an example using Google's open source abseil-cpp library (<https://github.com/abseil/abseil-cpp>):

Before:

```
package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0

# Expose license for external usage through bazel.
exports_files([
    "AUTHORS",
    "LICENSE",
])
```

After:

```
package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0

# Expose license for external usage through bazel.
exports_files([
    "AUTHORS",
    "LICENSE",
])

load("@rules_coverity//coverity:defs.bzl", "cov_enable_link", "cov_gen_script")
cov_enable_link(
    name = "enable_link",
    build_setting_default = True,
)
cov_gen_script(
    name="cov",
    deps = [
        "//absl/status:statusor",
        "//absl/status:status",
        "//absl/random:bit_gen_ref",
        "//absl/functional:bind_front",
        "//absl/flags:parse",
        "//absl/flags:usage",
        "//absl/flags:flag",
        "//absl/debugging:leak_check",
        "//absl/debugging:failure_signal_handler",
        "//absl/debugging:leak_check_disable",
        "//absl/container:node_hash_set",
        "//absl/container:hashtable_debug",
        "//absl/random:random",
        "//absl/random:seed_sequences",
        "//absl/random:seed_gen_exception",
        "//absl/random:distributions",
        "//absl/container:flat_hash_set",
        "//absl/types:any",
        "//absl/types:bad_any_cast",
        "//absl/container:btree",
        "//absl/types:compare",
        "//absl/cleanup:cleanup",
        "//absl/container:node_hash_map",
        "//absl/container:node_hash_policy",
        "//absl/flags:reflection",
        "//absl/container:flat_hash_map",
        "//absl/container:raw_hash_map",
        "//absl/container:raw_hash_set",
        "//absl/container:hashtablez_sampler",
        "//absl/container:hashtable_debug_hooks",
        "//absl/container:hash_policy_traits",
        "//absl/container:common",
        "//absl/container:hash_function_defaults",
        "//absl/strings:cord",
        "//absl/container:layout",
        "//absl/container:inlined_vector",
        "//absl/hash:hash",
        "//absl/types:variant",
        "//absl/types:bad_variant_access",
        "//absl/hash:city",
        "//absl/container:fixed_array",
        "//absl/container:compressed_tuple",
        "//absl/container:container_memory",
        "//absl/flags:marshalling",
        "//absl/strings:str_format",
        "//absl/numeric:representation",
        "//absl/functional:function_ref",
        "//absl/flags:config",
        "//absl/flags:commandlineflag",
        "//absl/types:optional",
        "//absl/types:bad_optional_access",
        "//absl/utility:utility",
        "//absl/synchronization:synchronization",
        "//absl/time:time",
        "//absl/debugging:symbolize",
        "//absl/strings:strings",
        "//absl/numeric:int128",
        "//absl/numeric:bits",
        "//absl/debugging:stacktrace",
        "//absl/types:span",
        "//absl/memory:memory",
        "//absl/algorithm:container",
        "//absl/meta:type_traits",
        "//absl/algorithm:algorithm",
    ],
    enable_link = ":enable_link",
)
```

## Customization: compilation mnemonics

Which Bazel actions are treated as build commands is determined by the mnemonic of
the action. For now, the only mnemonics that are treated as a build commands by
default are CppCompile, Javac and Compile. These are the mnemonics that the builtin
cc_binary/cc_library rules, the builtin java_binary/java_library rules and the
standard csharp_binary/csharp_library rules use for their compilation actions,
respectively. If you have custom rules that generate actions that should be treated
as build commands, modify the BUILD file again, extending from this:

```
load("@rules_cc//cc:defs.bzl", "cc_binary")
cc_binary(name="foo", srcs=["foo.cc"])
cc_binary(name="bar", srcs=["bar.cc"])
 
load("@rules_coverity//coverity:defs.bzl", "cov_gen_script")
cov_gen_script(name="coverity-target", deps=[":foo", ":bar"])
```

to something like the following:

```
load("@rules_cc//cc:defs.bzl", "cc_binary")
cc_binary(name="foo", srcs=["foo.cc"])
cc_binary(name="bar", srcs=["bar.cc"])
 
load(
    "@rules_coverity//coverity:defs.bzl", 
    "cov_gen_script", 
    "cov_compile_mnemonics"
    )
cov_compile_mnemonics(
    name="extra_mnemonics", 
    build_setting_default=["FirstMnemonic", "SecondMnemonic"]
    )
cov_gen_script(
    name="coverity-target", 
    deps=[":foo", ":bar"], 
    extra_compile_mnemonics=":extra_mnemonics"
    )
```
