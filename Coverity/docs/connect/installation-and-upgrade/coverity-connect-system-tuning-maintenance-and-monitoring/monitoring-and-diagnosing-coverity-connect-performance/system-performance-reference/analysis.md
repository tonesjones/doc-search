---
title: "Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis.html"
content_id: "UYA4kgBE8qwE4OU99ohNzQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:21.379493+00:00"
---

# Analysis

```
13:32:28 Analysis summary report:
13:32:28 ------------------------
13:32:28 Files analyzed                 : 4425
13:32:28 Total LoC input to cov-analyze : 2858216
13:32:28 Functions analyzed             : 84963
13:32:28 Paths analyzed                 : 6174509
13:32:28 Time taken by analysis         : 00:19:13
13:32:28 Defect occurrences found       : 4539 Total
13:32:28                                     1 ALLOC_FREE_MISMATCH
13:32:28                                    50 ARRAY_VS_SINGLETON
13:32:28                                     1 ASSERT_SIDE_EFFECT
13:32:28                                   154 ATOMICITY
13:32:28                                     3 BAD_COMPARE
13:32:28                                     9 BAD_FREE
13:32:28                                     2 BAD_SIZEOF
13:32:28                                    21 BUFFER_SIZE
13:32:28                                    48 BUFFER_SIZE_WARNING
13:32:28                                   251 CHECKED_RETURN
13:32:28                                   100 CONSTANT_EXPRESSION_RESULT
13:32:28                                    16 COPY_PASTE_ERROR
13:32:28                                   280 DEADCODE
13:32:28                                    30 DIVIDE_BY_ZERO
13:32:28                                    51 EVALUATION_ORDER
13:32:28                                   426 FORWARD_NULL
13:32:28                                    15 INCOMPATIBLE_CAST
13:32:28                                     6 INFINITE_LOOP
13:32:28                                    73 INTEGER_OVERFLOW
13:32:28                                   151 LOCK
13:32:28                                   255 MISSING_BREAK
13:32:28                                   242 MISSING_LOCK
13:32:28                                     9 MIXED_ENUMS
13:32:28                                    25 NEGATIVE_RETURNS
13:32:28                                    20 NESTING_INDENT_MISMATCH
13:32:28                                   406 NO_EFFECT
13:32:28                                   103 NULL_RETURNS
13:32:28                                    23 ORDER_REVERSAL
13:32:28                                    28 OVERFLOW_BEFORE_WIDEN
13:32:28                                   317 OVERRUN
13:32:28                                     2 PASS_BY_VALUE
13:32:28                                    10 PW.ASSIGN_WHERE_COMPARE_MEANT
13:32:28                                     1 PW.BOOLEAN_CONTROLLING_EXPR_IS_CONSTANT
13:32:28                                     6 PW.BRANCH_PAST_INITIALIZATION
13:32:28                                    12 PW.CONVERSION_TO_POINTER_ADDS_BITS
13:32:28                                     8 PW.INCLUDE_RECURSION
13:32:28                                     2 PW.MISSING_INITIALIZER_ON_CONST
13:32:28                                    52 PW.PARAMETER_HIDDEN
13:32:28                                     5 PW.PARAM_SET_BUT_NOT_USED
13:32:28                                    54 PW.POINTER_CONVERSION_LOSES_BITS
13:32:28                                    17 PW.SIGNED_ONE_BIT_FIELD
13:32:28                                     2 PW.SWITCH_SELECTOR_EXPR_IS_CONSTANT
13:32:28                                     2 PW.USELESS_TYPE_QUALIFIERS
13:32:28                                   135 RESOURCE_LEAK
13:32:28                                     2 RETURN_LOCAL
13:32:28                                   168 REVERSE_INULL
13:32:28                                    13 REVERSE_NEGATIVE
13:32:28                                    61 SIGN_EXTENSION
13:32:28                                     9 SIZECHECK
13:32:28                                    20 SIZEOF_MISMATCH
13:32:28                                     1 STACK_USE
13:32:28                                     5 STRAY_SEMICOLON
13:32:28                                     8 STRING_NULL
13:32:28                                     1 STRING_SIZE
13:32:28                                     3 SWAPPED_ARGUMENTS
13:32:28                                   355 TAINTED_SCALAR
13:32:28                                     4 TAINTED_STRING
13:32:28                                     7 TOCTOU
13:32:28                                   199 UNINIT
13:32:28                                    32 UNREACHABLE
13:32:28                                   114 UNUSED_VALUE
13:32:28                                    85 USE_AFTER_FREE
13:32:28                                    14 VARARGS
13:32:28 
13:32:28 cov-analyze: 1153 seconds.
```
