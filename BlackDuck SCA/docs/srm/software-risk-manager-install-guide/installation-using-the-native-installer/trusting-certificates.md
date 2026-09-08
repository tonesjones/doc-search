---
title: "Trusting Certificates"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/trusting-certificates.html"
content_id: "S5WPhJ907tr3Zt2TIFXCWA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:54.151666+00:00"
content_hash: "40a4dbb6572b69d58174b2b1da8122cc0a26c0cfc6f2f28302cded3a839c3748"
---

# Trusting Certificates

If you're connecting with an application (such as Jira or Git) that is using a
self-signed HTTPS certificate, you will need to add it to the Software Risk Manager Java
trust store, as explained below.

## Getting Software Risk Manager to Trust Your Third-party or Self-signed Certificate

### Windows

1. Open a command prompt in administrator mode.
2. Change directory to the Software Risk Manager Java trust store: `cd
   <installation-directory>\Code Dx\java\bin` where the
   `<installation-directory>` default is
   `C:\Program Files\Software Risk Manager`.
3. Run `keytool -printcert -rfc -sslserver <server
   hostname:port> | keytool -importcert -keystore
   "../lib/security/cacerts" -storepass changeit -alias <name for
   your server> -noprompt`. Replace `<server
   hostname:port>` and `<name for your
   server>` with the appropriate information for your
   environment.
4. Restart the Software Risk Manager services.

### Linux

1. Open a terminal window.
2. Change directory to the Software Risk Manager Java trust store: `cd
   <installation-directory>/java/bin` where the
   `<installation-directory>` defaults are
   `/opt/srm/` for Linux root and
   `/home/srm/` for Linux non-root.
3. Import the key to the Software Risk Manager Java installation's
   keystore:
   - [root] use `./keytool -printcert -rfc -sslserver
     <server hostname:port> | sudo ./keytool -importcert
     -keystore "../lib/security/cacerts" -storepass changeit
     -alias <name for your server> -noprompt`.
     Replace `<server hostname:port>` and
     `<name for your server>` with the
     appropriate information for your environment.
   - [non-root] use `./keytool -printcert -rfc -sslserver
     <server hostname:port> | ./keytool -importcert
     -keystore "../lib/security/cacerts" -storepass changeit
     -alias <name for your server> -noprompt`.
     Replace `<server hostname:port>` and
     `<name for your server>` with the
     appropriate information for your environment.
4. Restart the Software Risk Manager services.

## Deleting a Certificate from the Trust Store

1. Open a Windows command prompt in administrator mode or a terminal in
   Linux.
2. Change the directory to the Software Risk Manager Java trust store: `cd
   <installation-directory>/java/bin` where the
   `<installation-directory>` defaults are
   `C:\Program Files\Software Risk Manager` on Windows;
   `/opt/srm` for Linux root; and `/home/srm/`
   for Linux non-root. Replace `<name for your server>` with
   the appropriate information for your environment.
   - [Windows] use `keytool -delete <name for your server>
     -keystore ../lib/security/cacerts`.
   - [Linux root installation] use `sudo ./keytool -delete <name
     for your server> -keystore ../lib/security/cacerts`.
   - [Linux non-root installation] use `./keytool -delete <name for
     your server> -keystore ../lib/security/cacerts`.
3. Restart the Software Risk Manager services.
