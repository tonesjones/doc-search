---
title: "Options: Java analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-java-analysis.html"
content_id: "IVLZwhHoLyh9E96tymw3Gw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:40.671088+00:00"
---

# Options: Java analysis

--java
:   As of version 2022.9.0 this option has been deprecated. Use --tu-pattern
    lang("<lang>") instead. See "Translation unit pattern matching"
    in the `cov-analyze` documentation for more
    details.

    Filters by Java translation units on which this command operates or
    reports. The command will fail with an informative error message if none of
    the translation units in the emit subdirectory match
    any of the specified language options in the intermediate directory.

--no-java
:   As of version 2022.9.0 this option has been deprecated. Use --tu-pattern
    lang("<lang>") instead. See "Translation unit
    pattern matching" in the `cov-analyze` documentation
    for more details.

    Disables Java analysis. By default, the
    `cov-analyze` command otherwise analyses any Java code it
    finds in the intermediate directory.
