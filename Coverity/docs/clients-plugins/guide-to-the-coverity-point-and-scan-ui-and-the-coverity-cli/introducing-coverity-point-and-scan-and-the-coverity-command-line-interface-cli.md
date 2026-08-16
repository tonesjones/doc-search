---
title: "Introducing Coverity Point and Scan and the Coverity command-line interface (CLI)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introducing-coverity-point-and-scan-and-the-coverity-command-line-interface-cli-.html"
content_id: "p5mBLiW2ZU8tNyjUdb1RYQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:43.984460+00:00"
---

# Introducing Coverity Point and Scan and the Coverity command-line interface (CLI)

This guide describes the graphic Point and Scan UI and the Coverity command-line (CLI) interface.

We recommend that new analysis projects use Point and Scan or the CLI. These allow you to do the following:

- Scan a project without any knowledge about project contents.
- Understand which project files have been captured and which have not.

For more information, please see Using the Coverity Point and Scan UI
and Using the Coverity CLI.

Note: Analysis projects already invested in traditional Coverity Analysis might
choose to continue using that set of commands. The traditional Coverity Analysis commands are still required to analyze source
projects in the CUDA or Fortran languages.

For a description of the full,
traditional Coverity Analysis, please see the Coverity Analysis 2026.6.0 User and Administrator Guide.

## Advantages of the Coverity CLI

This interface enables you to analyze your source code just by specifying the
location of the code base and the platform where scan results should be uploaded and stored.
The Coverity CLI takes care of everything else.
You don't need detailed knowledge about the commands needed to build the code,
you don't need to know where the configuration files are located, and you don't need to know anything about the
composition of the project.

The Coverity CLI is ideal for situations where you have little or no knowledge of the
tested environment; for example, you are a security operations consultant needing to
evaluate an application's security profile for a wide variety of clients.

## Using the Coverity CLI

You can use the Coverity CLI in one of three ways:

- Scan source and commit results to a local directory
- Scan source and commit results to your Coverity Connect server
- Scan source and commit results to both your Coverity Connect server and to a local directory

Independently of the method you use to scan your source, the scan will return results that show this information:

- The number of files that were successfully captured.
- The number of files that were only partially captured.

  This happens when the Coverity compiler is unable to understand all the source code in a given file.
- The number of files that could not be captured at all.

  In some cases, the Coverity compiler might not be able to understand anything in the file, in which case the file is
  not captured at all. Files that could not be captured will not be analyzed.
- The number of files that were ignored.

  A file is ignored either because it is not relevant or because Coverity cannot analyze it.

In this section:

- Point and Scan, the Coverity CLI, and file usage
- Default analysis
