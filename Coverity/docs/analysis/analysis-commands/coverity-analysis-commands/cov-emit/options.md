---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "9FNg3KLc4Tw~vrBvLR7dnA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:26.737616+00:00"
---

# Options

--add_builtin_stdarg_macro
:   Enables macros to be defined when a builtin include of
    `<stdarg.h>` is processed.

--add_type_modifier <modifier>
:   Enables `cov-emit` to recognize and parse previously unknown
    type modifiers such as __data16,__code32,__huge
    etc.

    Consider the following code:

    ```
    void foo(int *x) {
      /* Do something */
    }

    void foo(int __data16 * x) {
      /* Do something else */
    }
    ```

    Utilizing the `--add_type_modifier=__data16` will tell
    `cov-emit` that __data16 is a type
    modifier, and it will treat the two functions as distinct. Implicit
    conversions between types is done with reliance on the native compiler to
    enforce the conversion rules - that is, it is assumed that all conversions
    are valid.

    Note: You can specify one type modifier to be the
    default. The default
    setting is used when instantiating templates to mimic the native compiler's
    usage of default type modifiers as shown in the following
    example:

    ```
    --add_type_modifier=__data8,__data16:default
    ```

--allow-incompat-return-types
:   Allows a prototype of a function to specify different return types than those
    in the actual function definition.

--allow_incompat_throw
:   Indicates to `cov-emit` that it should not report an error
    if there are multiple prototypes of the same function with incompatible C++
    exception specifications.

--angle_include_search_first {default|user|system}
:   Controls the order that directories are searched when trying to find an
    included file. This option applies to files added by `#include
    <...>`.

    - `default` - Indicates that there is no change from
      previous behavior.
    - `user` - Indicates that user include directories (added with `-I`)
      will be searched first.
    - `system` - system include directories (added with `--sys_include`)
      will be searched first.

    The `--sys_include_first` option, which is now depreciated, is
    equivalent to `--angle_include_search_first=system`.

--arg_file <file>
:   Read arguments from the response file `<file>`. This is typically done by
    `cov-translate` to avoid command-line length
    limitations.

    The response file format is as follows:

    ```
    <compiler_args>
      <cov_emit_cmd_args>
        <arg>[cov-emit arg]</arg>
        <arg>[another cov-emit arg]</arg>
      </cov_emit_cmd_args>
    </compiler_args>
    ```

    Note: Note that spaces within the `<arg>` tags are
    interpreted literally. This means that
    `<arg>-DFOO=bar</arg>` will work, while
    `<arg> -DFOO=bar</arg>` will cause an error,
    as the argument is interpreted as a source file name.

--c
:   Compile standard C code (C89).

--c++11
:   Enable c++11 language features.

--c++14
:   Enable c++14 language features.

--c++17
:   Enable c++17 language features.

--c++
:   Compile standard C++ code. This is the default.

--c99
:   Enable C 99 extensions to the C programming language.

--cache_include_search
:   If you use large numbers of #include search directories with the
    `-I` option, specify this option to speed up
    compilation.

--calling_convention_group
:   Specifies the comma-delimited calling conventions that should be considered
    equivalent. For example, `--calling_convention_group
    default,stdcall,vectorcall` causes `stdcall` and
    `vectorcall` calling conventions to be treated the same
    as the default, or unspecified, calling convention in
    `cov-emit`. The list of valid calling conventions are:
    `default, cdecl, fastcall, stdcall, thiscall, vectorcall,
    clrcall.`

--char_bit_size <integer>
:   Used to specify the size (in bits) of the char type. If this option is not
    specified, the default is 8-bit chars.

--cygwin
:   This switch tells `cov-emit` to attempt to convert
    Unix-based (Cygwin) paths into their corresponding Windows (real) paths.

-D <identifier>[=<value>]
:   Add a macro definition of `<identifier>` with optional
    `<value>`.

--dir <intermediate_dir>
:   Specifies the emit repository (an intermediate directory) into which the
    `cov-emit` command outputs its results.

-E
:   Only preprocess the source file.

--emit_complementary_info
:   Enables emitting of complementary information for compliance checkers such as
    MISRA checkers. Selecting this option results in a slower build capture but
    a faster analysis, and it should be applied when using compliance checkers.
    The default value is `--no_emit_complementary_info`

    Note: Enabling the --emit_complementary_info option prior
    to running an analysis is likely to turn up additional
    defects.

    Any analysis involving `--coding-standard-config` requires the
    information generated during `cov-build` when including the
    `--emit-complementary-info` option. The
    `cov-build` command will take longer, so this option
    should only be used when `cov-analyze` is used with
    `--coding-standard-config`.

    If `cov-build` did not include the
    `--emit-complementary-info` option and
    `cov-analyze` does include
    `--coding-standard-config`,
    `cov-analyze` automatically re-runs every
    `cov-emit` command (for the Translation Units to be
    analyzed). This excludes the native build and the
    `cov-translate` overhead, but it will add significant
    overhead to `cov-analyze`. Note that analysis will fail if
    the emit database does not include source; that is re-emit is not
    possible.

--enable_80bit_float
:   The following switches provide the ability to turn on/off 80-bit float
    intrinsic types. This overrides implicit enablement or disablement implied
    by other `cov-emit` switches.

    - --enable_80bit_float
    - --no_enable_80bit_float

--enable_128bit_float
:   The following switches provide the ability to turn on/off 128-bit float
    intrinsic types. This overrides implicit enablement or disablement implied
    by other `cov-emit` switches.

    - --enable_128bit_float
    - --no_enable_128bit_float

--enable_128bit_int
:   The following switches provide the ability to turn on/off 128-bit integer
    types, independent of gnu_version:

    - --enable_128bit_int
    - --no_enable_128bit_int
    - --enable_128bit_int_extensions
    - --no_enable_128bit_int_extensions

    --enable_128bit_int implies
    --enable_128bit_int_extensions, however the same does
    not apply to the no_* variants.

    --enable_128bit_int enables type
    __int128, while
    --enable_128bit_int_extensions enables types
    __int128_t and __uint128_t.

--enable_user_sections
:   Enables the user sections compiler extension allowing variable placement at
    specific addresses in memory. Compilers that support this extension include
    the IAR ARM compiler which uses the "@" operator for this purpose, and the
    CodeWarrior compiler which uses ":". Please consult your compiler manual for
    more information.

    This option supersedes `cov-emit`'s deprecated
    `--allow_declare_at_address` option.

--encoding <enc>
:   Specifies the encoding of source files. Use this option when the source code
    contains non-ASCII characters so that Coverity Connect can display the code
    correctly. The default value is US-ASCII. Valid values are the ICU-supported
    encoding names:

    US-ASCII

    UTF-8

    UTF-16

    UTF-16BE
    :   UTF-16 Big-Endian

    UTF-16LE
    :   UTF-16 Little-Endian

    UTF-32

    UTF-32BE
    :   UTF-32 Big-Endian

    UTF-32LE
    :   UTF-32 Little-Endian

    ISO-8859-1
    :   Western European (Latin-1)

    ISO-8859-2
    :   Central European

    ISO-8859-3
    :   Maltese, Esperanto

    ISO-8859-4
    :   North European

    ISO-8859-5
    :   Cyrillic

    ISO-8859-6
    :   Arabic

    ISO-8859-7
    :   Greek

    ISO-8859-8
    :   Hebrew

    ISO-8859-9
    :   Turkish

    ISO-8859-10
    :   Nordic

    ISO-8859-13
    :   Baltic Rim

    ISO-8859-15
    :   Latin-9

    Shift_JIS
    :   Japanese

    EUC-JP
    :   Japanese

        Note: EUC-JP is now a valid output object encoding. See --output_object_encoding.

    ISO-2022-JP
    :   Japanese

    GB2312
    :   Chinese (EUC-CN)

    ISO-2022-CN
    :   Simplified Chinese

    Big5
    :   Traditional Chinese

    EUC-TW
    :   Taiwanese

    EUC-KR
    :   Korean

    ISO-2022-KR
    :   Korean

    KOI8-R
    :   Russian

    windows-1251
    :   Windows Cyrillic

    windows-1252
    :   Windows Latin-1

    windows-1256
    :   Windows Arabic

    Note: If your code is in SHIFT-JIS or EUC-JP, you must specify the
    `--output_object_encoding SHIFT-JIS` or
    `--output_object_encoding EUC-JP` option (respectively)
    in order to avoid receiving STRING_OVERFLOW false positives.

    For more
    information, see `--encoding <enc>`.

--encoding_selector <encoding-or-regularexpression>
:   Treats all files with file names that match the given, case-sensitive regular
    expression as though they have the specified encoding. For a list of valid
    encodings, see the `--encoding` option to this command. The
    regular expression syntax is a Perl regular expression, as described in
    <http://perldoc.perl.org/perlre.html>.

    Encoding selectors also apply to files that are included in source files, not
    just to the files specified on the `cov-emit` command line.
    This behavior allows for a finer granularity in selecting encodings.

    Note that encoding selectors have a higher priority than the
    `--encoding` option. If the `cov-emit`
    command line contains both `--encoding <encoding>` and
    `--encoding_selector <encoding>/<regular
    expression>`, and the regular expression is a match for the
    file that is currently getting opened, the encoding specified through the
    encoding selector will take precedence.

--encoding_selector_icase <encoding>/<regular expression>
:   Identical to `--encoding_selector`, except that the regular
    expression is case insensitive.

--error_limit <number>
:   For a file that fails to compile, specifies the number of errors that are
    output to build-log.txt before moving to the next file.
    Default is 5.

--float_bit_patterns
:   Enables parsing the ARM Development Studio C/C++ language extension that
    allows floating-point bit pattern literals, for example:

    ```
    float f = 0f_00000000;
    double d = 0d_0000000000000000;
    ```

--force
:   Disables incremental compilation by forcing the command
    to compile and generate output for all source files, including files that have
    already been compiled and are present in the Intermediate Directory and whose
    timestamps has not changed.

--gcc
:   Allow parsing of C code with gcc (GNU) extensions.

--g++
:   Allow parsing of C++ code with g++ (GNU) extensions.

--gnu_version <version>
:   Specifies the version of the GNU compiler to emulate. Only required when the
    code you are compiling exploits version-dependent features or bugs in the
    `gcc` or `g++` compilers. If the
    version of `gcc` you are using is 3.4.2, for example, then
    specify the version as 30402.

--ignore_std
:   Specifies that the namespace "`std`" should be ignored
    entirely. `g++` versions prior to 3.0 ignored the
    "`std`" namespace.

--include_recursion_limit <value>
:   Specifies the maximum number of times a source file is allowed to include
    itself (directly or indirectly) before the recursion is assumed to be
    infinite and compilation is terminated. The default limit is 10 levels of
    recursion.

--incompat_proto
:   Allows a prototype of a function to specify a different set of arguments than
    those in the actual function definition.

--inline_keyword
:   Explicitly enables support for the ISO C99 `inline` keyword,
    overriding any language dialect or compiler emulation mode setting. By
    default, `inline` is treated as a keyword if the selected
    language dialect or compiler emulation mode requires it.

-I <dir>
:   Add a directory to search for `#include` files. Directories
    added with this switch are considered 'user' include directories.

    The default behaviour is to search for headers in the order that both the
    `-I` and --sys_include were
    specified on the command line, regardless of `#include` type.
    This can be adjusted using `--angle_include_search_first
    {default|user|system}` and `--quote_include_search_first
    {default|user|system}`.

--lazy_hex_pp_number
:   This option affects grammar in which a statement such as '0x1e-1' can be
    parsed as either a single pp-number (C++11 2.10 [lex.ppnumber]) or as a
    subtraction expression.

    When using the Compiler Integration Toolkit (CIT), you will only need to use
    this option if the compiler correctly parses the example above, but
    `cov-emit` does not.

    In order to determine if you need to use this option, you will receive an
    error message from `cov-emit` that looks like the
    following:

    ```
    "test.cpp", line 3: error: extra text after expected end of number
    int foo = (0xD8E-0xD64);
                    ^
    ```

--list_macros
:   Print all macros defined in the translation unit to standard out.

    Note that this option prints *all* macros in the translation unit, while
    `--print_predefined_macros` prints only predefined
    macros.

--lowercase_header_filenames
:   In the `cov-emit` preprocessor, when the source refers to a
    header filename, turn it into all-lowercase before asking the operating
    system for the file. This can be useful when transitioning to a
    case-sensitive filesystem. Also translates backslash to slash, and removes a
    leading drive letter and (back)slash, as these are needed in the same
    situations.

--macro_stack_pragmas
:   Enables parsing of GNU macro stack manipulation pragmas (`#pragma
    push_macro` and `#pragma pop_macro`). This option
    is enabled by default in most cases, but may be automatically disabled in
    certain compatibility modes.

    To manually disable this option, use
    `--no_macro_stack_pragmas`.

--microsoft
:   Allow parsing of Microsoft extensions.

--ms_asm
:   When specified, enable support for parsing Microsoft-style inline assembly.
    By default, inline assembly is assumed to follow the format specified by the
    C standard, e.g.:

    ```
    asm("int $3");
    ```

    When enabled, inline
    assembly is parsed following Microsoft's style, e.g.:

    ```
    asm int 3;
    asm { int 3; };
    ```

    When enabled, Microsoft-style inline assembly
    may be specified using the `asm`, `_asm` or
    `__asm` keywords interchangeably.

--multiline_string
:   Allow the Coverity compiler to accept multi-line strings. Multi-line strings
    are supported by compilers such as gcc 3.4.

--nested_comments
:   Allow the Coverity compiler to accept nested block comments. Nested comments
    are supported by compilers such as Renesas RX 2.03.

--new_array_args
:   Enables parsing for options to array element constructors invoked by the
    new[] variant of the C++ memory allocation
    operator.

--no_atomic_commit
:   This option is deprecated as of the 5.0 release.

--no_emit_complementary_info
:   Disables emitting of complementary information for compliance checkers such
    as MISRA checkers.

--no_enable_user_sections
:   Disables the user sections compiler extension. To enable the use of user
    sections, see `--enable_user_sections`.

--no_exceptions
:   Disable parsing for exception handling in C++.

--no-headers
:   This option is deprecated as of the 5.0 release.

--no_inline_keyword
:   Explicitly disables support for the ISO C99 `inline` keyword,
    overriding any language dialect or compiler emulation mode setting. By
    default, `inline` is treated as a keyword if the selected
    language dialect or compiler emulation mode requires it.

--no_macro_stack_pragmas
:   Disables parsing of GNU macro stack manipulation pragmas (`#pragma
    push_macro` and `#pragma pop_macro`). This option
    is enabled by default in most cases, but may be automatically disabled in
    certain compatibility modes.

    To enable parsing of these pragmas, use
    `--macro_stack_pragmas`.

--no_ms_asm
:   Disable parsing of Microsoft-style inline assembly. This disables the
    keywords `asm`, `_asm` and
    `__asm`.

--no_predefined_feature_test_macros
:   Do not predefine the testing macros described in
    `--predefined_feature_test_macros`.

    This is the default behavior of `cov-emit`.

--no_predefined_stdc
:   Do not predefine __STDC__.

--no_predefines
:   Do not predefine any macros internally. All macro definitions must be in the
    source code or explicitly on the command line.

    This is the default behavior for `cov-emit`. Use the
    `--predefines` option to predefine specific macros.

    Note that `--no_predefines` has no effect on the following
    macros, which may still be predefined even if this option is specified:

    - Certain C/C++ standard macros (e.g., `__FILE__,
      __LINE__`)
    - Macros that begin with "`__COVERITY`"
    - Macros that are controlled by another switch (e.g.,
      `__STDC__` and
      `--no_predefined_stdc`)

--old_g++
:   For GNU versions prior to 3.x, specifies a more permissive version of
    `g++` compatibility.

--output_object_encoding
:   Specifies the output character encoding. This option accepts an encoding as a
    required argument. The accepted encodings are `Shift-JIS` and
    `EUC-JP`. For example:

    ```
    --output_object_encoding EUC-JP
    ```

    Using `--shiftjis_encode_obj` is effectively the same as
    specifying `--output_object_encoding Shift-JIS`.

    If `--output_object_encoding` is not specified, then the
    object encoding is UTF-8.

--pending_instantiations <integer>
:   Specifies the maximum number of instantiations of a given template that can
    be in progress at any given time. Use 0 (zero) to specify an unlimited
    number. You might need to increase this limit when using recursive
    templates.

--ppp_translator <translator>
:   Add `--ppp_translator <translator>` to the
    `cov-emit` command line to translate files before they
    are preprocessed. Possible <translator> values are:

    - cmd:<command>– Pipes file through <command> .
    - replace/<from>/<to>– Replaces regular expression
      <from> with <to> . The regular expression syntax is a
      Perl regular expression, as described in <http://perldoc.perl.org/perlre.html>.
      The '/' character can be replaced with any other character; and this
      separator character can be quoted with a backslash '\'.

--pp_sizeof
:   Allows the use of `sizeof()` in preprocessing directives. When
    compiling, the argument to `sizeof` can be anything permitted
    in an expression. However, when preprocessing, it is only possible to use
    built-in types like `int`. This means that preprocessing
    output might be different than what the compiler encounters during
    compilation. This feature is nonstandard and only supported by a few
    compilers.

--pre_preinclude <file.h>
:   Specify header file that should be processed prior all other source and
    header files.

--predefined_feature_test_macros
:   Compatible with C++ only. The [WG21 working paper N3694](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2013/n3694.htm) provides
    guidelines for predefined feature testing macros. When this option is
    specified, `cov-emit` will predefine the appropriate macros
    as suggested by these guidelines.

--predefines
:   When specified, `cov-emit` will predefine additional macros
    based on the current emulation mode.

    For example:

    ```
    > cov-emit --microsoft --predefines test.c
    ```

    The above command will predefine `_MSC_VER`, while the
    following command predefines `__GNUC__`.

    ```
    > cov-emit --gcc --predefines test.c
    ```

    Note that `--predefines` has no effect on the following
    macros:

    - Certain C/C++ standard macros (e.g., `__FILE__,
      __LINE__`)
    - Macros that begin with "`__COVERITY`"
    - Macros that are controlled by another switch (e.g.,
      `__STDC__` and
      `--no_predefined_stdc`)

--preinclude_macros <file.h>
:   Specify macros-only header file that should be processed immediately after
    the files specified with `--pre_preinclude` option (see
    above) and prior to all other source and header files.

--preinclude <file.h>
:   Specify header file that should be processed immediately after the files
    specified with `--pre_preinclude` and
    `--preinclude_macros` options (see above) and prior to
    all other source and header files.

--print_predefined_macros
:   Print all predefined macros (and their values) to stdout.

    Note that this option prints only predefined macros, while `--list_macros`
    prints all macros in the translation unit.

--ptrdiff_t_type <builtin-type>
:   Specify the type of ptrdiff_t. This is stored in the
    __COVERITY_PTR_DIFF_TYPE__ macro (as the type, not the character code). If
    unspecified, __COVERITY_PTR_DIFF_TYPE__ is set to the same type as
    ptrdiff_t (for example, "signed int"). The character
    code for <builtin-type> is typically one of the signed types shown in
    `--size_t_type <builtin-type>`. For example,
    `--ptrdiff_t_type i` sets the type of
    ptrdiff_t to "signed int".

--quote_include_search_first {default|user|system}
:   Controls the order that directories are searched when trying to find an
    included file. This option applies to files added by `#include
    "..."`.

    - `default` - Indicates that there is no change from
      previous behavior.
    - `user` - Indicates that user include directories (added with `-I
      <dir>`) will be searched first.
    - `system` - system include directories (added with --sys_include <dir>) will be
      searched first.

--short_enums
:   Enables optimization of enumeration sizes. The size of each enumeration will
    be set based on the largest values present when this option is
    specified.

--size_t_type <builtin-type>
:   Specify type of `size_t`. This is stored in the
    __COVERITY_SIZE_TYPE__ macro (as the type, not the character code). If
    unspecified, __COVERITY_SIZE_TYPE__ is set to the same type as
    `size_t` (generally, the default is "unsigned int"). Use
    an unsigned integral type from the single-character codes for
    `<builtin-type>` as follows:

    ```
    a  # signed char 
    h  # unsigned char 
    s  # short 
    t  # unsigned short 
    i  # int 
    j  # unsigned int 
    l  # long 
    m  # unsigned long 
    x  # long long, __int64 
    y  # unsigned long long, __int64
    ```

    For example, `--size_t_type j` sets the type of size_t to
    "unsigned int".

--source_chroot <chroot-path>
:   This option ensures that `cov-emit` only searches for source
    files under the listed chroot path. Source files outside of the chroot path
    will not be found. Note that for the `--source_chroot` option
    to work properly, the current working directory must be a child of the
    chroot path.

--sys_include <dir>
:   Add a directory to search for #include files.
    Directories added with this switch are considered 'system' include
    directories.

    The default behaviour is to search for headers in the order that both `-I`
    and `--sys_include` were specified on the command line,
    regardless of #include type. This can be adjusted using
    `--angle_include_search_first` and
    `--quote_include_search_first`.

--system_encoding <enc>
:   Specifies the encoding to use when interpreting command line arguments and
    file names. If not specified, a default system encoding is determined based
    on host OS configuration.

    See `--encoding` for a list of accepted encoding names.

--type_alignments <builtin-type>
:   Specify type of type_alignments. The `<builtin-type>` string consists of the
    ABI chars shown in `--size_t_type`, plus the following:

    ```
    f  # float 
    d  # double 
    e  # long double, __float80 
    P  # Coverity extension: pointer
    ```

    and lengths. For example,
    `--type_alignments x8li4s2P4` sets type_alignments to
    `long long 8, long & int 4, short 2, ptr 4`.

--type_sizes <builtin-type>
:   Specify type of type_sizes. The `<builtin-type>` string consists of the ABI
    chars shown in `--size_t_type`, plus the following:

    ```
    w  # wchar_t 
    f  # float 
    d  # double 
    e  # long double, __float80
    n  # __init128
    o  # unsigned __init128
    g  # __float128
    P  # Coverity extension: pointer
    ```

    and lengths. For example,
    `--type_sizes w4x8li4s2P4`, sets type_sizes to "wide char
    4 bytes, long long 8, long & int 4, short 2, ptr 4".

    If unspecified, `cov-emit` uses the machine's native type
    sizes.

    The C standard mandates that `sizeof(char) == 1` and
    `sizeof(any other type) ==
    multiple of sizeof(char)`. Therefore, all type sizes should be specified as multiples of a
    char size (and `char` should always be size 1). To set the
    bit size of a `char`, see
    `--char_bit_size`.

    For example, assume you have a compiler that has the following:

    - `16-bit chars`
    - `16-bit shorts`
    - `32-bit ints`
    - `32-bit longs`

    The correct arguments for this compiler are:

    ```
    cov-emit --char_bit_size 16 --type_sizes st1ijlm2
    ```

    Note: Note that if this option specifies contradictory sizes for signed and
    unsigned versions of the same type, the last value specified will be used.
    For example, `--type_sizes i4j6` will set the length of "int"
    and "unsigned int" to 6, and the 4 will be ignored.

--wchar_t_keyword
:   Indicates that `cov-emit` should treat the type
    wchar_t as a keyword built into the language.

--wchar_t_name <identifier>
:   Uses the specified identifier for the `wchar_t` intrinsic
    type. This option does not imply `--wchar_t_keyword`.

--wchar_t_type <builtin-type>
:   Specifies the type `--wchar_t`, where `<builtin-type>` is one
    of the unsigned integral types shown in `--size_t_type`. For
    example, `--wchar_t_type j` sets the type of
    `wchar_t` to "unsigned int".

-U <identifier>
:   Undefine the macro `<identifier>`.
