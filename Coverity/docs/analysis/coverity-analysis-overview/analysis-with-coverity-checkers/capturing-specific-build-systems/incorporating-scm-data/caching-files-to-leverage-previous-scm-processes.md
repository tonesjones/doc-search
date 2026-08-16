---
title: "Caching files to leverage previous SCM processes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/caching-files-to-leverage-previous-scm-processes.html"
content_id: "J0FZXcJ03PoWzAKY_pJbZQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:34.902602+00:00"
---

# Caching files to leverage previous SCM processes

Collecting SCM information is potentially time consuming. One approach for acceleration
is to use caching. After running your build and capturing your tests, and before you
execute queries of the SCM system, you can use caching whereby SCM change data from a
previous build is reused. To cache files:

1. From an older emit, use `cov-manage-emit dump-scm-annotations` to export all
   annotations to a file. For
   example:

   ```
   cov-manage-emit --dir previous_emitdir dump-scm-annotations --output scm_cache.txt
   ```
2. For the new emit, use `cov-manage-emit add-scm-annotations` to incorporate
   the cached data. For
   example:

   ```
   cov-manage-emit --dir current_emit add-scm-annotations --input scm_cache.txt
   ```

The SCM change data from the original build is used for all files with the same name and
content signature. The last SCM change data is not added to new or newly-modified
files.

After the cache has been established, you can perform additional SCM operations to
provide any needed SCM change data using the same steps used without the cache.
