---
title: "Adding reverse proxy authentication"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-reverse-proxy-authentication.html"
content_id: "A784AYB7ISCU0cgHUwTLLw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:55.277070+00:00"
---

# Adding reverse proxy authentication

Coverity Connect supports Reverse Proxy Authentication (RPA). RPA is an authentication
method that can be used to transmit authentication information from a Single Sign-On
(SSO) implementation to Coverity Connect.

Note: This section provides detailed instructions for adding RPA and configuring it for SSO.
It does not cover adding SSO itself. Instructions for adding SSO are beyond the scope of
this guide.

## RPA key concepts

After adding RPA, the following points apply:

- Only LDAP users are accessible. The built-in admin user is not accessible, so
  you must assign the System Admin role to an LDAP user before enabling
  RPA.

  In Coverity Connect, RPA is one of three "LDAP-only" authentication methods
  (the others are LDAP and Kerberos) that you can use. An "LDAP-only"
  authentication method is an authentication method that only works for LDAP
  users. Only one LDAP-only authentication method can be enabled at a time.
  However, each LDAP-only authentication method can be used at the same time
  as one or more non-LDAP-only authentication methods.
- Authentication and session management is delegated to the proxy. Coverity
  Connect does not time out users' sessions. The "log out" menu item is
  disabled.
- Optionally, for Web Services access and cov-commit-defects requests,
  password-based authentication can be disabled. Authentication keys can be
  used instead when password-based authentication is disabled.

  When enabled, RPA authenticates Coverity Connect UI requests. In addition,
  after enabling RPA, you can optionally disable password-based authentication
  for SOAP and REST Web services (WS), and for
  `cov-commit-defects`. Authentication keys can be used
  instead to authenticate those three services. For more information, see
  Working with authentication keys.

  Disabling password-based authentication for WS and
  `cov-commit-defects` provides assurance that the only way
  users can authenticate to Coverity Connect is by entering their password at
  the SSO Identity Provider's screen.

  The disadvantages of disabling password-based authentication for WS and
  `cov-commit-defects` are as follows:
  - After password-authentication is disabled, users cannot
    use `cov-manage-im` or desktop plugins to
    create authentication keys. Instead, users must use the Coverity
    Connect UI.
  - After password-authentication is disabled, users must store
    authentication keys on their computer's file system. This makes
    the keys vulnerable to security attacks unless they are properly
    protected.

  To disable password-based authentication, add the following line to
  <install_dir>/config/cim.properties and
  restart the server:

  ```
  authentication.proxy.disable.password=true
  ```
- Coverity Connect will accept HTTP and HTTPS connections only from clients on
  the same host as Coverity Connect. The proxy must be on the same host.

  When RPA is used, authentication of HTTP and HTTPS Coverity Connect UI
  requests is delegated to the RP. For security reasons, the RP must reside on
  the same host machine as the Coverity Connect server. After the RP server
  authenticates an HTTPS request, it forwards the request to the Coverity
  Connect server as an HTTP request and adds a header to the request. The
  header lets the Coverity Connect server know that the request has been
  authenticated, and the header also identifies the authenticated user.

    
   [image: image]   

  In addition, with RPA, session management is delegated to the RP server,
  Coverity Connect does not time-out users' sessions, and the "Log out" menu
  item is disabled.
- Verify the forward proxy connection for a successful commit. Client calls to
  cov-commit-defects are directed to the HTTP or HTTPS proxy server, which are
  then forwarded on to the hostname specified in the URL.

  An existing (nonempty) value for the http_proxy or
  https_proxy environment variable indicates that a
  proxy is used. You can use the `printenv` command to see what
  values exist. (The port default value is 1080.)

  Note: When
  https_proxy is defined and
  cov_commit_proxy is undefined (or empty), then
  the commit protocol uses the proxy for its connection, regardless of
  whether the connection is secure or not. We recommend that you set
  cov_commit_proxy to `none`, so
  that no proxy is used for the commit protocol.

  To ensure a working proxy connection, check for the following:
  - Correct syntax for your proxy address.
  - Schemes that match the protocol of the environment variable. The
    port syntax should look like this: `hostname` or
    `scheme://hostname[:port]`.
  - If the `--dataport` option is not set, then an
    HTTP or HTTPS request is sent to retrieve the dataport before
    the commit protocol begins. It uses
    http_proxy or
    https_proxy accordingly.
- The no_proxy setting overrides and disables the
  cov_commit_proxy, http_proxy, and
  https_proxy settings.

## Setting up RPA

This section describes how to set up RPA using basic authentication. You can modify
the steps provided such that RPA is set up using your SSO authentication method.

To set up RPA:

1. If you have not done so already, configure a reverse proxy server on the same
   host machine as the Coverity Connect server as described in Adding and configuring a reverse proxy server
2. `cd` into the /etc/apache2/coverity
   directory, and replace the contents of
   authentication.conf with the content found inside
   the 
   cim-installer-location/extras/proxy/apache2/authentication.conf
   file.
3. To enable SSO, replace the following line of
   authentication.conf as needed for your SSO
   protocol:

   ```
   # SSO implementation invoked here.
   ```

## Configuring Coverity Connect for RPA

After setting up RPA, and enabling and verifying SSO capability, you need to
configure Coverity Connect to use RPA.

To configure Coverity Connect for RPA:

1. In a Web browser, enter the URL for the Coverity Connect server (using either
   the `http://` or `https://` protocol).
2. When the sign-in page opens, log in as the admin
   user.
3. Configure LDAP if it is not already configured. See Integrating with LDAP servers.
4. Choose one or more LDAP users to be administrators, and assign the
   System Admin role to each user. See Managing roles for a user.
5. Modify the value of the web.url property in the file
   <install_dir>/config/web.properties to be the
   URL of the RP. For example:

   ```
   web.url=https\://coverity.example.com
   ```
6. Modify the file
   <install_dir>/server/base/conf/server.xml by
   adding the `address` attribute to all of the
   `Connector` entities that are not commented out. The
   `address` attribute must have a value of localhost or
   127.0.0.1 as shown below:

   ```
   <Connector port="8080" protocol="HTTP/1.1" URIEncoding="UTF-8"
       connectionTimeout="20000" compression="10240"
       compressableMimeType="text/html,text/xml,text/plain,application/json"
       address="127.0.0.1" redirectPort="8443"/>
   ```
7. Stop and restart the server. For example:

   ```
   <install_dir>/bin/cov-im-ctl stop                    
   <install_dir>/bin/cov-im-ctl start
   ```
8. In Configuration > System > Authentication and Sign In, in the Authentication Method for LDAP
   Users section, select Authenticate with: Reverse
   Proxy.

   Note: The Reverse Proxy option is disabled if the `address`
   attribute is not added correctly, as described in 6.
9. Click Done to save your changes and exit.
10. Check the <install_dir>/logs/cim.log file for
    errors that indicate RPA was not enabled.
11. Verify HTTPS browser access by connecting to the proxy. Log in as one of the
    LDAP users to which you assigned the System Admin role in 4.

    Following successful SSO login, you should see the Coverity Connect Web
    application.
12. In Configuration > System > Authentication and Sign In, in the Authentication Method for LDAP
    Users section, verify that it still says Authenticate with:
    Reverse Proxy. If it says *LDAP* instead of
    *Reverse Proxy*, then the changes made to
    server.xml, as described in 6, are incorrect or
    incomplete.
