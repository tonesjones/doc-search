---
title: "Synopsys MetaWare compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsys-metaware-compiler.html"
content_id: "x4Uwqq_Hn3VzFlTmwFCbWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:50.113332+00:00"
---

# Synopsys MetaWare compiler

Use a template configuration
for the Synopsys MetaWare C and C++ compilers:

```
> cov-configure --template --compiler ccac --comptype metawarecc:ccac
```

```
> cov-configure --template --compiler hcac --comptype metawarecc:mcc
```

```
> cov-configure --template --compiler mcc --comptype metawarecc:mcc
```

Language Limitations
:   The following language extensions are not supported for the specified compilers:

    - `long long` variants of the ISO/IEC TR 18037 fixed point
      `_Accum` and `_Fract` types are not
      supported for the hcac and mcc compilers.
    - Use of the ISO/IEC TR 18037 fixed point `_Accum` and
      `_Fract` types as the element type of vector types is
      not supported for the ccac, hcac, and mcc compilers.
    - Use of the ISO/IEC TR 18037 fixed point `_Accum` and
      `_Fract` types and fixed point literal expressions in
      C++ code is not supported for the hcac and mcc compilers.

    Functions and variable initializers that use these features will not be
    analyzed. However, other functions and variable initializers within the same
    translation unit will still be analyzed.
