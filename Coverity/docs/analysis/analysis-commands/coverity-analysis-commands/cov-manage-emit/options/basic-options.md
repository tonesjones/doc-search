---
title: "Basic options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/basic-options.html"
content_id: "RU207E7N66u9pZGo6~QIvQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:46.672838+00:00"
---

# Basic options

The `--dir` option is required. If you use a sub-command that uses
translation units, you can filter this information with either the `--tu`
or `--tu-pattern` option, or both.

--cpp
:   Filters by C/C++ translation units on which this command operates or reports.
    The command will fail with an informative error message if none of the
    translation units in the emit match any of the specified language
    options.

--case-normalized-filename
:   By default, `cov-manage-emit` displays case-preserved file
    names in the output. Specifying this option allows
    `cov-manage-emit` to display normalized file names
    (that is, names that are entirely lower case).

    For example (assuming you are on Windows and have a file in your emit named
    MyFile.c):

    ```
    cov-manage-emit.exe --dir intdir --case-normalized-filename list
    ```

    The output will include the following:

    ```
    c:/cygwin/space/int_dir/myfile.c
    ```

    Note: In previous releases, case-preserved file names were always printed for
    Java and C# (regardless of `--case-preserved-filename`. As
    of the 7.5.0 release, Java and C# file names will be case-preserved or
    case-normalized according to specification of this option
    (--case-normalized-filename), like C/C++ file
    names. As a result, it is impossible to get the old output of
    `cov-manage-emit` (which would case-normalize C/C++ but
    case-preserve Java/C#) in a multi-language scenario.

--case-preserved-filename
:   Allows `cov-manage-emit` to display case-preserved file
    names. This option is enabled by default, so you do not need to specify it
    with `cov-manage-emit list`. To switch to normalized file
    names, use --case-normalized-filename.

--cs
:   Filters by C# translation units on which this command operates or reports.
    The command will fail with an informative error message if none of the
    translation units in the emit subdirectory match any of
    the specified language options.

--dir <intermediate_directory>
:   Specifies an existing intermediate directory that was created with the
    `cov-build` command. While certain other sub-commands
    (for example, add) allow you to specify intermediate directories, the one
    specified with `--dir` is the directory modified by
    `cov-manage-emit`.

--java
:   Filters by Java translation units on which this command operates or reports.
    The command will fail with an informative error message if none of the
    translation units in the emit match any of the specified language
    options.

--preprocess-native
:   Invokes the native compiler to generate preprocessed output. The emit
    database is not modified by this operation. The preprocessed output file is
    stored in the `c/output/preprocessed` subdirectory of the
    intermediate directory. This option works only for C/C++ source code.

--rust
:   Filter to Rust translation units.

--ticker-mode <mode>
:   Set the mode of the progress bar ticker. The available modes are:

    none
    :   No progress bar is displayed.

    no-spin
    :   Only the print stars are displayed; the spinning bar is
        not.

    spin
    :   This is the default mode. Stars with a spinning bar at the
        end are displayed. Each file, function, or defect committed
        corresponds to steps of spin.

--tu translation_unit_id(s)

-tu translation_unit_id(s)
:   Identifies a set of translation units (TUs), named by their numeric ID
    attribute(s). A translation unit approximately maps to the output from a
    single run of a compiler. This option requires a comma-separated list of
    id(s), and `--tu` can be specified multiple times. The union
    of all these identifier sets is the set of TUs to operate on subsequently,
    for operations that work on TUs. It is an error if any of the specified IDs
    do not correspond to any existing translation unit. To get the IDs for
    translation units, use the list sub-command.

    You can use the `--tu` and `--tu-pattern` options
    together.

--tu-pattern translation_unit_pattern

-tp translation_unit_pattern
:   Identifies a set of translation units specified with a translation unit pattern. The
    `--tu-pattern` option can be specified multiple times.
    Matching TU sets are unioned together across all patterns.

    Both `--tu` and `--tu-pattern` can be specified
    on a single command line. The final set of TUs operated upon includes a
    given TU if it matches any specified translation unit pattern or its ID is
    listed explicitly as an argument to `--tu`.

    It is an error if at least one `--tu-pattern` argument is specified but no
    translation unit matches any of the specified patterns.

    You can get useful information on TUs with the list sub-command.

    For more information, see Translation unit pattern matching.

--tu-sort sort_spec
:   Specifies the sort order for TU output. The sort_spec
    accepts the values listed below. To sort on more than one attribute, you can
    use a non-empty, comma-separated list of values. Additionally, to specify
    ascending or descending sort order for any attribute, you can add
    `:a` or `:d` (respectively) directly after
    the attribute name. All attributes are ordered in ascending order by
    default.

    The available sort attributes are:

    - `emittime`: the time spent emitting TUs.

--tus-per-psf value
:   Indicates how the set of primary source files affects the set of selected
    TUs. The possible values are as follows:

    - `all`: Select all TUs, possibly as specified by other
      TU filters. This is the default.
    - `latest`: Select only the latest TU with a given
      primary source file according to the time of compilation. If there
      are multiple TUs with the same primary source file within a single
      build, a deterministic TU is chosen within that build, regardless of
      time of compilation, which allows determinism in the case of
      parallel builds. This corresponds to the default set of TUs that
      `cov-analyze` analyzes. That is,
      `cov-analyze` with `--one-tu-per-psf`corresponds to `--tus-per-psf=latest`
      without any other filtering options (see the --one-tu-per-psf option to
      `cov-analyze`).

      With at least one `--tu` option and without a search
      pattern, the option has no effect. In this case, the system includes
      only the TUs specified with `-tu`.
    - `non-latest`: Select any but the
      `latest` TU with a given primary source file.
      This is applied after search pattern filtering. The result is
      undefined if `-tu` is also used. For instance, to
      keep only one TU per primary source file, run the following
      command:

      ```
      cov-manage-emit --tus-per-psf=non-latest delete
      ```

    Examples:

    To list all the TUs that cov-analyze will operate on:

    ```
    > cov-manage-emit --dir <intermediate_directory> \
        --tus-per-psf=latest list
    ```

    To delete TUs and leave only the ones that cov-analyze would operate on:

    ```
    > cov-manage-emit --dir <intermediate_directory> \
        --tus-per-psf=non-latest delete
    ```
