---
title: "SSL_Protocol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ssl_protocol.html"
content_id: "bBB05O2uJ7DMXIyvrIvRpA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:16.066647+00:00"
---

# SSL_Protocol

Attention:

- In the C/C++ library each protocol value begins with
  `__coverity_crypto_`.
- The C# & Visual Basic and the Java & Kotlin libraries use string
  values, rather than enum values, to specify protocols.

| Value | Protocol | Notes |
| --- | --- | --- |
| `SSLPROTO_DEFAULT` | The protocol values that have been set to be the default. |  |
| `SSLPROTO_LENGTH` |  | Placeholder for an arbitrary length. |
| `SSLPROTO_SSLV2` | SSL 2.0 |  |
| `SSLPROTO_SSLV3` | SSL 3.0 |  |
| `SSLPROTO_TLSV10` | TLS 1.0 |  |
| `SSLPROTO_TLSV11` | TLS 1.1 |  |
| `SSLPROTO_TLSV12` | TLS 1.2 |  |
| `SSLPROTO_TLSV13` | TLS 1.3 |  |
| `SSLPROTO_UNKNOWN` |  | Placeholder for a nonspecified protocol. |
