---
title: "Build capture (for compiled languages)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/build-capture-for-compiled-languages-.html"
content_id: "GWABOpS5dT8jyZr1jcEjHQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:46.561733+00:00"
---

# Build capture (for compiled languages)

Build capture is part of the overall analysis workflow for code that you need to compile,
such as C/C++. The Coverity Analysis compiler builds your source code into an
intermediate representation of your software. The intermediate representation is a
binary form of the source code that provides Coverity Analysis with a view of the
operation of your software that is optimized for the efficient analysis of software
issues. Compiling all of your source code with the Coverity Analysis compiler is often
an iterative process. Though Coverity Analysis makes every effort to parse the compiled
code that each supported compiler generates, the nuances of a particular code base
sometimes introduce subtle incompatibilities. Nevertheless, analyses of such code bases
can still produce useful results.

The `cov-build` command wraps the native build to observe native
compiler invocations and operations. It invokes the native build system, and it runs
the `cov-translate` command to translate the native compiler's
command-line arguments to the Coverity Analysis compiler command-line arguments. For
each observed native compiler call, `cov-translate` runs the Coverity Analysis compiler on the same files
with the same arguments, which in turn invokes the
`cov-emit` command to compile the file and outputs the intermediate
representation into the intermediate directory.

Figure 1. Example: Building source with the Coverity Analysis compiler (The Coverity Static
Analysis build)
[image: image]

The Coverity Analysis compiler requires information about build processes, dependencies,
and build-related programs that are only revealed during a native build. Because
`cov-build` parses and compiles each source file, first with the
native compiler and then with the Coverity Analysis compiler, it takes longer to
complete the `cov-build` process than it does to compile your source
code with your native compiler alone.

Note that the simplest way to build source code is to use `cov-build`
because you do not have to modify your native build. However, the
`cov-build` command does not allow you to specify which source
files to compile. Instead, it simply compiles everything the native build compiles
(except for unchanged source code). If you need to specify which source code to compile,
you can invoke the `cov-translate` command directly. This task is more
complex and requires you to modify the native build process, but it might also provide
greater build efficiency. Running `cov-translate` is also the only
supported way to run the Coverity Analysis compiler on AIX systems. For more
information, see Alternative build command: 'cov-translate'.
