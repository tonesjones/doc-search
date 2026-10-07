---
title: "coverity verify-compliance"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/coverity-verify-compliance.html"
content_id: "wVYLWyAHkbF~vQQDajsn~w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:56.465348+00:00"
---

# coverity verify-compliance

Verify scan configuration compliance with checker policy.

## Synopsis

```
coverity verify-compliance [options]... [-- <cov-analyze-command>...]
coverity verify-compliance (-h | --help)
```

## Description

The verify-compliance command checks whether a proposed scan
complies with the effective checker policy for a Coverity Connect stream. Provide
the configuration via -c and -o options and/or as a cov-analyze
command. The configuration must specify `commit.connect.url` and
`commit.connect.stream.`

## Options

-h, --help
:   Displays the information in this section.

--project-dir project-dir-name
:   Project directory containing the source files to capture. If not specified,
    defaults to the current working directory.

## Advanced options

-c, --config config-file-name
:   The name of the configuration file to use. If not specified, defaults to
    coverity.yaml, coverity.yml, or
    coverity.json under
    <project-dir>. Guidance on creating and
    modifying configuration files is available in the form of a JSON schema at
    <coverity-dir>/doc/configuration-schema.json.

-o, --config-override <key>=<val>
:   Key and value to override in the setup configuration.
