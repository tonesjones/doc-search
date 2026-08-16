---
title: "Microsoft Visual C and C++ compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/microsoft-visual-c-and-c-compiler.html"
content_id: "Nvff6XgVvIrQef~pm13m8w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:45.612175+00:00"
---

# Microsoft Visual C and C++ compiler

Because `cov-configure` invokes the native compiler to determine
built-in include paths and built-in preprocessor defines, the Microsoft Visual C and C++
compiler might require additional steps to configure correctly.

The Microsoft Visual C and C++ compiler executable is named `cl.exe`.
Generally, `cl.exe` requires that the path settings include the
location of all required DLLs.

Coverity Analysis can simulate parsing bugs that occur in some versions of Microsoft Visual C
and C++. Supply the correct version of MSVC to the `cov-configure`
command to get the correct `cov-emit` arguments automatically. The
`--typeinfo_nostd` option allows some codebases, which rely on the
typeinfo structure to not be in the std namespace, to compile.

The Coverity compiler supports cross compiling to 64-bit MSVC platforms.
