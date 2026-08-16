---
title: "Working with the TrustStore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/working-with-the-truststore.html"
content_id: "SPrWwTfkrG1Ib7F6Ohv4rw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:20.641842+00:00"
---

# Working with the TrustStore

The TrustStore is implemented as a directory: <install-dir>/certs.
There are two kinds of files in the TrustStore. The first is the collection of
certificate authority certificates mentioned above, ca-certs.pem.
Secondly, there may be single-certificate files with names like
host-<host-name>,port-<port-number>.der. These files
store trust-first-time certificates. The file name tells which host and port the
certificate was seen on.

In this section:

- Viewing trust-first-time Certificates
- Viewing Certificate Authority certificates
- Interpreting a certificate file
- Adding a certificate to ca-certs.pem
- Removing a trust-first-time certificate from the TrustStore
- Removing certificates from ca-certs.pem
