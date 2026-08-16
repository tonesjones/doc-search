---
title: "Test tags"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/test-tags.html"
content_id: "GaBj00RtjyVxE5L2m3xRcQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:14.363995+00:00"
---

# Test tags

The following tags are used to configure basic test for your compiler through the
<compiler>_config.xml file. Not all of the tests are enabled
by default. To ensure that the tests are enabled or disabled, explicitly specify the
test in the format, `<test>true|false</test>`.

<custom_test>
:   Probes for arbitrary switches using custom code. For
    example:

    ```
    <custom_test>
         <source>
            int __global;
         </source>
         <prepend_arg>--no_sun_linker_scope</prepend_arg>
    </custom_test>
    ```

<disable_comp_tests>
:   When set to `true`, all compiler probes are disabled by default, but may be
    individually enabled using the other tags described in this section. Defaults to
    `false` when no setting is specified.

<test_128bit_ints>
:   Tests whether or not 128-bit ints are enabled. This test is disabled by default.

<test_alternative_tokens>
:   Tests whether or not alternative tokens are in use. This test is disabled by default.

<test_altivec>
:   Probes for altivec extension support and adds the appropriate compiler switches. This test
    is disabled by default.

<test_arg_dependent_overload>
:   Tests whether or not function overloading is argument dependent. This test is disabled by
    default.

<test__Bool>
:   Determines whether or not `_Bool` is a keyword in GNU mode. This test is
    disabled by default.

<test_c99>
:   Tests to determine whether or not c99 mode is on by default. This test is disabled by
    default.

    Note: This tag is deprecated, and will be removed in a future
    release. It is replaced by the `<test_c_version>`
    tag.

<test_c_version>
:   Tests to determine whether or not c99 mode is on by default. This test is disabled by
    default.

<test_char_bit_size>
:   Tests to determine the bit width of a single character. If the probe is disabled or the
    tests are inconclusive, defaults to 8 bits. This test is enabled by
    default.

<test_const_string_literals>
:   Tests whether or not string literals are `const char *` or `char
    *`. This test is disabled by default.

<test_cr_term>
:   Test whether carriage return characters (`\r`) are treated as line
    terminators. This test is enabled by default.

<test_csharp6>
:   Test whether the compiler supports C#6 features. This test is enabled by default.

<test_cygwin>
:   Test whether the compiler is Cygwin-aware and can understand Cygwin-style paths. Only
    applicable on Windows platforms. This test is disabled by default.

<test_declspec>
:   Tests for the presence of `__declspec` is present in the native compiler, and
    whether it is as a macro or a keyword. This test is enabled by default.

<test_exceptions>
:   Tests whether the native compiler supports exceptions by default in C++ modes. This test is
    disabled by default.

<test_gnu_version>
:   Checks to see if GCC derived compilers support extensions added by GCC. This test is
    disabled by default.

<test_ignore_std>
:   Tests whether the native compiler ignores the `std:: namespace`, that is,
    whether it can directly use the names without specifying using `namespace
    std;`. This test is enabled by default.

<test_include_path>
:   Attempt to determine the compiler's include search paths by probing its behavior. This test
    is enabled by default.

<test_include_paths_with_strace>
:   Attempt to determine the compiler's `include` search paths by probing its
    behavior with `strace`. This test is enabled by default.

<test_incompat_proto>
:   Tests whether the compiler accepts incompatible prototypes. Incompatible prototypes still
    need to have compatible return types. This test is disabled by default.

<test_inline_keyword>
:   Tests for the presence of the ISO C99 `inline` keyword in the native
    compiler. Enabled by default.

<test_macro_stack_pragmas>
:   Tests whether or not the compiler supports macro stack pragmas. This test is enabled by
    default.

<test_multiline_string>
:   Tests whether the native compiler tolerates newlines within a string. For
    example:

    ```
    char *c = "Hello
        World";
    ```

    This test is disabled by default.

<test_new_for_init>
:   Tests whether the native compiler uses modern C++ `for` loop scoping rules,
    or the old Cfront-compatible scoping rules. For
    example:

    ```
    {
        for (int i = 0; i < a; ++i) { }
        for (int i = 0; i < a; ++i) { }
    }
    ```

    This code is valid in modern C++, since the scope of the
    '`i`' in the first loop ends at the closing brace. However,
    compilers that implement the old scoping rules will usually issue an error:
    '`i`' is in scope for the entire enclosing block after its
    declaration, and the second loop redeclares it. This test is disabled by
    default.

<test_old_style_preprocessing>
:   Tests whether macros are checked for number of arguments before expansion. This test is
    disabled by default.

<test_restrict_keyword>
:   Test whether the compiler supports the `restrict` keyword. This test is
    enabled by default.

<test_rtti>
:   Tests whether or not the native compiler supports RTTI by default. This test is disabled by
    default.

<test_size_t>
:   Test whether the compiler intrinsically supports the `size_t` type. This test
    is enabled by default.

<test_stdarg?
:   Test whether the compiler intrinsically supports types and functions from the
    `<stdarg.h>` header. This test is enabled by default.

<test_target_platform>
:   Determines the code instrumentation target platform by examining the platform macros
    expanded by the native compiler. This test is disabled by default. The allowed
    values for platform are `x64`, `x86`, and
    `all`. For example, with the follow tags the code
    instrumentation target platform is set to x64 if the macro
    `_M_AMD64` is defined by the native
    compiler.

    ```
    <platform_if_macro>
         <macro_name>_M_AMD64</macro_name>
         <platform>x64</platform>
    </platform_if_macro>
    ```

<test_trigraphs>
:   Tests whether or not trigraphs are supported by the compiler. This test is disabled by
    default.

<test_type_size>
:   Runs tests for basic data types to determine their respective sizes and alignments. This
    test is enabled by default.

<test_type_size_powers_of_two_only>
:   The same as `<test_type_size>`, but assumes power of two sizes. Makes
    `cov-configure` finish the tests slightly faster. This test
    is disabled by default. If enabled,
    `<test_type_size_powers_of_two_only>` will only take
    effect if `<test_type_size>` is also enabled.

<test_type_traits_helpers>
:   Tests whether or not the native compiler has type traits helpers enabled by default. This
    test is disabled by default.

<test_vector_intrinsics>
:   Tests whether the native compiler supports various vector type intrinsics, such as the
    `__vector` keyword. This test is disabled by default.

<test_wchar_t>
:   Tests for the presence of the `wchar_t` keyword in the native compiler. This
    test is enabled by default.

<test_x86_calling_conventions>
:   Enables or disables tests to determine whether the compiler supports and enforces x86
    calling convention specifications. When disabled, the compiler is assumed to
    enforce calling conventions.

    These tests are disabled by default.

<use_gnu_version_macro>
:   When `test_gnu_version` is enabled, this tag determines how the compiler is
    probed to determine the GNU compiler version. When set to `true`,
    the GNU intrinsic version macros are used (i.e., `__GNUC__`,
    `__GNUC_MINOR__` and `__GNUC_PATCHLEVEL__`).
    When unset or explicitly set to `false`, a heuristic approach is
    used to determine the GNU version.
