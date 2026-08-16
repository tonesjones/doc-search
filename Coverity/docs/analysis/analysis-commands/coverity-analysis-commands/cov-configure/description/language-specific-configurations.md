---
title: "Language-specific configurations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/language-specific-configurations.html"
content_id: "oNdbP4nNLQpIGfs_jGJD2w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:17.452474+00:00"
---

# Language-specific configurations

The following sections explain build capture and buildless capture configurations for
each supported language.

## Apex file capture

The `cov-configure --apex` command will be performed automatically. See the
`coverity capture` command for capturing Apex files. By default,
`cov-configure --apex` configures file capture for files with the
`*.cls`, `*.tgr`, and `*.page`
filename extensions.

## C/C++ compiler and build capture configuration

In general, for C/C++ `cov-configure` tries to make an intelligent
guess as to the native compiler's built-in macro definitions and system include
directories. For some compilers, such as gcc, there are command line arguments that
reveal this information, and `cov-configure` invokes the native
compiler to discover this information. For some compilers, there is no standard way
of getting this information, so `cov-configure` tries several
methods to gather this information. However, these methods are not perfect and
sometimes a configuration is generated that is incomplete or incorrect, with the
result that some obscure parsing error occurs during the parsing of some source file
or header file. Some manual configuration could be necessary. See the compiler
information in the Coverity Analysis 2026.6.0 User and Administrator Guide.

Because the `cov-configure` command invokes the native compiler to
determine its built-in macro definitions and the system include directories, you
must run it in an environment that is identical to the one in which your native
compiler runs. Otherwise, the emulation will be inaccurate.

## CUDA build capture configuration

Use the `cov-configure --cuda` command to configure build capture
for CUDA.

## C# build capture configuration

Use the `cov-configure --cs` command to configure build capture for C# source code.

## Clang build capture configuration

Use the configuration, `cov-configure --clang`.

## Dart buildless capture configuration

Use the template configuration `cov-configure --dart` syntax to enable Dart buildless capture.

By default, `cov-configure --dart` configures buildless capture for files with the *.dart filename extension.

You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option
with the `coverity capture` CLI command.

## Go build capture configuration

Use the `cov-configure --go` command to configure build capture for Go source code.

## Java build capture configuration

Use the `cov-configure --java` command to configure build capture for Java source code.

The Java template configuration also enables buildless capture for the following
file types:

- You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option with the
  `coverity capture` CLI command.
- JavaServer Pages (JSPs) for files with the .jsp and
  .jspx extensions. The buildless capture of
  JSPs can be disabled by using the `--no-jsp` option with
  the `cov-configure` command.
- Java Android files that are needed by Coverity Analysis, including the
  manifest (AndroidManifest.xml) and the layout
  resource files. The buildless capture of Java Android files can be
  disabled by using the `--no-android` option along with
  the `cov-configure` command.

For information about other compilers, see Friend compilers.

## Java buildless capture configuration

Use the template configuration, `cov-configure --java-buildless` command
syntax to enable Java buildless capture.

The generated configuration matches Java source files (such as *.java).
When using the configuration with the `coverity capture --compiler-config-file` command, Coverity Analysis
will recursively search the capture directory for matching Java source files.
You can customize the match pattern by using the --file-glob option and --file-regex options along with the specified pattern.

The Java filesystem template configuration also enables buildless capture for the
following file types:

- You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option with the
  `coverity capture` CLI command.
- JavaServer Pages (JSPs) for files with the .jsp and
  .jspx extensions. The buildless capture of
  JSPs can be disabled by using the `--no-jsp` option with
  the `cov-configure` command.
- Java Android files that are needed by Coverity Analysis, including the
  manifest (AndroidManifest.xml) and the layout
  resource files. The buildless capture of Java Android files can be
  disabled by using the `--no-android` option along with
  the `cov-configure` command.

Note:
It is an error to enable Java buildless capture and also Java build capture (using the
`--java` option). Any pre-existing Java build configuration must
be deleted before buildless capture is configured.
See also Friend compilers.

## JavaScript-related buildless capture configuration

Use the template configuration `cov-configure --javascript` command
syntax to enable JavaScript buildless capture.

By default, `cov-configure --javascript` configures buildless
capture to search for files ending in *.js,
*.jsx, *.htm,
*.html, *.map,
*.ts, tsconfig.json,
*.tsx, *.vue,
*.xsjs, and *.xsjslib and to emit
their code for later analysis.

The optional 
`--no-html`
 option excludes *.html and *.htm
files from the emit. Similarly, `--no-jsx` excludes
*.jsx files; `--no-typescript` excludes
*.ts, *.tsx, and
tsconfig.json files; and `--no-vue`
excludes *.vue files.

You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option with the
`coverity capture` CLI command.

See also, Friend compilers.

## Kotlin build capture configuration

Use the `cov-configure --kotlin` command to configure build capture
(to capture Kotlin source files from your build) and buildless capture (to capture
configuration files). The Kotlin configuration also enables buildless capture of
configuration files by default. You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option with the
`coverity capture` CLI command.

## PHP buildless capture configuration

Use the template configuration `cov-configure --php` syntax to
enable PHP buildless capture.

By default, `cov-configure --php` configures buildless capture for
files with the *.php, *.phtml,
*.php3, *.php5,, and
*.php7 filename extensions.

You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option with the
`coverity capture` CLI command.

## Python buildless capture configuration

Use the template configuration `cov-configure --python` syntax to
enable Python buildless capture.

By default, the `cov-configure --python` configures buildless
capture for files with the *.py filename extension.

CAUTION:

This command does *not* detect Python scripts that don't have
this filename extension.

You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option with the
`coverity capture` CLI command.

## Ruby buildless capture configuration

Use the `cov-configure --ruby` command to configure buildless
capture for Ruby source code.

By default, the `cov-configure --ruby` configures buildless capture
for files with the *.rb filename extension.

CAUTION:

This command does *not* detect Ruby scripts that don't have
this file name extension.

## Rust build capture configuration

Use the `cov-configure --rust` command to configure build capture for
Rust source code.

CAUTION:

Only projects built using `cargo` are captured.
Direct `rustc` invocations are not captured.

## Scala buildless capture configuration

Use the template configuration `cov-configure --scala` syntax to enable Scala
buildless capture.

By default, the `cov-configure --scala` configures buildless capture
for files with the `*.scala` filename extension.

You can limit which specific configuration files are captured by using the
`--file-include-glob or file-include-regex` option with the
`coverity capture` CLI command.

## Visual Basic build capture configuration

Use the `cov-configure --vb` command to configure build capture for Visual Basic source code.
