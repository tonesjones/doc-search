---
title: "Java concurrency primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-concurrency-primitives.html"
content_id: "3XwanR6Lw~DLwEdwqAqFrg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:07.871671+00:00"
---

# Java concurrency primitives

These primitives represent conditions for managing concurrent execution.

## `void lock( java.lang.Object o )`

Models acquiring a lock specified by `o`.

## `void model_timed_wait( java.lang.Object o )`

Models a `wait` operation with a timeout.

## `void model_wait( java.lang.Object o )`

Models a `wait` operation.

## `void thread_safe_function()`

Indicates that the function being modeled is thread-safe.

## `void thread_unsafe_function()`

Indicates that the function being modeled *is not* thread-safe.

## `void thread_unsafe_update( java.lang.Object o )`

Models an update to a thread-unsafe function.

## `void unlock( java.lang.Object o )`

Models the release of the lock specified by `o`.
