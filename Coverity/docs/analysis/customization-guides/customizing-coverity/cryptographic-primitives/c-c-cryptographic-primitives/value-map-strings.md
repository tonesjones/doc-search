---
title: "Value-map strings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/value-map-strings.html"
content_id: "E0jPO9ZMTWYIk488GXRabA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:09.900921+00:00"
---

# Value-map strings

Certain C/C++ primitives let you set arbitrary values (the name of these ends in
`_parameter`).

A primitive to set an arbitrary value has both a `value` argument and
a `value_map_string` argument to describe how value is
interpreted.

The `value_map_string` argument must be a string literal that contains
a space-separated series of <string> <value> pairs.

`<string>`
:   This component of a pair indicates which `<value>` to
    use. It can be one of the following:

    - The string representation of the integer argument in the target
      program (as ASCII decimal)
    - A constant string value
    - For an SSL protocol
      set, an integer that has only a single bit set in its
      binary representation. This value can be a decimal or hexadecimal
      representation, and must be followed by a `b`; for
      example, `0x800b`.

      If the bit that corresponds to
      the SSL protocol is nonzero, the protocol is included in the
      current set.

`<value>`
:   This component of a pair specifies the component for which the parameter is
    being set. This can correspond a value in the library's standard enum
    for this parameter, but it does not need to do so.

For example, in the following primitive call, `algId` is an integer
that indicates which encryption algorithm to use: A value of `1`
means DES/EDE, `2` means AES, and so on.

```
__coverity_crypto_set_algorithm_parameter(
    context,
    algId,
    "1 DESEDE 2 AES 3 BLOWFISH"
);
```

The following is an example of using single-bit integers to manage an SSL protocol
set:

```
__coverity_crypto_remove_ssl_protocol_parameter(
    ctx,
    (void const *)op,
    "0x01000000b SSLV3"
    "0x02000000b SSLV3"
    "0x04000000b TLSV10"
    "0x08000000b TLSV12"
    "0x10000000b TLSV11"
    "0x20000000b TLSV13"
);
```
