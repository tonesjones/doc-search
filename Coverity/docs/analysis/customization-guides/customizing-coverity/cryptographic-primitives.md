---
title: "Cryptographic primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cryptographic-primitives.html"
content_id: "7UB7BTSwMdyPexi0OUv3Bw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:08.541408+00:00"
---

# Cryptographic primitives

The primitives described in this chapter model encryption, decryption, and other
security operations.

## The context object

Cryptographic models require a *cryptographic context* object. This is named
`void *cryptoContext` in the primitive definitions. If the API
you work with defines such an object, use that. If the project you work with does
not define a context object, use a local variable as the context (its initial value
does not matter).

Once the context object is declared, use the primitives to set up the cryptographic
operation. This includes specifying the input stream and the output.

## Example

The following C code models a representative encryption:

```
void *ctxt;

__coverity_crypto_set_algorithm(
    ctxt,
    __coverity_crypto_CRA_DES
);
__coverity_crypto_set_blockmode(
    ctxt,
    __coverity_crypto_CRBM_CBC
);
__coverity_crypto_set_operation(
    ctxt,
    __coverity_crypto_CRO_ENCRYPT
);
__coverity_crypto_set_input(
    ctxt,
    input
);

__coverity_crypto_output_final(
    ctxt,
    output
);
```

The components of this example are as follows:

1. `void *ctxt` declares the context object this model code will
   use.
2. The call to `__coverity_crypto_set_algorithm()` says to model DES
   encryption (`CRA_DES`).
3. The call to `__coverity_crypto_set_blockmode()` says to model the
   Cipher Block Chaining block mode (`CRBM`).
4. The call to `__coverity_crypto_set_operation()` says to model an
   encryption (`CRO_ENCRYPT`).
5. The call to `__coverity_crypto_set_input()` sets the input
   stream.
6. Finally, the call to `__coverity_crypto_output_final()` says to
   model performing the encryption.

## Categories of cryptographic information

Specifying the context of a cryptographic operation requires a variety of
information. The following list shows the overall categories that might be
needed:

- Algorithm
- Block mode
- Padding
- Implementation
- Operation
- Key size
- Transformation
- Input
- SSL/TLS protocol

The cryptographic primitive libraries provided with Coverity use enumerations to describe most of these
categories. A couple of categories (*key size* and *transformation)*
require only a numeric value or a string, and *input* is simply an untyped
parameter.
