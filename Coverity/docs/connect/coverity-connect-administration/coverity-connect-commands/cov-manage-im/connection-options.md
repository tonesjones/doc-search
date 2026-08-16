---
title: "CONNECTION options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connection-options.html"
content_id: "NGM0o2bPu8ccEy9PqZW17w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:38.568424+00:00"
---

# CONNECTION options

The following CONNECTION options are common to all modes. You can also store connection
details in the 
<install_dir>/config/coverity_config.xml
file.

--auth-key-file <keyfile>
:   Specify the location of your authentication key file, created in
    Authentication key mode. See the Coverity Platform 2026.6.0 User and Administrator Guide for important information about
    authentication key restrictions.

--certs <filename>
:   In addition to CA certificates obtained from other truststores, use the CA certificates in the
    given `filename`. This file is in PEM format. For information on the TLS/SSL certificate
    management functionality, please see Coverity Platform 2026.6.0 User and Administrator Guide.

--host <server-hostname>
:   Specify the Coverity Connect server hostname. To use this option, the
    Coverity Connect server must be running. If this option is unspecified, the
    default is the value from the cim/host element from the XML configuration
    file.

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

--password <password>
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    Specify the password for either the current user name, or the user
    specified with the `--user` option. For security reasons,
    the password transmitted to Coverity Connect is encrypted. If
    unspecified, the default is (in order of precedence):

    1. The password from the `--url` option.
    2. The password element from the XML configuration file.
    3. The environment variable `COVERITY_PASSPHRASE`.
    4. The password in the file pointed to by the environment variable
       `COVERITY_PASSPHRASE_FILE`.

    Note: The passphrase can be stored in a file without any other
    text, such as a newline character.

    Attention: On multi-user systems, such as Linux, users can see
    the full command line of all commands that all users execute. For
    example, if a user uses the `ps -Awf` command,
    identifying information such as usernames, process identities, dates and
    times, and full command lines display.

--port <server-port >
:   Specify the Coverity Connect server HTTP or HTTPS connection port. To use
    this option, the Coverity Connect server must be running. If this option is
    unspecified, the default is established in the following order:

    1. The value from the `cim/port` element from the XML configuration file.
    2. `8080`. If `--ssl` is present, the default is
       `8443`.

--ssl
:   Allow Coverity Connect to use a TLS/SSL-encrypted channel.
    This option is deprecated. Instead, using the --url option with the `https:` scheme is recommended.

--url <path>
:   Allows you to connect to a Coverity Connect instance that has a context path in its
    HTTP(S) URL. You can use this option instead of the `--host`,
    or `--port` options. The `--url` option is
    provided to accommodate the use of a context path and to deal with setting
    up Coverity Connect behind a reverse proxy.

    Use HTTPS or HTTP to connect to a Coverity Connect HTTPS or HTTP port. For
    `http`, the default port is 80; for
    `https`, the default port is 443. For example:

    ```
    https://example.com/coverity
    ```

    ```
    https://cimpop:8008
    ```

    ```
    http://cim.example.com:8080
    ```

    Note: You may not use the commit:// scheme in the URL.

--user <user_name>
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    Specifies the Coverity Connect user name. If unspecified, the default is:

    1. The username specified by the `--url` option, if
       any.
    2. The user element from the XML configuration file.
    3. The environment variable `COV_USER`.
    4. The environment variable `USER`.
    5. The name of the operating system user invoking the command (where
       supported).
    6. The UID of the operating system user invoking the command (where
       supported).
    7. `admin`.

--userLdapServer <domain>
:   Specify the domain of the user. If this option is not specified, the domain
    is resolved following this procedure:

    1. If the user name contains "@", two possible users are considered, one
       with the name as given, and one with the name comprising the
       substring after the last "@".
    2. If one and only one user name is found, then the domain is set to the
       domain of this user.
    3. Otherwise, an error is output explaining that the domain could not be
       automatically set, and asking the user to explicitly specify a
       domain with —userLdapServer for users who are ldap users.

    Note: Coverity recommends using this parameter to avoid issues when LDAP
    authentication is used.
