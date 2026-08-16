---
title: "Setup using Apache HTTP server"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setup-using-apache-http-server.html"
content_id: "W7pAQIobddvJZX9CaCGfng"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:54.483637+00:00"
---

# Setup using Apache HTTP server

This section describes how to add and configure *Apache HTTP Server 2.4* (apache2)
to act as a reverse proxy (RP) in front of the Coverity Connect server. It assumes the
reader has some familiarity with reverse proxy concepts, usage, and administration.

Note: If desired, web servers other than apache2 can be used. However, instructions specific
to other web servers are not provided.

The configuration described in this section also enables the transformation of HTTPS
requests to HTTP requests.

**To add and configure the reverse proxy:**

Note: In addition to the steps below, note the following:

- If you plan to use RPA, set up the reverse proxy on the same host as the Coverity
  Connect server.
- Assuming you use the `--host --port` method of connecting, the
  Coverity Connect implementation can provide service only for RPs for which the
  "context path" part of the URL is empty. For example, the RP works if it uses
  the URL `https://coverity.example.com/` for Coverity Connect, but
  not if it uses `https://example.com/coverity/`. If you wish to
  use context paths, then you must use the `--url` method of
  connecting instead of `--host --port`.
- You need to take steps to ensure that clients cannot reach CC directly - that is,
  by bypassing the proxy.

Note: These steps are for configuring apache2 on Ubuntu. The steps for other platforms are
similar.

1. On the reverse proxy host machine, make sure the necessary apache2 modules are
   installed and enabled:

   1. In the /etc/apache2 directory, run the following
      command to get a list of available apache2 modules:

      ```
      sudo a2enmod
      ```
   2. In response to the prompt asking you which modules you want to enable,
      enter the following list of modules:

      ```
      auth_basic
      authn_core
      authn_file
      authz_core
      authz_host
      authz_user
      env
      headers
      log_debug
      mime
      mpm_event 
      proxy_http
      proxy
      proxy_wstunnel
      rewrite
      setenvif
      socache_shmcb 
      ssl
      ```
2. In the /etc/apache2/sites-available directory, create a
   coverity.conf file and enter the following lines:

   ```
   Include coverity/ssl.conf
   Include coverity/authentication.conf
   Include coverity/proxy.conf
   ```

   Note: The authentication.conf and
   proxy.conf files are located in
   cim-installer-location/extras/proxy/apache2.
3. Enable the coverity site:

   ```
   sudo a2ensite coverity
   ```
4. Remove any unneeded sites from /etc/apache2/sites-enabled
   using the `a2dissite` command.
5. In the /etc/apache2 directory, create a
   coverity directory:

   ```
   sudo mkdir coverity
   ```
6. `cd` into the coverity directory, and
   create these configuration files:

   - ssl.conf—Modify your Apache SSL (HTTPS)
     configuration file as necessary to provide SSL service for your
     environment. If you want to use an RP URL without a port number, SSL
     service should be provided on port 443.
   - authentication.conf—This file is empty if RPA is not
     used. For details about using this file for RPA, see Adding reverse proxy authentication.
   - proxy.conf—To specify that requests to the RP using
     `http://ccserver_hostname.com/foo`
     be converted to a proxy request to the Coverity Connect address,
     `http://localhost:8080/foo`, copy the content from 
     cim-installer-location/extras/proxy/apache2/proxy.conf
     and paste it into the proxy.conf file.

   Note: This
   cim-installer-location/extras/proxy/apache2/proxy.conf
   configuration is for the scenario when the RP server is located on the same host
   as the Coverity Connect server.
7. Restart apache2 to activate the new configuration:

   ```
   sudo service apache2 restart
   ```

Note:

You should carefully examine any custom or stock `RequestHeader`
directives in the Apache server to ensure you are passing only the
`Host` header and not `X-Forwarded-Host`.

You might also need to pass the `X-Forwarded-Proto` header, for
example:

```
RequestHeader set X-Forwarded-Proto "expr=%{REQUEST_SCHEME}"
```
