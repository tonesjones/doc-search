---
title: "Using predefined macros for Coverity Analysis-specific compilations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-predefined-macros-for-coverity-analysis-specific-compilations.html"
content_id: "d4Mwj3MGBHKYo5cy19EDMA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:52.743138+00:00"
---

# Using predefined macros for Coverity Analysis-specific compilations

Predefined macros are preprocessor macros that are automatically defined by a compiler.
Coverity defines the predefined macros listed in the following table. These macros are
defined only when source code is being translated by Coverity; they are not defined
during compilation by a native compiler. You can use these macros to conditionalize code
so that the code is different when it is translated by Coverity than when it is compiled
by the native compiler.

You can use these macros for multiple purposes. Here are some examples:

- Define a macro differently for the purpose of static analysis.
- Workaround differences in parsing between Coverity and a native compiler.
- Guard Coverity `pragma` directives (see "Annotating
  compliance deviations" in the Customizing Coverity).

The following example demonstrates use of the `__COVERITY__`  predefined
macro to define a `logical_assert` macro differently for Coverity than
for the native compiler. Doing so enables static analysis to better detect potential
problems in the source code.

```
#ifdef __COVERITY__
#define logical_assert(x) (assert(x);)
#else
#define logical_assert(x) (if (!x) printf("Variable is null!");)
#endif
```

| Macro | Meaning |
| --- | --- |
| `__COVERITY__` | Defined as the integer value `1` when the source code is being translated by Coverity. |
| `__COVERITY_CLANG__` | Defined as the integer value `1` when the source code is being translated by `cov-internal-emit-clang`. |
| `__COVERITY_EDG__` | Defined as the integer value `1` when the source code is being translated by `cov-emit`. |
| `__COVERITY_HOTFIX__` | Defined to an integer value representing the Coverity hotfix release level. For release 2021.03-4.5, this macro has the value `5`. |
| `__COVERITY_MAINTENANCE__` | Defined to an integer value representing the Coverity maintenance release level. For release 2021.03-4.5, this macro has the value `4`. |
| `__COVERITY_MAJOR__` | Defined to an integer value representing the Coverity major release level. For release 2021.03-4.5, this macro has the value `2021`. |
| `__COVERITY_MINOR__` | Defined to an integer value representing the Coverity minor release level. For release 2021.03-4.5, this macro has the value `3`. |
| `__COVERITY_PREPROCESSOR__` | Defined as the integer value `1` when the source code is being preprocessed by the Coverity preprocessor. This macro is useful when the `cov-build --preprocess-first` or `--preprocess-next` options are being used for source code that is sensitive to differences between the native compiler preprocessor and the Coverity preprocessor. |
| `__COVERITY_PTR_DIFF_TYPE__` | Defined as the underlying type of the `ptrdiff_t` type that is used for pointer subtraction, for example, `long int`. This macro is useful for conditional code that requires the underlying type when the `ptrdiff_t` typedef is not available. The value of this macro depends on compiler configuration. |
| `__COVERITY_SIZE_TYPE__` | Defined as the underlying type of the `size_t` type that is used for the type of the `sizeof` operator, for example, `unsigned long int`. This macro is useful for conditional code that requires the underlying type when the `size_t` typedef is not available. |
| `__COVERITY_VERSION__` | Defined to an integer value representing the Coverity release version. The integer value has the format `MMMMNNCCHH` where `M`, `N`, `C`, and `H` correspond to the major, minor, maintenance, and hotfix release levels respectively. For release 2021.03-4.5, this macro has the value `2021030405`. |
