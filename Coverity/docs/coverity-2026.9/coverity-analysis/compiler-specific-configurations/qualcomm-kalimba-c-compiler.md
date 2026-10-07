---
title: "Qualcomm Kalimba C compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/qualcomm-kalimba-c-compiler.html"
content_id: "oSRC_pbcb_v8iJmfj0ElSA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:26.201121+00:00"
---

# Qualcomm Kalimba C compiler

Use a template configuration
for the Qualcomm Kalimba C compilers:

```
cov-configure --template --compiler kcc --comptype kalimba:kcc
cov-configure --template --compiler kalcc --comptype kalimba:kalcc
cov-configure --template --compiler kalcc32 --comptype kalimba:kalcc32
```
