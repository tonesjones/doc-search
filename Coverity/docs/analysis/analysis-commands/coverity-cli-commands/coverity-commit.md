---
title: "coverity commit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-commit.html"
content_id: "rqJYgUChp5okbB9lWI9Izw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:57.893545+00:00"
---

# coverity commit

Send analysis results to Coverity Connect or to a local
directory.

## Synopsis

```
coverity commit [options]
coverity commit [options] --local <results-path>
coverity commit (-h | --help)
```

## Description

The coverity commit command uploads analysis results to Coverity
Connect, to your Software Risk Manager (SRM), or writes them to a local directory.

This command requires either a configuration file or use of the --local
option, depending on where the analysis results are to be saved.

- For local analysis results, use the --local option.
- To commit results to Connect, use the Coverity configuration file to specify
  the Connect instance where to commit. You may specify the configuration file
  using the --config option, otherwise the file
  project-dir-name /coverity.yaml is used by default.

## Options

-h, --help
:   Displays the information in this section.

--project-dir project-dir-name
:   Project directory containing the source files to capture. If not
    specified, defaults to the current working directory.

## Advanced Options

-c, --config file-name
:   The name of the configuration file to use. If not specified, defaults to
    coverity.yaml, coverity.yml,
    or coverity.json in
    project-dir.

    Guidance on creating and modifying configuration files is available in
    the form of a JSON schema in the docs directory at
    coverity-dir/doc/configuration-schema.json.

--dir <idir-name>
:   The name of the intermediate directory to use. If not specified, defaults to
    <project-dir>/idir.

--local-format format
:   Specifies the format in which to save results: Must equal either `"html` (the default) or `"json"`.

--local-only
:   Force analysis results to be committed to the local filesystem.

--local results-path-name
:   Save analysis results to the specified local directory or file. For HTML format, this must specify a directory. For JSON format, this must be a file name.

    Note:
    When you invoke `coverity commit` and either the `--local` option is specified or
    `commit.local` is present in the configuration file (for example, coverity.yaml),
    then Coverity commits to both Coverity Connect *and* the local file or directory.

-o, –-config-override key=val
:   Key and value to override in configuration.
