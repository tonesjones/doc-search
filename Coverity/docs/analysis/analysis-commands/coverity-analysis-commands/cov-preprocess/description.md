---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "OvWu4hX~vwLEa4Q7EmMrkQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:59.854241+00:00"
---

# Description

The `cov-preprocess` command preprocesses a source file. This command
reads the command-line argument from
<intermediate_directory>/emit and outputs the
preprocessed source file or files into the
<intermediate_directory>/output/preprocessed directory.
Coverity recommends that you use the `--output-file` option to change the
default output behavior whenever you need for the combined output path and filename to
be an invariant (for example, in scripts) because the internal structure of the
intermediate directory might change in future releases. However, note that using this
option necessitates that only one file is preprocessed per invocation of
`cov-preprocess`.

If you do not use an absolute path name to specify a file name,
`cov-preprocess` searches for the specified file name in
<intermediate_directory>/emit. To speed up the search
time, use full path names to files that you want to preprocess.

Preprocessing expands all preprocessor directives such as #include,
and expands macro definitions. A preprocessed source file is self-contained and can be
compiled by itself with no additional files.

Note: `cov-preprocess`
doesn't read source files from the emit or re-create source folders. Therefore the
source files, directory structure, and working environment of the original build
captured in the emit must exist and be used when `cov-preprocess`
runs.
