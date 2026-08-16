---
title: "Tags for transforming the native command line to the Coverity compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-transforming-the-native-command-line-to-the-coverity-compiler.html"
content_id: "GiIaQuVgjMRcJ1U68udDDg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:05.120526+00:00"
---

# Tags for transforming the native command line to the Coverity compiler

<append_arg>
:   Adds an argument to the end of the `cov-emit` command line, after arguments
    put out by `cov-translate`. Only use this to override erroneous
    arguments put out by `cov-translate`.

<args_from_env_var>
:   Specifies an environment variable from which to extract options, in addition to the command
    line. The `<prepend>` attribute specifies the name of the
    environment variable to be used, while the optional
    `<ignore>` attribute specifies the name of another
    environment variable which may or may not be defined. (*Note*: The
    `<add>` subtag may be used instead of the
    `<prepend>` subtag. However, a warning will be issued
    if the `<add>` subtag is used.) Environment variables
    specified within the `<append>` subtag will be appended to
    the command line. If the second environment variable is specified in the
    `<ignore>` tag, and that variable is defined in the
    environment, then all other environment variables contained in the
    `<args_from_env_var>` tag are ignored. For
    example:

    ```
    <args_from_env_var>
      <append>CCTS_OPTIONS</append>
      <prepend>CCTS_OPTIONS</prepend>
      <ignore>CCTS_IGNORE_ENV</ignore>
     </args_from_env_var>
    ```

    A fifth subtag,
    `<append_args_found_after_delimiter>`, can also be
    used in conjunction with the above. This tag allows specifying one
    delimiter, where any arguments found in the environment variable following
    that delimiter will be appended, and any arguments preceding it will be
    prepended to the command line. For
    example:

    ```
    <args_from_env_var>
      <prepend>CCTS_OPTIONS</prepend>
      <append_args_found_after_delimiter>|</append_args_found_after_delimiter>
    </args_from_env_var>
    								
    CCTS_OPTIONS="-prepended_arg_1 -prepended_arg_2 | -appended_arg_1 -appended_arg_2"
    ```

    The
    `<accept_quoted_delimiters>` sub tag affects all of
    the delimiters specified by the
    `<append_args_found_after_delimiter>` tag. For
    example:

    ```
    <args_from_env_var>
      <append>FOO</append>
      <append_args_found_after_delimiter>|</append_args_found_after_delimiter>
      <accept_quoted_delimiters>true</accept_quoted_delimiters>
    </args_from_env_var>
    										
    FOO="|-DBAR"
    ```

    In the example above, -DBAR is
    added to the command line while the leading vertical bar `|`
    has been removed because it is treated as a delimiter. The
    `<accept_quoted_delimiters>` tag prevents the value
    |-DBAR from being treated as the additional command
    line switch. Note that the vertical bar isn't removed because it is not
    being treated as a delimiter in this case.

<drop_prefix> <drop_string>
:   The `cov-translate` command attempts to match the next argument
    (`-\-foobar`) after the prefix with the
    `<drop_string>` value. If this argument matches, it is
    ignored. Each time an argument is successfully matched and ignored, it tries to
    match the next argument against the list of `<drop_string>`
    values. As soon as the next argument does not match one of the
    `<drop_string>` values, it stops trying, and assumes
    the next argument after that is the compiler name. You can also use the
    `<drop_count>` tag to specify the number of additional
    arguments after the matching argument to unconditionally drop.

    **Skip the
    `-\-skip_me_1` argument, and also the next two
    arguments:**

    ```
    <drop_prefix>
      <drop_string>-\-skip_me_1</drop_string>
      <drop_count>2</drop_count>
    </drop_prefix>
    ```

<extern_trans>
:   Invokes an external command. The syntax is:

    ```
    <extern_trans>
      <extern_trans_path>path to your executable</extern_trans_path>
      <extern_trans_arg>…</extern_trans_arg>
      <extern_trans_arg>…</extern_trans_arg>
    <extern_trans>
    ```

    The path to the executable is required, but the arguments are
    optional and will depend on how the executable works. If the path is
    relative to the Coverity Analysis installation directory, you can use the
    `$CONFIGDIR$` environment variable, which expands to the
    absolute path of the installation's /config
    directory.

    Example:

    ```
    <extern_trans>
      <extern_trans_path>$CONFIGDIR$/../translator.exe</extern_trans_path>
    <extern_trans>
    ```

    In addition to whatever arguments you
    specify, the following additional arguments will be added:

    - The filename containing all the command line arguments that need to
      be processed, one argument per line.
    - The filename of where you should write the new command line, one
      argument per line.
    - After the first two arguments, there are the following optional
      arguments that are useful to locate helpful files, such as the
      compiler switch table:
      - -\-compiler_executable_dir <path>
        - Encodes the location of the native compiler
        executable.
      - -\-compiler_version <version> -
        Encodes the compiler version of the native compiler being
        translated.
      - -\-cov-home <path> - Encodes the
        location of the Coverity Analysis installation
        directory.
      - -\-cov-type <comp_type> - Encodes
        the compiler type.
      - -\-template_subdir <path> -
        Encodes the /template subdirectory for
        the compiler.

    The native command line arguments are not put on the command line to
    avoid any command line length issues and some instability in pipes on
    Windows.

<id>
:   A string matching the compiler to which the options under the current
    `<options>` tag apply. If you do not specify the
    `<id>` tag, the options will apply to all compilers.
    You can specify multiple compiler `<id>` tags under a
    single `<options>` tag, and the options will apply to all
    specified compilers.

    **Make the current `<options>` tag
    apply to the compiler with the identifier
    `gcc`:**

    ```
    <id>gcc</id>
    ```

<include_dir>
:   This is the directory where user headers are located, to be used by the
    `cov-emit` command line. The directory is appended with the
    `cov-emit`
    `-I` option.

<includes_from_env_var>
:   Specifies an environment variable that defines additional include directories that should be
    searched during source parsing.

<intern_trans>
:   Invokes a command that is built in to the product. For
    example:

    `<intern_trans>lintel_pre_translate</intern_trans>`

    This
    built-in command can be overridden by providing an external translator. The
    external translator will be found in the same directory as the Compiler
    Integration Toolkit (CIT) configuration and will have the same name as the
    built-in command. No user specified arguments are permitted. Only the extra
    options that were previously described for
    `<extern_trans>` are passed. If no extra options
    are required, specifying `<extern_trans>` is not
    necessary.

    When a valid internal command is specified, and an external
    translator of the same name is present in the same directory as the Coverity
    Compiler Integration Toolkit configuration, the external translator is
    preferred over the internal command without requiring the presence of
    `<extern_trans>`.

    It is also possible to
    specify an external translator within `<intern_trans>`
    that is not named the same as any preexisting internal command. In that
    case, the configuration would then be completely dependent upon the presence
    of the external translator.

<opt_preinclude_file>
:   Specify a file to preinclude during compilation. The file is optional. If no file is
    specified, this option is ignored.

    Add the nodefs.h file
    in the same directory as the current
    coverity_config.xml configuration file to the
    `cov-emit` command
    line:

    ```
    <opt_preinclude_file>$CONFIGDIR$/nodefs.h</opt_preinclude_file>
    ```

<pre_preinclude_file>
:   Specifies a header file to be included before all other source and header files when you
    invoke `cov-emit`. This is equivalent to the
    `-\-pre_preinclude` option of the `cov-emit`
    command. The header files that you specify with this tag are processed with
    `cov-emit` before all other header or source files. This
    tag is typically used to include the Coverity compiler and macro compatibility
    header files that the `cov-configure` command generates.

<pre_prepend_arg>
:   Adds an argument to the beginning of the `cov-emit` command line, ensuring
    that arguments precede arguments added by `<prepend_arg>`.
    Successive arguments will be placed in the order they are declared, the last one
    being just before the arguments added by `<prepend_arg>`.
    Only use this to force certain arguments to come first on the
    `cov-emit` command line.

<preinclude_file>
:   Specify `<file.h>` to be included before most of the source and header
    files except for those specified with
    `<pre_preinclude_file>`, when you invoke
    `cov-emit`. This is equivalent to the
    `-\-preinclude` option of the `cov-emit`
    command. Header files that you specify with this tag are processed by
    `cov-emit` immediately after those that are specified with
    the `<pre_preinclude_file>` tag and those passed to
    `cov-emit` via the `-\-preinclude_macros`
    option. This option is typically used to include special nodef files that
    contain macro suppression directives and macros predefined by the
    compiler.

    Preinclude the
    /nfs/foo/PrefixHeaderForCoverity.h
    file:

    ```
    <preinclude_file>
    /nfs/foo/PrefixHeaderForCoverity.h
    </preinclude_file>
    ```

<prepend_arg>
:   Adds an argument to the beginning of the `cov-emit` command line, preceding
    arguments put out by `cov-translate`. Successive arguments will
    be placed in the order they are declared, the last one being just before the
    arguments put out by `cov-translate`. Use
    `<prepend_arg>` unless a compelling reason is present
    to use `<pre_prepend_arg>` or
    `<append_arg>`.

    **Add `-\-ignore_std`
    to the `cov-emit` command line to ignore the
    std namespace for C++
    compiles:**

    ```
    <prepend_arg>-\-ignore_std</prepend_arg>
    ```

    **Add
    `-\-ppp_translator <translator>` to the
    `cov-emit` command line to translate files before
    they are
    preprocessed.**

    ```
    <prepend_arg>-\-ppp_translator</prepend_arg> 
    <prepend_arg>replace/(int) (const)/$2 $1</prepend_arg>
    ```

    **Prepend
    "-DNDEBUG" to the `cov-emit`
    command line to add the NDEBUG
    define:**

    ```
    <prepend_arg>-DNDEBUG</prepend_arg>
    ```

<remove_arg>
:   Removes a single argument from the `cov-emit` command line. This is only
    needed if for some reason the `cov-translate` program is
    putting something undesirable onto the `cov-emit` command
    line.

    **Remove the `-ansi` argument from the
    `cov-emit` command line (only needed if
    `-ansi` appears and is causing a parsing
    problem):**

    ```
    <remove_arg>-ansi</remove_arg>
    ```

<remove_args>
:   Removes several arguments from the `cov-emit` command line. This is only
    needed if for some reason the `cov-translate` program is
    putting something undesirable onto the `cov-emit` command line.
    This differs from `<remove_arg>` in that you can specify
    the additional number of arguments after the matching
    `<arg>` to remove.

    **Remove `-foo a
    b` from the `cov-emit` command line, where
    a and b are the two arguments
    that follow
    `-foo`:**

    ```
    <remove_args>
      <arg>-foo</arg>
      <num>2</num>
    </remove_args>
    ```

<replace_arg>, <replace_arg_regex>
:   `<replace_arg>` replaces an argument from the original compiler command
    line with an argument that should go into the `cov-emit`
    command line. `<replace_arg_regex>` replaces a regular
    expression from the original compiler command line with a regular expression
    that should go onto the `cov-emit` command line. These tags are
    useful if the translator does not understand a custom command line option that
    can be handled by `cov-emit`.

    **For example for
    `<replace_arg>`, if the compiler command line
    contains `-mrtp`, add `-D__RTP__` to the
    `cov-emit` command
    line:**

    ```
    <replace_arg>
      <replace>-mrtp</replace>
      <with>-D__RTP__</with>
    </replace_arg>
    ```

    **For example for
    `<replace_arg_regex>`, if the compiler command
    line contains `-i<directory>`, add
    `--include=<directory>` to the
    `cov-emit` command
    line:**

    ```
    <replace_arg_regex>
      <replace>-i(.*)</replace>
      <with>--include=$1</with>
    </replace_arg_regex>
    ```

    Both
    `<replace_arg>` and
    `<replace_arg_regex>` accept multiple
    `<with>` tags, so it is possible to translate a
    single argument to multiple output arguments. For example (using
    `<replace_arg_regex>`):

    ```
    <replace_arg_regex>
      <replace>-foo=(.*)</replace>
      <with>-bar=$1</with>
      <with>-baz=$1</with>
    </replace_arg_regex>
    ```

    In this case,
    `-foo=test` will be replaced with
    `-bar=test` and `baz=test`.

    When a
    `<replace_arg>` or
    `<replace_arg_regex>` tag is matched, the resulting
    output is inserted in-place, meaning that the order of the resulting command
    line is unchanged. Furthermore, `<replace_arg>` and
    `<replace_arg_regex>` tags are applied in the order
    they appear in the XML, and the results of a given replacement are passed to
    the next possible replacement. For
    example:

    ```
    <replace_arg>
      <replace>-foo</replace>
      <with>-bar</replace>
    </replace_arg>
    <replace_arg>
      <replace>-bar</replace>
      <with>-baz</replace>
    </replace_arg>
    ```

    In this case, `-foo` will
    be replaced by `-baz`, because the second
    `<replace_arg>` tag will match the output of the
    first.

<replace_icase>
:   A child tag to `<replace_arg>` and
    `<replace_arg_regex>`. When this tag is used, the
    replacement is applied in a case sensitive manner. For
    example:

    ```
    <replace_arg>
      <replace_icase>-FOO</replace_icase>
      <with>-bar</with>
    </replace_arg>
    ```

    In this case, `-FOO`,
    `-foo`, `-Foo`, and all other
    combinations, will be replaced.

<sysinclude_dir>
:   This is the directory where system headers are located, to be used by the
    `cov-emit` command line. The directory is appended with the
    `cov-emit`
    `-\-sys_include` option.

<version_includes_from_env_var>
:   Specifies a regex that is run against the compiler version to determine if the environment
    variable should be used.

    The specified environment variable is added to the
    includes if the given regex matches any part of the version string after
    applying the substitution given by the version_regex
    tag.

    The syntax is as
    follows:

    ```
    <version_includes_from_env_var>
       <version_regex><regex></version_regex>
       <name><environment_variable_name></name>
    </version_includes_from_env_var>
    ```
