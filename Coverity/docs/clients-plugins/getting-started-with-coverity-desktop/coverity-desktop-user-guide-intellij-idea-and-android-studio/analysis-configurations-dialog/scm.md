---
title: "SCM"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scm.html"
content_id: "xsZ_gLMQWCJTouAAAi9aMg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:54.014073+00:00"
---

# SCM

The SCM tab is an optional configuration, which specifies any SCM
information for the current project/analysis configuration. This is required only if you
want to use the Analysis scope options command for
local analysis.

Figure 1. SCM tab
[image: image]

Select SCM
:   Select your source code management system from the drop-down menu. The
    following SCM systems are currently supported:

    - Git
    - Perforce
    - Plastic
    - Plastic (distributed)
    - Subversion

Executable (tool)
:   This is the executable for querying the specified SCM. To be used, the SCM
    must be installed in the command PATH.

Source code project root
:   This is the path to the root of the source repository.

Additional tool arguments
:   This is a sequence of additional command line arguments to pass after the
    executable ("tool") name.

P4PORT (Perforce only)
:   The protocol, host name, and port number of the Perforce server, in the
    format
    "`protocol:host:port`".

    The `protocol` is either
    `tcp` or `ssl`.

P4CLIENT (Perforce only)
:   The name of the Perforce Client, as typically shown in the P4CLIENT
    environment variable. This is also known as a workspace name.

Remote Repository (Plastic (distributed) only)
:   The location of the central Plastic server. This should be in the format of
    `"<repository>@<remote-server>:<port>"`.

    This field is required.

Authentication Arguments (Plastic (distributed) only)
:   If needed, the arguments that will be passed directly to 'cm replicate'.
    Arguments include, but are not limited to, `--user` and
    `--password`.

    This field is optional.
