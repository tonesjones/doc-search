---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "DOmkbl6hR45WgnNaFu_6pQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:49.757247+00:00"
---

# Options

--cpp
:   Filters the results by the C/C++ translation units on which this command operates or reports. The
    command will fail with an informative error message if none of the
    translation units in the `emit` subdirectory match any of the
    specified language options. See also, `--cs`,
    `--java` and `--rust`.

--cs
:   Filters the results by the C# programming language. The command will fail with an informative
    error message if none of the translation units in the `emit`
    subdirectory match any of the specified language options. See also,
    `--cpp`, `--java` and
    `--rust`.

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--exact, -x
:   Assume that `<name>` is a full function prototype, not just
    a substring of the mangled name. Not commonly used.

--include-builtins
:   Look for given functions in the built-in model library.

--java
:   Filters the results by the Java programming language. The command will fail with an informative
    error message if none of the translation units in the `emit`
    subdirectory match any of the specified language options. See also,
    `--cs`, `--cpp` and
    `--rust`.

--model-file <file.xmldb>
:   Look for the function in the given user model file. See also, the `--model-file`
    option to `cov-analyze`.

--module <module>, -m <module>
:   Requires `--show`. Pick the model for module
    `<module>` when showing a model for a function. Values
    can be *`all`*, *`generic`*,
    *`security`*,
    *`concurrency`*, *`stack_use`*,
    *`uninit`*, and
    *`ptr_arith`*. Defaults to
    *`generic`*.

--output <directory>, -of <directory>
:   Specify the directory in which the output of `--save` is
    stored. The default is the current directory. If the directory does not
    exist it is created.

--rust
:   Filters the results by the Rust programming language. The command will fail
    with an error message if none of the translation units in the emit
    subdirectory match the specified language options. See also,
    `--cs` and `--cpp`.

--save
:   Save the model file in `<key>.<module>.models.xml`, a
    description of edges in `<key>.<module>.model_edges`,
    and a .ps file of the graph (as shown by `--show`) in
    `<key>.<module>.ps`. Each model is uniquely
    identified by an MD5 hex-key. `cov-find-function` uses this
    *key* to immediately find a model. If given a function name, it
    does a linear search of the model database. This search might take some
    time, but when it finds a function, it prints its model key for the
    specified module.

    Requires the `dot` command from the Graphviz package.

--show, -s
:   Show the model for the function. Requires `dot` (from the
    Graphviz package) as well as `ggv` (GNOME's PS viewer).

--subdir
:   When used in conjunction with `--use-emit`, specifies a
    subdirectory in which to look for the given function. Might substantially
    speed execution.

--use-emit, -ue
:   Iterate over the emit directory to find functions, instead of looking at the
    cache database. Useful if the cache is not present (for example, it has been
    cleaned or the analysis has never been run) or corrupted.

--user-model-file <file.xmldb>
:   [Deprecated] This option is deprecated as of version 7.7.0. Use `--model-file`
    instead.

## Shared options

--debug

-g
:   Turn on basic debugging output.

--ident
:   Displays the version of Coverity Analysis and build number.

--info
:   Displays certain internal information (useful for debugging), including the
    temporary directory, user name and host name, and process ID.

--tmpdir <tmp>

-t <tmp>
:   Specifies the temporary directory to use.

    - On UNIX, the default is `$TMPDIR`, or
      `/tmp` if that variable does not exist.
    - On Windows, the default is to use the temporary directory specified
      by the operating system.
