---
title: "Translation unit sub-commands with required filtering"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/translation-unit-sub-commands-with-required-filtering.html"
content_id: "U50RMujhXbH~6ksUK4zIBQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:48.811310+00:00"
---

# Translation unit sub-commands with required filtering

The following filtering sub-commands work on translation units. You must supply the translation
units used in these operations with the `--tu` and/or
`--tu-pattern` options. The TU `list` sub-command
identifies the TUs available for your required filter.

delete
:   Delete all TUs that satisfy the specified translation unit filter.

preprocess
:   Similar to recompile, except that when `cov-emit` is
    invoked, it is passed the `-E` (preprocess) and
    `--output_defs` options, which results in preprocessing
    only. The emit database is not modified by this operation.

    The preprocessed output file (which is the stdout of
    `cov-emit`) is stored in the
    preprocessed subdirectory of the
    c/output subdirectory of the intermediate
    directory. The name of the file is the name of the primary source file for
    the TU, minus any path information, minus any file extension, plus either
    .i or .ii.

    This option works only for C/C++ source code, not Java.

print-compilation-info [options]
:   For the specified translation units, print the command lines for
    `cov-emit`, `cov-translate` (if it was
    run), and `cov-build` (if it was run).

    The options are:

    - `--detailed` - provides all process details
      except environment variables.
    - `--print-env` - provides the environment
      variable definitions for the process.

print-compilation-time
:   Prints the invocation time of any `cov-build`,
    `cov-emit`, `cov-emit-cs`,
    `cov-emit-java`, `cov-emit-vb`,
    `cov-translate`, or for a given translation unit (TU)
    to be easily accessible.

    Usage examples

    ```
    cov-manage-emit --dir dir -tu <TU#> print-compilation-time
    ```

    ```
    cov-manage-emit --dir dir -tp <pattern> print-compilation-time
    ```

    Output example:

    ```
    cov-manage-emit --dir idir -tp "success()" print-compilation-time

    Looking for translation units
    |0----------25-----------50----------75---------100|
    ****************************************************
    Translation unit:
    1 -> /Users/emoriarty/Testing/BZ55606/test.cpp
    cov-emit invocation time (seconds): 1
    cov-translate invocation time (seconds): 1
    cov-build invocation time (seconds): 2
    Translation unit:
    2 -> /Users/emoriarty/Testing/BZ55606/test.cpp
    cov-emit invocation time (seconds): 2
    cov-translate invocation time (seconds): 2
    cov-build invocation time (seconds): 2
    Translation unit:
    3 -> /Users/emoriarty/Testing/BZ55606/test.cpp
    cov-emit invocation time (seconds): 2
    cov-translate invocation time (seconds): 2
    cov-build invocation time (seconds): 2
    Translation unit:
    4 -> /Users/emoriarty/Testing/BZ55606/test.cpp
    cov-emit invocation time (seconds): 2
    cov-translate invocation time (seconds): 2
    cov-build invocation time (seconds): 2
    ```

print-source
:   For the specified translation units, list the name and the contents of the
    primary source file associated with the TU. This option also reports, in
    parentheses, the internal row ID of the source file. It accepts the same
    command options as 
    `print-source-files-contents`
    .

print-source-files
:   For the specified translation units, list the names of all the source files
    associated with the TU. Also reports, in parentheses, the internal row ID of
    the source file.

print-source-files-contents
:   For the specified translation units, list the names and contents of all the
    source files associated with the TU. Also reports, in parentheses, the
    internal row ID of the source file.

    `print-source-files-contents` has the following options:

    - `--scm-annotations` - Prefixes each source line with
      the change record (or commit record) that contributed most recently
      to the line. The change record data that is as follows:

      Date and time that the change record was applied according to the SCM
      system.

      The author (username) attributed to the change record.

      The revision of the change, which is an identifier for the change
      record provided by the SCM system.

print-source-files-stats
:   For the specified translation units, list the names of all of the source
    files associated with the TU. Also reports the internal row ID of the source
    file (in parentheses) followed by statistics for that source file. The
    statistics listed include:

    - The file contents time stamp, size, and MD5 sum
    - The count of blank lines
    - The count of comment lines
    - The count of code lines
    - The count of code lines with inline comments

    Example output is as follows:

    ```
    1 -> /example_dir/a.cpp
      Primary SF : /example_dir/a.cpp (row ID 1)
        Timestamp:     2013-07-19 11:37:35
        Size:          25
        MD5 sum:       7edc175dc475923c51c579924b724a8c
        Blank lines:   1
        Comment lines: 0
        Code lines:    2 (1 with inline comments)
    ```

print-tuid
:   Prints the TU ids for the TU requested using either `-tu` or
    `--tu-pattern`. Unlike most commands that will error if
    an invalid `tu` is specified, `print-tuid`
    will silently ignore it. For example:

    ```
    $ cov-manage-emit --dir foo --tu-pattern 'success()' print-tuid
    Looking for translation units
    |0----------25-----------50----------75---------100|
     ****************************************************
     1
     3
     4
                    
                    
    $ cov-manage-emit --dir foo --tu-pattern 'success()' print-tuid -of tuids.txt
    Looking for translation units
    |0----------25-----------50----------75---------100|
     ****************************************************
     $ cat tuids.txt 
     1
     3
     4
    ```
