---
title: "Adding files under a directory hierarchy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/adding-files-under-a-directory-hierarchy.html"
content_id: "hdNEYQNfrmVCJLcNjOQLqQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:28.992797+00:00"
---

# Adding files under a directory hierarchy

Some of the limitations of `cov-import-scm` can be mitigated by using
`--filename-regex`. This option allows finer control over the
gathering of SCM information. Information is gathered only for filenames that match the
regular expression. For example, if all of the source under SCM control is in a
directory named src, it can be imported using the following
command:

```
cov-import-scm --scm git --dir idir --filename-regex "/src/" --log log.txt
```
