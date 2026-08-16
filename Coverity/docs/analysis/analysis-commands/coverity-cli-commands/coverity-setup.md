---
title: "coverity setup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-setup.html"
content_id: "Wq~d_wmTyUkG8VRSJ9hetg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:01.345047+00:00"
---

# coverity setup

Set up a new project.

## Synopsis

```
coverity setup [options]
coverity setup (-h | --help)
```

## Description

The coverity setup command creates a Coverity configuration file
that specifies where to send the analysis results.

## Options

-h, --help
:   Displays the information in this section.

--project-dir project-dir-name
:   Project directory containing the source files to capture. If not
    specified, defaults to the current working directory.

Advanced Options

-c, --config config-file-name
:   The name of the configuration file to generate. The file extension must
    be one of .yaml, .yml, or
    .json. If not specified, the file
    project-dir
    /coverity.yaml is used by default.

-o, --setup-override <key>=<val>
:   Key and value to override in the setup configuration.
