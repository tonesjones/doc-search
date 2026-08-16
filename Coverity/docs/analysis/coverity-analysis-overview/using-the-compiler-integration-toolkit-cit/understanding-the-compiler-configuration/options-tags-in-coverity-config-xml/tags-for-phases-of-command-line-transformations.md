---
title: "Tags for phases of command-line transformations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-phases-of-command-line-transformations.html"
content_id: "YFNzn3B8oyMAjkMAp594mA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:05.855133+00:00"
---

# Tags for phases of command-line transformations

All of the options for manipulating command lines (see Tags for transforming the native command line to the Coverity compiler) can go directly into the `<options>` tag. For more control over when the
transformation occurs, they can be placed into one of the translation phases using one
of the following tags:

<expand>
:   The `--coverity_resp_file` option is processed during the expand phase. It
    takes the contents of a text file and adds it to the command line. For example,
    to map from `@file` you would use the following XML:

    ```
    <expand>
        <options>
            <replace_arg_regex>
                <replace>@(.*)</replace>
                <with>--coverity_resp_file=$1</with>
            </replace_arg_regex>
        </options>
    </expand>
    ```

    During this phase, the following switches are
    processed:

    - `--coverity_config_file` - Takes the form
      `--coverity_config_file=<value>` where value is
      the name of a response file. Only the argument to the last
      `--coverity_config_file` will be used.
    - `--coverity_resp_file_or_env_var` - Takes the form
      `--coverity_resp_file_or_env_var=<value>` where
      `<value>` is either a file name or an
      environment variable name. If the environment variable named
      `<value>` exists and is non-empty, then its
      value will be added to the command line. Otherwise,
      `<value>` will be treated as the file name of
      a response file, and this will be equivalent to
      `--coverity_resp_file=<value>`.
    - `--coverity_translate_config` - Takes the form
      `--coverity_translate_config=<value>` where
      `<value>` is a response file filter.
      `<value>` should be a regular expression to
      be applied to response files before they are interpreted; you might
      think of it as `ppp_translator` for response files. The
      switch applies to a `--coverity_config_file` specified
      earlier or later in the command line but only applies to
      `--coverity_resp_files` specified later in the
      command line.

<post_expand>
:   Processes the same switches as <expand>.

<pre_trans>
:   During this phase, the compiler switch file will be processed.

<split>
:   During this phase, the following switches are processed:

    - `-coverity_no_default_suffixes` - Only treats explicitly
      defined source file suffixes (for example, those defined through
      switches such as `-coverity_c_suffixes`,
      `-coverity_cxx_suffixes`, and so on) as source file
      name extensions. Default file name extensions such as
      .c for C source files will be disabled. This
      option should be added during the pre-translate phase and is not
      implemented for non-CIT (that is, non-Compiler Integration Toolkit
      (CIT)) compilers.
    - `-coverity_c_suffixes` - Takes the form
      `-coverity_c_suffixes
      <extension>[;<extension>;<extension...]`.
      Treats the given file name extensions as C source files. Example:
      `-coverity_c_suffixes c;i` treats files named
      src.c and src.i as files
      that contain C code. See
      `-coverity_no_default_suffixes`.
    - `-coverity_c_header_suffixes` - Treats the given file
      name extensions as C header files. See
      `-coverity_c_suffixes`.
    - `-coverity_cxx_suffixes` - Treats the given file name
      extensions as C++ source files. See
      `-coverity_c_suffixes`.
    - `-coverity_cxx_header_suffixes` - Treats the given file
      name extensions as C++ header files. See
      `-coverity_c_suffixes`.
    - `-coverity_objc_suffixes` - Treats the given file name
      extensions as Objective-C source files. See
      `-coverity_c_suffixes`.
    - `-coverity_objc_header_suffixes` - Treats the given file
      name extensions as Objective-C header files. See
      `-coverity_c_suffixes`.
    - `-coverity_objcxx_suffixes` - Treats the given file name
      extensions as Objective-C++ source files. See
      `-coverity_c_suffixes`.
    - `-coverity_objcxx_header_suffixes` - Treats the given
      file name extensions as Objective-C++ header files. See
      `-coverity_c_suffixes`.

<trans>
:   Intended to add any additional prevent compiler switches that are specific to whether the
    source is C or C++. You can avoid this phase in Compiler Integration Toolkit
    (CIT) implementations by using the `–coverity_cxx_switch` and
    `–coverity_c_switch` options to specify language specific
    switches.

    - `–coverity_c_switch` - Takes the form
      `-coverity_c_switch,<switch>[,<switch>,switch...]`.
      Specify the given switches for compiling the C sources on the command
      line only. For example, `-coverity_c_switch,-DNOT_CPP src.c
      src.cpp` will provide `-DNOT_CPP` for
      src.c but not src.cpp.
    - `–coverity_cxx_switch` - Takes the form
      `-coverity_cxx_switch,<switch>[,<switch>,switch...]`.
      Specify the given switches for compiling the C++ sources on the command
      line only. See `–coverity_c_switch`.

    `-coverity_tu_multiplier`
    :   Allows generating multiple front-end invocations for a single
        source file. Its argument has the form
        `<id>:<language>:<option>`,
        where the components are as follows:

        `id`
        :   An arbitrary numeric value that identifies the
            generated invocation.

        `language`
        :   A string to identify the languages to which the
            multiplier applies: It can be either the short name of
            the language, such as `"c++"`; a regular
            expression pattern with a leading and trailing
            slash—for example, `/cs|vb/`
            matches C# and Visual Basic); or `*`
            which matches any language.

        `option`
        :   Any argument or switch that is understood by the
            `trans` phase or subsequent phases.

        Here is an example of using
        `-coverity-tu-multiple`:

        ```
        -coverity_tu_multiplier=0:*:-Dfoo
        -coverity_tu_multiplier=0:*:-Dbar
        -coverity_tu_multiplier=1:*:-Dbaz
        -Dquux
        ```

        When these switches are specified on the command line passed to
        the `trans` phase, each source file (of any
        language) will generate two front-end invocations instead of
        one. The first invocation, "0", will include the arguments
        `-Dfoo -Dbar` while the second, "1", will
        include the argument `-Dbaz`. *Both*
        invocations will include the argument `-Dquux`.

    `-coverity-tu-multiplier-flag`
    :   Like `-coverity_tu_multiplier` but specifies the
        value of the `<tu_multiplier>` XML tag of the
        configuration that should be used to perform the
        `trans` phase of command-line translation. This
        allows the creation of multiple front-end invocations that have
        different type sizes and alignments as probed by
        `cov-configure`.

        Arguments to
        `-coverity-tu-multiplier-flag` have the same
        form as arguments to `-coverity_tu_multiplier`,
        with the last, `option` field being interpreted
        as an XML tag value rather than a switch.

        Here is an example of using
        `-coverity-tu-multiple-flag`:

        ```
        -coverity_tu_multiplier_tag=0:*:foo
        -coverity_tu_multiplier_tag=1:*:bar
        -coverity_tu_multiplier=1:*:-Dbar
        ```

        When these switches are specified on the command line passed to
        the `trans` phase, each source file (of any
        language) will generate two front-end invocations instead of
        one. The first invocation, "0", will redirect to a configuration
        with
        `<tu_multiplier>foo</tu_multiplier>`
        in its `<compiler>` node, while the second,
        "1", will behave the same for a configuration with
        `bar`. The second invocation will also
        include `-Dbar` on its command line.

<post_trans>
:   Translates the command line after the trans phase. This is primarily
    useful for manipulating the command line in the context of legacy
    compilers.

<src_trans>
:   During this phase, the following switch is processed:

    - `--coverity_remove_preincludes` - Erases all `--preinclude`
      and `--pre_preinclude` switches from the command line
      that appear before
      `--coverity_remove_preincludes`.

      Usage
      example:

      ```
      --add-arg --preinclude --add-arg foo --add-arg --coverity_remove_preincludes
      ```
