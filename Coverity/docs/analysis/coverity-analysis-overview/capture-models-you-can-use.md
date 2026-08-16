---
title: "Capture models you can use"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/capture-models-you-can-use.html"
content_id: "Gkp4bda4SB19vYlv~sWnqQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:24.397432+00:00"
---

# Capture models you can use

Prior to analyzing a project, Coverity needs to translate the project's source files into a format that
Coverity Analysis can understand.
We refer to this translation process as *capture*.

The traditional approach to capture involves using the `cov-build` command.
The `cov-build` command only captures files that it observes being compiled by the build command it recognizes.

In contrast, the Coverity command-line interface (CLI) takes a more conservative approach and captures more files in the project directory so that
as many defects as possible are reported.
After an initial CLI scan, users can then decide to exclude certain files or directories from a capture, to avoid scanning files that report unwanted defects.

The following list summarizes the available capture and scanning options:

`cov-build`
:   This command only captures files it observes being compiled by the specified
    build command, and where the corresponding compiler has been configured using
    `cov-configure`.

    For example, source files for languages
    that don't have a compilation step, such as JavaScript, are never captured.

The Command Line Interface (CLI) commands `coverity capture` and `coverity scan`
:   By default, with very few exceptions, these capture and scan all files in the project directory.

    These are the exceptions, which are ignored by default:

    - Directories that start with a dot ("."), except for files in directories named .terraform/
    - Directories named node_modules/
    - Directories named vendor/

    For more information about the Command Line Interface, please see the
    Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.

The Coverity CLI provides both command-line options and configuration settings that can override the defaults outlined above,
so that additional files and directories can be included or excluded.
