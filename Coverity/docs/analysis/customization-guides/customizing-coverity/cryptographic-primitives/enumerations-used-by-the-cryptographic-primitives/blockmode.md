---
title: "BlockMode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/blockmode.html"
content_id: "KqdoKRq7c2lM3AJ0x7pDzg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:13.383895+00:00"
---

# BlockMode

The table in this section shows the available block modes.

Attention: In the C/C++ library each block-mode value begins with
`__coverity_crypto_`. Block-mode enumeration values in the C#
& Visual Basic library and the Java & Kotlin library do not include this
leading substring.

| Value | Bloock Mode | Notes |
| --- | --- | --- |
| `CRBM_CBC` | Cipher Block Chaining |  |
| `CRBM_CCM` | Cipher block chaining with counter |  |
| `CRBM_CFB` | Cipher Feedback |  |
| `CRBM_CTR` | Counter mode |  |
| `CRBM_CTS` | Ciphertext Stealing |  |
| `CRBM_ECB` | Electronic Codebook |  |
| `CRBM_GCF` | Güralp Compressed Format |  |
| `CRBM_GCM` | Gaulois/Counter Mode |  |
| `CRBM_GOF` | Gost Output Feedback | The GOST 28147 OFB counter mode (GCTR) block mode published by Bouncy Castle. |
| `CRBM_LENGTH` |  | Placeholder for blocks of arbitrary length. |
| `CRBM_NOBM` | No block mode in use |  |
| `CRBM_OFB` | Output Feedback |  |
| `CRBM_PCBC` | Plaintext Cipher Block Chaining |  |
| `CRBM_PGPCFB` | Pretty Good Privacy Cipher Feedback | The CFB RCF 2440 block mode published by OpenPGP |
| `CRBM_SIC` | Segmented Integer Counter |  |
| `CRBM_UNKNOWN` |  | Placeholder for a nonspecified block mode. |
| `CRBM_XTS` | XEX-based Tweaked CodeBook mode (TCB) with ciphertext stealing (CTS) |  |
