---
title: "C/C++ function annotations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-function-annotations.html"
content_id: "xyY1yauqYrzREaRJGdsEqQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:21.316536+00:00"
---

# C/C++ function annotations

You can enhance automatically generated models by adding function annotations to your
source, and you can enhance your custom models in the same way.

A function annotation's format is similar to a that of a code-line annotation:
It appears at the beginning of a C comment (`/* coverity[+...]...` )
or a C++ comment (`//coverity[+...]...` ) and before the function
definition. The function annotation applies to the function definition that follows
it.

For example, the following annotation specifies that all paths through
`special_abort()` are killpaths:

```
//coverity[+kill]
void special_abort(const char* msg)  {
    ...
}
```

When a specified behavior affects all the paths of a function, you can use function
annotations instead of calls to modeling primitives such as
`__coverity_panic__()` or
`__coverity_alloc__()`.

## Suppressing a model

When you precede a function annotation tag with a minus-sign
(`coverity[-tag_name]`*)*, this suppresses the
function's model instead of enhancing it.

For example, the following code suppresses the allocation behavior of
`my_alloc1()`:

```
//coverity[-alloc]
void* my_alloc1(size_t size) {
    return malloc(10);
}
```

In this case, Coverity Analysis
*will not check* that the memory allocated by calling
`my_alloc1()` is freed. This might be useful, for instance, if
the code is allocating memory for global variables, and this memory is not freed
until the program terminates.

You can use all the tags listed in the following subsection with the suppressing
function annotation.

## Function annotation tags

The following tags can appear within `coverity[...]` in a function
annotation and can help suppress false positives:

`+alloc / -alloc`
:   Specifies that a function does / does not return allocated memory or store
    allocated memory in an argument.

    As an example of an allocation function
    annotation, the annotation in the following code specifies that
    `my_alloc()` always returns memory:

    ```
    //coverity[+alloc]
    void* my_alloc(size_t size) {
        ...
    }
    ```

    When a function annotation specifies that memory is always allocated to a
    dereference of a function's `n` position argument,
    you must include the string `arg-*n` after a colon that
    follows the annotation's tag. Arguments are numbered
    `0..n` as they appear from left to right.

    For example, the annotation in the following code specifies that
    `my_alloc()` always assigns memory to its
    dereferenced zero-position argument (`p`).

    ```
    //coverity[+alloc : arg-*0]
    void my_alloc0(void **p, size_t size) {
        ...
    }
    ```

`+free / -free`
:   Specifies that a function does / does not free memory passed in as an
    argument.

    Function annotations with the `+free` tag must always
    specify an argument, which is assigned the memory to be freed. Whether
    this argument is dereferenced is optional. The notation for specifying
    an argument is the same as for the `+alloc` tag: Include
    the string `arg-*n` after a colon that follows the
    annotation's tag. Arguments are numbered `0..n` as
    they appear from left to right.

    For example, the following code specifies that `my_free()`
    always frees memory assigned to its #1-position argument
    (`memory_to_free`) without a dereference:

    ```
    //coverity[+free : arg-1]
    void my_free(void** arg, void* memory_to_free) {
        ...
    }
    ```

`+kill / -kill`
:   Specifies that a function does / does not abort.

`+no_checked_return / -no-checked-return`
:   When active, labels a function so that the inconsistent checking of its return value
    *will not* generate CHECKED_RETURN defects.
    This can reduce the number of false positive reports.

`+returnsnull / -returnsnull`
:   Specifies that a function might / might not return `NULL`.
    In the positive case, the return value must be verified to be
    non-`NULL` before it is dereferenced.

    For example, the `+returnsnull` annotation in the
    following code specifies that the value of `fetch_ptr`
    should always be verified. Unverified values will be reported by the
    NULL_RETURNS checker (and do not depend on statistical analysis).

    ```
    //coverity[+returnsnull]
    int* fetch_ptr(int idx) {
        ...
    }
        
    void caller() {
        int * p = fetch_ptr(0);
        *p = 0;                 // NULL_RETURNS defect
    }
    ```

    Conversely, the `-returnsnull` function annotation can be
    used to suppress defect reports from NULL_RETURNS. A value returned by a
    function with the negative annotation will not be reported by the
    checker even if the value is in fact `NULL`.
