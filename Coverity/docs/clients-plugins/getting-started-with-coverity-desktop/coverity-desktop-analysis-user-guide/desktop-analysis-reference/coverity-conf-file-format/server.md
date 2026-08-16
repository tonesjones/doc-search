---
title: "Server"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/server.html"
content_id: "hc02iWi3Qp7f8qRBLC2EwA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:17.162749+00:00"
---

# Server

The `Server` class contains Coverity Connect server configuration
attributes:

host?: string
:   Identifies a Coverity Connect server.

    The value of this field can be either the host
    name or the numeric (IPv4 or IPv6) address of the server. No dependent
    variables can appear in this string.

    There is no default for this
    setting, so it must be set either in a
    coverity.conf file, or on the command line.

    The `"host"` field must be accompanied by
    `"port"` and `"ssl"` fields.

    Important: The `"host"` field is being superseded
    by the `"url"` field.

port?: int
:   The port number of the HTTP or HTTPS service of the Coverity Connect server.

    The default
    is 8080 if `ssl` is `false` and 8443 if it
    is `true`.

    This field is not needed if
    `"url"` is used instead of `"host"`.

ssl?: bool
:   If `true`, then the communication with Coverity Connect will be protected by
    the SSL/TLS protocol. If `false`, communication will be
    conducted in cleartext.

    The default is `false`.

    This field is not needed if `"url"` is used
    instead of `"host"`.

url?: string
:   Identifies the Coverity Connect server. This field is an alternative to the
    `"host"` field, and is now the preferred way to identify
    a server within coverity.conf.

    When
    `"url"` is used instead of `"host"`,
    the `"port"` and `"ssl"` fields do not
    need to be present.

    The string for `"url"` must
    include (1) the protocol, `http://` or
    `https://`, and (2) the host URL. The port value
    defaults to 80 for a nonsecure server (`http`) or 443 for
    a secure server (`https`).

    Note: These are the
    standard defaults, and they differ from the defaults for the
    `"host"` field. The `"host"` field
    uses the Coverity Connect defaults, which are 8080 for a nonsecure
    server, or 8443 for a secure server.

username?: string
:   The Coverity Connect username to use when authenticating.

    The default value is "$(env:COV_USER:USER:USERNAME)".

    That
    means that if the COV_USER environment variable is set, its value is
    used. Otherwise, if USER is set then it is used; finally, USERNAME is
    tried.

password?: string
:   The password corresponding to the user. If it is empty, no password is specified.

    The
    default value is "".

    For security reasons, it is not recommended
    to put a password into coverity.conf, but there may
    be cases where it is expedient to do so anyway.

auth_key_file?: path
:   Name of a file to use as an authentication key (see the Coverity 2026.6.0 Command Reference
    for details).

    The default value is "$(cov_user_dir)/authkeys/ak-$(server_host_as_fname)-$(server_port)".

    That means that, by default,
    authentication keys are stored in a directory associated with the
    invoking user. Consequently, a single key can be used with many code
    bases and branches.

certs?: path
:   Use the CA certificates in the given file path. Requires ssl.

on_new_cert?: string
:   Indicates whether to trust (with trust-first-time) self-signed certificates, presented by
    the server, that haven't been seen before. The accepted string values are
    `trust` and `distrust`. Requires ssl.
