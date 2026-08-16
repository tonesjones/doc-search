---
title: "Security considerations for TLS/SSL certificates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-considerations-for-tls/ssl-certificates.html"
content_id: "lqkqVW2n25PinqKw7q50SQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:19.097675+00:00"
---

# Security considerations for TLS/SSL certificates

Be aware that there are tradeoffs involved in choosing between
fully-authenticated mode or trust-first-time mode:

- Using trust-first-time mode lowers security, as it can allow man-in-the-middle attacks.
- Fully-authenticated mode relies on the ca-certs.pem provided
  by Coverity Analysis. This means that the Certificate Authority (CA) list is
  set once the application is installed.
  Depending on your project configuration, you might want
  to use your own CA list instead.

  See Adding a certificate to ca-certs.pem and
  Removing certificates from ca-certs.pem.
