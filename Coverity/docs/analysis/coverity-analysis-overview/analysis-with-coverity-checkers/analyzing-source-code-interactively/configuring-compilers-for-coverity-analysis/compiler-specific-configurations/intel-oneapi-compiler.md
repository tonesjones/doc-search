---
title: "Intel oneAPI compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/intel-oneapi-compiler.html"
content_id: "zAnnOyn8v~RC2Qb8p9EoVw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:43.664975+00:00"
---

# Intel oneAPI compiler

Use a template configuration
for the Intel oneAPI compilers:

```
cov-configure --template --compiler icx --comptype intel_oneapi_icx
cov-configure --template --compiler dpcpp --comptype intel_oneapi_dpcpp
```

Note:
Compiler types `intel_icx:windows`, `intel_icx:linux`, and
their `icpx`, `dpcpp` variants are deprecated. Use `intel_oneapi_icx` instead.
