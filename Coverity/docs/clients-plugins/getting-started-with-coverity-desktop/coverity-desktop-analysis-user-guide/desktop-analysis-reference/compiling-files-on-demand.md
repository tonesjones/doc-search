---
title: "Compiling files on demand"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiling-files-on-demand.html"
content_id: "b~jaKH0aWSFi2py5liyXZQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:59.013640+00:00"
---

# Compiling files on demand

To analyze compiled code, `cov-run-desktop` must have seen a compiler
invocation for that code so that it knows the proper context for parsing and analyzing
the code. This is normally accomplished by capturing builds with
`cov-run-desktop --setup` or `--build`, but an
alternative is to configure a script for building specific files on demand, using the
`specific_files_build_cmd` option in
coverity.conf.

When `cov-run-desktop` is asked to analyze source files that are not already
part of a captured compilation and are not captured with filesystem capture,
`cov-run-desktop` will attempt to *auto-compile* them with the
`specific_files_build_cmd`, if it is set. If successful,
`cov-run-desktop` proceeds with analysis as usual, without the need
for a specific build step by the user. Some with a configured
`specific_files_build_cmd` might choose to skip build capture during
`--setup`, with `--skip-build` or `build_cmd:
[]` in coverity.conf.

Consider a coverity.conf configuration example for auto-compilation:

```
cov_run_desktop: {
    "specific_files_build_cmd": [ "python", "scripts/compile-specific-files.py", "--response-file=$(response_file_utf8)" ],
    "specific_files_regex": "[.](c|cpp)$"
}
```

First, like other commands specified in coverity.conf, arguments
comprising the build command are specified as strings in a JSON array.
`cov-run-desktop` will construct a temporary text file listing the
files to compile, one per line, and the path to that file will be substituted for use of
special variable `$(response_file_utf8)` or
`$(response_file_platform_default)`. The script should read the list
from that file, using either UTF-8 or platform default character encoding, depending on
the variable used. Only one use of a response file special variable is allowed in the
`specific_files_build_cmd`. If no response file special variable is
used, files to compile will instead be appended as command line arguments. This is more
convenient for writing scripts, but is not recommended because it risks exceeding OS
limits on command line length when compiling many files on demand, especially on
Windows.

The example runs the system's `python` command and gives it a relative
path to a Python script, scripts/compile-specific-files.py. This
relative path works because `cov-run-desktop` always executes the
`specific_files_build_cmd` with the current directory set to
`$(code_base_dir)`. On Unix-like systems, with proper permissions,
and so on, it is possible to execute the .py script directly, but
specifying the interpreter for the script is more portable to Windows platforms.

Some requirements for `specific_files_build_cmd` scripts:

- The script must be able to handle relative or absolute paths (in platform-native format,
  system default encoding), where relative paths will be relative to
  `$(code_base_dir)`, the working directory for the command.
- It must also handle more than one file specified for compilation, perhaps by grouping related
  files together for compilation or perhaps by naively building one at a time.
- It must not skip compilation if the object file is already newer than the source file. For
  builds driven by `make`, the script will likely need to
  `touch` source files before invoking `make`, or
  use the -W option of `make`, to force invocation of the
  compiler.

The `specific_files_regex` option is highly recommended with
`specific_files_build_cmd` because it reduces or improves errors when
attempting to analyze an uncaptured file that would fail when passed to the
`specific_files_build_cmd`. In the example above, we know that our
script only handles C and C++ source files, with .c and
.cpp extensions in our code base. Thus, the regex ensures
`specific_files_build_cmd` is only invoked with such files. This
option works in concert with other regex filtering options, such as
`restrict_modified_file_regex`.

Non-primary source files, mostly C and C++ header files, present a challenge for
auto-compilation, but the `specific_files_regex` can make this work in
some cases. For example, suppose foo.c includes
foo.h, nothing has been captured, and
`cov-run-desktop` is using the above configuration. Although
`cov-run-desktop foo.h` will fail because we do not know how to
capture a .h file automatically, `cov-run-desktop foo.c
foo.h` will succeed because auto-compiling foo.c will
enable `cov-run-desktop` to analyze foo.h, as a
non-primary file included by foo.c.

Note: Advanced note: `specific_files_build_cmd` can directly invoke
`cov-translate` on applicable compiler commands instead of actually
running those compiler commands. This can be more efficient by avoiding compiler
invocations, but it might be more difficult to set up and to debug.
