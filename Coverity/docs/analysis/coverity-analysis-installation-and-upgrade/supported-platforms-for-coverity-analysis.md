---
title: "Supported platforms for Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/supported-platforms-for-coverity-analysis.html"
content_id: "El1~l~68M9F3Tm2Pak2xVg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:59.813047+00:00"
---

# Supported platforms for Coverity Analysis

This section describes platform support for Coverity Analysis. Table 1 provides a bird's eye view of platform support indexed
by language. The table lists supported languages and, for each language, a general
listing of the platforms on which the language is supported. For detailed support
information on any of the listed platforms, click the corresponding link in the
"Supported platforms" column.

For detailed information on language support, including language version numbers, see the
section "Coverity language support" in the Coverity Analysis 2026.6.0 User and Administrator Guide.

Note:

Virtual machine (VM) implementations of supported platforms are also supported if you
use FlexNet licensing or a default license that is not node-locked to a particular
host machine (see Supported platforms for Extend SDK and FlexNet licensing for more
information).

Table 1. Platform support matrix indexed by language

| Language analysis capability | Supported platforms | Notes |
| --- | --- | --- |
| Apex | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | Coverity supports the execution of PMD analysis (through Coverity Analysis for Apex) and requires Oracle Java SE Runtime Environment 8 (JRE 8) platform support. |
| C/C++ | AIX (see Table 2)  FreeBSD (see Table 3)  Linux (see Table 4)  macOS (see Table 5)  Solaris (see Table 6)  Windows (see Table 7) | Compliance analysis is available with all C/C++ analysis platforms except AIX. |
| C# | Linux (see Table 4)  Windows (see Table 7) |  |
| CUDA | Linux (see Table 4)  Windows (see Table 7) | Compliance and C++ analysis is available with all CUDA analysis platforms. |
| Dart | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | Dart support is provided by the Sigma engine. |
| Fortran | Linux (see Table 4)  Windows (see Table 7) |  |
| Go | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) |  |
| Java | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | Coverity supports the execution of Web application security analysis (through Coverity Analysis for Java). When performing Java code analysis, Coverity requires Oracle Java SE Runtime Environment 8 (JRE-8) as its executable platform. This requirement is unrelated to your choice of Java compiler.  For information about supported Java compilers or about invoking a Java compiler with `cov-build`, see section "Java Compilers."  Coverity does not support the Oracle JRockit JDK. |
| Kotlin | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) |  |
| Objective-C/ Objective-C++ | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | Compliance and analysis is available for Linux, macOS, and Windows platforms. Coverity supports Objective-C and Objective-C++ for Clang compilers. For information about supported platforms for Clang compilers, see section "C/C++ Compilers".  Coverity does not support Objective-C or Objective-C++ for gcc compilers. |
| PHP | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | PHP support is provided by the Sigma engine. |
| Python | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) |  |
| Ruby | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) |  |
| Rust (beta) | Linux (see Table 4) macOS (see Table 5) Windows (see Table 7) | Rust support is a beta feature. Only Cargo-based builds are supported. |
| Scala | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | Scala support is provided by the Sigma engine. |
| Sigma-based, multi-language analysis | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | Coverity invokes the Sigma engine on supported platforms, to gain additional language, file format and software issue capabilities |
| Swift | Linux (see Table 4)  macOS (see Table 5)  Windows (see Table 7) | Swift support is provided by the Sigma engine. |
| Visual Basic | Windows (see Table 7) |  |

Table 2. AIX: Coverity Analysis platform support

| Platform version | C/C++ | Notes |
| --- | --- | --- |
| AIX 7.1 on PowerPC | Yes | Only manually integrated build capture is supported because the `cov-build` command is not available, and it is necessary to run `cov-analyze` on a fully supported platform. For details, see the references to AIX in the *Coverity Analysis User and Administrator Guide*. |

Table 3. FreeBSD: Coverity Analysis platform support

| Platform version | C/C++ analysis | Notes |
| --- | --- | --- |
| FreeBSD 14 (32-bit and 64-bit x86) | Yes |  |
| FreeBSD 15 (64-bit x86) |  |

Table 4. Linux: Coverity Analysis platform support

| Platform version | Apex analysis | C/C++ analysis | C# analysis | Go analysis | Java analysis | JavaScript, TypeScript analysis | Python, Ruby analysis | Kotlin analysis | Objective-C/C++ analysis | CUDA analysis | Fortran analysis | Sigma-based analysis | Rust analysis | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Linux Kernel 2.6.32+ (32-bit) with glibc 2.18 or later (32-bit) on x86 |  | Yes |  |  |  |  |  |  | Yes |  |  |  |  |  |
| Linux Kernel 2.6.32+ (64-bit) with glibc 2.18 or later (64-bit) on x86_64 | Yes | Yes | Yes | Yes |  | Yes | Yes | Yes | Yes |  | Yes |
| Linux Kernel 2.6.32+ (64-bit) with glibc 2.18 or later (64-bit) on arm64 |  |  |  |  |  |
| Linux Kernel 2.6.32+ (64-bit) with glibc 2.28 or later (64-bit) on x86_64 |  |  |  |  |  | Yes |  |  |  |  |  | Yes |  |  |
| Linux Kernel 2.6.32+ (64-bit) with glibc 2.28 or later (64-bit) on arm64 |  |  |  |  |  |  |  |  |  |  |  | Yes |  |  |

Table 5. macOS: Coverity Analysis platform support

| Platform version | Apex analysis | C/C++ analysis | C# analysis | Go analysis | Java analysis | JavaScript, Kotlin, Python, Ruby, TypeScript analysis | Objective-C/C++ analysis | Sigma-based analysis | Rust analysis | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| macOS 15 on Intel | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |  | On Intel: Build capture requires Xcode (*with command line tools*) 12 - 26 in order to function. Please ensure `xcodebuild -version` runs without error.  On Apple Silicon: Build capture requires both Rosetta 2 and Xcode (*with command line tools*) 12 - 26 in order to function. Please ensure `xcodebuild -version` runs without error.  **Deprecation notice:** Support for macOS on Intel (`macosx`) is deprecated as of 2025.12.0 and will be removed in 2026.12.0.  **Deprecation notice:** Support for macOS 14 is deprecated as of 2026.6.0 and will be removed in a future release.  Rust is supported on Apple Silicon only. It is not supported on Intel. |
| macOS 15 on Apple silicon | Yes |
| macOS 16 on Intel |  |
| macOS 16 on Apple silicon | Yes |
| macOS 26 on Intel |  |
| macOS 26 on Apple silicon | Yes |

Table 6. Solaris: Coverity Analysis platform support

| Platform version | C/C++ analysis | Notes |
| --- | --- | --- |
| Solaris 11.4 (64-bit) on x86_64 | Yes |  |
| Solaris 11.4 (64-bit) on SPARC |

Table 7. Windows: Coverity Analysis platform support

| Platform version | Apex analysis | C/C++ analysis | Go analysis | Java analysis | C#/Visual Basic analysis | JavaScript, Kotlin, Python, Ruby, TypeScript analysis | Objective-C/C++ analysis | CUDA analysis | Fortran analysis | Sigma-based analysis | Rust analysis | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Windows 11 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Coverity Analysis for C# and Visual Basic supports analysis of programs compiled by the Visual C# compiler (`csc.exe`) and Visual Basic compiler (`vbc.exe`) from .NET Framework versions 3.5 SP1 and 4.5.2-4.8. |
| Windows Server 2022 | Coverity Analysis for C# and Visual Basic supports analysis of programs compiled by the Visual C# compiler (`csc.exe`) and Visual Basic compiler (`vbc.exe`) from .NET Framework versions 3.5 SP1 and 4.5.2-4.8. Coverity Analysis is not supported on 'Server Core' installations at this time. |
| Windows Server 2025 |
