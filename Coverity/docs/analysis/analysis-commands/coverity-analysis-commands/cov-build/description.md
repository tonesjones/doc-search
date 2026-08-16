---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "H_P3j8d2XdLlM2gmgmU7Dg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:52.676029+00:00"
---

# Description

The `cov-build` command is the primary tool to capture and emit source
code. It performs build capture, where source code is emitted by intercepting all calls
to the compiler invoked by the build system.

For more information about the build capture processes, see the section "Coverity analyses"
in the overview to the Coverity Analysis 2026.6.0 User and Administrator Guide.)

Note: Parallel builds for ASP.NET 4 and earlier applications cannot be virtualized directly with
the `cov-build` command.

Attention:
Coverity does not log environment variables in its
build-log.txt or configure-log.txt files
unless the environment variable COVERITY_LOG_ENVIRONMENT_VARIABLES is
set to 1 or the option --debug-flags envvars is specified. Environment
variables on command lines such as `bash -c "MYVAR=secret command"` are
still at risk, since command lines *are* logged. Take care to be sure that scripts
such as Makefiles are not invoking commands in this way. To make sure, review the
contents of build-log.txt.

Environment variables are recorded
in the emit database in the intermediate directory (`idir/`).
Sensitive environment variables can be excluded from the emit database by adding
their names to the environment variable
COVERITY_FILTER_ENVVARS_DENYLIST; for example,
`COVERITY_FILTER_ENVVARS_DENYLIST=var1,var2,...`.

Which environment variables are being recorded can be examined in two ways: by
setting COVERITY_LOG_ENVIRONMENT_VARIABLES equal to 1 and looking
at the build-log.txt and configure-log.txt
files, or by invoking `cov-manage-emit --dir idir print-environment-variables`.

For more information, see "Security considerations for running Coverity scans"
in the *Coverity Analysis User and Administrator Guide*.

In general, the `cov-build` command name and option can prefix the
original build command. However, if the `cov-build` command depends on
features of the command shell that usually invokes it, such as certain shell variables
or non-alphanumeric arguments, you can invoke it using a wrapper script. This preserves
the original behavior because the `cov-build` command is again invoked
directly by the shell type (on which it depends).

For example, if the normal invocation of a Windows build is:

```
> build.bat Release"C:\Release Build Path\"
```

use `cov-build` as follows:

```
> cov-build --dir <intermediate_directory> <wrapper.bat>
```

where `<wrapper.bat>` is an executable command script that contains
the original and unmodified build command.

On Windows, specify both the filename and extension for the build command when using
`cov-build`. For example:

```
> cov-build --dir <intermediate_directory> custombuild.cmd
```

Because `cov-build` uses the native Windows API to launch the build
command, the appropriate interpreter must be specified with any script that is not
directly executable by the operating system. For example, if the normal invocation of a
build within Msys or Cygwin is:

```
> build.sh
```

prefix `cov-build` with the name of the shell:

```
> cov-build --dir <intermediate_directory> sh build.sh
```

Similarly, if a Windows command file does not have Read and Execute permissions, or if
you want `cov-build` to report the command file's
%ERRORLEVEL%, explicitly invoke it as a
`cmd.exe` command string. For example, to run the Java builder
ant.bat:

```
> cov-build --dir <intermediate_directory> cmd /c "ant && exit/b"
```

Note:
Keep the following in mind:

- If you run `cov-build` more than once, only the last build's
  metrics are saved.
- If you change the set of compilation options used by your build process, delete
  the `<intermediate_directory>` and capture a full build
  from scratch. Otherwise, the translation units captured using the old options
  will remain in the emit. The new translation units will not replace the old
  translation units due to the changed compilation options.

As a final step, this command invokes `cov-security-da`, which runs a
dynamic analysis in order to perform a security assessment.

Note: Coverity Security Dynamic Analysis for C# and Visual Basic
requires requires a Windows 64-bit or Linux 64-bit system that supports .NET 6.
