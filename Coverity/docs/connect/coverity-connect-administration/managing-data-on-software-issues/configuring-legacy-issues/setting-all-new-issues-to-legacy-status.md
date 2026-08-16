---
title: "Setting all new issues to legacy status"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-all-new-issues-to-legacy-status.html"
content_id: "yQA9ev2B6qXr4zfijroHPg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:26.601239+00:00"
---

# Setting all new issues to legacy status

The most common scenario for using the legacy attribute is identifying all issues in a
code base which existed before the adoption of Coverity Analysis. A company may want to
implement a policy where all code check-ins have been checked by Coverity Analysis and
are free of new issues. To do so, all existing issues in a given stream must be
highlighted as legacy by running the following command after committing your first
analysis to Coverity Connect:

```
> cov-manage-im --mode defects --stream streamName --update --set legacy:True
```

This will set the legacy status of all previously existing issues to true.
