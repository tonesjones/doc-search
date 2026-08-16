---
title: "The 'cov-preprocess' command"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-cov-preprocess-command.html"
content_id: "WgWZZ8NEDIEwryVgHAxvog"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:59.843708+00:00"
---

# The 'cov-preprocess' command

The first step of the `cov-preprocess` process is to find the
appropriate configuration, similar to `cov-translate`. For
`cov-translate`, however, a native compiler command line is mapped
to what the Coverity compiler expects. For native preprocessing, a native compiler
compile command line must be mapped into a native compiler pre-process command line.
While it is not as complicated as the former mapping, it is not as simple as adding an
option for preprocessing. For example, the following is the command to compile a file
with GCC:

```
gcc -c src.cpp -o src.o
```

If it is simply transformed by adding the `-E` option for preprocessing as
in the following example, the result would be that the preprocessing would output to
src.o:

```
gcc -E -c src.cpp -o src.o
```

The mechanism for transforming a native compile command into a native pre-process command
is described in Tags for native preprocessing.
