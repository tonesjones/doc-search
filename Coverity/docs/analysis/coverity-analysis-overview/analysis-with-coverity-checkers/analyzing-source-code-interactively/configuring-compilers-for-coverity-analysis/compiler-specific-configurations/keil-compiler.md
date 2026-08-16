---
title: "Keil compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/keil-compiler.html"
content_id: "y5lsNwbfrf_bjcUUeQ8i7A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:44.338913+00:00"
---

# Keil compiler

The Keil compiler for the ARM target platform requires the device argument, and so you
must pass the device argument to the compiler when configuring it with the
`cov-configure` command. After the `cov-configure`
options, specify the characters `--` and then the --device option. For
example:

```
> cov-configure --comptype keilcc --compiler armcc -- --device=<device_name>
```

Use a template configuration
for the Keil MDK for ARM
Compiler:

```
cov-configure --template --compiler armcc --comptype armcc
cov-configure --template --compiler armclang --comptype armcc
```
