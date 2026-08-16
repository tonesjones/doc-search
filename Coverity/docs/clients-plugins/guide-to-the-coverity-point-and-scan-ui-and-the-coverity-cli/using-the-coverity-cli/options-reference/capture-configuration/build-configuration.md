---
title: "Build configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/build-configuration.html"
content_id: "p6oSL4MXv~fFeTcuoqE5Cg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:01.397805+00:00"
---

# Build configuration

The following keys can be defined for compiled languages only: Java, C#, C, C++, Objective-C,
Objective-C++, Visual Basic.

| Key | Type | Description |
| --- | --- | --- |
| `aspnet-compiler` | Boolean | Specifies whether to enable or disable the automatic invocation of `Aspnet_compiler.exe` for any ASP.NET 4 and earlier Web applications that are detected in the build. The output of `Aspnet_compiler.exe` is required by the C# and Visual Basic security checkers. |
| `bazel` | Boolean | Specifies whether to enable Bazel capture. Default: `false` |
| `build-command` | string | The build command to invoke when using build capture to capture the project. A build command specified on the command line will override this setting.  Note: Invoking `coverity capture` without specifying a --build-command captures all files analyzed by Sigma, along with those analyzed by Coverity Analysis. |
| `clean-command` | string | The clean command will be invoked prior to doing build capture to capture the project. |
| `cov-build-args` | array of strings | Additional arguments to pass to `cov-build` when doing build capture. |
| `defer-decomp` | Boolean | Specifies whether the build should only record the decompilations of byte code during the build and not attempt to decompile and emit the byte code. During the analysis phase, `cov-build` will be rerun with --replay-decomp to decompile and emit the byte code. |
| `instrument` | Boolean | Specifies whether to use the instrumentation mode instead of the debugger. For certain builds, this configuration can significantly improve build times. This setting is applicable only on Windows. |
| `parallel-translate` | Parallel translate configuration | Specifies how to parallelize translation of C and C++ code. |
| `propagate-build-failure-status` | Boolean | Specifies whether the Coverity CLI should exit with the same status as the build command when the build fails. Default: `false` |
| `scan-transparency` | Boolean | Specifies whether to enable the collection of scan transparency data for build capture. This setting must be enabled if the Coverity Connect instance has `scan.transparency.enabled=true` in its configuration. For more information, see "Enabling collection of scan transparency data" in the Coverity Platform 2026.6.0 User and Administrator Guide.  Default: `true` |
