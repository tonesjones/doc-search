---
title: "The checkers Subcommand"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-checkers-subcommand.html"
content_id: "wVDsbnTGcsDuGLBkQ_3FpQ"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:32.670575+00:00"
---

# The checkers Subcommand

## Syntax

sigma
checkers [`-f {html | markdown}` [`-o`
output_path] ]

## Description

The `checkers` subcommand lists all the checks. The checks are grouped under
checkers and, for each check, the command provides information about tags,
languages, CWEs, severity, and enablement.

Note: User defined enablements, either through one of the
`--config`, `--enable`, or
`--disable` options, or through the environment variables
`SIGMA_ENABLE` and `SIGMA_DISABLE`, are not
taken into account.

Running the
command

```
sigma checkers
```

will print the 'Checkers' table in plain text (Markdown format) at the
`stdout`, as it can be seen in the following screenshot.

  
 [image: image]   

Running the
command

```
sigma checkers -f {html | markdown}
```

will print the 'Checkers' table at the `stdout` in the chosen format.

Note: The commands `sigma checkers -f markdown`
and `sigma checkers` are equivalent.

You can also set the
format using the environment variable
`SIGMA_CHECKERS_FORMAT`.

Running the
command

```
sigma checkers -f {html | markdown} -o <output_file>
```

where output_file is the output file path, saves the 'Checkers' table in
the file specified by output_file, in the chosen format. The
output_file parameter can be either a relative path or an
absolute path.

Note: The `-o` option requires `-f` to be
specified, but not the other way around.

You can also set the output file path
using the environment variable
`SIGMA_CHECKERS_OUTPUT`.

## Examples

```
sigma checkers -f html -o /home/user/checkers.html  # save output to "checkers.html" in html format
sigma checkers -f markdown -o ../abc.md             # save output to "abc.md" in markdown format
sigma checkers -f html             # print output to stdout in html format
sigma checkers -f markdown         # print output to stdout, equivalent to `sigma checkers`
```
