---
title: "Tags for native preprocessing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-native-preprocessing.html"
content_id: "w_TVTdTsztRRCc1Nir_xAQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:03.090828+00:00"
---

# Tags for native preprocessing

<fix_macro_regex>
:   Specifies a regex that describes how to transform a command line switch from the Coverity
    `-DMACRO=VALUE` syntax, to the native compiler's format. This
    is required to add macros to the native command line when it is used for
    preprocessing.

<pch_options>
:   Specifies configuration options relating to precompiled header support. The
    following child tags are supported:

    <archetype> (required)
    :   Specifies the PCH archetype modeled by the native compiler. Allowed
        values are `gcc` (GNU GCC-like compilers with
        implicit PCH support), `gnu` (alias for
        `gcc`), `clang` (clang-like
        compilers) and `msvc` (Microsoft
        `cl`-like compilers which require explicit PCH
        switches).

    <native_pch_suffix> (optional)
    :   Specifies the default file extension used by the native compiler for
        PCH artifacts. If omitted, defaults to the extension implied by the
        archetype.

<preprocess_command>
:   Runs a command, if any, that replaces the real compiler, to preprocess a file.

    Figure 1. Run `cpp` instead of `gcc`:

    ```
    <preprocess_command>cpp</preprocess_command>
    ```

<preprocess_compile_switch>
:   Indicates options that are added to the native compiler command line when preprocessing a
    source file. This is used in addition to <preprocess_switch>. This switch
    is not used during `cov-configure` when the native compiler is
    probed.

<preprocess_output>
:   Indicates the output of the `cov-preprocess` command by using a
    value.

    The value `1` or `-`
    specifies standard output; `2` specifies standard
    error; any other value is considered a file name. A file name can contain
    the special values `$FILE$` to indicate the name of the
    file, `$FILEBASE$` to indicate the name of the file
    without its extension, and `$PPEXT$` to indicate
    i for a C file, or ii for a
    C++ file.

    Figure 2. Transform test.c into
    test.i and test.cc into
    test.ii:

    ```
    <preprocess_output>$FILEBASE$.$PPEXT$</preprocess_output>
    ```

<preprocess_remove_arg>
:   A Perl regular expression that indicates arguments that should be removed from a compile
    line to preprocess a file.

    Figure 3. Remove output files and compile arguments:

    ```
    <preprocess_remove_arg>-o.+</preprocess_remove_arg>
    <preprocess_remove_arg>-c</preprocess_remove_arg>
    ```

<preprocess_remove_next_arg>
:   A Perl regular expression that indicates arguments that should be removed, as well as the
    argument immediately following it, from a compile line to preprocess a file
    (e.g. `-o`).

    Figure 4. Remove output files:

    ```
    <preprocess_remove_next_arg>-o</preprocess_remove_next_arg>
    ```

<preprocess_switch>
:   Adds an argument to the compiler line to preprocess a file.

    Figure 5. Use `-E` to preprocess files:

    ```
    <preprocess_switch>-E</preprocess_switch>
    ```

<preprocess_response_file>
:   Instructs `cov-translate` to use a response file when invoking the native
    compiler to preprocess. You can use <switch> to specify the native
    response file switch, <suffix> to specify response file suffix, and
    <format> to specify how response files should be formatted. The following
    is an example.

    ```
    <preprocess_response_file>
        <switch>@</switch>
        <suffix>.rsp</suffix>
        <format>default</format>
    </preprocess_response_file>
    ```

    `default` is
    currently the only allowed value for <format>. It causes each compiler
    switch to be written on a separate line in the response file.

<preprocess_output_dir_switch>
:   Specifies the native switch that instructs the native compiler to generate the preprocess
    output to a particular directory.

<trailing_preprocess_switch>
:   Similar to the <preprocess_switch> arguments. The <trailing_preprocess_switch>
    argument is added near the end of the command line (that is, after the arguments
    and before the file name) rather than at the beginning.
