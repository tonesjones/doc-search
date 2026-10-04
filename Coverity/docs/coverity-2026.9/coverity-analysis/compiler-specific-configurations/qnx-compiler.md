---
title: "QNX compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/qnx-compiler.html"
content_id: "ixVbqAMM1f1y2tgOf42Mug"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:26.163762+00:00"
---

# QNX compiler

Use a template configuration for the
QNX compiler. The native compiler options `-V` and `-Y`
change the behavior of the compiler and require different Coverity Analysis
configurations. For example:

```
cov-configure --template --compiler qcc --comptype qnxcc
```
