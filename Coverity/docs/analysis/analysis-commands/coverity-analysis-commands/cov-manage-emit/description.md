---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "x03Gp0EemlpkWYrg3qnNFA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:45.362950+00:00"
---

# Description

The `cov-manage-emit` command is used to query and manipulate an emit
repository. Each intermediate directory contains a single emit repository that contains
data for languages emitted via `cov-build`,
`cov-emit`, and other similar commands.

The `cov-manage-emit` command requires the `--dir`
option, plus at least one sub-command. the `cov-manage-emit` command
line typically follows this pattern:

```
cov-manage-emit <general_options> <sub-command> <sub-command_options>
```

The sub-commands can be used for various operations, including:

- Repairing database integrity (`repair`).
- Recompiling (`recompile`).
- Decompiling (`decompile`).
- Copying information from one intermediate directory into another
  (`add`).
- Aggregating the results of a distributed build into a single intermediate
  directory (`add-other-hosts`).
- Listing source files (`print-source-files`).
- Listing AST definitions (`find --print-definitions`).
- Inputing and outputting SCM data (`add-scm-annotations`,
  `dump-scm-annotations`).

The `cov-manage-emit` options are grouped by basic, options that cannot be
filtered by translation units, options that require translation unit filtering, options for listing emit
database information, and options for recompiling.
