---
title: "Java use-after-free primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/java-use-after-free-primitives.html"
content_id: "kv3GN9n5HAligll2pnRdMA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:06.084003+00:00"
---

# Java use-after-free primitives

These primitives model the use of `free()` and its consequences.

## `void assert_freed( java.lang.Object o )`

Kills the current path if the parameter `o` is not in a freed state.

## `void assert_usable( java.lang.Object o )`

Kills the current path if the parameter `o` is not in a usable state.

## `void free( java.lang.Object o )`

Simulates freeing the resources of the parameter `o`.

## `void use( java.lang.Object o )`

Simulates using the resources of the parameter `o`.
