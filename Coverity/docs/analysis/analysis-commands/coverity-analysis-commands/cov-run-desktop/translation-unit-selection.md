---
title: "Translation unit selection"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/translation-unit-selection.html"
content_id: "VCi~i8xclSO4FNL9d5fhtw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:08.269151+00:00"
---

# Translation unit selection

In order to improve the speed of the analysis, `cov-run-desktop` limits
the number of files or translation units considered. In this context, a translation unit
refers to any primary source file from the intermediate directory, along with any files
included by that primary source file. The selection process is defined using various
options that affect what code will be analyzed.

There are two methods to select which translation units will be analyzed, and it is
required that the user specify one. The first method is to explicitly pass a list of
source files to be analyzed at the end of the command line:

```
cov-run-desktop [OPTIONS] FILE1 [FILE2 [...]]
```

For C and C++, the files will typically be .c or
.cpp source files. If you want to analyze a header file, see
Coverity
Desktop Analysis
2026.6.0 User Guide.

This can also be accomplished by listing your chosen source files in a response file, and then
specifying it on the command line with the `@@<response_file>` syntax.

The second method of translation unit selection is to query your source code management
(SCM) system for the set of files that have been modified locally and analyze those.
This method is designated with the `--analyze-scm-modified` option. See
--analyze-scm-modified
and A note on Git superprojects
for more information on this method.

Note: You will receive an error if you attempt to
pass more than one of these methods in the same command.
