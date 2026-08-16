---
title: "Concurrency models"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/concurrency-models.html"
content_id: "Ujk4tEXLYXVAec_8DjHUvQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:35.757381+00:00"
---

# Concurrency models

Concurrency checkers support functions for various standard libraries. It is also
possible to write custom concurrency models.

## Library functions

The concurrency checkers support locking functions as used by the Linux™ kernel, POSIX® Threads (*pthreads),* and so on.

## Adding models for concurrency checking

The concurrency models that install with Coverity Analysis are
declared in the file <install_dir>/library/primitives.h.

Note:
When modeling concurrency code that involves locks, you need to model the
acquisition and release of the lock. For example, your models should include calls
to both the `__coverity_exclusive_lock_acquire__( void *lock )` and
`__coverity_exclusive_lock_release__( void *lock )` primitives.

This practice avoids false positive reports by the LOCK checker.

When you use `cov-make-library` to generate the models, make
sure to use the `--concurrency` option, as shown in the section that
follows.

For descriptions of all the concurrency primitives, see
C/C++ concurrency primitives.

## Example of a new concurrency model

If you have a function other than those in the standard libraries that the
concurrency checker supports, you can add a stub function that models the custom
function's behavior. For example, if you have an exclusive lock function called
`custom_lock()`, you can write a model for it that might have the
following code:

```
void custom_lock(void **l) {
    __coverity_exclusive_lock_acquire__(*l);
}
```

To model releasing the lock, you might write a model as follows:

```
void custom_unlock(void **l) {
    __coverity_exclusive_lock_release__(*l);
}
```

You can then use the following command lines to generate the models and add them to
user_models:

```
> cov-make-library --output-file user_models --concurrency custom_lock.c
> cov-make-library --output-file user_models --concurrency custom_unlock.c
```

These models indicate that the `custom_lock()` function locks the
dereference of its first parameter, and the `custom_unlock()`
function releases that lock. This pattern holds for other concurrency management
functions, which are passed a pointer to the lock (`l`) data
structure.
