---
title: "What you will need"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/what-you-will-need.html"
content_id: "9YS6vuDnt6lxpj8cZwaKwg"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:06.230229+00:00"
---

# What you will need

Make sure that you have access to the following:

Coverity Connect stream name
:   Coverity Connect must be configured in advance to provide analysis summary data to Desktop
    Analysis users. Desktop Analysis relies on a "reference snapshot" to provide
    analysis summary data. This requires an initial analysis and commit to a
    stream enabled for Desktop Analysis. You will need the name of that
    stream.

    See Coverity Platform User and Administrator Guide for information
    on configuring Coverity Connect for use with Desktop Analysis.

Coverity Connect access information
:   - Host name
    - Port number and type (HTTP or HTTPS)
    - User name
    - Password

Source code to analyze
:   You can use Desktop Analysis with C, C++, C#, Java, JavaScript, PHP, Python, Ruby, or Scala
    code.

    For C, C++, C#, and Java you need to know the command to build
    the software, and which compilers your project uses.

Coverity® Analysis installer and license file
:   The Coverity® Analysis installer and license file are available from
    the Coverity customer portal, and may also be made available from the
    Coverity Connect downloads page by your Coverity Connect administrator. This
    is the recommended configuration.

    Instructions for adding the installer
    and license file to the Coverity Connect downloads page are found in the
    Coverity Platform User and Administrator Guide.
