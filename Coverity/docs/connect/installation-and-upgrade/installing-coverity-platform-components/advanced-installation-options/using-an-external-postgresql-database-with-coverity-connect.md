---
title: "Using an external PostgreSQL database with Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-an-external-postgresql-database-with-coverity-connect.html"
content_id: "iqRiQ8_tYkLANSDcXcpnwA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:58.250427+00:00"
---

# Using an external PostgreSQL database with Coverity Connect

Coverity Connect can use a PostgreSQL database as an external database.

If you use an existing, external PostgreSQL database you are responsible for the
database, including implementing a database backup and recovery system.

CAUTION:

This section is intended only for experienced PostgresSQL DBAs
(database administrators).

**Configuring PostgreSQL for Coverity Connect**

You should be familiar with the following before performing this procedure.

**Prerequisites for external PostgreSQL configuration**

- A working installation of a supported PostgreSQL database: For supported PostgreSQL versions,
  see Coverity Connect software requirements.
- The ability to create a database role and a database.
- A database back-up and recovery system. Coverity Connect does not back up external
  databases.
- If you are running PostgreSQL 18 on older operating system versions (RHEL 8, Ubuntu
  20, Debian 11, and so on), you must ensure that OpenSSL 3 is available before
  installing PostgreSQL 18.

To configure an external PostgreSQL database for Coverity Connect:

1. Create a new database and a role that has permissions
   to create, modify, and drop tables for Coverity Connect. For
   example:

   ```
   createdb -O role name...
   ```

   The
   permissions allow the installer to create the database schema and to alter or
   drop tables when you upgrade Coverity Connect.

   It is required that you
   create the database with the following encoding
   settings:

   `--encoding UTF8 --locale C`

   These settings might not be available on some existing PostgreSQL
   installations, depending on the version, the operating system, and the options
   used when initially creating the database cluster. For more information consult
   the PostgreSQL documentation.
2. Record the following information prior to configuring
   Coverity Connect:
   - PostgresSQL role name and password.
   - Database name.
   - PostgresSQL database server name.
   - Port of the database listener.
   - Root certificate if SSL is enabled and you want to do server authentication.
     It must be a PEM encoded X509 certificate.
   - Client certificate if SSL is enabled and you want to do client
     authentication. It must be a PEM encoded X509 certificate.
   - Client certificate key if SSL is enabled and you want to do client
     authentication. The key file must be in PKCS-12 or in PKCS-8 DER format.

     A
     PEM key can be converted to DER format using the
     `openssl` command, for
     example:

     ```
     openssl pkcs8 -topk8 -inform PEM -in postgresql.key -outform DER
                                 -out postgresql.pk8 -v1 PBE-MD5-DES
     ```

     PKCS-12
     key files are recognized only if they have the `.p12`
     (42.2.9+) or the `.pfx` (42.2.16+) extension.

     If
     your key has a password, provide it using the key password described in
     Table 2.
     Otherwise, you can add the flag `-nocrypt` to the command
     above to prevent the connection from requesting a password.
   - Key password, if client certificate key has a password.

   For more information about connecting to PostgreSQL with SSL, see
   [Connecting to the Database](https://jdbc.postgresql.org/documentation/head/connect.html#ssl).
3. Using the Coverity Platform installer, specify **Connect to an existing PostgreSQL
   database**, and follow the prompts to complete the installation. The settings
   used by the installer for this configuration are described in Table 1.

   Table 1. External PostgresSQL installer settings

   | Name | Description | Default |
   | --- | --- | --- |
   | PostgreSQL server name | Usually the host name where the PostgreSQL server runs. | None |
   | Database port | The TCP port on which the server is listening for connections. | `5432` |
   | Database name | Name of the database that you previously created for use by Coverity Connect. | None |
   | Database user | User name that owns the database name previously specified. | None |
   | Database password | Password for previously specified user. | None |
   | SSL mode | SSL mode for external PostgreSQL database connection. Valid values: `disable`, `allow`, `prefer`, `require`, `verify-ca`, `verify-full`. For more information about SSL mode, see Table 2. | `verify-ca` |
   | Root certificate | SSL root certificate that you previously prepared for the server authentication. | None |
   | Perform client authentication | Specifies that the external PostgreSQL database connection will use client authentication. | `False` |
   | Client certificate | Client certificate file that you previously prepared for the client authentication. | `None` |
   | Client certificate key | Client certificate key that you previously prepared for the client authentication. | None |
   | Key password | Key password that you previously prepared for the client certificate key. | None |
   | Run as service | (Windows only) If you have Windows Administrator privileges and want to run Coverity Connect as a service. The service runs as the built-in Windows account LocalService. | `Yes` |
   | Launch web browser | (Windows only) Opens a web browser on the URL to the Coverity Connect server. | `Yes` |

   Table 2. SSL mode descriptions

   | SSL mode | Eavesdropping protection | MITM protection | User objective |
   | --- | --- | --- | --- |
   | disable | No | No | I don't care about security, and I don't want to pay the overhead of encryption. |
   | allow | Maybe | No | I don't care about security, but I will pay the overhead of encryption if the server insists on it. |
   | prefer | Maybe | No | I don't care about encryption, but I wish to pay the overhead of encryption if the server supports it. |
   | require | Yes | No | I want my data to be encrypted, and I accept the overhead. I trust that the network will make sure I always connect to the server I want. |
   | verify-ca | Yes | Depends on CA-policy | I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server that I trust. |
   | verify-full | Yes | Yes | I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server I trust, and that it's the one I specify. |

   For more information about configuring SSL connections with a PostgresSQL
   database, see [SSL Support](https://www.postgresql.org/docs/9.1/libpq-ssl.html) .
4. Start Coverity Connect.
5. Sign in to Coverity Connect by entering the following URL in your web browser's
   location bar:

   `http://hostname:http_port`

   When installing Coverity Connect with an external PostgreSQL database, you
   are not asked to specify an administrator account password. Instead, sign in
   with user name **admin**, and password **coverity**. For security reasons,
   after the initial sign-in, change the password for this account.

In the event of difficulties connecting to an external database, you might want to
examine and edit the property file (`cim.properties`) that controls the
external database configuration. If you want to modify the SSL configuration of your
external database connection, you must edit this property file. See Understanding database information in the cim.properties file.
