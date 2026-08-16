---
title: "Padding"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/padding.html"
content_id: "ZpBqUgETozlXC7g1cB96bA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:14.036090+00:00"
---

# Padding

The table in this section shows the available padding methods.

Attention: In the C/C++ library each padding value begins with . Block-mode
enumeration values in the C# & Visual Basic library and the Java & Kotlin
library do not include this leading substring.

| Value | Padding | Notes |
| --- | --- | --- |
| `CRPD_ISO10126` | ISO 10126 padding | This method was withdrawn as a standard in 2007. |
| `CRPD_ISO101262` | ISO 10126-2 padding |  |
| `CRPD_ISO78144` | ISO 7814-4 padding |  |
| `CRPD_ISO9796D1` | ISO 9796-1 padding |  |
| `CRPD_LENGTH` |  | Placeholder for padding of arbitrary length. |
| `CRPD_NOPD` | No padding in use |  |
| `CRPD_OEAPP` | Optimal Asymmetric Encryption Padding |  |
| `CRPD_PKCS1` | Public-Key Cryptography Standards #1 padding | Published by RSA Laboratories. |
| `CRPD_PKCS5` | Public-Key Cryptography Standards #5 padding | Published by RSA Laboratories. |
| `CRPD_PKCS7` | Public-Key Cryptography Standards #7 padding | Published by RSA Laboratories. |
| `CRPD_TBC` | Trailing Bit Complement padding | Published by the GNU Crypto project. |
| `CRPD_UNKNOWN` |  | Placeholder for a nonspecified padding method. |
| `CRPD_X923` | ANSI X.923 padding |  |
| `CRPD_ZERO` | Padding with zeroes |  |
