---
title: "Example: Override a default C model"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-override-a-default-c-model.html"
content_id: "1qtVJ1Tv4LYCJVvHbfFijQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:31.828313+00:00"
---

# Example: Override a default C model

As a simple example, suppose that you want to override the default model for the function
`malloc()` such that it returns allocated memory but it can never
return `NULL`.

To do so, create a file named
my_memory_allocators.c, in which you put the new definition of
the `malloc()` function. The new model of `malloc()` is as follows:

```
void *malloc(unsigned n) {
    return __coverity_alloc__(n);
}
```

The primitive `__coverity_alloc__()` models returning a block of
dynamically allocated memory, but it does not return a `NULL` pointer in
any case. As a point of reference, here is the built-in model for
`malloc()`: This version of the model does return
`NULL` in the out-of-memory case:

```
void *malloc(size_t size) {
    int has_memory;
    __coverity_negative_sink__(size);
    if(has_memory)
        return __coverity_alloc__(size);
    else
        return 0;
}
```

The default model for `malloc()` also indicates that the size parameter
should not be negative. Also, the model simulates the out-of-memory behavior by
switching on the uninitialized variable `has_memory`. Doing so allows Coverity Analysis to assume
that any call to `malloc()`
could return either `NULL` or non-`NULL`. Because this
code for `malloc()` is only a model, it does not matter that this code is
not "correct" C programming.

To install this new model of `malloc()`, compile this file into the library
format read by the analysis:

```
> cov-make-library --output-file memory_models my_memory_allocators.c
```

After updating the library, the following test case no longer reports a
NULL_RETURNS defect if you invoke
`cov-analyze` with a command-line switch that points to the
generated models.

(There is a pointer leak at the end of `test()`, when `p` is no longer defined,
and a file leak when `fopen()` exits.)

```
typedef struct _FILE {

} FILE;

void test() {
    FILE* f = 0;
    int *p = (int*)malloc(10);
    *p = 0;                        // Leak the pointer.

    f = fopen("file.txt", "w");    // Leak the file.
}
```

The following command line ensures the current models are used:

```
> cov-analyze --dir /tmp/tmp-intermediate  \
--user-model-file memory_models
```

Tip:
You do not have to put all your models into a single file. The
`cov-make-library` command can take any number of files on
the command line.
