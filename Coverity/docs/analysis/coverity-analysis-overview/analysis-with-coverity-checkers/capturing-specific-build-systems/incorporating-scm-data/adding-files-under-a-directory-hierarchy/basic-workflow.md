---
title: "Basic workflow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/basic-workflow.html"
content_id: "R0JEiiJCpaIZzvtxfU31RA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:34.248253+00:00"
---

# Basic workflow

The basic workflow for `cov-import-scm` and the underlying commands
invoked are as follows:

1. Identify the files that need SCM change data
   added.

   ```
   cov-manage-emit --dir idir list-scm-unknown --output needed-files.txt
   ```
2. Get the SCM change data for the source
   files.

   ```
   cov-extract-scm --scm git --input needed-files.txt --output scm-data.txt
   ```
3. Add the SCM change data to the
   emit.

   ```
   cov-manage-emit --dir idir add-scm-annotations --input scm-data.txt
   ```

If you cannot use `cov-import-scm` because of one of the limitations, the underlying commands can be invoked directly. For example,
if you want to import all of the unknown files except the files in a directory named
/usr/include (which are not under SCM control), you can use
`cov-manage-emit`
`list-scm-unknown` and then the following command:

```
grep -v /usr/include needed-files.txt > subset-needed-files.txt
```

You would then proceed with `cov-extract-scm` and
`cov-manage-emit add-scm-annotations` commands as outlined
above.
