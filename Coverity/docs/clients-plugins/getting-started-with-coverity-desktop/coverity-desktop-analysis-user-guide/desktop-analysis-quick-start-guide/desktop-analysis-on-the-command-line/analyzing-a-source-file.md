---
title: "Analyzing a source file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyzing-a-source-file.html"
content_id: "4QvsbM~TAF7YYfXvRwM12g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:45.427120+00:00"
---

# Analyzing a source file

To analyze a source file, run:

```
> cov-run-desktop source_file_name
```

If everything is configured correctly, this will parse the named source file and analyze
it for defects, using a previously created reference snapshot with interprocedural
summaries in order to understand how that file relates to the code around it.

source_file_name is the path and file name of the source file to be
analyzed. You can pass as many files as you want to analyze.

For C and C++, source_file_name is typically the name of a
.c or .cpp file. If you want to analyze a
header file, see Analyzing non-primary source files (C/C++).

When the analysis completes, it prints the defects it has detected to the console, less any
defects removed by the filtering options. The `cov-run-desktop` command
reference in the Coverity 2026.6.0 Command Reference explains how to adjust the output,
including formatting and filtering.

Note: Depending on what file you choose, there may not be any defects detected. You can log into
Coverity Connect, select a file that has defects detected by the central analysis, and
pass it to `cov-run-desktop` to confirm those defects.

After your initial analysis, you can make additional changes to the source file and run
`cov-run-desktop` again on the same file, or any other file in the
project.
