---
title: "Detecting parse warnings, parse errors, and build failures"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/detecting-parse-warnings-parse-errors-and-build-failures.html"
content_id: "sXIMgSLWwDBAzxjNhLCPVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:00.937435+00:00"
---

# Detecting parse warnings, parse errors, and build failures

Different incompatibilities can occur between differing dialects of C and especially C++,
which result in parse errors and the `cov-build` command compiling less
than all of the source code. You do not need all of the source code compiled to analyze
the code for defects. However, the `cov-analyze` command analyzes only
the files that `cov-build` was able to compile successfully.

The `cov-build` command, by default, is considered to be successful if
it compiles 95% or more of the compilation units. You can change this percentage with
the `--parse-error-threshold` option. For example, if you want
`cov-build` to return without a warning only if 100% of the code
compiles, add the following option to the `cov-build` command:

```
cov-build --dir <intermediate_directory> --parse-error-threshold 100
```

The more compilation units that you can compile without parse errors, the more code you
can analyze. To improve the analysis, you can fix or work around many or all of the
parse errors.

Sometimes the compiler can recover from a parse error. When the compiler recovers from an
error, the compilation unit is compiled successfully, but the function that has the
parse error cannot be analyzed. You can see these warnings (as RW.* checkers) in the
Coverity Connect when you use the `--enable-parse-warnings` option to the
`cov-analyze` command.
To see cases when the compiler could not
recover from errors, you should also specify the `--enable PARSE_ERROR`
option to `cov-analyze`.

A variety of problems found by the Coverity compiler are called parse warnings, which you can
see in the Coverity Connect (as PW.* checkers) when parse warnings are enabled. Parse
warnings can show simple problems in the code, or can be signs of deeper defects. You
can change which parse warnings are exposed as defects by creating a configuration file.
A sample file is provided at
<install_dir>/config/parse_warnings.conf.sample. For more
information, see Coverity 2026.6.0 Command Reference.

If the compiler finds non-standard code, and it can infer what is intended by that code,
the compiler generates a semantic warning, which you an see in the Coverity Connect (as
SW.* checkers) when parse warnings are enabled.

The `cov-build` command returns a non-zero exit code when either there
is a fatal error while attempting to initialize the `cov-build` state
before launching the command, or when there is a non-zero exit code from the build
command specified on the command line. In the case that there are build failures due to
incompatibilities between the Coverity Analysis compiler and the source code being
analyzed, if the error does not cause the native compiler to fail and the build to exit,
`cov-build` will not exit with a non-zero status code. You can
change this behavior by using the option `--return-emit-failures`.

For details about how to handle and resolve parsing incompatibilities, see Compiler-specific configurations.
