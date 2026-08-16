---
title: "Creating coverity.conf for a code base"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-coverity.conf-for-a-code-base.html"
content_id: "JMtytYGu2CtfMiAG7G5GWQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:52.278524+00:00"
---

# Creating coverity.conf for a code base

In order to set up a code base so that developers can easily run desktop analysis, we
recommend creating a file called coverity.conf and putting this
file into the root directory of the source code management (SCM) repository. The file
contains configuration information that will be shared by all developers working on that
code base.

At minimum, it must contain:

- The host name and port number of the Coverity Connect server

  You can also use a URL in
  place of a host name. For example,
  https://example.com/coverity or
  http://connectserver:8080.
- The name of the Coverity Connect stream that is associated with the code base

It is recommended that it also contain:

- The name of the SCM system in use
- Shell command lines to build (compile) and to clean the code base

The configuration file uses JSON syntax. The following sample file contains all the
required and recommended elements:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "server": {
            "url": "http://<coverity-server.example.com>:443"    // server location
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

Whenever `cov-run-desktop` is invoked, it will search upward from its
invocation directory to find a coverity.conf file. If it finds one,
the settings from that file are used unless the user overrides them with a command-line
option. The order of precedence for selecting which settings
`cov-run-desktop` will use is illustrated below:

[image: image]

As shown in the diagram, any settings specified on the command line take precedence over
the settings in any coverity.conf file. From there, the per-user
coverity.conf file (generally located in
$HOME/.coverity or %APPDATA%\Coverity) is
processed, with any *true* conditional settings taking precedence over top-level,
“unconditional” settings. The conditional settings are processed in order, such that
earlier conditional settings (whose condition is *true)* take precedence over later
conditional settings. Next, the per-branch coverity.conf file
(located in the code base directory) is processed. Finally, default values are assigned
to any settings that are not specified on the command line or configured in a
coverity.conf file.

See coverity.conf file format for full details on
the structure and meaning of the configuration file. Note in particular CompilerConfiguration if you are using a
compiler *other than* GNU C/C++ as "gcc" or "g++", Microsoft C/C++/C#, or Oracle
Java.
