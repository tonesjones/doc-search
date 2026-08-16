---
title: "Capture configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/capture-configuration.html"
content_id: "iFnAarstrAJY7vse7rpQkw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:00.757615+00:00"
---

# Capture configuration

The following table describes the capture configuration; subsections describe the fields
that make up the Capture type.

| Key | Type | Description |
| --- | --- | --- |
| `build` | Build configuration | Specifies that build capture should be used to capture the project and provides the build configuration to use. If not specified and the project directory contains compiled source files, automatic build capture will be used to capture compiled source files in the project directory.  For compiled languages only: Java, C#, C, C++, Objective-C, Objective-C++, Visual Basic.  This key is mutually exclusive with the `cov-translate` key. |
| `build-command-inference` | Boolean | Specifies whether to enable or disable build command inference. If build command inference is disabled and no build command is provided, no attempt at build capture is made.  For compiled languages only: Java, C#, C, C++, Objective-C, Objective-C++, Visual Basic.  Default: `true`. |
| `compiler-configuration` | Compiler configuration | Specifies which compilers to configure. CAUTION:  If a setting is supplied for `compiler-configuration`, then the Coverity CLI *will not configure* any other compilers that normally it might configure automatically. A possible outcome of this behavior is that a large number of files in the project will not be captured or analyzed. This might not be an intended or a desirable result. In order to capture and analyze all of the expected files when you use the `compiler-configuration` option, make sure that all of the compilers are explicitly configured for the languages and files that you wish to analyze. For an overview, see "Configuring compilers for Coverity Analysis" in the Coverity Analysis 2026.6.0 User and Administrator Guide. For detailed information, see the `cov-configure` command in the Coverity 2026.6.0 Command Reference.  Default: Configure template (default) compilers   This key is mutually exclusive with the `languages` key. |
| `cov-translate` | Coverity translate configuration | Specifies that `cov-translate` capture should be used to capture the project, and provides the `cov-translate` configuration to use. Attention: For the Coverity CLI, `cov-translate` is supported only on macOS systems.  This key is mutually exclusive with the `build` key. |
| `delete-stale-tus` | Boolean | Enables (default) or disables the deletion of all stale translation units (TUs) from the intermediate directory after a capture completes.   - `true` - When a capture completes, Coverity deletes all stale TUs from the intermediate   directory. - `false` - Stale TUs are not deleted after a   capture completes.   Default: `true` |
| `encoding` | string | Specifies the encoding to use when parsing and emitting the source files in C, C++, JavaScript. Default: `US-ASCII` |
| `emit-complementary-info` | Boolean | Records additional information during the emit process needed for the compliance checkers. If a `coding-standards` configuration is present, this flag is automatically set to `true`.  Default: `false`. |
| `failure-threshold-percent` | integer | (Optional) Sets a threshold that is the minimum percentage of files that must be captured in order to proceed with analysis. This value applies only to files that the analysis attempted to capture. Files that are ignored because of exclusion or because they are unsupported are not included in this calculation.  If the capture rate is not met, `coverity capture` or `coverity analyze` can exit and report an error. |
| `files` | Files configuration | Specifies which specific non-compiled files to include or exclude for capture. Default: All relevant files are captured. |
| `force-dependency-resolution` | Boolean | When `true`, forces Coverity to resolve Maven, Gradle, and MSBuild dependencies even if this seems not to be needed, based on the detected source languages in the project. Default: `false` |
| `import-scm` | Import SCM configuration | Specifies how to import data about source file changes from the current source control management (SCM) system. The valid values are as follows:  - `"git"` - `"perforce"` - `"plastic"` - `"plastic-distributed"` - `"svn"`   Note: This key is mutually exclusive with the Connect configuration `scm` key. Both serve the same purpose, but we recommend that you upgrade to `import-scm`, as it is more general and more widely applicable. |
| `languages` | Language configuration | Specifies which languages to include or exclude for capture. Default: all languages are included This key is mutually exclusive with the `compiler-configuration` key. |
| `minimal-classpath-emit` | Boolean | Specifies whether to limit the group of emitted JAR files to those needed for compilation of the Java files. When this option is `false`, the default behavior is to emit all the JAR files in the classpath regardless of whether they are referenced by a Java file in the compilation. Default: `false` |
| `record-with-source` | Boolean | Specifies whether to do a complete capture or a record with source capture. Applies to Java, C, C++, C#, Visual Basic, JavaScript, and TypeScript only.  Default: `false` |
| `security-da` | Boolean | Enables or disables security dynamic analysis. If set to `true` (the default), security dynamic analysis runs as part of the capture step. If set to `false`, security dynamic analysis is not run.  Default: `true` |

In this section:

- Build configuration
- Compiler configuration
- Coverity translate configuration
- Files configuration
- Language configuration
- Parallel translate configuration
- Web archive configuration
