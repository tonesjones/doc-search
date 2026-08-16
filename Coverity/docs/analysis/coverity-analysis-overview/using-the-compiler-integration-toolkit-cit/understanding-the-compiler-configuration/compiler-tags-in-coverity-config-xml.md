---
title: "<compiler> tags in 'coverity_config.xml'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-tags-in-coverity_config.xml-.html"
content_id: "VoL_NdFPlm0MMhyo9CSjXg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:01.792602+00:00"
---

# <compiler> tags in 'coverity_config.xml'

The <compiler> tag is used to identify which compiler invocations this
configuration applies to using the configuration matching rules in The 'cov-translate' command. The possible tags in this section include:

<comp_desc>
:   The optional description of this compiler. This information is provided by
    `cov-configure` for Compiler Integration Toolkit (CIT)
    implementations.

<comp_dir>
:   Specifies the directory name for this compiler.

<comp_generic>
:   Provides the name of the directory where Compiler Integration Toolkit (CIT) files (for
    example, the switch table, compatibility headers, and configuration XML) for a
    given compiler are stored. For example,

    ```
    <comp_generic>csc</comp_generic>
    ```

    means
    that the Compiler Integration Toolkit (CIT) files for the compiler are stored
    under the following
    directory:

    <template_dir>/csc

    The default
    value of <template_dir> is
    <install_dir>/config/templates. You can
    change this default with <template_dir>.

<comp_name>
:   Specifies the binary name for this compiler.

<comp_next_type>
:   Gives the comptype for another possible configuration if the language of this configuration
    is not appropriate after the source is split between C and C++.

<comp_require>
:   Defines the parameters that are required before the compiler matches a particular
    <compiler> tag.

<comp_translator>
:   The command-line translator to use for this compiler. This specifies which compiler command
    line the `cov-translate` program should imitate. You can get a
    list of supported translators by running `cov-configure
    --list-compiler-types`. The translators are the first,
    comma-separated entries on each line in the list. (See sample command output
    in Configuring compilers for Coverity Analysis.) Required.

<could_require_regen>
:   Indicates `cov-translate` needs to invoke the native compiler to
    re-generate files (such as .TLH files) needed by compilation when it replays a
    compilation command.

<file_exclude_pattern>
:   *Use only with buildless capture.* Files and subdirectories that match the specified
    regular expression are excluded from the search results and are not included in
    the analysis. For example, the following tag excludes all paths that contain a
    directory named `node_modules`.

    ```
    <file_exclude_pattern>[/\\]node_modules[/\\]</file_exclude_pattern>
    ```

    Contents of excluded directories are not searched for further
    matches.

<file_include_pattern>
:   *Use only with buildless capture.* Specify a regular expression pattern to match
    source files to be passed to the associated compiler. For example, the following
    tags comprise a configuration that captures files with a `.js`
    extension that will be compiled as JavaScript:

    ```
    <comp_generic>javascript</comp_generic>
    <file_include_pattern>^.*\.js$</file_include_pattern>
    ```

    Note that the regular expression matches only on filenames and not on
    directories or path information.

<id>
:   A unique name for this compiler.

<is_ide>
:   Indicates the configured target is an IDE binary.

<target_platform_fn>
:   Specifies the internal function to be used to determine target platform for code
    instrumentation.

<tu_multiplier>
:   Specifies a tag that can be used by the `-coverity_tu_multiplier_tag` switch to redirect to this configuration.
    See the description of `-coverity_tu_multiplier_tag`
    in Tags for phases of command-line transformations.

<version>
:   Specifies a version string for the compiler. This tag is only descriptive.

<version_macro>
:   A macro that contains compiler version information.

    gcc version macros:

    - ```
      <version_macro>__GNUC__</version_macro>
      ```
    - ```
      <version_macro>__GNUC_MINOR__</version_macro>
      ```

<version_output_stream>
:   By default, compiler version auto detection looks for output on `stdout`.
    This can be overridden with the value `2`, which specifies output
    to standard error (`stderr`).

<version_regex>
:   An arbitrary number of regular expressions can be specified in
    `<version_regex>` tags to form the compiler output into
    the required format. The expressions are applied in the order they are given in
    the configuration. For
    example:

    ```
    <version_regex>replace/.*([0-9]+\.[0-9]+) \[Build .*/$1</version_regex>
    ```

    The
    following example takes the result of version macros
    `__GNUC__=3` and `__GNUC_MINOR_=4` and
    returns
    `3.4`:

    ```
    <version_regex>replace/(\d+)\s(\d+)/$1.$2</version_regex>
    ```

<version_switch>
:   Enables `cov-configure` to attempt to automatically detect the compiler's
    version number. The value is the compiler switch that prints out the version.
    For example, for
    gcc:

    ```
    <version_switch>--version</version_switch>
    ```

    If
    a compiler prints out the version information when invoked with no
    arguments, you should add this option with an empty value.

    If the
    wrong version is being reported, you can override the result by manually
    providing the version number to `cov-configure`. For
    example:

    ```
    cov-configure --version 2.1 --comptype ...
    ```

<wchar_t_name>
:   Defines a custom identifier for the `wchar_t` type. During compiler probes,
    this type name is used in place of `wchar_t`.
