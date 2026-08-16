---
title: "The 'cov-translate' command in place of the native compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-cov-translate-command-in-place-of-the-native-compiler.html"
content_id: "Q38pmgPwgloskDfG2q~XLA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:13.263677+00:00"
---

# The 'cov-translate' command in place of the native compiler

If the default method of build integration using the Coverity build utility
(`cov-build`) is unsuitable for any reason, you can use the
`cov-translate` command as a replacement for any of the supported
compilers. In this mode, `cov-translate` can be prepended to any
compile line and, when supplied the appropriate arguments, can run both the native
compile and the Coverity Analysis compile. For example, you need to follow this
procedure to run the Coverity compiler on AIX, which does not support the
`cov-build` command.

The `--run-compile` option to `cov-translate` indicates that it
runs both the native compile and the Coverity Analysis compile. For example, the
following command creates the object file test.o, and adds the
analysis intermediate form for test.c to the emit repository:

```
> cov-translate --dir <intermediate_directory> --run-compile gcc -c test.c
```

For most build systems, it is sufficient to prepend the compiler name with the command
sequence `<install_dir>/bin/cov-translate --run-compile`
command. For example, you can specify the following to run `make` with
its CC/CXX macro defined as a `cov-translate` command that is
configured to execute the appropriate native C/C++ compiler:

```
> CC="cov-translate --dir int-dir --run-compile cc" make
```

Manually integrating `cov-translate` into a Makefile becomes more
complex when a build system includes scripts that rely on the exact format of the output
to stdout from the compilation. For example, any build that invokes
GNU autoconf configuration scripts during the build requires that the compilations
invoked within the autoconf scripts mirror the output of the native gcc compiler
invocations exactly. To address this issue, Coverity Analysis provides an argument
translator, the `--emulate-string` option to the
`cov-translate` command. This option is used to specify a regular
express that, if matched on the command line, makes the command to run the native
compiler command line only (that is, without attempting to call
`cov-emit`). The output from the native compiler invocation is
printed verbatim to stdout, and `cov-translate`
does not make any attempt to run the Coverity compiler.

The regular expressions to the `--emulate-string` option are Perl regular
expressions. For example, to indicate that any option to gcc containing the word dump
should cause the emulation behavior, the `cov-translate` command line
can be specified as follows:

```
> cov-translate --dir <intermediate_directory> --run-compile --emulate-string ^-dump.* gcc -dumpspecs
```

This command causes the verbatim output of `gcc -dumpspecs` to be
printed to stdout. Note that the ^ and $ elements of the Perl
regular expression are implicitly added to the beginning and end of the specified
regular expression when they are not present. This addition means that the terminating
.* at the end of the option in the above example is required to ensure that any sequence
of characters can follow -dump.

For gcc in particular, the following arguments should be emulated using the
emulate-string option because they are commonly used by the GNU autoconf-generated
`configure` scripts:

- `-dumpspecs`
- `-dumpversion`
- `-dumpmachine`
- `-print-search-dirs`
- `-print-libgcc-file-name`
- `-print-file-name=.*`
- `-print-prog-name=.*`
- `-print-multi-directory`
- `-print-multi-lib`
- `-E`
