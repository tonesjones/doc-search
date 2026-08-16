---
title: "Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect.html"
content_id: "s7kwhfK6vTJNBB4_WXHP5Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:41.674196+00:00"
---

# Coverity Connect

The Coverity Connect tab specifies server and authentication information
for the Coverity Connect instance relevant to each analysis configuration.
This information is required for local analysis, and for retreiving remote issues.

Figure 1. Coverity Connect tab
[image: image]

Coverity Connect URL
:   The fully qualified URL for your Coverity Connect
    server. This should include protocol, host name, and port number; for
    example, `https://connect.blackduck.com:8080`. If you are
    connecting to a Coverity Connect server over SSL,
    using a certificate signed by a recognized CA, the host name needs to match
    the name of the host on the certificate. This is not necessary when you use
    an unsecured connection, or when you use a self-signed certificate from
    Coverity Connect.

Validate server certificate
:   Turn on this check box to validate the certificate. We recommend that you do turn it on. For
    additional details, see "Using SSL with Coverity Analysis"
    in the Coverity Platform 2026.6.0 User and Administrator Guide.

Authentication Key
:   This field displays information about any existing authentication key file
    for the specified Host name and
    Port.

    If authentication fails, or no authentication key exists, you will be
    prompted to import or generate a new key file. You can generate a new key by
    clicking the generate link and entering your username
    and password. You can also import an existing key by clicking the
    import link and choosing a key file that's
    already been created or saved.

    If you attempt to import or generate a key when a key file already exists,
    then a Replace key dialog box appears, prompting you
    to either Replace the old key file or to
    Save as new.

Test Connection
:   Click this button after entering all connection information. This will test
    the connection and validate your settings.
