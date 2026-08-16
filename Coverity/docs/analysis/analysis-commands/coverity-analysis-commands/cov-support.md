---
title: "cov-support"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cov-support.html"
content_id: "p44gyB4GpwIpd4nctL5_tw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:40.630899+00:00"
---

# cov-support

Create a support information package for Coverity Analysis consisting of
important logs and configuration files (with minimal collection of proprietary
information).

## Synopsis

Example:

```
cov-support --dir idir -of support.zip
```

Contents of output file:

```
user1@user1-virtual-machine:~/workspace/projects/postgres$ tree support -L 2
support
├── home
│   └── user1
└── idir
    ├── build-log.txt
    ├── BUILD.metrics.xml
    ├── build-timings.txt
    ├── emit
    ├── output
    └── security-da-log.txt

5 directories, 4 files
```

## Description

The `cov-support` command adds the config and the logs from the idir
into a log package. The command minimizes the collection of proprietary information
and does not include your source code or emit-db. The contents should still be
managed with appropriate care. It is useful in cases where providing the entire IDIR
is not possible.

The contents are obtained from the IDIR, the coverity_config.xml directory, and the
product installation config directory. It will include configuration, build, and
analysis logs, metrics and timing information, and configuration files. The
`--all` option adds additional analysis logs, analysis
frameworks, and C# logs. Unless `--quiet` is specified, cov-support
will print the list of files going into the ZIP file.

Note:
The behavior of `cov-support` for Coverity Analysis differs from the Coverity Connect
command of the same name. If both commands are on the PATH, execution defaults to the
Coverity Connect command. To avoid conflict, you may use the full path
to `cov-support` for Coverity Analysis, temporarily modify your PATH, or create
an alias in your shell configuration.

## Options

-of, --output-file <support.zip>
:   Specifies output ZIP file.

-q, --quiet
:   When set, list of files in ZIP will not be printed out.

-c, --config <coverity_config.xml location>
:   Specifies coverity_config.xml directory path.

--all
:   Adds additional analysis logs, analysis frameworks, and C# logs to ZIP file.
