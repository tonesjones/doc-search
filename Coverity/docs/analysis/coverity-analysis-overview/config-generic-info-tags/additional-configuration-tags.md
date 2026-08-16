---
title: "Additional configuration tags"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/additional-configuration-tags.html"
content_id: "upQRIIV~DFw198iF~UyU~g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:15.008366+00:00"
---

# Additional configuration tags

This section describes additional general tags that can have an impact on the Compiler
Integration Toolkit (CIT) configuration.

<macro_candidate>
:   Adds a macro to the list of macros that cov-configure should try to
    determine if it should be defined.

<excluded_macro_candidate>
:   Ensures that this macro is excluded from the list of macros that
    `cov-configure` tries to determine if it should define. A
    macro is usually excluded if its definition will be controlled by the handling
    of a command line option.

<excluded_macro_candidate_regex>
:   Ensures that any macros matching the given regex are excluded from the list of macros that
    `cov-configure` tries to determine if it should define. A
    macro is usually excluded if its definition will be controlled by the handling
    of a command line option.

<extra_header>
:   Specifies additional headers to be searched for when trying to determine the include path
    for a compiler. This is necessary when the detected include path is
    incomplete.

<extra_compat_header>
:   Specifies additional compatibility headers that should be appended to the generated
    compatibility headers by `cov-configure`. This can be useful for
    sharing compatibility header information between different compiler
    configurations.

    To specify the compatibility header in a different folder,
    you can either use a relative path or
    `$CONFIG_TEMPLATES_BASE_DIR$`, which is expanded to the
    absolute path name of the directory that contains the configuration files.
    For example, the following text, if used in a configuration file, specifies
    that `compiler-compat-clang-common.h` in the clang folder
    will be appended to the generated compatibility headers by
    `cov-configure`.

    ```
     <extra_compat_header>$CONFIG_TEMPLATES_BASE_DIR$/clang/compiler-compat-clang-common.h</extra_compat_header>
    ```

<function_like_macro_candidate>
:   Like `<macro_candidate>`, adds the macro specified via the name tag to the
    list of candidate macros that `cov-configure` probes, in order to
    determine an appropriate definition.

    The named macro is assumed to be a
    function-like macro that takes a single argument, and the set of possible
    arguments is given by the argument_candidate tags that follow. For
    example:

    ```
    <function_like_macro_candidate>
        <name>fcn_name</name>
        <argument_candidate>argument_the_1st</argument_candidate>
        <argument_candidate>argument_the_2nd</argument_candidate>
    </function_like_macro_candiate>
    ```

<include_dependency>
:   Specifies that cov-configure should use dependency information instead
    of preprocessing to determine include paths.

<intern_generate_headers>

<extern_generate_headers>
:   Experimental feature to allow external programs to generated extra compatibility headers
    during cov-configure. These headers might be removed in a
    future release.

<no_header_scan>
:   Disable performing a header scan for macro candidates during the probing of a compiler.
    Values are `True` or `False`.

<platform_if_macro>
:   Specifies the `<macro_name>` and `<platform>` pairs used
    by the target platform probe. Please refer to <test_target_platform>.

<set_env_var>
:   Sets the environment variable to the specified value before probing the native compiler. For
    example, the following tags cause environment variable FOO to be set to value
    BAR before the native compiler is probed. The value of this environment variable
    is restored after probing.

    ```
    <set_env_var>
        <env_name>FOO</env_name>
        <env_value>BAR</env_value>
     </set_env_var>
    ```

<unset_env_var>
:   Unsets the specified environment variable before probing the native compiler. The value of
    this environment variable is restored after probing.
