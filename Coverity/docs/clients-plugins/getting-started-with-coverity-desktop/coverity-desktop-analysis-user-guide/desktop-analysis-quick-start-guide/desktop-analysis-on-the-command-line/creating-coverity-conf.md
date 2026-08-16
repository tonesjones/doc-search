---
title: "Creating coverity.conf"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-coverity.conf.html"
content_id: "kt0YQxDAsh~sFZKJPR9iug"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:43.475004+00:00"
---

# Creating coverity.conf

The coverity.conf file contains settings required to run desktop
analysis. It should be checked into your Source Code Management (SCM) repository,
usually in the root directory. The `cov-run-desktop` command searches
upward in the file tree from wherever it is invoked to find this file. If your code base
already has a coverity.conf file, skip this section.

This file should contain at least:

- The host name and port number of the Coverity Connect server.
- The name of the stream on Coverity Connect that is associated with the particular code base.
- Shell command lines to perform a clean build (compile) of the code.

The configuration file uses [JSON syntax](http://www.json.org/), but unlike standard JSON, comments *are*
allowed.

Create a coverity.conf file with the following contents:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "server": {
            "url": "https://coverity-server.example.com:443"    // server location
        },
        "stream": "codebase-branch",                            // stream name
        "scm": {
            "scm": "git"                                        // SCM name
        },
        "cov_run_desktop": {
            "build_cmd": ["make"],                              // build command
            "clean_cmd": ["make", "clean"],                     // clean command
            "reference_snapshot": "scm"
        }
    }
}
```

In place of "`coverity-server-name`", enter the host name of the machine
running Coverity Connect. If it is using a non-default port number, for example 1234,
add another attribute `"port" : "1234"` to the server section.

In place of "`stream-name`", enter the name of the stream that contains the
reference snapshots that desktop analysis should use to get inter-procedural summary
information from.

In place of "`make`" and "`make clean`", enter shell
commands to build and clean your code base. If you are not going to analyze any compiled
code, use `"build_cmd": []` in your coverity.conf
file to indicate that you do not have a build to capture. Even if you have a build
command, the `clean` command can be set to `[]` or
omitted, but you should include it if the build command omits calling the compiler when
object files are newer than source files, as with `make`. Note that
separate shell command words must be written as separate strings.

See coverity.conf file format for full details on the structure and meaning of the
configuration file. Note in particular the `compiler_configurations` element if you are using a
compiler other than GNU C/C++ as "gcc" or "g++", Microsoft C/C++/C#, or Oracle Java.
