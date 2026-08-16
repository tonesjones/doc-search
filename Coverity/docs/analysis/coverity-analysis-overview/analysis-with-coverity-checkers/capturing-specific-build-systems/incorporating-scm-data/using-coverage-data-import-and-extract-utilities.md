---
title: "Using coverage data import and extract utilities"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-coverage-data-import-and-extract-utilities.html"
content_id: "yil2j9SFnUrX8WKVNhxPGQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:32.942824+00:00"
---

# Using coverage data import and extract utilities

After you build your tests, the resulting emit describes source files that were used in
the build. SCM change data is not added to these sources during the build process but
are added later in a specific SCM operation. You must add SCM change data before you
perform an analysis, or before you commit your code to Coverity Connect.

This can be achieved using `cov-import-scm`. For example:

```
cov-import-scm --dir idir --scm git --log log.txt
```

While `cov-import-scm` can simplify the process, there are some
limitations:

- Any of the files encountered during parsing (such as header files) might not be under SCM
  control, and querying the SCM for these files might be inefficient.
- The build might combine files from multiple repositories or SCM systems for which a single
  invocation of `cov-extract-scm` might not be appropriate.
- For files that have not changed from a previous analysis, there might be an advantage to
  re-using previously gathered data.

In these cases, you should use the underlying workflow and commands described in Adding files under a directory hierarchy.
