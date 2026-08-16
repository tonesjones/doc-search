---
title: "Using Cygwin to invoke 'cov-build'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-cygwin-to-invoke-cov-build-.html"
content_id: "poLlEuE~HTjHKFJqQKJH7Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:31.622318+00:00"
---

# Using Cygwin to invoke 'cov-build'

Coverity Analysis supports the Cygwin development environment. The
`cov-build` command supports build procedures that run within
Cygwin, so you can use build procedures without modifications.

You can run Coverity Analysis commands from within Cygwin. However, when running these
commands, you cannot use Cygwin paths as command line option values. Cygwin paths are
UNIX-style paths that Cygwin translates into Windows paths. Instead, use only Windows
paths. You can convert Cygwin paths to Windows paths with the Cygwin utility
`cygpath -w`.

The command that `cov-build` runs is found through a Windows path. If
`cov-build` cannot find the correct build command, invoke
`bash` first. For example:

```
> cov-build --dir <intermediate_directory> bash -c "<cygwin command>"
```
