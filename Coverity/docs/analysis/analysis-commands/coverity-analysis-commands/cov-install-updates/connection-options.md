---
title: "Connection options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connection-options.html"
content_id: "vnri_Y7OtYSgTJw8NdKKsw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:32.191179+00:00"
---

# Connection options

The `check`, `list` and `install`
sub-commands accept the options in this list. These sub-commands must connect to a
Coverity Connect instance. The options in this list provide the information needed to
establish that connection.

Minimally, the `--url` and `--auth-key-file` (or
`--user` and `--password`) options are required.

--auth-key-file <keyfile>
:   Specify the location of a previously created authentication key file, used for connecting to the
    Coverity Connect server. Authentication keys can be registered with a
    Coverity Connect instance and used for authentication in place of the
    `--user` and `--password` options. See
    "Working
    with authentication keys" in Coverity Platform 2026.6.0 User and Administrator Guide.

--authenticate-ssl
:   This is equivalent to `--on-new-cert distrust`.

--certs <filename>
:   In addition to CA certificates obtained from other truststores, use the CA certificates in the
    given `filename`. This file is in PEM format. For information on the TLS/SSL certificate
    management functionality, please see Coverity Platform 2026.6.0 User and Administrator Guide.

--connect-timeout <n>
:   Sets the timeout for establishing connections to `n` seconds. If a connection to
    Coverity Connect cannot be established within this time, the transaction is
    aborted. This timeout cannot be disabled. The default value is 60
    seconds.

--dataport <coverityconnect_commitport>
:   This option is accepted for compatibility with the `cov-commit-defects` command,
    but is ignored. The `cov-install-updates` command does not
    use the commit:// protocol. Use the
    --port option to specify a command port. This option
    is deprecated.

--host <coverityconnect_host>
:   Specifies the host name of the Coverity Connect instance from which to download Coverity
    Analysis updates. The `--host` option is required. This
    option is deprecated.

--https-port <coverityconnect_port>
:   Using `--https-port <coverityconnect_port>` is equivalent
    to specifying `--port <coverityconnect_port> --ssl`. This
    option is deprecated.

--max-retries <n>
:   Sets the number of times to retry failed or aborted requests with Coverity Connect to
    `n`. Note that this does not include the initial attempt,
    so a setting of 1 results in at most 2 request attempts. A setting of 0
    means to never retry failed requests. The default value is 1.

--on-new-cert <trust | distrust>
:   Indicates whether to trust (with trust-first-time) self-signed certificates, presented by the
    server, that the application has not seen before. Default is `distrust`. If
    `distrust` and the certificate is self-signed, the connect attempt will fail.
    For information on the new TLS/SSL certificate management functionality, please
    see Coverity Platform 2026.6.0 User and Administrator Guide.

    CAUTION:

    Setting `on-new-cert` to
    `trust` does not currently work with Coverity Analysis and
    Black Duck® Bridge. The workaround is to manually
    add the self-signed certificate to your operating system's
    certificate store. This will tell the operating system that it can
    trust this certificate, and should allow you to continue.

--port <coverityconnect_port>
:   Specifies the command port to use when connecting to the Coverity Connect
    server. If `--port` is not specified on the command line, the
    default is `8080` without --ssl and `8443`
    with --ssl. This option is deprecated.

--response-timeout <n>
:   Sets the response timeout to `n` seconds. For every request for data sent to
    Coverity Connect, if a response is not received within this time, the
    request is aborted. A setting of `0` disables this timeout.
    The default value is `300` seconds.

--sleep-before-retry <n>
:   Sets the time to sleep before retrying a failed or aborted request with Coverity Connect to
    `n` seconds. A setting of `0` disables
    this sleep. The default value is 1 second.

--ssl
:   Specifies that TLS/SSL is to be used for both HTTPS port and dataport connections. For the
    negotiation with the server on whether to use TLS/SSL on the dataport, this
    is the equivalent of `--encryption required`. This option
    is deprecated. Instead, using the --url option with the
    `https:` scheme is recommended.

--user <username>

--password <password>
:   The username and password used to log into the Coverity Connect instance.
    These will be encrypted if `--ssl` is used. These options
    are required if the `--auth-key-file` option is not
    present.

--url <path>
:   Use this option in place of --host and
    --port to specify the Coverity Connect server to
    consult for incremental releases.

    The --host and --port options are
    deprecated and will be removed in a future release.

    The --url option may also be used to provide username and
    password information, making the --user and
    --password options redundant in those cases.

    The `<path>` operand has the following format:

    ```
    <scheme>://[<username>[:<password>]@]<hostname>[:<port>][/<context_root>]
    ```

    - `<scheme>` is either http or https;
      https is preferred.
    - `<username>` is a valid user name for the specified Coverity Connect
      server.
    - `<password>` is a valid password for the specified Coverity Connect server. Use
      of this field is discouraged because it is insecure. The use of an
      auth-key file or the COVERITY_PASSPHRASE
      environment variable is preferred.
    - `<hostname>` is the host name of the Coverity Connect server.
    - `<port>` is the command port for the Coverity Connect server. If not supplied,
      defaults to 80 for http and 443 for https.
    - `<context_root>` the context route for the Coverity Connect instance if that
      instance uses a context route other than the default top-level
      context root. For example,
      https://example,com:8080
