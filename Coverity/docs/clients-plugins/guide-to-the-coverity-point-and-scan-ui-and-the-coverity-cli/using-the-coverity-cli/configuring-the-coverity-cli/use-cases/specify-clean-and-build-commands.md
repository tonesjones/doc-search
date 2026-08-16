---
title: "Specify 'clean' and 'build' commands"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-clean-and-build-commands.html"
content_id: "8_Q1ddTMiCm3bB~LcSXKQA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:50.946874+00:00"
---

# Specify 'clean' and 'build' commands

The following configuration specifies `clean` and `build` commands;
specifically, Apache Maven `clean` and `install`.
The `clean` command will be executed prior to capturing the build.

`capture: record-with-source`
:   This setting specifies that the capture step should
    defer the emit process so that the actual compilation of the source files is deferred.

`analyze: location: connect`
:   This setting directs the analysis to be completed in Coverity Connect.

`commit: connect: stream`
:   This setting specifies that the results should be committed to a stream
    called `commons-cli`.

`commit: connect: url`
:   This setting directs the analysis to use the Connect instance located at
    `https://connect.example.com`.

```
capture:
    build:
        clean-command: mvn clean
        build-command: mvn install
    record-with-source: true

analyze:
    location: connect

commit:
    connect:
        stream: commons-cli
        url: https://connect.example.com
```

You can use the `help` subcommand (see Shared command options) to print configuration examples in a given format.
