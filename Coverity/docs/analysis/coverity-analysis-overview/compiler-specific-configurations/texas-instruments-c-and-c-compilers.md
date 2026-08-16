---
title: "Texas Instruments C and C++ compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/texas-instruments-c-and-c-compilers.html"
content_id: "PVKKIaEvdYWM3ye4LaDF_g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:51.413717+00:00"
---

# Texas Instruments C and C++ compilers

Coverity supports 2.53 and later of a number of C and C++ TMS compilers. Use
`cov-configure list-compiler-types` for a complete list. The
compiler's executable name in a TMS470R1x installation, for example, is generally
`cl470.exe`. To configure this compiler, you might specify the
command line as follows:

```
> cov-configure --compiler <TMS Installation>\cgtools\bin\cl470.exe \
  --comptype ti
```

Change the preceding example to match the version and installation path of the TMS
compiler tools that you are using.

Note:
TI compilers require an environment variable to be set in order for `cov-configure` to properly probe compiler behavior.
The environment variable should point to the include directories, and be specific to the compiler (for example, `C6X_C_DIR` for the C6000 compiler).

When `cov-build` is launched for a project that uses the TMS compiler,
all of the invocations of the compiler will be accompanied with a call to
`cov-emit` unless one of the following command-line arguments is
present:

1. `-ppd` (generate dependencies only)
2. `-ppc` (preprocess only)
3. `-ppi` (file inclusion only)
4. `-ppo` (preprocess only)

There are currently a small number of unsupported options and keywords to the TMS
compilers. These keywords can be translated into nothing, when appropriate, or into a
supported ANSI C and C++ equivalent using user_nodefs.h.
Contact Coverity support regarding any parse errors that you see with this compiler.

Use a template configuration
for the Texas Instruments C7000 compiler:

```
cov-configure --template --compiler cl7x --comptype ti:cl7x
```

Language Limitations
:   The following language extension is not supported for the specified compiler:

    - Operators and functions for vector data types are not supported for the
      Texas Instruments C7000 compiler.

    Functions and variable initializers that use these features will not be
    analyzed. However, other functions and variable initializers within the same
    translation unit will still be analyzed.
