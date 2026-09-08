---
title: "Manual Installation"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/manual-installation.html"
content_id: "i~qsKj_bPnMl2BMMVDDt9g"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:16.675295+00:00"
content_hash: "7bc5bb3522a7d5c4ba99ae9135a943d90188604ce8d1c4d7bf64a76989d69bcb"
---

# Manual Installation

This section provides information on installing SRM manually. Note that while manual
installation provides expanded configuration options, it also requires a high level of
technical knowledge and experience with the third-party tools and software required to
deploy SRM.

## Stack

The supported stack for SRM is as follows:

- Java 21
- Apache Tomcat 9.0.x
- MariaDB 10.6.x or MySQL 8.0.x

Note: Other configurations are not guaranteed to work.

## Prerequisites

Nothing specific beyond the stack should be required to install SRM on macOS.

On Windows, the VC15 runtime is required. For more information, see <https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows>.

On Linux, the Chromium binary used internally by SRM requires the following system
packages to be available:

- ca-certificates
- libglib2.0-0
- libnss3
- libnspr4
- libatk1.0-0
- libatk-bridge2.0-0
- libcups2
- libdrm2
- libxkbcommon0
- libxcomposite1
- libxdamage1
- libxfixes3
- libxrandr2
- libgbm1
- libpango-1.0-0
- libcairo2
- libasound2
- fonts-liberation
- libxshmfence1
- libjpeg-turbo8
- libpng16-16

To install these, run one of the following commands depending on your Linux distribution:

**On Ubuntu/Debian-based:**

```
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    ca-certificates libglib2.0-0 libnss3 libnspr4 libatk1.0-0 \
    libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 \
    libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 \
    fonts-liberation libxshmfence1 libjpeg-turbo8 libasound2 libpng16-16
```

Note:
For Ubuntu 24.04+, some package names have changed. If the above fails for
`libasound2` or `libpng16-16`, use these
alternatives instead: `libasound2t64`, `libpng16-16t64`.

**On RHEL/CentOS/RPM-based:**

```
sudo dnf install -y \
    ca-certificates glib2 nss nspr atk at-spi2-atk cups-libs \
    libdrm libxkbcommon libXcomposite libXdamage libXfixes libXrandr \
    mesa-libgbm pango cairo alsa-lib \
    libxshmfence libjpeg-turbo libpng liberation-fonts
```

Note:
On older versions that use `yum` as the package manager, such as
RHEL/CentOS 7 and earlier, replace `dnf` with `yum`.

## Setup

Start by extracting the SRM zip file. The three files of interest are as follows:

- `srm`
- `codedx.props`
- `logback.xml`

### AppData

SRM stores a variety of files, including configuration files, temporary files
created during analyses, log files, and copies of files uploaded by the user.
The root location for these files is the SRM `AppData`
directory. You will need to create a directory to serve as the
`AppData` directory (which will be referred to in these
instructions as `SRM_APPDATA`). Make sure that the user running
Tomcat has read-and-write privileges to `SRM_APPDATA`.

Move both `codedx.props` and `logback.xml` into
`SRM_APPDATA`.

The user that Tomcat will be running as will need to have full access to the
appdata folder. Since sensitive data may be stored here as well, it is
recommended that access to this folder be restricted via disk permissions as
well as access restrictions to the machine SRM will be running on.

### Database

Create a new, empty database for SRM to use and create a user for SRM with
`SELECT, INSERT, UPDATE, DELETE, CREATE, CREATE TEMPORARY TABLES,
ALTER, REFERENCES, INDEX, DROP, TRIGGER` permissions on the
database.

For example,

```
CREATE USER 'srm'@'%' IDENTIFIED BY 'enter-a-password-here';
CREATE DATABASE srm;
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, CREATE TEMPORARY TABLES, ALTER, REFERENCES, INDEX, DROP, TRIGGER ON codedx.* to 'srm'@'%';
FLUSH PRIVILEGES;
```

Edit the `codedx.props` file to reflect your new database and the
credentials required to connect to it. For example,

```
swa.db.url = jdbc:mysql://localhost/srm?permitMysqlScheme
swa.db.user = srm_username
swa.db.password = srm_user_password
```

**Required changes:**

- Make sure `sql_mode` doesn't contain
  `ONLY_FULL_GROUP_BY` or
  `PAD_CHAR_TO_FULL_LENGTH`. Newer versions of MySQL
  (as of v5.7) use a `sql_mode` that includes
  `ONLY_FULL_GROUP_BY`. MariaDB includes neither
  setting by default, as of this writing. Make sure if using MySQL,
  `sql_mode` doesn't include
  `NO_AUTO_CREATE_USER` as it's no longer supported in
  MySQL 8. To view the current configuration of this, you may run the
  query `select @@sql_mode`. For example, the defaults for
  MySQL 8 with the `ONLY_FULL_GROUP_BY` option removed
  would be
  `sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION`.
- `optimizer_search_depth=0`
- `character_set_server=utf8mb4`
- `collation_server=utf8mb4_general_ci`
- `log_bin_trust_function_creators=1`

### Tomcat

Drop the `srm.war` file into Tomcat's `webapps`
directory. (You can also deploy it via Tomcat's manager interface if you
prefer).

You also need to add a property to let the SRM app know the value of
`SRM_APPDATA`. You will need to set a value for the Java
property `codedx.appdata`. You will also need to add
`-Dcodedx.appdata=SRM_APPDATA` to the list of
`CATALINA_OPTS` values. (Where that's done is
system-dependent: see the [Tomcat Documentation](https://tomcat.apache.org/tomcat-8.0-doc/RUNNING.txt) for details.) Alternatively,
you can define a `SRM_APPDATA` environment variable with this
value, if you'd prefer that to configuring `CATALINA_OPTS`.

Additionally, you will need to ensure that the JVM will use
`UTF-8` as its file encoding. Doing so prevents issues with
Japanese user input like comments and manual results. Add
`-Dfile.encoding=UTF-8` to the list of
`CATALINA_OPTS` values.

Now when you start Tomcat, SRM will be able to access the
`codedx.props` file.

**Configuration**

To make Tomcat stop reporting about cache issues, edit
`conf/context.xml` and add `<Resources
cachingAllowed="true" cacheMaxSize="128000" />` inside the
`<Context>`.

It is also recommended to edit `conf/server.xml` and raise the
value of `Connector`
`connectionUploadTimeout`, if applicable. This is set to 3600000
by default when using the SRM installer. We also recommend setting
`disableUploadTimeout` to `false`. In the same
file, `connectionTimeout` on the `Connector` is by
default `20000` for an installation of SRM.

Further configuration may be performed per your deployment and requirements (such
as configuring AJP and placing an instance of Apache HTTPD in front of Tomcat or
changing the logging configuration).

### Starting SRM

For version 2023.12.5 or later, if SRM is being deployed behind a proxy that is using HTTPS, it is recommended to set the prop `auth.cookie.secure` to `true`. This will allow the secure flag on the session cookie to be set and passed along through HTTPS via the proxy.

Once everything is configured, start the database and Tomcat (make sure the
database is running before you start Tomcat). Open a web browser and point it at
SRM (e.g., `http://localhost/srm/`). You will be presented with
an installation screen allowing you to set the super admin username and password
and initialize SRM.

You may need to add a `codedx.internal-url` setting to your
`codedx.props` file. This should contain a URL that SRM can
access itself at, for example `http://localhost/srm/` or
`https://localhost/srm`. This will depend on how exactly SRM
is deployed.
