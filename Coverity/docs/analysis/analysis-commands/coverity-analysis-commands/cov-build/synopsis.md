---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsis.html"
content_id: "jn1hmpCqxri6B5BlFcKj6A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:52.021251+00:00"
---

# Synopsis

C, C++, C#, CUDA, Go, Java, Kotlin, Objective-C, Objective-C++, Rust:

```
cov-build
   (--dir <intermediate_directory> | --da-broker <broker_servername:port>)
   [--disable-scan-transparency-data]
   [--capture-ignore <program.extension>]
   [--enable-scan-transparency-data]
   [--test-capture]
   [SHARED_OPTIONS]
   BUILD_COMMAND
```

**[SHARED_OPTIONS]**:

```
    [--config <coverity_config.xml>]
    [--debug]
    [--debug-flags <flag> [, <flag>, ...]]
    [--ident]
    [--info]
    [--redirect stdout|stderr,<filename>]
    [--tmpdir <tmp>]
    [--treat-as-64bit <exe-name>]
    [--verbose <level>]
```
