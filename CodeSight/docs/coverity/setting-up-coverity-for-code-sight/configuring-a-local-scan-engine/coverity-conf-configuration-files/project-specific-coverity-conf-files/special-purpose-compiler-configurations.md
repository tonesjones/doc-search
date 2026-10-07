---
title: "Special-purpose compiler configurations"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/special-purpose-compiler-configurations.html"
content_id: "12VWcvkmBktx9lf4_~qwTg"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.843336+00:00"
---

# Special-purpose compiler configurations

Here are a couple of use cases for specifying a custom compiler configuration, and examples of how to do so.

**Use case:** Your build uses the ARM (RISC) compiler rather than the more
widespread GCC (GNU Compiler Collection). The following JSON configuration code specifies this:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "add_compiler_configurations": [
            /* arm-none-eabi-gcc is a common gcc variant
               for ARM-based embedded development */
            {
                "cov_configure_args": [
                    "--template",
                    "--compiler",
                    "arm-none-eabi-gcc",
                    "--comptype",
                    "gcc"
                ]
            }
        ]
    }
}
```

**Use case:**
You want to continue using the Clang compiler front end, but you want to invoke it using the
old-style (and self-descriptive) aliases `cc` and `c++`.
The following JSON configuration code specifies this:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "add_compiler_configurations": [
            /* On a Mac, CMake will use the "cc" and "c++" aliases
               instead of "clang" */
            {
                "cov_configure_args": [
                    "--template",
                    "--compiler",
                    "cc",
                    "--comptype",
                    "clangcc"
                ]
            },
            {
                "cov_configure_args": [
                    "--template",
                    "--compiler",
                    "c++",
                    "--comptype",
                    "clangcxx"
                ]
            }
        ]
    }
}
```

Note:
On a site that connects via Coverity Connect, these sample configurations would also
require `server` and `stream` fields.
