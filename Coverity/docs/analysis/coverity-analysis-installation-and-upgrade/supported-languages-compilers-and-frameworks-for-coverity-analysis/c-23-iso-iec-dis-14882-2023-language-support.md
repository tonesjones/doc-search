---
title: "C++23 (ISO/IEC DIS 14882:2023) language support"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-23-iso/iec-dis-14882-2023-language-support.html"
content_id: "pNuE2VWdGHzBFCrVNoJ1CA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:02.720642+00:00"
---

# C++23 (ISO/IEC DIS 14882:2023) language support

The following table describes Coverity support for specific proposals incorporated into
the ISO/IEC DIS 14882:2023 draft standard, colloquially known as C++23. Values that appear in the **Support level** column, have
the following meanings:

- Full – Fully supported and known to be working without major issues for all supported compilers. May interact poorly
  with other unsupported or partially supported features.
- Partial – Partially supported. Most uses cases are expected to work, but there are
  known issues that customers might encounter and the feature may not be supported for all compilers.
- Not Supported - The feature is known to have major issues or limitations that hinder
  its use in the current version.
- Unevaluated - The feature has not yet undergone any rigorous evaluation to determine
  its proper support status.

Table 1. C++23 core language features

| Number | Summary | Support level |
| --- | --- | --- |
| P1102R2 | Permit removing unnecessary `()`'s from C++ lambdas | Full |
| P1938R3 | `if consteval` | Full |
| P2242R3 | Non-literal variables (and labels and `goto` instructions) in `constexpr` functions | Full |
| P0849R8 | `auto(x)` and `auto{x}` | Partial |
| P0330R8 | Literal suffix for (signed) `size_t` | Unevaluated |
| P2186R2 | Removing garbage collection support | Unevaluated |
| P1949R7 | DR: C++ identifier syntax using Unicode standard annex 31 | Unevaluated |
| P2156R1 | DR: Allow duplicate attributes | Unevaluated |
| P1401R5 | Narrowing contextual conversions in `static_assert` and `constexpr if` | Unevaluated |
| P2223R2 | Trimming whitespaces before line splicing | Unevaluated |
| P1847R4 | Make declaration order layout mandated | Unevaluated |
| P2201R1 | Removing mixed wide string literal concatenation | Unevaluated |
| P0847R7 | Explicit object parameter (deducing this) | Unevaluated |
| P2036R3 | Change scope of lambda trailing-return-type | Unevaluated |
| P2334R1 | `#elifdef` and `#elifndef` | Unevaluated |
| P2316R2 | Consistent character literal encoding | Unevaluated |
| P2314R4 | Character sets and encodings | Unevaluated |
| P2360R0 | Extend init-statement (of `for` loop) to allow alias-declaration | Unevaluated |
| P2128R6 | Multidimensional subscript operator | Unevaluated |
| P2173R1 | Attributes on lambdas | Unevaluated |
| P2493R0 | DR: Adjusting the value of feature-test macro `__cpp_concepts` | Unevaluated |
| P2437R1 | `#warning` | Unevaluated |
| P2362R3 | Remove non-encodable wide character literals and multicharacter wide character literals | Unevaluated |
| P2324R2 | Labels at the end of compound statements | Unevaluated |
| P2290R3 | Delimited escape sequences | Unevaluated |
| P2071R2 | Named universal character escapes | Unevaluated |
| P2448R2 | Relaxing some `constexpr` restrictions | Unevaluated |
| P2266R3 | Simpler implicit move | Unevaluated |
| P1169R4 | `static operator()` | Unevaluated |
| P1467R9 | Requirements for optional extended floating-point types | Unevaluated |
| P2582R1 | Class template argument deduction from inherited constructors | Unevaluated |
| P1774R8 | Attribute `[[assume]]` | Unevaluated |
| P2295R6 | Support for UTF-8 as a portable source file encoding | Unevaluated |
| P2327R1 | DR: De-deprecating `volatile` bitwise compound assignment operations | Unevaluated |
| P2460R2 | DR: Relax requirements on `wchar_t` to match existing practices | Unevaluated |
| P2280R4 | DR: Using unknown pointers and references in `constant` expressions | Unevaluated |
| P2468R2 | DR: The equality operator you are looking for | Unevaluated |
| P2513R4 | DR: `char8_t` compatibility and portability fix | Unevaluated |
| P2589R0 | `static operator[]` | Unevaluated |
| P2647R1 | Permitting `static constexpr` variables in `constexpr` functions | Unevaluated |
| P2718R0 | Extending the lifetime of temporaries in range-based `for` loop initializer | Unevaluated |
| P2615R0 | DR: Meaningful `export` declarations | Unevaluated |
| P2564R0 | DR: `consteval` needs to propagate up | Unevaluated |
