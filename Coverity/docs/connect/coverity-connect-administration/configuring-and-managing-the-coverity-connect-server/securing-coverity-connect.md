---
title: "Securing Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/securing-coverity-connect.html"
content_id: "xpPUe64mjrB3qTJgk9LIfA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:09.794675+00:00"
---

# Securing Coverity Connect

Several features of Coverity Connect control access to the
system and protect the critical data it contains. Review the following sections to learn
how to enhance system security in your data environment.

Configuring Coverity Connect to use SSL
:   SSL provides authentication and encryption between clients and servers. See
    Configuring Coverity Connect for TLS/SSL.

Integrating with LDAP servers
:   LDAP provides centralized user authentication and management. See LDAP security.

Configuring Coverity Connect to use Kerberos
:   Kerberos provides authentication among clients and servers in a realm. See
    Configuring Coverity Connect to use Kerberos.

Role-Based Access and Control (RBAC)
:   RBAC provides detailed control over users and what parts of the Coverity
    Connect system they have access to. See Roles and role-based access control.

To operate Coverity Connect in a safety- and security-conscious manner, please keep the
following tips in mind:

- Make sure physical access is restricted to the machine where Coverity Connect
  is installed.
- Verify that file permissions for installed files (including Postgres files)
  are set only to the Coverity Connect user. Note that the installer correctly
  applies permissions to all files and directories during the initial install.
  It is not recommended that these privileges be modified as it may affect the
  security of the application.
- Use standard IT password rules for users, such as long and complex passwords,
  and requiring that passwords be changed periodically.
- Note that Coverity Connect will not run under the root or Administrator
  accounts. The installer requires a dedicated user account on Unix-like
  systems and should refuse to install or start if attempted to run under
  root. On Windows, by default Coverity Connect uses a Service Account when
  configured to start as a service. Although the installer requires
  Administrator privileges to run, this requirement addresses installation
  location privileges only, not the privileges required to run Coverity
  Connect.
- It is highly recommended that Coverity Connect be configured to use HTTPS
  using a corporate SSL certificate authority.
- Application configuration files ($CIM_HOME/config) contain sensitive
  information. By default, $CIM_HOME/config/pgpass and
  $CIM_HOME/config/cim.properties are accessible only by the account running
  Coverity Connect and administrators (root/Administrator).
- When installing Coverity Connect with the embedded DB option, the database
  listens exclusively to `localhost` and does not accept
  network connections. Only a single application account is configured for
  accessing the database. This mechanism should not be subverted by adding
  additional users. If this functionality is required, an external database
  should be used with configuration vetted by a certified database
  administrator (DBA).
- For even stronger security, use system-level access logging (i.e. syslogNG,
  Splunk, etc.) to report when connections are made to the Coverity Connect
  account.
- To ensure that configuration files are not modified without notification,
  customers can use a tripwire application to watch the configuration
  directory ($CIM_HOME/config).
- To protect data on the drive from being read by untrusted third parties in
  the event the drive is moved, make sure to use hardware which supports the
  Trusted Computing standard.
