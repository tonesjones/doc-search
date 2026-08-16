---
title: "TrustStore overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/truststore-overview.html"
content_id: "pKDfkTgrzE6j05mOzNQXwQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:18.456805+00:00"
---

# TrustStore overview

This section describes the *TrustStore,* a storage location for certificates used by
`cov-commit-defects` and other Coverity Analysis applications that
connect using TLS/SSL. This TrustStore is specific to the Coverity Analysis client; for
information on the server-side TrustStore, see the Coverity Platform 2026.6.0 User and Administrator Guide.

Note:
This trust store is not the same as the one used by the Java-based command-line tools
(`cov-manage-im`, `cov-integrity-report`, and
`cov-security-report`).

The discussion assumes a basic level of familiarity with TLS/SSL. Comprehensive information
on TLS/SSL can be found at
<http://en.wikipedia.org/wiki/Transport_Layer_Security>.

When connecting to a network peer (such as a Coverity Connect server, in the case of
`cov-commit-defects`), the TLS/SSL protocol must authenticate the peer.
That is, it must prove that the peer has the identity that it claims to have. The
authentication step uses a digital certificate to identify the peer. To authenticate,
the application must find a digital certificate of a host that it trusts: That
certificate must vouch for the veracity of the peer’s certificate. Any number of
certificates may be used to form a chain of trust between the peer’s certificate and a
certificate trusted by the application. If the application is successful in finding such
a chain of trust, it can then treat the peer as trusted and proceed with the data exchange.

Coverity Analysis uses the TrustStore as the location for storing trusted certificates.
When initially installed, the TrustStore directory (<install_dir>/certs) contains a single file,
ca-certs.pem, which contains a collection of certificates
published by certificate authorities such as Verisign. (Coverity gets this list from the
corresponding list, cacerts, in the Java Runtime Environment.)

There are two trust modes for certificates in Coverity Analysis.

- fully authenticated

  The application accepts a chain of trust only if it ends in a certificate in
  ca-certs.pem *or* if the certificate was previously saved in trust-first-time mode.
- trust-first-time

  The application uses a weaker standard, where it accepts a certificate as trusted if either of the following is true:

  - The same peer has sent the same certificate in the past.
  - The certificate is self-signed (that is, the certificate’s next link in
    the chain of trust is itself) and Coverity does not already have a
    certificate stored for that host/port combination. In this case, Coverity saves the certificate
    and starts accepting it even in fully-authenticated mode.

    In other words, when the application receives a self-signed certificate it has not encountered
    before from that peer and port, it stores the certificate in the TrustStore in its own
    file. Subsequent connections to the same peer and port verify that the peer’s
    certificate matches the certificate in the file.

Both trust modes result in an encrypted connection. The difference between them is that
connections secured using trust-first-time mode do not have the same level of assurance
of the identity of the peer. Specifically, the first time you use a certificate in
trust-first-time mode, you need to take a leap of faith that the peer your application
contacted is not being impersonated by another peer.

Both trust modes are provided because there is an administrative cost involved in setting
up fully authenticated mode: The administrator must get the server's certificate from a
certificate authority and install it in the server. If the certificate authority's root
certificate is not included in ca-certs.pem, then the administrator
must also add it to that file on every client.
See the Coverity Platform 2026.6.0 User and Administrator Guide for additional details. In contrast,
trust-first-time mode requires no administrative work to allow the application to
encrypt its communications with the peer.

For more discussion of the difference between
these trust modes, see the description of the `--authenticate-ssl` option to
`cov-commit-defects`.
Also see Security considerations for TLS/SSL certificates.
