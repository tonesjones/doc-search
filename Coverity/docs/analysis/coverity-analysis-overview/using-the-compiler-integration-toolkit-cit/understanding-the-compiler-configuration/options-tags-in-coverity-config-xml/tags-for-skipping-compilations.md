---
title: "Tags for skipping compilations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-skipping-compilations.html"
content_id: "1aOtKsi7pDYeHV~bBq1_WA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:03.745434+00:00"
---

# Tags for skipping compilations

<emulate_compile_arg>
:   Used in combination with `cov-translate --run-compile`. When the
    `arg` matches the native command line,
    `cov-emit` will not be invoked and the output of the native
    compiler will be passed through verbatim.

<skip_arg>
:   Skips compiles that contain the value given. This causes the translator to not call
    `cov-emit` whenever this value is seen on the native
    compiler's command line as a separate, complete argument.

    Figure 1. Do not call `cov-emit` on compiler invocations with
    the "-G" argument:

    ```
    <skip_arg>-G</skip_arg>
    ```

<skip_arg_icase>
:   Identical to <skip_arg>, except that this tag ignores the case of the expression. The
    following tag set ignores command lines that contain arguments with the string
    '-HeLp', '-HELP', '-help', and so forth:

    ```
    <skip_arg_icase>-help</skip_arg_icase>
    ```

<skip_arg_regex>
:   <skip_arg_regex> works the same as <skip_arg>, except it performs a regex match.
    This is similar to <skip_substring> as well, however it provides for
    situations where a simple substring would not work.

    Figure 2. The following example shows how to match
    `--preprocess=cnl`, `--preprocess=nl`,
    but not `--preprocess=cl` or`--preprocess`.

    ```
    <skip_arg_regex>--preprocess=.*n.*</skip_arg_regex>
    ```

<skip_arg_regex_icase>
:   Identical to <skip_arg_regex>, except that this tag ignores the case of the
    expression. The following tag set ignores command lines that start with '-h' or
    '-H'.:

    ```
    <skip_arg_regex_icase>-h.*</skip_arg_regex_icase>
    ```

<skip_substring>
:   Skips compiles that contain the value given as a substring of any argument. This causes the
    translator to not call `cov-emit` whenever any argument on the
    native compiler's command line contains the value as a substring.

    Figure 3. Do not call `cov-emit` on compiler invocations with
    ".s" as a substring of any argument on the command line:

    ```
    <skip_substring>.s</skip_substring>
    ```

<skip_substring_icase>
:   The tag is identical to <skip_substring>, except that this tag ignores the case of the
    command line when matching. In the following example, command lines will be
    ignored that have options or arguments that contain "skipme", "SKIPME",
    "sKiPmE", and so forth.
    example:

    ```
    <skip_substring_icase>skipme</skip_substring_icase>
    ```

<skip_file>
:   Do not compile files that match the given Perl regular expression. This only affects the
    compilation of the given files, so if several files are on a single command line
    it will only skip those that actually match (unlike <skip_arg> or
    <skip_substring>). The file being matched is the completed file name (for
    example, the current directory is put in front of relative file names), with
    / as a directory separator (even on windows). The match
    is partial: use ^ and $ to match boundaries.

    Figure 4. Do not compile parser files ending with ".tab.c":

    ```
    <skip_file>\.tab\.c$</skip_file>
    ```

    Note: Java limitation: Though this option removes matching files from the
    `cov-emit-java` command line, the command will
    nevertheless emit files that it identifies as dependencies, even if they
    match the <skip_file> value.
