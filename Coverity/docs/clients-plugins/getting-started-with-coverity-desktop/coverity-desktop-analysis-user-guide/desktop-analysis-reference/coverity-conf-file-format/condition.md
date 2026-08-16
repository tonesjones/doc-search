---
title: "Condition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/condition.html"
content_id: "Gdd9EU72jrznQ23beLJQ4w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:15.838324+00:00"
---

# Condition

A `Condition` contains one or more simple predicates (attributes) that
must be true for the condition to be met. The attributes are:

platforms?: string[]
:   If present, then the current host platform must be among those in the sequence for the
    condition to be satisfied. The possible platforms are:

    - freebsd
    - freebsd64
    - linux
    - linux64
    - macosx
    - solaris-sparc
    - solaris-x86
    - win32
    - win64

    Important: Support for macOS is specific to Intel
    systems. Apple silicon systems are not currently supported.

hostname_regex?: regex
:   If present, the fully qualified hostname of the host machine must match (as a substring,
    unless anchors are specified) the specified perl-syntax regular expression.
    Note that regular expression matching for `hostname_regex` is
    case-insensitive.

username_regex?: regex
:   If present, the OS username of the user invoking the tool reading the configuration file
    must match the specified regular expression.

regex_matches_string?: string[]
:   If present, this array must contain an *even* number of strings, such that they form a
    sequence of (regex,string) pairs. Each regex is matched against each corresponding
    string; all must match for the condition to be met.

    For example:

    ```
        "regex_matches_string": [
            "^user1$", "$(env:USER)",        // user = user1, AND
            "^win", "$(platform)"            // OS is Windows
        ]
    ```

file_exists?: path
:   If present, this condition is true if there is any named file system entity (file,
    directory, named pipe, etc.) at the given location.

configurations?:string[]
:   If present, this condition is true if the current analysis configuration name exactly
    matches any of the listed strings.

    Configuration names are specified using
    the `—configuration-name <name>` on the command
    line or matching an Analysis Configuration name in the Coverity Desktop
    Analysis plugins. If no configuration name is specified, the current
    configuration is Default.
