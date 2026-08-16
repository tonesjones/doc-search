---
title: "Re-running failed compiles without re-running the build"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/re-running-failed-compiles-without-re-running-the-build.html"
content_id: "veXjVQHAaSvp3Ceyn2RZGA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:04.206832+00:00"
---

# Re-running failed compiles without re-running the build

When a compile failure occurs, it would be useful to re-run the Coverity compiler over just the
file or files that failed without incurring the overhead of re-running the entire build.
The build might not work fast incrementally, or there might be additional overhead to
launching a complete build. As an alternative, the `--replay-failures`
option to `cov-build` uses information that is cached in the
intermediate directory from each failed compile to re-run the Coverity compiler on just
those files that failed to compile. If compilation failures are fixed, subsequent runs
of `cov-build --dir <intermediate_directory> --replay-failures`
recognize that a previously failed compile is now fixed and the subsequent runs do not
attempt to re-compile the (now-fixed) compilation failure again.

Each time that `cov-build --replay-failures` finds a record of a compile failure
in the intermediate directory, it reads both the command line used to invoke the native
compile of that file and the full environment that was set when the native compile was
attempted. After restoring this environment, it re-invokes
`cov-translate`
native_cmd, where native_cmd is the original
compile command used in the build. The benefit of re-invoking
`cov-translate` rather than calling `cov-emit`
directly is that you can test both configuration changes to the
.xml files and patches to `cov-translate`
supplied by Coverity without re-running the build. These changes are applied when the
compile failures are replayed. There are some cases where you might not want to
re-translate with `cov-translate`. To avoid this step and have
`cov-build --replay-failures` invoke `cov-emit`
directly, specify the `--no-refilter` option to
`cov-build`.

To summarize the different options for replaying compile failures:

```
> cov-build --dir <intermediate_directory> --replay-failures
```

finds all compile failures and re-applies `cov-translate` to the compile
command used in your build. The build-time environment is restored before the
re-translate is run.

```
> cov-build --dir <intermediate_directory> --replay-failures --no-refilter
```

finds all compile failures and re-applies `cov-emit` to the translated
argument list. This option runs faster than without `--no-refilter`, but
it does not allow you to verify fixes to the Coverity configuration files and it does
not allow you to verify `cov-translate` patches supplied by
Coverity.
