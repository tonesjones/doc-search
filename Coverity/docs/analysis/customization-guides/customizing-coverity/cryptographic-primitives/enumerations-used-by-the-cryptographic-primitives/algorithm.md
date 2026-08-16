---
title: "Algorithm"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/algorithm.html"
content_id: "SlZk5OZHnp9Qy4yeWLk0yw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:12.718126+00:00"
---

# Algorithm

The table in this section shows the available encryption algorithms.

Attention:

- The **Language** column mentions only algorithms that a language *does
  not* support. If this entry is empty, all six languages support that
  algorithm.
- In the C/C++ library each algorithm value begins with
  `__coverity_crypto_`. Algorithm enumeration values in the
  C# & Visual Basic library and the Java & Kotlin library do not
  include this leading substring.

| Value | Algorithm | Language | Notes |
| --- | --- | --- | --- |
| `CRA_AES` | Advanced Encryption Standard (AES) cipher |  |  |
| `CRA_AESWRAP` | Advanced Encryption Standard (AES) Key Wrap cipher |  |  |
| `CRA_ARIA` | ARIA cipher | Not supported by C# or Visual Basic. |  |
| `CRA_BLOWFISH` | Blowfish cipher |  |  |
| `CRA_CAMELLIA` | Camellia cipher |  |  |
| `CRA_CAMELLIAWRAP` | Camellia Key Wrap cipher |  |  |
| `CRA_CAST5` | CAST5 cipher |  | Also known as CAST-128. |
| `CRA_CAST6` | CAST6 cipher |  | Also known as CAST-256. |
| `CRA_CHACHA` | ChaCha cipher |  |  |
| `CRA_DES` | Data Encryption Standard (DES) cipher |  |  |
| `CRA_DESEDE` | Data Encryption Standard (DES) Encrypt-Decrypt-Encrypt (EDE) cipher |  | Also known as Triple DES, 3DES, TDES, Triple Data Encryption Algorithm (TDEA or Triple DEA). |
| `CRA_DESEDEWRAP` | Data Encryption Standard (DES) Encrypt-Decrypt-Encrypt (EDE) key wrap cipher |  |  |
| `CRA_DH` | Diffie-Hellman (DH) key exchange | Not supported by C# or Visual Basic. |  |
| `CRA_DHE` | Diffie-Hellman ephemeral (DHE) key exchange | Not supported by C# or Visual Basic. |  |
| `CRA_DSA` | Digital Signature Algorithm (DSA) | Not supported by C# or Visual Basic. |  |
| `CRA_ECCPWD` | Elliptic-Curve Cryptography (ECC) password authentication | Not supported by C# or Visual Basic. | Also known as RFC 8492 |
| `CRA_ECDH` | Elliptic-Curve (EC) Diffie-Hellman (DH) key protocol | Not supported by C# or Visual Basic. |  |
| `CRA_ECDHE` | Elliptic Curve (EC) Diffie-Hellman ephemeral (DHE) key protocol | Not supported by C# or Visual Basic. |  |
| `CRA_ECDSA` | Elliptic-Curve (EC) Digital Signature Algorithm (DSA) | Not supported by C# or Visual Basic |  |
| `CRA_ECIES` | Elliptic-Curve (EC) Integrated Encryption Scheme (IES) |  |  |
| `CRA_ELGAMAL` | ElGamal encryption |  |  |
| `CRA_GOST28147` | GOST 28147 block cipher |  |  |
| `CRA_GRAIN128` | Grain 128a stream cipher |  |  |
| `CRA_GRAINV1` | Grain cipher version 1.0 |  |  |
| `CRA_HC128` | HC-128 cipher |  |  |
| `CRA_HC256` | HC-256 cipher |  |  |
| `CRA_IDEA` | International Data Encryption Algorithm (IDEA) cipher |  |  |
| `CRA_IES` | Integrated Encryption Scheme (IES) encryption |  |  |
| `CRA_ISAAC` | ISAAC stream cipher |  |  |
| `CRA_LENGTH` |  |  | Placeholder for a key of arbitrary length. |
| `CRA_MD2` | MD2 Message Digest algorithm |  |  |
| `CRA_MD4` | MD4 Message Digest algorithm |  |  |
| `CRA_MD5` | MD5 Message Digest algorithm |  |  |
| `CRA_NACCACHESTERN` | Naccache-Stern encryption |  |  |
| `CRA_NOALG` | No encryption algorithm |  |  |
| `CRA_NOEKEON` | NOEKEON cipher |  |  |
| `CRA_PBEMD53DES` | Password-Based Encryption (PBE) with MD53 and DES |  |  |
| `CRA_PBEMD5DES` | Password-Based Encryption (PBE) with MD5 and DES |  |  |
| `CRA_PBESHA1DESEDE` | Password-Based Encryption (PBE) with SHA-1 and Triple DES (DESEDE) |  |  |
| `CRA_PBESHA1RC240` | Password-Based Encryption with Secure Hash Algorithm 1 (SHA-1), Rivest Cipher 2 (RC2), and 40-bit key size |  |  |
| `CRA_PBKDF1` | PBKDF1 key derivation | Not supported by C or C++. |  |
| `CRA_PBKDF2` | PBKDF2 key derivation | Not supported by C or C++. |  |
| `CRA_PBKDF2_SALTED` | PBKDF2 with salt value | Not supported by C or C++. |  |
| `CRA_PSK` | Pre-shared Key (PSK) authentication |  |  |
| `CRA_RABBIT` | Rabbit stream cipher | Not supported by C# or Visual Basic. |  |
| `CRA_RC2` | Rivest Cipher 2 (RC2) |  |  |
| `CRA_RC4` | Rivest Cipher 4 (RC4) |  |  |
| `CRA_RC5` | Rivest Cipher 5 (RC5) |  |  |
| `CRA_RC6` | Rivest Cipher 6 (RC6) |  |  |
| `CRA_RIJNDAEL` | Rijndael cipher |  |  |
| `CRA_RIPEMD` | RIPEMD (RIPE Message Digest) hash function |  |  |
| `CRA_RSA` | RSA cryptosystem |  |  |
| `CRA_SALSA20` | Salsa20 stream cipher |  |  |
| `CRA_SCRYPT` | scrypt key derivation | Not supported by C# or Visual Basic. |  |
| `CRA_SEED` | SEED cipher |  |  |
| `CRA_SERPENT` | Serpent cipher |  |  |
| `CRA_SHA0` | Secure Hash Algorithm 0 (SHA-0) |  |  |
| `CRA_SHA1` | Secure Hash Algorithm 1 (SHA-1) |  |  |
| `CRA_SHA2_FAMILY` | Secure Hash Algorithm 2 (SHA-2) family | Not supported by C# or Visual Basic. |  |
| `CRA_SHA224` | Secure Hash Algorithm 3 (SHA-3), variant 224 | Not supported by C# or Visual Basic. |  |
| `CRA_SHA256` | Secure Hash Algorithm 3 (SHA-3), variant 256 |  | A nonspecific SHA-2 hash: Used by the Data Security Standard (DSS) when the Digital Signature Algorithm (DSA) key length dictates which SHA-2 hash to use, but *a priori* we can't know which variant it will be. |
| `CRA_SHA384` | Secure Hash Algorithm 3 (SHA-3), variant 384 |  |  |
| `CRA_SHA512` | Secure Hash Algorithm 3 (SHA-3), variant 512 |  |  |
| `CRA_SHACAL2` | SHACAL-2 cipher |  |  |
| `CRA_SHAKE128` | Secure Hash Algorithm 3 (SHA-3), variant SHAKE128 |  |  |
| `CRA_SHAKE256` | Secure Hash Algorithm 3 (SHA-3), variant SHAKE256 |  |  |
| `CRA_SKIPJACK` | Skipjack cipher |  |  |
| `CRA_SRP` | Secure Remote Password (SRP) protocol | Not supported by C# or Visual Basic. |  |
| `CRA_TEA` | Tiny Encryption Algorithm (TEA) cipher |  |  |
| `CRA_THREEFISH` | Threefish cipher |  |  |
| `CRA_TWOFISH` | Twofish cipher |  |  |
| `CRA_UNKNOWN` |  |  | Placeholder for a nonspecified algorithm. |
| `CRA_VMPC` | Variably Modified Permutation Composition (VMPC) stream cipher |  |  |
| `CRA_XSALSA20` | XSalsa20 stream cipher |  |  |
| `CRA_XTEA` | eXtended Tiny Encryption Algorithm (XTEA) cipher |  |  |
