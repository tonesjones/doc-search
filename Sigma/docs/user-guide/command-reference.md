---
title: "Command Reference"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/command-reference.html"
content_id: "2V9mPkdcYJfpFdnJT3CEaA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:30.486943+00:00"
---

# Command Reference

This section describes the syntax of the `sigma` command and of its
subcommands.

## Using the Sigma CLI

Use the sigma command and its subcommands to do the following:

- Configure Sigma (optional).

  sigma config
- Scan your code and return results.

  sigma analyze
- Provide help and information.

  sigma help

  sigma checkers

  sigma explain

The following sections describe the syntax of the `sigma` command and its
subcommands.

Note: The output of Sigma commands contains unicode. Some terminals
disable unicode support by default, requiring support to be enabled manually. If using a
terminal that does not support unicode, the output can be redirected to a file and read
in a viewer that supports unicode.
