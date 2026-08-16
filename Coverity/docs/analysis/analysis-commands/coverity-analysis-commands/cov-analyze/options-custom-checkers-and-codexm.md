---
title: "Options: Custom checkers and CodeXM"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-custom-checkers-and-codexm.html"
content_id: "KViCOKmfsz~F_mY4QUdG9Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:38.712281+00:00"
---

# Options: Custom checkers and CodeXM

--codexm <checker-file>*
:   Specifies the CodeXM (.cxm) file or files to use in the
    analysis.

    Example:

    ```
    cov-analyze --dir mycxm  --codexm myChecker.cxm --codexm myOtherChecker.cxm
    ```

    CodeXM is a specialized language used to write customized checkers that run
    using the Coverity engine.

--codexm-print-debug
:   Enables the CodeXM `debug()` function.

    When enabled, the `debug()` function prints values or messages
    to the system console.

    If this option is not present when `cov-analyze` is invoked,
    calls to `debug()` are treated as no-ops.
