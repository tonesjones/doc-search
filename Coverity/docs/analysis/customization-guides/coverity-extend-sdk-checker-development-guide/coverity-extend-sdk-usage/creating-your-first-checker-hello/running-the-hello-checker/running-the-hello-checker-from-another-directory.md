---
title: "Running the hello checker from another directory"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-the-hello-checker-from-another-directory.html"
content_id: "HEi8mDtf6S1~tamPsYh6IA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:24.970688+00:00"
---

# Running the hello checker from another directory

You can run a Coverity Extend SDK checker from a directory other than
<install_dir>/bin (as shown in Running the hello checker). You might do so
if Coverity is installed to a read-only directory.

The Hello checker requires the following options:

- The installation directory: Specified by the `--prevent-root`
  option.
- The intermediate directory: Specified by the `--dir` option.

For example:

```
> cd HELLO
> <install_dir>/sdk/build-checker hello
> <install_dir>/bin/cov-build --dir int_dir_2 gcc -c test1/hello.test.c
> ./hello --dir int_dir_2 --prevent-root=<install_dir>
```
