---
title: "Coverity Platform silent installer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-platform-silent-installer.html"
content_id: "J0BGoGr7rJ8McvJtdbDnTw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:56.891761+00:00"
---

# Coverity Platform silent installer

The Coverity Platform silent installer allows you to specify all of the installation
configuration details on the command line so you do not need to run the "step-through"
process either through the command line (`-c`) or the graphical
(`-g`) installer modes.

To run the silent installer, execute the installer file with the `-q` option,
followed by the installation parameters. The `-q` option and the
installation parameters must all be on the same command line. The following example
installs a "production" Coverity Connect deployment with an embedded database.

```
./cov-platform-linux64-2026.6.0.sh -q \
  --installation.dir ~/cov-platform-linux64-2026.6.0 \
  --license.region=0 \
  --license.agreement=agree \
  --license.path=/tmp/license.dat \
  --db.type=0 \
  --db.embedded.performance=0 \
  --admin.password.env=ADMIN_PASSWORD \
  --hostname=myhostname \
  --http.port=14800 \
  --commit.port=14801 \
  --control.port=14802 \
  --db.embedded.port=14803
```

If you are installing on Windows, use the `-q -console` options preceded
by a `start /wait` command. If the executable filename contains spaces,
precede it with empty double quotes, even if the filename itself is double-quoted, for
example:

```
> start /wait "" "<my executable name>" -q -console
```

Note: You can include the empty double quotes whether or not the executable name contains
spaces.

The silent installer accepts the following options. Note that not all of the options are
required. For example, you do not need to specify the options for an external
(`postgres`) database if you are installing Coverity Connect with an
embedded database. If you use any of the following parameters, you should provide
specifically assigned values. Some values, if left blank, will accept the default value,
but this is not a recommended practice. For more information about the installation
options, see Installing Coverity Connect.

## Installer command line options

Note: Do not use the `-V` prefix with these options:

| Option | Description |
| --- | --- |
| `-q` | Required. Enables the silent installer. |
| `-console` | Required on Windows. Displays status messages in the console from which you invoked the silent installer. |

## General parameters

| Parameter | Description |
| --- | --- |
| `--install.type=0 | 1 | 2 | 3 | 4` | Sets the installer to backup-and-restore mode. For this option, the following values are available:  - 0 - Fresh install - 1 - In-place upgrade - 2 - Backup and restore - 3 - Intermachine upgrade - 4 - Upgrade preparation  Otherwise, the default value is set to `0`. |
| `--license.agreement=agree` | **Required.** Agree to the terms of the Coverity product license. |
| `--license.region=1 | 2 | 3 | 4 | 5 | 6 | 7` | **Required.** Specifies your region, used for selecting the correct product license. The following values (and representative region) are available:  - 1 - Americas, Africa, and Israel - 2 - Japan - 3 - Taiwan - 4 - China Mainland - 5 - Korea - 6 - International license (for any countries not mentioned in 1-5) - 7 - Evaluation Only. This installation is being used solely for evaluation purposes,   and is not for production use |

## Fresh installation parameters

These parameters specify the options used for completing a fresh installation of
Coverity Connect. For a fresh installation, the `--install.type`
setting value must be set to `0`.

| Parameter | Description |
| --- | --- |
| `--accept.https=true | false` | Specifies that Coverity Connect should use SSL (HTTPS) communication. The HTTPS protocol requires an installed server certificate from a certificate authority. The default value is `false`. |
| `--admin.password=password` | **Deprecated:** This option is not recommended because the password might be visible to any user who has access to the list of running processes during the installation. Post installation, the password might also be visible to users who have access to the command history. Use either the `admin.password.file` or `admin.password.env` option instead. |
| `--admin.password.env=environment variable name` | The name of an environment variable containing the administrator password that you will use to log into Coverity Connect upon installation. |
| `--admin.password.file=absolute file path` | The absolute file path of a file containing the administrator password that you will use to log into Coverity Connect upon installation. |
| `--commit.port=port` | **Optional.** Specifies the Coverity Connect Commit port. Default value is 9090. The HTTP(S) port is recommended over the Commit port. The Commit port will be deprecated in a future release. |
| `--control.port=port` | **Recommended.** Specifies the port used by the embedded application server for internal server communication. Default value is 8005. |
| `--create.program.group=true | false` | Grants the user who is running the installer permission to create all program group actions that rely on a default program group. This parameter is optional and only valid on Windows. The default value is `true`. |
| `--db.type=0 | 1` | Specifies the type of database that is used with the Coverity Connect application server. The following option values are available:  - 0 - Embedded database parameters This includes the `--db.embedded.data` and   `--db.embedded.port`   options. - 1 - External database parameters This includes the following options:   `--db.external.client.auth`,   `--db.external.client.cert`,   `--db.external.client.cert.key`,   `--db.external.key.password`,   `--db.external.host`,   `--db.external.name`,   `--db.external.password`,   `--db.external.port`,   `--db.external.root.cert`,   `--db.external.sslmode`, and   `--db.external.user`. Note: The   external database must be created before you run the   installer. For more information, see Advanced installation options.  Otherwise, the default value is 0. This specifies that Coverity Connect will connect to the embedded database. |
| `--db.embedded.performance=0 | 1` | Selects the Coverity Connect database performance tuning option. Based on your installation type, choose one of the following values:  - 0 - Production - 1 - Demo  The default value is 0. |
| `--hostname=host-name` | **Required.** Specifies the hostname of the Coverity Connect server. |
| `--http.port=port` | **Recommended.** Specifies the HTTP port number for Coverity Connect. Default value is `8080`. |
| `--https.port=port` | **Recommended.** Specifies the HTTPS port number for Coverity Connect. Default value is 8443. Valid if the `--accept.https` value is set to `true`. |
| `--installation.dir=directory-path` | Location in which to install Coverity Connect. This must be an absolute directory path. |
| `--license.path=path` | **Required.** Specifies the full directory path of a Coverity license.dat file. |
| `--program.group.all.users=true | false` | Specifies that the program group will be created for all Windows users. This parameter is optional and only valid on Windows. The default value is `false`. |
| `--program.group.name=directory path` | Specifies the name for the program group that appears in the Windows Start menu and the subpath in which the program group files are installed (this subpath is appended to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\). This parameter is optional and valid only on Windows. Default value is `Coverity\Coverity Platform` release version number, for example, Coverity\Coverity Platform 2022.9.0. |
| `--service.enable=true | false` | Specifies that Coverity Connect will be enabled as a Windows service. This parameter is optional and will not affect any installations on non-Windows platforms. Default value is `false`. |

## In-place upgrade parameters

These parameters specify the options used for completing an in-place upgrade of an
installed instance of Coverity Connect. To upgrade a previously installed instance,
the `--install.type` setting value must be set to
`1`.

Prior to beginning an upgrade, see Upgrading Coverity, Upgrade overview and Important upgrade considerations for important upgrade information and procedures.

| Parameter | Description |
| --- | --- |
| `--db.backup=true | false` | Default value is set to `false`. If set to `true`, this option determines if the in-place upgrade process creates a backup of the existing embedded database. |
| `--db.backup.dir=directory-path` | **Required.** Specifies the directory where the backup database is stored. Valid if the `--db.backup` option is set to `true`. |
| `--db.backup.file= filename` | **Required.** File name of backup. Valid if the `--db.backup` option is set to `true`. |
| `--db.embedded.performance=0 | 1` | Selects the Coverity Connect database performance tuning option. Choose values depending on your installation type. The following setting values are available:  - 0 - Production - 1 - Restore  Otherwise, the default value is 0. |
| `--installation.dir=directory-path` | Location in which to install Coverity Connect. This must be an absolute directory path. |
| `--license.path=path` | **Required.** Specifies the full directory path of a Coverity license.datfile. |
| `--upgrade.db.external.sslmode=0 | 1 | 2 | 3 | 4 | 5` | Sets the SSL mode for external PostgreSQL database connection. For this option, the following values are available:   - 0: disable - 1: allow - 2: prefer - 3: require - 4: verify-ca - 5: verify-full   For more information about SSL mode, see Table 2.  By default, this property is not set, which means that the SSL property settings from the previously installed instance are used. If the `sslmode` property is not specified in the previously installed instance, the in-place upgrade adds an `sslmode` property and sets its value to `2`.  This property is valid if the previously installed instance connected to an external PostgreSQL database. It is skipped if the previously installed instance connected to an embedded database. |
| `--upgrade.db.external.root.cert=absolute file path` | The absolute file path for the SSL root certificate. The certificate must be PEM X.509 encoded.  Recommended if the `--upgrade.db.external.sslmode` option is set to `4` or `5`.  Valid if the `--upgrade.db.external.sslmode` option is set. |
| `--upgrade.db.external.client.auth=true | false` | Specifies that the external PostgreSQL database connection uses client authentication. Default value is `false`.  Valid if the `--upgrade.db.external.sslmode` option is set. |
| `--upgrade.db.external.client.cert=absolute file path` | The absolute file path for the certificate file. The certificate must be PEM X.509 encoded.  This parameter is ignored when using PKCS-12 keys because in that case the certificate is retrieved from the same key file.  Valid if the `--upgrade.db.external.client.auth` option is set to `true`. |
| `--upgrade.db.external.client.cert.key=absolute file path` | The absolute path for the key file. The key file must be in PKCS-12 or in PKCS-8 DER format.  A PEM key can be converted to DER format using the `openssl` command, for example:  `openssl pkcs8 -topk8 -inform PEM -in postgresql.key -outform DER -out postgresql.pk8 -v1 PBE-MD5-DES`  PKCS-12 key files are recognized only if they have the `.p12` (42.2.9+) or the `.pfx` (42.2.16+) extension.  If your key has a password, provide it using the `--upgrade.db.external.key.password` option described in this table. Otherwise, you can add the flag `-nocrypt` to the command above to prevent the connection from requesting a password.  Required and valid if the `--upgrade.db.external.client.auth` option is set to `true`. |
| `--upgrade.db.external.key.password=key password` | Use this option to specify the password if the key file set by the `--upgrade.db.external.client.cert.key` option has a password. Valid if the `--upgrade.db.external.client.auth` option is set to `true`. |

## Backup-and-restore upgrade parameters

These parameters specify the options used for completing a backup-and-restore upgrade
of an installed instance of Coverity Connect. To backup and restore an upgrade, the
`--install.type` setting value must be set at 2.

| Parameter | Description |
| --- | --- |
| `--accept.https=true | false` | Specifies that Coverity Connect should use SSL (HTTPS) communication. The HTTPS protocol requires an installed server certificate from a certificate authority. Default value is taken from the previous Coverity Connect instance that is stored. |
| `--backup.dir=directory-path` | Specifies the directory where the backup data is stored. Required if the `--backup.automated` option is set to `false`. |
| `--db.type=0 | 1` | Specifies the type of database that is used with the Coverity Connect application server. The following option values are available:  - 0 - Embedded database parameters This includes the `--db.embedded.data` and   `--db.embedded.port`   options. - 1 - External database parameters Setting `--install.type` to   `2` when performing a   backup-and-restore upgrade on an instance that uses an   external database is not supported. For more information   about performing a backup-and-restore upgrade on an   instance that uses an external database, see Upgrading instances that use an external database.  For more information, see Advanced installation options.  Otherwise, the default value is `0`. This specifies that Coverity Connect will connect to the embedded database. |
| `--backup.automated=true | false` | Initiates the automated backup and restore process if set to true. Default value is `true`. When set to `false`, the installer upgrades from a previously created backup. Note that when `--backup.automation=false`, the `--backup.dir` option must be specified. |
| `--commit.port=port` | **Recommended.** Specifies the Coverity Connect commit port. Default value remains the same from the previous Coverity Connect instance that is stored. |
| `--control.port=port` | **Recommended.** Specifies the port used by the embedded application server for internal server communication. Default value remains the same from the previous Coverity Connect instance that is stored. |
| `--db.embedded.performance=0 | 1` | Selects the Coverity Connect database performance tuning option. Choose values depending on your installation type. The following setting values are available:  - 0 - Production - 1 - Restore  Otherwise, the default value is 0. |
| `--existing.instance.dir=directory-path` | **Required.** The path to the existing Coverity Connect installation. |
| `--hostname=host-name` | **Required.** Specifies the hostname of the Coverity Connect server. |
| `--http.port=port` | **Recommended.** Specifies the HTTP port number for Coverity Connect. Default value remains the same from the previous Coverity Connect instance that is stored. |
| `--https.port=port` | **Recommended.** Specifies the HTTPS port number for Coverity Connect. Default value remains the same from the previous Coverity Connect instance that is stored. Valid if the `--accept.https` option is set to `true`. |
| `--installation.dir=directory-path` | Location in which to install Coverity Connect. This must be an absolute directory path. |
| `--license.path=path` | **Required.** Specifies the full directory path of a Coverity license.datfile. |
| `--service.enable=true | false` | Specifies that Coverity Connect be enabled as a Windows service. This parameter is optional and will not affect any installations on non-Windows platforms. Default value is `false`. |

## Intermachine upgrade parameters

These parameters specify the options used for completing an intermachine upgrade of
an installed instance of Coverity Connect. This is similar to the backup-and-restore
upgrade, but the upgraded instance will be on a different machine than the original.
To prepare your system for an intermachine upgrade, the
`--install.type` setting should be set to 3.

| Parameter | Description |
| --- | --- |
| `--accept.https=true | false` | Specifies that Coverity Connect should use SSL (HTTPS) communication. The HTTPS protocol requires an installed server certificate from a certificate authority. Default value is taken from the previous Coverity Connect instance that is stored. |
| `--backup.dir=directory-path` | **Required**. Specifies the directory where the backup data is stored. |
| `--commit.port=port` | **Recommended.** Specifies the Coverity Connect commit port. Default value remains the same from the previous Coverity Connect instance that is stored. |
| `--control.port=port` | **Recommended.** Specifies the port used by the embedded application server for internal server communication. Default value remains the same from the previous Coverity Connect instance that is stored. |
| `--db.backup.dir=directory-path` | **Required.** Determines if the in-place upgrade process creates a backup of the existing embedded database. |
| `--db.embedded.performance=0 | 1` | Selects the Coverity Connect database performance tuning option. Choose values depending on your installation type. The following setting values are available:  - 0 - Production - 1 - Demo Otherwise, the default value is 0. |
| `--db.type=0 | 1` | Specifies the type of database that is used with the Coverity Connect application server. The following option values are available:  - 0 - Embedded database parameters This includes the `--db.embedded.data` and   `--db.embedded.port`   options. - 1 - External database parameters This includes the following options:   `--db.external.client.auth,`   `--db.external.client.cert`,   `--db.external.client.cert.key`,   `--db.external.key.password`,   `--db.external.host`,   `--db.external.name`,   `--db.external.password`,   `--db.external.port`,   `--db.external.root.cert`,   `--db.external.sslmode`, and   `--db.external.user`. Note: The   external database must be created before you run the   installer. For more information, see Advanced installation options.  Otherwise, the default value is `0`. This specifies that Coverity Connect will connect to the embedded database. |
| `--hostname=host-name` | **Required.** Specifies the hostname of the Coverity Connect server. |
| `--http.port=port` | **Recommended.** Specifies the HTTP port number for Coverity Connect. Default value remains the same from the previous Coverity Connect instance that is stored. |
| `--https.port=port` | **Recommended.** Specifies the HTTPS port number for Coverity Connect. Default value remains the same from the previous Coverity Connect instance that is stored. Valid if the `--accept.https` option is set to `true`. |
| `--license.path=path` | **Required.** Specifies the full directory path of a Coverity license.datfile. |
| `--service.enable=true | false` | Specifies that Coverity Connect be enabled as a Windows service. This parameter is optional and will not affect any installations on non-Windows platforms. Default value is `false`. |

## Upgrade preparation parameters

These parameters specify the options used for completing an upgrade preparation of an
installed instance of Coverity Connect. This creates a backup for future use by the
upgrade installer. To prepare your system for an upgrade, the
`--install.type` setting should be set to `4`.

Prior to beginning an upgrade, see Upgrading Coverity, Upgrade overview and Important upgrade considerations for important upgrade information and procedures.

| Parameter | Description |
| --- | --- |
| `--backup.dir=directory-path` | **Required.** Specifies the directory where you want to store the backup data when using the automated backup and restore process. You can also use this setting to retrieve backed up database information if you are upgrading (from a previously created backup). |
| `--existing.instance.dir=directory-path` | **Required.** The path of the existing Coverity Connect. |

## Embedded database parameters

These options set the parameters for installing Coverity Connect with an embedded
PostgreSQL database. The installer will automatically install and configure the
database.

| Parameter | Description |
| --- | --- |
| `--db.embedded.data=path` | Specifies the full path of the directory to which the database files will be installed. If you do not enter this option, the database directory defaults to <install_dir>/database. |
| `--db.embedded.port=database_port_number` | **Optional.** Specifies the database port. Default value remains the same from the previous Coverity Connect instance that is stored. However, for a fresh installation, the default value is `5432`. |

## External database parameters

These options set the parameters for installing Coverity Connect with an external
PostgreSQL database.

| Parameter | Description |
| --- | --- |
| `--db.external.client.auth=true | false` | Specifies that the external PostgreSQL database connection uses client authentication. Default value is `false`. |
| `--db.external.client.cert=absolute file path` | The absolute file path for the certificate file. The certificate must be PEM X.509 encoded.  This parameter is ignored when using PKCS-12 keys because in that case the certificate is retrieved from the same key file.  Valid if the `--db.external.client.auth` option is set to `true`. |
| `--db.external.client.cert.key=absolute file path` | The absolute path for the key file. The key file must be in PKCS-12 or in PKCS-8 DER format.  A PEM key can be converted to DER format using the `openssl` command, for example:  `openssl pkcs8 -topk8 -inform PEM -in postgresql.key -outform DER -out postgresql.pk8 -v1 PBE-MD5-DES`  PKCS-12 key files are recognized only if they have the `.p12` (42.2.9+) or the `.pfx` (42.2.16+) extension.  If your key has a password, provide it using the `--db.external.key.password` option described in this table. Otherwise, you can add the flag `-nocrypt` to the command above to prevent the connection from requesting a password.  Required and valid if the `--db.external.client.auth` option is set to `true`. |
| `--db.external.host=host_name` | **Required.** Specifies the hostname of the external PostgreSQL database. |
| `--db.external.key.password=key password` | Use this option to specify the password if the key file set by the `--db.external.client.cert.key` option has a password. Valid if the `--db.external.client.auth` option is set to `true`. |
| `--db.external.name=database-name` | **Required.** Specifies the name of the external PostgreSQL database. |
| `--db.external.password=database-password` | **Required.** Specifies the administrative password of the external PostgreSQL database. |
| `--db.external.port=port_number` | **Required.** Specifies the external PostgreSQL database port. |
| `--db.external.sslmode=0 | 1 | 2 | 3 | 4 | 5` | **Recommended.** Sets the SSL mode for an external PostgreSQL database connection. For this option, the following values are available:   - 0: disable - 1: allow - 2: prefer - 3: require - 4: verify-ca - 5: verify-full   For more information about SSL mode, see Table 2. |
| `--db.external.root.cert=absolute file path` | The absolute file path for the SSL root certificate. The certificate must be PEM X.509 encoded.  Recommended if the `--db.external.sslmode` option is set to `4` or `5`. |
| `--db.external.user=admin-user-name` | **Required.** Selects the name of the administrative user that created the external PostgreSQL database. |
