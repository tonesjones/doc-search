---
title: "Green Hills compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/green-hills-compiler.html"
content_id: "R6cOp~Y39srpiGf6h_hO~A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:42.383623+00:00"
---

# Green Hills compiler

Use a template configuration for the
Green Hills C and C++ compiler. This is necessary because some native compiler options
like -bsp <my_hardware_config> and -os_dir <dir> change the behavior of the
compiler and require different analysis configurations.

In this compiler's standard installation, the compiler executable names are
`cc<target name>` (for C code) and `cx<target
name>` (for C++ code). The compilers are located in an
architecture-specific sub-directory of the Green Hills installation, such as
Linux-i86. Additionally, there are compilers named
`ccint<target name>`, and these should be configured as well
if used.

Lastly, there is a binary called `ecom<target name>`. This is an
undocumented internal binary that is used by some tools. This should be configured using
`green_hills_ecom`.

For example:

```
cov-configure --template --compiler ccintppc --comptype green_hills
cov-configure --template --compiler ecomppc --comptype green_hills_ecom
```
