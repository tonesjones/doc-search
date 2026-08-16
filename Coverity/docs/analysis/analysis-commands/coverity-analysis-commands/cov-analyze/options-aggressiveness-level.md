---
title: "Options: Aggressiveness level"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-aggressiveness-level.html"
content_id: "wMFNMepORbdcgyr~5xL6_A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:31.630953+00:00"
---

# Options: Aggressiveness level

--aggressiveness-level <level>
:   Enables a set of checker flags and `cov-analyze` options
    that cause Coverity Analysis to make more aggressive assumptions during
    analysis. Higher levels report more defects, and the analysis time
    increases. Values for level are low, medium, or high. Default is low.

    Starting in version 7.0, this option applies to all programming languages
    that undergo analysis with `cov-analyze`. If a checker
    option applies to multiple languages, the aggressiveness level tuning will
    apply to that option for all supported languages. Changes to checker options
    that do not apply to a given language have no effect or related
    warnings.

    The aggregate false positive rate for all checkers that are not parse
    warnings checkers is approximately 50% higher for medium, and 70% higher for
    high. Different aggressiveness levels do not change the rate of false
    positives that parse warning checkers report. A higher aggressiveness level
    for parse warning checkers enables more warnings for less severe
    defects.

    The value low uses the default for all checkers and options. For a list of checker option
    defaults, see the "Checker Enablement and Option Defaults by Language"
    table in the Coverity 2026.6.0 Checker Reference (HTML only).

    The value medium uses the settings at the low level with the overrides shown
    in the following table:

Table 1. Increasing aggressiveness from 'low' to 'medium'

| Checker | Option | Low → Medium | Languages |
| --- | --- | --- | --- |
| BAD_ALLOC_STRLEN | report_plus_any | false → true | C/C++, CUDA, Objective-C/C++ |
| BAD_EQ | stat_threshold | 80 → 70 | C# |
| CALL_SUPER | report_empty_overrides | false → true | C#, Visual Basic |
| threshold | 0.65 → 0.55 | C#, Java, Visual Basic |
| CHECKED_RETURN | error_on_use | false → true | C/C++, CUDA, Go, Java, Kotlin, Objective-C/C++ |
| stat_threshold | 80 → 55 | C/C++, CUDA, Go, Java, Kotlin, Objective-C/C++ |
| CONSTANT_EXPRESSION_​RESULT | report_bit_and_with_zero | false → true | C, C++, CUDA, Go, JavaScript, Objective-C/C++, Ruby, TypeScript |
| report_constant_logical_operands | false → true | C, C++, C#, CUDA, Go, Java, Kotlin, Objective-C/C++ |
| FORWARD_NULL | aggressive_null_sources | false → true | C#, C/C++, CUDA, Go, Java, JavaScript, Kotlin, Objective-C/C++, Python, TypeScript, Visual Basic |
| deref_zero_errors | false → true | C, C++, CUDA, Go, JavaScript, Objective-C/ C++, TypeScript |
| track_macro_nulls | false → true | C, C++ |
| INFINITE_LOOP | allow_asm | false → true | C, C++ |
| allow_pointer_derefs | false → true | C#, C/C++, CUDA, Go, Java, Kotlin, Objective-C/C++, Visual Basic |
| report_no_escape | false → true | C#, C/C++, CUDA, Go, Java, Kotlin, Objective-C/C++, Visual Basic |
| MISSING_RESTORE | report_restore_not_dominated_​by_​modify | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| report_uncorrelated_with_return | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| MIXED_ENUMS | report_anonymous_enums | false → true | C, C++, CUDA, Objective-C, Objective-C++ |
| NO_EFFECT | self_assign_to_local | false → true | C/C++, CUDA, JavaScript, Objective-C/C++, TypeScript |
| unsigned_enums | false → true | C, C++, Objective-C, Objective-C++ |
| NULL_RETURNS | allow_unimpl | false → true | C#, C/C++, CUDA, Go, Java, JavaScript, Objective-C/C++, TypeScript, Visual Basic |
| stat_bias | 3 → 10 | C#, Java, Visual Basic |
| 1 → 10 | JavaScript, TypeScript |
| 0 → 10 | C, C++, CUDA, Go, Objective-C, Objective-C++ |
| stat_include_max_checked | false → true | JavaScript, TypeScript |
| stat_min_checked | 1 → 0 | JavaScript, TypeScript |
| stat_threshold | 80 → 50 | C#, C/C++, CUDA, Go, Java, JavaScript, Objective-C/C++, TypeScript, Visual Basic |
| suppress_under_related_​conditional | true → false | C#, C, C++, CUDA, Go, Java, Objective-C/C++, Visual Basic |
| OS_CMD_INJECTION | distrust_all | false → true | C#, C/C++, CUDA, Go, Java, JavaScript, Kotlin, Objective-C/C++, Python, TypeScript, Visual Basic |
| OVERFLOW_BEFORE_WIDEN | check_macros | false → true | C, C++ |
| check_nonlocals | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| relaxed_operator_context | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| report_intervening_widen | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| OVERRUN | allow_array_of_uniform_​structs | true → false | C/C++, CUDA, Objective-C/C++ |
| report_bitand | true → false | C/C++, CUDA, Objective-C/C++ |
| report_scanf_unbounded_​input_string_length | true → false | C/C++, CUDA, Objective-C/C++ |
| report_underrun | false → true | C/C++, CUDA, Objective-C/C++ |
| PATH_MANIPULATION | distrust_all | false → true | C#, C/C++, CUDA, Go, Java, JavaScript, Kotlin, Objective-C/C++, Python, TypeScript, Visual Basic |
| RESOURCE_LEAK | allow_cast_to_int | false → true | C, C++ |
| allow_main | false → true | C, C++ |
| allow_overwrite_model | false → true | C, C++ |
| allow_unimpl | false → true | C, C++ |
| SIZEOF_MISMATCH | strict_memcpy | false → true | C/C++, CUDA, Objective-C/C++ |
| SQLI | distrust_all | false → true | C#, C/C++, CUDA, Go, Java, JavaScript, Kotlin, Objective-C/C++, Python, TypeScript, Visual Basic |
| TAINTED_SCALAR | tainting_byteswaps | false → true | C/C++, CUDA, Objective-C/C++ |
| UNINIT | check_arguments | false → true | C/C++, CUDA, Objective-C/C++ |
| enable_write_context | false → true | C/C++, CUDA, Objective-C/C++ |
| UNINIT_CTOR | report_scalar_arrays | false → true | C++, CUDA, Objective-C++ |
| UNREACHABLE | report_unreachable_empty_​increment | false → true | C#, Java, JavaScript, TypeScript, Visual Basic |
| UNUSED_VALUE | report_dominating_assignment | false → true | C#, C/C++, CUDA, Go, Java, Kotlin, Objective-C/C++ |
| report_unused_final_assignment | false → true | C#, C/C++, CUDA, Go, Java, Kotlin, Objective-C/C++ |
| report_unused_initializer | false → true | C#, C/C++, CUDA, Go, Java, Kotlin, Objective-C/C++ |
| USELESS_CALL | include_current_object_call_sites | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++, Rust |
| include_macro_call_sites_fn | false → true | C, C++ |
| include_macro_call_sites_plain | false → true | C, C++ |

The value high uses all the medium level settings, with the overrides shown in the
following table:

Table 2. Increasing aggressiveness from 'medium' to 'high'

| Checker | Option | Medium → High | Languages |
| --- | --- | --- | --- |
| BAD_EQ | stat_bias | 0.25 → 0.5 | C# |
| CONSTANT_EXPRESSION_​RESULT | report_bit_and_with_zero_​in_​macros | false → true | C, C++ |
| report_constant_logical_​operands_​in_macros | false → true | C, C++, C#, CUDA, Go, Java, Kotlin, Objective-C/C++ |
| report_unnecessary_op_​assign | false → true | C, C++, C#, CUDA, Go, Java, JavaScript, Objective-C/C++, Python, TypeScript |
| DC.DANGEROUS |  | false → true | Java, Kotlin |
| DC.DEADLOCK |  | false → true | Java, Kotlin |
| DC.PREDICTABLE_KEY_PASSWOROD |  | false → true | C/C++, CUDA, Objective-C/C++ |
| DC.STREAM_BUFFER |  | false → true | C/C++, CUDA, Objective-C/C++ |
| DC.STRING_BUFFER |  | false → true | C/C++, CUDA, Objective-C/C++ |
| DC.WEAK_CRYPTO |  | false → true | C/C++, CUDA, Objective-C/C++ |
| FORMAT_STRING_​INJECTION | paranoid | false → true | C/C++, CUDA, Objective-C/C++ |
| FORWARD_NULL | aggressive_derefs | false → true | C#, C/C++, CUDA, Go, Java, JavaScript, Kotlin, Objective-C/C++, Python, TypeScript, Visual Basic |
| as_conversion | false → true | C#, Visual Basic |
| INFINITE_LOOP | report_bound_type_​mismatch | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++, Visual Basic |
| suppress_in_macro | true → false | C, C++ |
| INTEGER_OVERFLOW | enable_deref_sink | false → true | C/C++, CUDA, Objective-C/C++, Rust |
| report_unsigned_overflow_immediately | false → true | C/C++, CUDA, Objective-C/C++, Rust |
| report_unsigned_underflow_cast_to_signed | true → false | C/C++, CUDA, Objective-C/C++, Rust |
| LOCK | track_globals | false → true | C/C++, CUDA, Go, Objective-C/C++ |
| MIXED_ENUMS | report_disjoint_enums | false → true | C/C++, CUDA, Objective-C/C++ |
| NESTING_INDENT_​MISMATCH | report_bad_indentation | false → true | C#, C/C++, CUDA, Java, JavaScript, Kotlin, Objective-C/C++, TypeScript |
| NO_EFFECT | report_useless_continue | false → true | C, C++, Objective-C, Objective-C++ |
| self_assign_in_macro | false → true | C, C++, Objective-C/C++ |
| NULL_RETURNS | stat_threshold | 50 → 0 | C#, C/C++, CUDA, Go, Java, JavaScript, Objective-C/C++, TypeScript, Visual Basic |
| OVERFLOW_BEFORE_WIDEN | check_bitwise_operands | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| check_types | `(?:unsigned )?long long|.*64.*` → `.*` | C, C++ |
| ignore_types | `s?size_t|off_t|time_t|__off64_t|ulong|.*32.*` → `^$` | C, C++ |
| general_operator_context | false → true | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| relaxed_operator_context | true → false | C#, C/C++, CUDA, Java, Kotlin, Objective-C/C++ |
| OVERRUN | aggressive_intervals_in_​callees | false → true | C/C++, CUDA, Objective-C/C++ |
| check_nonsymbolic_​dynamic | false → true | C/C++, CUDA, Objective-C/C++ |
| report_buffer_size_integer_arithmetic | false → true | C/C++, CUDA, Objective-C/C++ |
| report_sprintf_may_​overrun | false → true | C/C++, CUDA, Objective-C/C++ |
| REGEX_CONFUSION | report_character_hiding | false → true | Java, Kotlin |
| RESOURCE_LEAK | allow_address_taken | false → true | C, C++ |
| allow_constructor | false → true | C++ |
| allow_template | false → true | C++ |
| allow_virtual | false → true | C++ |
| STRING_NULL | report_string_copy_output | false → true | C/C++, CUDA, Objective-C/C++ |
| UNCAUGHT_EXCEPT | report_all_fun | false → true | C++, C#, CUDA, Objective-C++ |
| UNINIT | allow_unimpl | false → true | C/C++, CUDA, Objective-C/C++ |
| assume_loop_always_taken | true → false | C/C++, CUDA, Objective-C/C++ |
| check_malloc_wrappers | false → true | C/C++, CUDA, Objective-C/C++ |
| UNINIT_CTOR | allow_unimpl | false → true | C++, CUDA, Objective-C++ |
| UNREACHABLE | report_unreachable_in_​macro | false → true | C, C++ |
| URL_MANIPULATION | distrust_all | false → true | C, C++ |
| USE_AFTER_FREE | report_out_parameter_free | false → true | C, C++, CUDA, Objective C, Objective C++ |
| XPATH_INJECTION | distrust_all | false → true | C, C++ |
