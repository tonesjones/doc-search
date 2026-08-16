---
title: "Implementation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/implementation.html"
content_id: "xq_5V9758W7deeSFOLoygQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:14.747184+00:00"
---

# Implementation

The table in this section shows the available implementations.

Attention:

- The **Language** column mentions only implementations that a language
  *does not* support. If this entry is empty, all six languages
  support that algorithm.
- In the C/C++ library each implementation value begins with
  `__coverity_crypto_`. Implementation enumeration values
  in the C# & Visual Basic library and the Java & Kotlin library do
  not include this leading substring.

| Value | Implementation | Language | Notes |
| --- | --- | --- | --- |
| `CRI_BOUNCYCASTLE` | Bouncy Castle cryptography libraries |  |  |
| `CRI_BOUNCYCASTLE_API` | | | |
|  | Bouncy Castle APIs |  |  |
| `CRI_GNU` | GNU cryptography libraries |  |  |
| `CRI_JASYPT` | Jasypt encryption |  |  |
| `CRI_JDK_SSL_SOCKET` | Java Development Kit Secure Socket Extension | Not supported by C# or Visual Basic. |  |
| `CRI_LENGTH` |  |  | Placeholder for an arbitrary length. |
| `CRI_NODE_BCRYPT` | The node.bcrypt.js hash library | Not supported by C# or Visual Basic. | The bcrypt library is published by npm®. |
| `CRI_NODE_CRYPTO` | The Node.js® cryptographic library | Not supported by C# or Visual Basic. |  |
| `CRI_NODE_SCRYPT` | The Scrypt library for Node.js | Not supported by C# or Visual Basic. | The Scrypt library is published by npm. |
| `CRI_OPENSSL` | The OpenSSL® library | Not supported by C# or Visual Basic. |  |
| `CRI_SUNJCE` | The SunJCE cryptography provider |  | SunJCE is published by Oracle®. |
| `CRI_UNKNOWN` |  |  | Placeholder for a nonspecified implementation. |
| `CRI_WINDOWS_API` | The Windows® cryptographic API |  |  |
