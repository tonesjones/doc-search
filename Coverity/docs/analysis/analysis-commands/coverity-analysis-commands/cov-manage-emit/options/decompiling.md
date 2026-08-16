---
title: "Decompiling"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/decompiling.html"
content_id: "nFeLazwd9Ev~29epzuIr9g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:50.803669+00:00"
---

# Decompiling

The `decompile-binary-tus-from-dir` subcommands repeat a decompilation
recorded in the emit.

decompile-binary-tus-from-dir [OPTIONS]
:   Decompiles translation units from byte code source contained within the emit
    directory. Replaying from the emit will have the same results, regardless of
    changes to the files in the filesystem (including deletion).

    This option is similar to `cov-build --replay-decomp`, but
    it allows you to perform finer-grained filtering of the TUs that are being
    replayed. For example:

    ```
    cov-manage-emit --dir idir --tu 10 decompile-binary-tus-from-dir
    ```

The decompile sub-commands are:

--compilation-log <log_file>
:   Saves diagnostic messages to `<log_file>` (instead of
    the default of standard output and standard error). Also displays a progress
    ticker bar.

--disable-decomp-bodies
:   Disable decompiling method bodies of the byte code.
