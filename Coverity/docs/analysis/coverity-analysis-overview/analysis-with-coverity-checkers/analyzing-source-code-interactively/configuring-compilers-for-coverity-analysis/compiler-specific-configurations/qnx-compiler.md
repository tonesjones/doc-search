---
title: "QNX compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/qnx-compiler.html"
content_id: "ixVbqAMM1f1y2tgOf42Mug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:46.914254+00:00"
---

# QNX compiler

Use a template configuration for the
QNX compiler. The native compiler options `-V` and `-Y`
change the behavior of the compiler and require different Coverity Analysis
configurations. For example:

```
cov-configure --template --compiler qcc --comptype qnxcc
```
