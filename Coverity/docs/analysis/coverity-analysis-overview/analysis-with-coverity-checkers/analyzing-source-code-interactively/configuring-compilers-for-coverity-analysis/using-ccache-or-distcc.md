---
title: "Using 'ccache' or 'distcc'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-ccache-or-distcc-.html"
content_id: "LBrxoZKVxqSRGgpNq1jf3g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:24.259038+00:00"
---

# Using 'ccache' or 'distcc'

If you use either of these tools, you need to
use the `--comptype prefix` setting when configuring Coverity
Analysis for your compiler, as shown in the examples below. This setting can
help avoid unexpected defect reports.

## 'ccache' configuration

If you use `ccache` (for example, with `gcc`),
your `cov-configure` command line should specify the following:

```
> cov-configure --comptype prefix --compiler ccache
```

```
> cov-configure --comptype gcc --compiler gcc
```

## 'distcc' configuration

- If `ccache` is set up to execute `distcc` (for
  example, through the CCACHE_PREFIX variable), it is only necessary to
  configure the prefix for `ccache`.
- If your `distcc` installation uses the name of the underlying
  compiler (for example, `gcc -c sampleProgram.c`, where
  `gcc` is really `distcc`), your
  `cov-configure` command line should specify the following:

  ```
  > cov-configure --comptype <comptype_of_real_compiler> \
    --compiler <distcc_executable_name>
  ```
- If you are prepending `distcc` to compiler command lines (for
  example, `distcc gcc -c sampleProgram.c`), your
  `cov-configure` command line should specify the following:

  ```
  > cov-configure --comptype prefix --compiler distcc
  ```

  ```
  > cov-configure --comptype <comptype_of_real_compiler> \ 
    --compiler <first_argument_to_distcc>
  ```

  The first argument to `distcc` is the name of executable for the
  real compiler, for example, `gcc`.
- If `distcc` is used directly as a compiler (for example,
  `distcc -c sampleProgram.c`), your command line should specify the following:

  ```
  > cov-configure --comptype <comptype_of_real_compiler> \
    --compiler distcc
  ```
