---
title: "C/C++ concurrency primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-concurrency-primitives.html"
content_id: "IKZ4ve50iwfYoAlJBUFJjQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:43.258699+00:00"
---

# C/C++ concurrency primitives

These primitives represent conditions for managing concurrent execution.

## `__coverity_assert_locked__( void *lock )`

Assert that lock `lock` is held.

## `__coverity_exclusive_lock_acquire__( void *lock )`

Indicates that the exclusive lock `lock` is acquired.

## `__coverity_exclusive_lock_release__( void *lock )`

Indicates that the exclusive lock `lock` is released.

## `__coverity_lock_alias__( void *proxy, void *lock )`

Indicates, in a constructor, that a wrapper class is a proxy for operations on the
real lock.

For example:

```
struct Lock;
struct AutoLock {
    nsAutoLock(Lock *a) {
        __coverity_lock_alias__(this, a);
        __coverity_exclusive_lock_acquire__(this);
    }
    ~nsAutoLock() {
        __coverity_exclusive_lock_release__(this);
    }
    void lock() {
        __coverity_exclusive_lock_acquire__(this);
    }
    void unlock() {
        __coverity_exclusive_lock_release__(this);
    }
};
```

## `__coverity_recursive_lock_acquire__( void *lock )`

Indicates that the recursive lock `lock` is acquired.

## `__coverity_recursive_lock_release__( void *lock )`

Indicates that the recursive lock `lock` is released.

## `__coverity_sleep__( void )`

Indicates that the calling function might take a long time to complete or otherwise
block.

## `__coverity_thread_unsafe_function__( void )`

A call to this primitive in the model for a function indicates that calling the function from multiple concurrent contexts is an error.
This issue will be reported by the UNLOCKED_ACCESS checker.
