---
title: "Running 'cov-build' with '--record-only'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-cov-build-with-record-only-.html"
content_id: "Jgm~6tMowHrwykhZ1zZxKw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:06.212978+00:00"
---

# Running 'cov-build' with '--record-only'

Coverity Analysis has the ability (for C/C++ only) to record the environment, working
directory, and command line for each file in the build, and replay all of those recorded
commands either with a single process or multiple processes at a later time. The
advantages of this approach are:

- If build-time is critical for the native build, you can allow the native build to complete
  with minimal overhead (~10%), and run the Coverity build at a later time when the
  machines are idle or the build timing is not as critical.
- If your build cannot be made parallel by default, using the record/replay mechanism allows
  you to at least parallelize the Coverity portion of the build if you have more than
  one processor on the build machine.

The required operations to record the environment, command line, and working directory
are executed during each invocation of `cov-build`. If you want to run
`cov-build` with *just* the record step, either specify the
`--record-only` option of the `cov-build` command or
the `cov-translate` command:

```
> cov-build --dir <intermediate_directory> --record-only <build command>
```

```
> cov-translate --record-only <compile command>
```

After a record-only build is complete, use the recorded information to run the Coverity
compiler with the `--replay` option:

```
> cov-build --dir <intermediate_directory> --replay
```

The `--replay` functionality can also be run using multiple processes on a
single machine. To specify more than one process on a single machine, use the `-j
<process count>` option:

```
> cov-build --dir <intermediate_directory> --replay -j 4
```

This command line replays all of the recorded compilations using 4 processes. At the end
of the replay step, all of the information from the 4 replay processes is aggregated
into a single replay-log.txt file, which you can then use to
discover and diagnose compilation failures.

Note: Only run one `cov-build --replay` command or `cov-build
--replay-failures` command with a given `--dir
<intermediate_directory>` option at any one time.
