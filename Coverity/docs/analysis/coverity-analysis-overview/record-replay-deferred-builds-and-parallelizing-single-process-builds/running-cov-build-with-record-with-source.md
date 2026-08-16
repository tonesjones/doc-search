---
title: "Running 'cov-build' with '--record-with-source'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-cov-build-with-record-with-source-.html"
content_id: "q1gCNRaG~H_2hvAcb41lkw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:06.849238+00:00"
---

# Running 'cov-build' with '--record-with-source'

You can use the `--record-with-source` option to run
`cov-build` through the record step, and also collect all of the
necessary source files in the build (for C, C++, C#, Visual Basic, and Java only). Then you can then
complete the `cov-build` run at a later time using the
`replay-from-emit` option:

```
> cov-build --dir <intermediate_directory> --record-with-source <build command>
```

```
> cov-translate --record-with-source <compile command>
```

After a record-with-source build is complete, use the recorded information to run the Coverity
compiler with the `--replay-from-emit` option:

```
> cov-build --dir <intermediate_directory> --replay-from-emit
```

This is helpful if you need the ability to complete the replay build on a different
platform than you started from. For example, you could complete the `cov-build
--record-with-source` step on a Windows machine, then transfer the emit
file and complete the `cov-build --replay-from-emit` step on a Linux
machine. The `--record-with-source` option is also beneficial for
recording builds with transient files, such as #import files;
`--record-only` fails when attempting to record these builds.

Note: Be aware of the following:

- Running `cov-build` with the
  `--record-with-source` option takes significantly longer
  than using `--record-only`.
- The recording of Java Webapps needs to be done outside of the `cov-build
  --record-with-source` command. Refer to the `cov-record-source` command in the Coverity 2026.6.0 Command Reference for details.
- Java record with source cannot replay builds that were recorded on a non-Windows
  machine on a Windows machine. However, builds recorded on Windows can be
  replayed on a non-Windows machine.
- C# record with source only supports recording builds on Windows and Linux.
  Builds recorded on Windows can be replayed on both Windows and Linux; builds
  recorded on Linux can only be replayed on Linux.
- Visual Basic record with source only supports recording builds on Windows.
  Builds recorded on Windows can be replayed on both Windows and Linux;
