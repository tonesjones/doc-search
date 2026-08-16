---
title: "C, C++, C#, and Visual Basic build capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-c-c-and-visual-basic-build-capture.html"
content_id: "JaiU1Of8WiUS_ITAT7dpFA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:53.316079+00:00"
---

# C, C++, C#, and Visual Basic build capture

For C, C++, C#, and Visual Basic source code, after the compiler calls have been
intercepted, `cov-build` captures the compiler command line and other
information and invokes cov-translate to translate the native command line into one appropriate for
`cov-emit`, `cov-emit-cs`, or
`cov-emit-vb`, which in turn parses and emits the code. Before
running `cov-build`, you need to configure your compiler (such as gcc
or msvc) by using the `cov-configure` command.

For C# and Visual Basic only, if an ASP.NET 4 and earlier Web application is detected,
`cov-build` will attempt to run
Aspnet_compiler.exe on the Web application. The output of
Aspnet_compiler.exe is required by the C# security
checkers.

Note: C# and Visual Basic build capture is supported on Windows and Linux platforms.

The `cov-build` command creates a log file called
build-log.txt in the intermediate directory. This log file
shows each command that is intercepted, including compiler invocations. For each
compiler invocation, the call to `cov-translate` and
`cov-emit` are shown, along with any parsing errors and any other
compilation errors.

The `cov-build` command intercepts compiler invocations for
single-threaded builds and parallel builds on a single machine. Distributed builds,
which use remote procedure calls or some other protocol to invoke builds or compilations
on several machines, cannot be virtualized directly with `cov-build`.
Contact Coverity support for assistance.

On UNIX, `cov-translate` is invoked before each native compiler
invocation. On Windows, `cov-translate` is invoked after each native
compiler invocation.

The `cov-build` command expects the configured C and C++ compilers to be
those used by the build. The analysis might be skewed if different compiler versions are
used. So, consider values that the build scripts and makefiles might define for
`$PATH`, `$CC`, and so on. If compiler pathnames are
unknown, configure a template.

See Build capture example.
