---
title: "The analysis: Special cases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-analysis-special-cases.html"
content_id: "zFfLlR9CtGMl25fJYtcaBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:54.185938+00:00"
---

# The analysis: Special cases

Depending on the purpose of your analysis, there are some special cases you might
want to be aware of before you run `cov-analysis`:

- For web application analyses, pass web application options:

  ```
  > cov-analyze --dir <intermediate_directory> --strip-path <path/to/source/code> \
    --webapp-security
  ```

  For troubleshooting information and important details about web
  application security analyses for Java and ASP.NET,
  see Running web application security analyses.
- For Android applications that are written in Java, use the
  --android-security option. See Running a security analysis on an Android mobile application.
- If you intend to run a MISRA analysis, see Running coding-standard analyses.
