---
title: "Building non-ASCII source code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/building-non-ascii-source-code.html"
content_id: "XlC_Jq0CSGpfE91ZlISKCw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:00.290143+00:00"
---

# Building non-ASCII source code

Coverity Analysis supports non-ASCII encoding of source files. To use the
`cov-build` command for non-ASCII-encoded source code, add the
`--encoding <enc>` option with the appropriate encoding name.
This option enables the following support:

- Appropriate display of the Unicode source code in Coverity Connect.
- Improved parsing of the source code, and reducing parse errors and warnings.

For example, the following command specifies that the source code is in Japanese:

```
cov-build --dir <intermediate_directory> --encoding Shift_JIS make my_build
```

The `--encoding <enc>` option is also available for the
`cov-translate` and `cov-emit` commands.
