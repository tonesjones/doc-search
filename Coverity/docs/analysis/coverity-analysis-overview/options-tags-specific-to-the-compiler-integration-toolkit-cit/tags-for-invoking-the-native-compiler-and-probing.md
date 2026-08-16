---
title: "Tags for invoking the native compiler and probing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-invoking-the-native-compiler-and-probing.html"
content_id: "L26G8BhgqKJklyJYJgkiWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:12.986855+00:00"
---

# Tags for invoking the native compiler and probing

<dependency_switch>
:   Specifies which switch or switches to add to a compiler command line to get it to dump the
    list of include files it is using. For example, `gcc -M`.

<dependency_output>
:   Indicates the output from the file dependency listing. If you do not specify a
    `<dependency_output>` value, the default is the value set
    by `<preprocess_output>`. The value `1`
    or `-` specifies standard output; `2`
    specifies standard error; any other value is considered a file name.

    See the
    `<preprocess_output>`
    tag.

<compile_switch>
:   Specifies which switch or switches to add to a compiler command line so it can compile a
    source file. For example `-c` is the compile switch for
    `gcc -c t.cpp`.

<dryrun_switch>
:   Specifies which switch or switches to add to a compiler command line so it can dump its
    dryrun or verbose output. This usually describes the internal processes that are
    invoked to support the native compiler. By processing this,
    `cov-emit` can discover the include directories and
    predefined macros used by the native compiler.

<dryrun_parse>
:   Indicates which format of the native compiler dryrun output. The supported formats are
    `generic`, `gcc`, and
    `qnx`.

<dump_macros_arg>
:   Specifies which switch or switches to add to a compiler command line to get it to dump the
    macros that are predefined by this compiler. For example, `gcc -dM -E
    t.cpp`. Not all compilers support this option.

<dump_macros_output>
:   Specifies where the compiler dumps the macros that are predefined by this compiler. The
    value `1` or `-` specifies standard output.
    `2` specifies standard error, and any other value is
    considered a file name. A file name can contain the special values
    `$FILE$` to indicate the name of the file,
    `$FILEBASE$` to indicate the name of the file without its
    extension, and `$PPEXT$` to indicate `i` for a C
    file, or `ii` for a C++ file.
