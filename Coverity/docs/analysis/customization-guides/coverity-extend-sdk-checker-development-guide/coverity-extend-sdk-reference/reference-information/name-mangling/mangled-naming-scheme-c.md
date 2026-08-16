---
title: "Mangled naming scheme: C++"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/mangled-naming-scheme-c-.html"
content_id: "Iy1CDqUYI2s3AYXkN~LkYg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:03.728480+00:00"
---

# Mangled naming scheme: C++

For C++ name mangling, Coverity uses the IA64 C++ ABI name mangling scheme, regardless of
whether it is running on the IA64 platform or not. Table 1 provides the mangled
names of two functions, as defined by that scheme.

Table 1. C++ Mangled names

| Unmangled name | Mangled name |
| --- | --- |
| `f(int)` | `_Z1fi` |
| `f(int,int)` | `_Z1fii` |
