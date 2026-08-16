---
title: "Options: C, C++, Objective-C, Objective-C++"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-c-c-objective-c-objective-c-.html"
content_id: "xP9cIjoNexzFwLFrqVIYyg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:35.854534+00:00"
---

# Options: C, C++, Objective-C, Objective-C++

--concurrency
:   [C, C++ analysis option] Enables C, C++ concurrency checkers that are
    disabled by default.

    For a list of concurrency checkers that you can enable with this option, see
    list-checkers.

--cpp
:   As of version 2022.9.0 this option has been deprecated.
    Use --tu-pattern lang("<lang>") instead.
    See Translation unit pattern matching for more details.

    [C, C++ analysis option] Filters by C, C++ translation units on which this
    command operates or reports. The command will fail with an informative error
    message if none of the translation units in the emit
    subdirectory match any of the specified language options in the intermediate
    directory.

--cxx
:   This option is deprecated and no longer has any effect. The corresponding
    checkers BAD_OVERRIDE, CTOR_DTOR_LEAK, DELETE_ARRAY, INVALIDATE_ITERATOR,
    PASS_BY_VALUE, UNCAUGHT_EXCEPT, UNINIT_CTOR, WRAPPER_ESCAPE, and, on
    Windows, COM.BAD_FREE and COM.BSTR.CONV, are now enabled by default.
    Checkers that can only find defects in C++ code automatically do not run on
    C code. Note that PASS_BY_VALUE can find defects in C code. If you were
    using `--disable-default --cxx`, replace it with individual
    `--enable` options.

--cxx-container-type-regex <regex>
:   Allows you to specify C++ container types for all checkers that look for
    them. The analysis will consider C++ classes whose name matches the
    specified <regex> to be container classes.

--disable-fnptr
:   [C, C++ analysis option] Disables analysis of calls to function pointers for
    defects. See also --enable-fnptr.

--disable-parse-warnings
:   [C, C++ analysis option] Disables all parse warnings, and override other
    arguments that might have enabled them, such as `--all` or
    `--enable-parse-warnings`. The order of command-line
    options is irrelevant; the `--disable-parse-warnings` option
    takes precedence.

--enable-exceptions
:   Enables exceptional control flow analysis for C++. If specified, this option
    will report the following type of resource leak as a defect:

    ```
    bool maybe;

    void test1() {
      int *x = new int;
      if (maybe) {
        throw 0; // x is leaked
      }
      delete x;
    }
    ```

    By default, the analysis ignores the exception type
    `std::bad_alloc` because some applications might not be
    designed to handle out-of-memory scenarios. If you specify
    `--enable-exceptions --handle-badalloc`, the analysis
    will report the following example as a defect. The example leaks memory if
    `new char` throws a `std::bad_alloc`
    exception:

    ```
    void test() {
      int *x = new int;
      char *y = new char; // Leaks 'x' if this throws std::bad_alloc
      delete y;
      delete x;
    }
    ```

    Note that defects are not limited to leaks. For example, the FORWARD_NULL
    checker finds the following defect:

    ```
    int *global;

    void foo() {
        int *y = 0;
        try {
            // if std::bad_alloc is thrown, y remains null
            global = new int;
            y = global;
        } catch (...) {
            // empty
        }
        *y = 1; //FORWARD_NULL defect.
    }
    ```

    This option is disabled by default for C++ but enabled by default for Java,
    Visual Basic, and C#.

    See also, --handle-badalloc.

--enable-fnptr
:   [C, C++ analysis option] Enables analysis of calls to function pointers for
    defects. By default, calls through function pointers are not used by the
    analysis engine for interprocedural analysis. When specified, this option
    allows up to 100 function resolutions for any function pointer. If that
    limit is exceeded, the analysis engine reverts to the default behavior.

    When using this option, the analysis time typically increases by approximately 20%. However,
    the false positive rate might increase. See also
    `--disable-fnptr`.

--enable-parse-warnings
:   [C, C++ analysis option] Enables parse warnings, recovery warnings, and
    semantic warnings that are produced by the `cov-build`
    command so that they appear as defects in Coverity Connect. See also
    `--parse-warnings-config`.

    This option is set automatically if the
    `--aggressiveness-level` option is set to
    `medium` (or to `high`).

--field-offset-escape
:   [C++ analysis option] A pointer escapes the analysis if it is written to
    memory, passed to `free()`, or passed to a function
    definition that is inaccessible to `cov-analyze`. Once the
    pointer escapes the analysis, the storage to which it points will never be
    treated as a leak or uninitialized.

    This option eliminates certain false positives in C++ by making the analysis
    treat `&v->field` as an alias for `v`
    because some programs exploit the fact that `(&v->field) -
    offsetof(typeof(v), field) == v` to free `v`
    given `&v->field`.

    By default, this heuristic applies to only to C code (but not C++). This
    option enables this heuristic for C++, as well.

    See also, `--no-field-offset-escape`.

--fnptr-models
:   [C, C++ analysis option] Enables function pointer models if the analysis
    fails to analyze certain function pointers calls. You can enable analysis of
    calls to function pointers, without requiring explicit models, using the
    --enable-fnptr option.
    For more information and examples, see
    "Model for function pointers" in
    the Customizing Coverity.

--handle-badalloc
:   [C, C++ analysis option] Causes the analysis as a whole to handle exceptions
    of type `std::bad_alloc`, both for exceptional control flow
    and for UNCAUGHT_EXCEPT. By default, such exceptions are otherwise ignored
    even when you use `--enable-exceptions`.

    For an example, see `--enable-exceptions`.

--hfa
:   [C-only analysis option] Reports unnecessary header file includes. For more
    information, see "HFA" in the Coverity 2026.6.0 Checker Reference.

    The `--all` option does not enable this checker.

--inherit-taint-from-unions
:   Enable taint to flow downwards from a C, C++ union to its component fields.
    This is required to check code that writes to a union using
    `memcpy(&u, &tainted, n)` and later reads using
    `u.field`.

    Affects security checkers "TAINTED_SCALAR"
    and "INTEGER_OVERFLOW"
    (see Coverity 2026.6.0 Checker Reference for details).

--no-field-offset-escape
:   [C, C++ analysis option] Disables a heuristic that can cause RESOURCE_LEAK
    and UNINIT to produce false negatives when tracking aliases of pointers.

    A pointer escapes the analysis if it is written to memory, passed to
    `free()`, or passed to a function whose definition is
    inaccessible to `cov-analyze`. Once the pointer escapes
    analysis, the storage to which it points will never be considered leaked or
    uninitialized.

    To eliminate false positives in C code (but not C++ code), the analysis
    considers `&v->field` to be an alias for
    v because some programs exploit the fact that
    `(&v->field) - offsetof(typeof(v), field) == v` to
    free v given `&v->field`.

    If a program does not use this idiom, this heuristic might lead to false
    negatives. For example, if you call
    `myfunction(&v->field)` when this heuristic is
    enabled, the analysis assumes that v escapes, so the
    analysis will not catch a RESOURCE_LEAK or UNINIT on v.
    This option disables the application o f that heuristic.

    This option is set automatically if the
    `--aggressiveness-level` option is set to
    `medium` (or to `high`).

--parse-warnings-config <filename>
:   [C, C++ analysis option] Specifies the name for the configuration file, which
    allows you to change the parse warnings that pass through a warning filter.
    For a sample, see config/parse_warnings.conf.sample.
    See also `--enable-parse-warnings`.

    To use the parse warnings configuration file (`--parse-warnings-config <config_file_name>`) in the response file,
    replace any white space that precedes the file name with an equals sign ( `=` ); for example:

    ```
    parse-warnings-config=standard_parse_warnings.conf
    ```

    (If you don't replace the white space, Coverity Analysis reports an error.)

    Alternatively, you can put the configuration file name on a line of its own.

--rule
:   [C, C++ analysis option] Enables rule checkers.

    For a list of rule checkers, you can use list-checkers.

--security
:   [C, C++ and Objective-C, Objective-C++ analysis option] Enables C, C++,
    Objective-C and Objective-C++ security-related checkers.

    For a list of the security checkers to which this option applies, you can use
    --list-checkers.

--enable-single-virtual
:   Enables single, virtual-call resolution. By default, a C++ analysis treats
    all virtual functions as unimplemented, whereas full virtual call resolution
    is enabled by default for Java, Visual Basic, and C# analyses. When this
    option is enabled, interprocedural analysis across virtual calls takes place
    when the analysis engine finds only one implementation of a virtual
    function. When the analysis engine finds more than one implementation, it
    assumes that the virtual function is unimplemented. Do not specify this
    option if you specify the `--enable-virtual` option.

    A C++ analysis can take longer than the default analysis because the analysis
    engine looks at implementations of virtual functions, which can result in
    more defect reports. Although using this option might expedite Java, Visual
    Basic, and C# analyses, it also significantly affects results for
    interprocedural checkers.

    Specify this option, or `--enable-virtual`, to enable
    interprocedural analysis of Apple Block invocations in C and C++ code.

    Starting in version 7.0, applies to all programming languages.

--enable-virtual
:   Enables full, virtual-call resolution. By default, a C++ analysis treats all
    virtual functions as unimplemented, whereas full virtual call resolution is
    enabled by default for Java and C# analyses. When specified, this option
    allows up to 100 function resolutions for any virtual method. If that limit
    is exceeded, the analysis engine reverts to the default behavior.

    Do not use this option if you specify the
    `--enable-single-virtual` option. The analysis can take
    significantly longer than the default or when the
    `--enable-single-virtual` option is enabled because the
    analysis engine looks at all implementations of virtual functions, which can
    result in more defect reports.

    Specify this option, or `--enable-single-virtual`, to enable
    interprocedural analysis of Apple Block invocations in C and C++ code.

    Note: To make the analysis resolve to a model of a virtual or pure virtual
    function without using `--enable-virtual`, see
    "Model for
    analyzing models of virtual functions" in the Customizing Coverity.
