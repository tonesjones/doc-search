---
title: "Operation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation.html"
content_id: "blaE3JuqnQupdYfztis9sQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:15.398237+00:00"
---

# Operation

The table in this section shows the available operations.

Attention: In the C/C++ library each block-mode value begins with
`__coverity_crypto_`. Block-mode enumeration values in the C#
& Visual Basic library and the Java & Kotlin library do not include this
leading substring.

| Value | Operation | Notes |
| --- | --- | --- |
| `CRO_DECRYPT` | Decrypt the input. |  |
| `CRO_ENCRYPT` | Encrypt the input. |  |
| `CRO_HASH` | Generate a hash value. |  |
| `CRO_LENGTH` |  | Placeholder for an arbitrary length value. |
| `CRO_SSL_CONNECTION` | Connect to a TLS/SSL socket. |  |
| `CRO_UNKNOWN` |  | Placeholder for a nonspecified implementation. |
