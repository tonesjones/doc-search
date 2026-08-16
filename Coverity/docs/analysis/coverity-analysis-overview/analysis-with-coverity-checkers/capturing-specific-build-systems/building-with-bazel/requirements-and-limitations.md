---
title: "Requirements and limitations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/requirements-and-limitations.html"
content_id: "UCI8xoMKLtGfjRTfCzqghg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:37.537333+00:00"
---

# Requirements and limitations

Builds using Bazel can be captured and analyzed if they meet the requirements shown in
the following table.

|  | Notes |
| --- | --- |
| Bazel version | Bazel versions 7, 8, and 9 are supported with this integration. |
| Host OS | Bazel builds can be captured on the versions of Windows, Linux and macOS that are supported by Coverity Analysis. |
| Source language | - C/C++, C# and Java builds can be captured. C# capture is not supported on macOS. - Java capture is supported, but the minimum supported version is Java 1.8. |
| Bazel build rules | Bazel capture has been tested with the following rules:  - C/C++: `cc_binary/cc_library` (built in to   Bazel) - Java: `java_binary/java_library` (built in   to Bazel) - C#: `csharp_binary/csharp_library` (from   [rules_dotnet](https://github.com/bazelbuild/rules_dotnet))   To enable support for other rules, see Customization: Compilation mnemonics. |
| Compilers | Compilers for Coverity Analysis are supported, but all compilers must be accessible and runnable on the host system: Remote Bazel builds are supported, but all remote machines must be using the same platform as the host. |
| Caching | Building with Bazel does not support caching. |
