---
title: "Compiler compatibility header files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-compatibility-header-files.html"
content_id: "EdqW5~JwtK4z3iUgF6ZoZQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:16.399746+00:00"
---

# Compiler compatibility header files

Compiler compatibility headers are pre-included by `cov-emit` to define
things that are predefined by the native compiler like macros, intrinsics, or built-in
types. Create a file called
config/templates/name/compile-compat-comptype.h
and cov-configure will arrange for it to be included in every
invocation of `cov-emit`.
