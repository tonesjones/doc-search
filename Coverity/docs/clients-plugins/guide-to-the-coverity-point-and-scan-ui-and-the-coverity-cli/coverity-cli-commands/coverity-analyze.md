---
title: "coverity analyze"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analyze.html"
content_id: "vvUhIhtg7kg8Fz~_bpGpJw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:31.549249+00:00"
---

# coverity analyze

Analyze captured source files.

## Synopsis

```
coverity analyze [options]
coverity analyze (-h | --help)
```

## Description

The `coverity analyze` command analyzes the code that was captured
to the given intermediate directory.

## Options

--project-dir <project-dir-name>
:   Project directory containing the code to analyze. If not specified, defaults to the current working directory.

-h, --help
:   Displays the information in this section.

## Advanced Options

--dir <idir-name>
:   The name of the intermediate directory to use. If not specified, defaults to
    <project-dir>/idir.

-c, --config <file-name>
:   The name of the configuration file to use. If not specified, defaults to
    coverity.yaml, coverity.yml,
    or coverity.json in `<project-dir>`.

    Guidance on creating and modifying configuration files is available in
    the form of a JSON schema in the docs directory at
    <coverity-dir>/doc/configuration-schema.json.
    The file can also be found in the Coverity documentation under
    Clients, plug-ins, integrations, and APIs > Getting started with Coverity Desktop
    > Coverity Desktop Analysis: User Guide > Desktop Analysis reference > coverity.conf file format
    > Example coverity.conf file.

--cra
:   Enable EU Cyber Resilience Act (CRA) analysis mode.

-o, –-config-override <key>=<val>
:   Key and value to override in configuration.

–-pool-size <size>
:   Pool size to use when `analyze.location=connect` in
    coverity.yaml, which means that the analysis is
    performed in the cloud.

    For a Thin Client analysis performed in the cloud, use this optional
    parameter to specify a scan job node pool size to use for a scan
    (analysis) in the cloud. Valid values are `"small"`,
    `"medium"`, `"large"`,
    `"extralarge"`, and custom pools. If you use a custom
    node pool, obtain the name of the node pool from the Coverity cloud
    administrator. See also Initiating a scan in the cloud.

--upload-artifacts <value>
:   Artifacts to upload following a scan when
    `analyze.location=connect` in
    coverity.yaml, which means that the analysis is
    performed in the cloud. Valid values are `"All"` (the
    default), `"LogsOnly"`, `"None"`, and
    `"OnFailure"`. See also Initiating a scan in the cloud.
