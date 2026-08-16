---
title: "Java and Kotlin build capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-and-kotlin-build-capture.html"
content_id: "zQTGNS_cyc5cVr4KyUCzRQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:54.634634+00:00"
---

# Java and Kotlin build capture

The `cov-build` command works somewhat differently for the Java and Kotlin
compilers (than for the C, C++, and C# compilers). In addition to gathering and
compiling source files, the `cov-build` command for Java and Kotlin also
collect compiled files and any JAR files or class files in the classpath.

For Java and Kotlin, the command also runs the compilers in debug mode so that Coverity
Analysis can analyze the compiled code. This automatic behavior is equivalent to running
the `javac -g` command prompt or using the
debug="true" property setting in an Ant compile task.

Note: You must use supported compilers when using `cov-build` with Java and Kotlin.
For details, see "Supported languages, compilers, and frameworks for Coverity
Analysis" in the Coverity 2026.6.0 Installation and Upgrade Guide.

You can use the `--config` option to `cov-configure` and
`cov-build` to establish and maintain separate configuration
directories for each language.

The `cov-build` command expects the build to use the configured Java and Kotlin
compilers. Compile commands with different pathnames will not be analyzed because
`cov-build` cannot identify the compiler version. So, consider which
compilers the build scripts and tools might invoke. For example, `ant`
can refer to `$JAVA_HOME` or a default pathname (not
`$PATH`) to find the `java` command. When using
`ant` on the Mac OS, you need to set the `$JAVA_HOME`.
Otherwise, the Mac OS will select something other than what
`cov-configure` will set. If compiler pathnames are unknown, then a
template must be configured.

Note: When running 64-bit Coverity Analysis tools against a 32-bit Java SDK,
`cov-build` may fail to capture compilations. Use
`--instrument` to work around the issue.

See Build capture example.
