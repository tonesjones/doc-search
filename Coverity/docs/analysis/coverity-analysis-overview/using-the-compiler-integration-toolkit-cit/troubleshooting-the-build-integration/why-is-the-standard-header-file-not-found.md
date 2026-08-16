---
title: "Why is the standard header file not found?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/why-is-the-standard-header-file-not-found-.html"
content_id: "etXR6ZSEEX4PtmiGz0p5VA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:23.382211+00:00"
---

# Why is the standard header file not found?

It is possible that during the probing of the compiler, that it does not report all the
directories needed. The mechanism that `cov-configure` uses is to give
the compiler a small file that does a `#include` of some standard
filenames and then looks at the preprocessed output to see where the file came from on
the system.

For a C compiler, the test gives the compiler these file:

- stdio.h
- stdarg.h

For a C++ compiler the test gives the compiler these file:

- stdio.h
- stdarg.h
- cstdio
- typeinfo,
- iostream,
- iostream.h
- limits

The paths that are recorded for these files are passed to the `cov-emit`
process as a `--sys_include` option. If the directory that a particular
file is in is not listed on the `cov-emit` command line, then you can
add an extra header filename to the template files. To do this, add a line similar to
the following to the type_config.xml file:

`<extra_header>headerfile.h</extra_header>`

If you have multiple variants defined in your 
type_config.xml file and the header file only applies
to one variant, then the extra_header line would go in the options section for that
particular variant. The entry is just the filename itself unless you want
`cov-configure` to pick up a parent directory. This may be the case
when the source code being built might have lines similar to the following:

```
#include sys/compiler.h
```
