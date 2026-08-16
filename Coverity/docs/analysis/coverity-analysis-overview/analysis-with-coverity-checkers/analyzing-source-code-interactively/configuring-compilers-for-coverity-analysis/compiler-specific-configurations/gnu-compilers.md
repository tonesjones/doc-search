---
title: "GNU compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gnu-compilers.html"
content_id: "a6CZtGHUXArc5AzoMxUFMA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:41.740024+00:00"
---

# GNU compilers

Coverity Analysis is compatible with most `gcc`-compiled code. This includes support for
`gcc`-specific extensions. For example, Coverity Analysis can compile virtually all of the
Linux kernel, which heavily uses many gcc extensions. Some known `gcc` incompatibilities
include:

- Nested functions are not supported.
- Abbreviated function template syntax is not supported.
- Computed `goto` statements are handled in a very approximate fashion.
- The `-fpermissive` compiler mode is not supported.
- The `__fp16` built-in type is not supported.

Attention:
Mac OS X users, see Building with Xcode.

Coverity Analysis compatibility with modern g++ versions is also good. Older g++ versions
(before 3.0) are far more relaxed in their type checking and syntax, and their
incompatibilities might be difficult to solve. The `--old_g++` option
loosens Coverity Analysis's parsing and type checking enough to let many older code
bases compile. If you specify the compiler version when you run `cov-configure`, this option is in
coverity_config.xml.

Because `cov-configure` invokes the native compiler to determine
built-in include paths and built-in preprocessor defines, the GNU C and C++ compiler
might require additional steps to configure correctly.

To invoke it properly from the command line, the GNU compiler might require additional
`cov-configure` options. In particular, GNU compiler installations
that use a non-standard preprocessor (`cpp0`) path require the GNU -B
option that specifies it:

```
> cov-configure --compiler gcc --comptype gcc -- -B/home/coverity/gcc-cpp0-location/bin
```

If your build explicitly uses the GNU compiler on the command line with either the `-m32`
or `-64` option, also supply the option to the `cov-configure` command.
For example:

```
> cov-configure --compiler gcc --comptype gcc -- -m32
```

On some platforms, `gcc` allows multiple `-arch <architecture>`
options to be specified in a single compiler invocation. `cov-analysis` will only compile and analyze the source once,
as though only the last `-arch` option specified on the command line was
present. If all compiler invocations are not consistent regarding the last architecture
specified on the command line, `cov-analysis` might produce false positive
or false negative results.
