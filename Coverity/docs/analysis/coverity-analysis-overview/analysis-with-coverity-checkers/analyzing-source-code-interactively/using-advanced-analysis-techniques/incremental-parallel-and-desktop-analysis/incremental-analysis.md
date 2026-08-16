---
title: "Incremental analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incremental-analysis.html"
content_id: "tHf3UddauRDbAkLeFwH~HQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:14.328938+00:00"
---

# Incremental analysis

By default, `cov-analyze` caches build and analysis results in the
intermediate directory. Once you create an intermediate directory with
`cov-build` and analyze it with `cov-analyze`, you
can speed up subsequent build and analysis using *incremental analysis* mode.

To use incremental analysis mode:

1. Pass your analyzed intermediate directory to subsequent
   `cov-build` runs on the same code base.
2. Run `cov-analyze` on this same intermediate directory with the
   same command-line options as your previous `cov-analyze` run.

As long as you reuse your intermediate directory in this way,
`cov-build` and `cov-analyze` automatically run in
incremental mode. In this mode, `cov-build` only re-emits files that
have changed since your last `cov-build`. Likewise,
`cov-analyze` is able to reuse some of its work on the files and
functions that have not changed since the previous `cov-analyze` run.
Incremental mode is often faster than a build and analysis using a fresh intermediate
directory.

CAUTION:

There are two phases to incremental analysis: reusing the build results, and reusing the analysis results.
Reusing the analysis always produces the same analysis results as building and analyzing the same code from scratch with a fresh intermediate directory.
On the other hand, when it reuses the build results, `cov-analyze` cannot detect when a file has been deleted or removed from the build.
It appears as if you haven't recompiled or re-emitted the file, and so the analysis uses the version of the file that was cached.
Because of this, if you do use incremental mode, it's a good idea to periodically start from scratch with a fresh intermediate
directory—particularly if you've moved or deleted files from your source tree or build.

In general, analysis runs about 5 times faster in incremental mode. However, this performance
improvement can depend on the source being analyzed and does not apply in all cases;
also see the following note.

Note:
Not all Coverity checkers speed up in incremental mode. Many Java, C#, and Visual
Basic checkers enabled by `--webapp-security` or
`--android-security` do not run any faster in incremental mode.
