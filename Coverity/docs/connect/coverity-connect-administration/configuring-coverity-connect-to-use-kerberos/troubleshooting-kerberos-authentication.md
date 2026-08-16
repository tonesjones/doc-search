---
title: "Troubleshooting Kerberos authentication"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/troubleshooting-kerberos-authentication.html"
content_id: "q4d4xkgyRkerJBWnZ3K4Zg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:45.964903+00:00"
---

# Troubleshooting Kerberos authentication

Kerberos authentication relies on the proper configuration of various network resources
outside of Coverity Connect. If problems occur, the following tips may help you resolve
them.

## How can I test that my Kerberos-enabled client is working with a Kerberos-enabled web server?

The end to end test involves having network access from the client to the kerberos
server and a keytab file for the web server. Settings for the kerberos server and
associated realm are specified in the kerberos configuration file (e.g.
krb5.conf or krb5.ini).

1. If the initial kerberos token (Ticket Granting Ticket) is required,
   authenticate to the Kerberos server:

   ```
   kinit kuser1@YOUR-REALM
   kuser1@YOUR-REALM's Password:
   ```
2. Verify that a valid kerberos token (TGT) is available:

   ```
   klist
   Credentials cache: API:678E11A7-D99A-45AE-8FBE-C8ED45AD8338
   Principal: kuser1@YOUR-REALM
   Issued                Expires               Principal
   Nov 23 11:03:13 2015  Nov 23 21:03:08 2015  krbtgt/YOUR-REALM@YOUR-REALM
   ```
3. Send a web request with a kerberos-enabled web client, such as a browser:

   ```
   http://your-server.company.com:8080/
   ```

## Why am I getting errors about unsupported encryption types?

The Kerberos server may be using encryption that is not supported by the Java runtime
environment. For information on updating the JRE with more encryption types, see:
[Java Cryptography Extension (JCE) Unlimited
Strength Jurisdiction Policy Files 8 Download](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html). In addition, the Kerberos
server may be configured to use weaker encryption (that is available in the default
JRE) by editing the Kerberos configuration file:

```
# use weak encryption so as not to require the unlimited strength security jars
default_tgs_enctypes = des3-hmac-sha1
default_tkt_enctypes = des3-hmac-sha1
permitted_enctypes = des3-hmac-sha1
```
