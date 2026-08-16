---
title: "Options: C#"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-c-.html"
content_id: "JDwBu9buKhujfi11m2Xlog"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:36.513349+00:00"
---

# Options: C#

--cs
:   As of version 2022.9.0 this option has been deprecated.
    Use --tu-pattern lang("<lang>") instead.
    See Translation unit pattern matching for more details.

    Filters by C# translation units on which this command operates or reports.
    The command will fail with an informative error message if none of the
    translation units in the emit subdirectory match any of
    the specified language options in the intermediate directory.

--resolve-calls-to-all-delegates <true|false>
:   When `true` (the default is `false`), it allows
    resolving more calls to C# delegates, which may report more defects, notably
    `LOCK_INVERSION` defects. It may cause more false
    positives to be reported.
