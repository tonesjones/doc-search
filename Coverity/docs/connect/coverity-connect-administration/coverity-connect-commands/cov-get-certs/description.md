---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "BSatKmKeIDiJqUDbv9Lkxg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:21.369380+00:00"
---

# Description

In situations where Coverity Connect is a client of other services (email, Bugzilla, JIRA,
LDAP) and one or more of those services uses a self-signed certificate,
`cov-get-certs` is used to transfer that server's self-signed
certificate to the Coverity Connect truststore of CA root certificates, thus enabling
Coverity Connect to connect to the service using TLS/SSL.

Note:
Before the Coverity 8.0 release, `cov-get-certs` was needed for all
Java applications. Now it is needed only for Coverity Connect.

If you want to edit the certificate file, use your JRE's keytool
command. The password for the certificates file is `changeit`.
