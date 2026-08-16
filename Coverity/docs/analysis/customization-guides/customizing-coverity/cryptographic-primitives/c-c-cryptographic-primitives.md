---
title: "C/C++ cryptographic primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-cryptographic-primitives.html"
content_id: "3yEH32WW8sDy2nCoBvMXrw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:09.259705+00:00"
---

# C/C++ cryptographic primitives

These are the primitives for modeling cryptography in C or C++ source. The primitives
that reference `cryptoContext` alter the context object, to model either
setting up the cryptographic operation or performing it.

## `__coverity_crypto_add_ssl_protocol()`

```
void __coverity_crypto_add_ssl_protocol(
                        void *cryptoContext,
                        enum __coverity_crypto_SSLProtocol protocol
                    );
```

Adds an SSL protocol to the set currently in use.

## `__coverity_crypto_add_ssl_protocol_parameter()`

```
void __coverity_crypto_add_ssl_protocol_parameter(
                        void *cryptoContext,
                        const void *value,
                        const char *value_map_string
                    );
```

Adds an SSL protocol to the current set, interpreting `value`
according to the `value_map_string`.

## `__coverity_crypto_copy_parameters()`

```
void __coverity_crypto_copy_parameters(
                        void *obj,
                        const void *from
                    );
```

Copies parameters from `from` to `obj`.

Can be used, for example, to copy the key size information that belongs to a key
object into the full cryptographic context.

## `__coverity_crypto_output_final()`

```
void __coverity_crypto_output_final(
                        void *cryptoContext,
                        void *output
                    );
```

Models the generation of output, such as encryption or decryption, from the currently
specified context.

It is acceptable for `output` to be null if the output data is not
going to be used.

## `__coverity_crypto_remove_ssl_protocol()`

```
void __coverity_crypto_remove_ssl_protocol(
                        void *cryptoContext,
                        enum __coverity_crypto_SSLProtocol protocol
                    );
```

Removes an SSL protocol from the current set.

## `__coverity_crypto_remove_ssl_protocol_parameter()`

```
void __coverity_crypto_remove_ssl_protocol_parameter(
                        void *cryptoContext,
                        const void *value,
                        const char *value_map_string
                    );
```

Removes an SSL protocol from the current set, interpreting `value`
according to the `value_map_string`.

## `__coverity_crypto_reset_input()`

```
void __coverity_crypto_reset_input(
                        void *cryptoContext
                    );
```

After this call, any previous input used with this context object no longer affects
its result.

## `__coverity_crypto_set_algorithm()`

```
void __coverity_crypto_set_algorithm(
                        void *cryptoContext,
                        enum __coverity_crypto_Algorithm alg
                    );
```

Sets the algorithm to use in the
current context.

## `__coverity_crypto_set_algorithm_parameter()`

```
void __coverity_crypto_set_algorithm_parameter(
                        void *cryptoContext,
                        const void *value,
                        const char *value_map_string
                    );
```

Sets the algorithm to use, interpreting `value` according to the `value_map_string`.

## `__coverity_crypto_set_blockmode()`

```
void __coverity_crypto_set_blockmode(
                        void *cryptoContext,
                        enum __coverity_crypto_BlockMode bm
                    );
```

Sets the block mode to use in the
current context.

## `__coverity_crypto_set_blockmode_parameter()`

```
void __coverity_crypto_set_blockmode_parameter(
                        void *cryptoContext,
                        const void *value,
                        const char *value_map_string
                    );
```

Sets the block mode to use, interpreting `value` according to the
`value_map_string`.

## `__coverity_crypto_set_implementation()`

```
void __coverity_crypto_set_implementation(
                        void *cryptoContext,
                        enum __coverity_crypto_Implementation impl
                    );
```

Sets the implementation to use in
the current context.

## `__coverity_crypto_set_input()`

```
void __coverity_crypto_set_input(
                        void *cryptoContext,
                        const void *input
                    );
```

Sets the input to use in the current context.

## `__coverity_crypto_set_keysize()`

```
void __coverity_crypto_set_keysize(
                        void *cryptoContext,
                        int keysize
                    );
```

Sets the key size to use in the current context.

The `keysize` value can be either a constant or a variable.

## `__coverity_crypto_set_operation()`

```
void __coverity_crypto_set_operation(
                        void *cryptoContext,
                        enum __coverity_crypto_Operation operation
                    );
```

Sets the operation to use in the
current context.

## `__coverity_crypto_set_operation_parameter()`

```
void __coverity_crypto_set_operation_parameter(
                        void *cryptoContext,
                        const void *value,
                        const char *value_map_string
                    );
```

Sets the operation to use, interpreting `value` according to the `value_map_string`.

## `__coverity_crypto_set_padding()`

```
void __coverity_crypto_set_padding(
                        void *cryptoContext,
                        enum __coverity_crypto_Padding pad
                    );
```

Sets the padding to use in the current
context.

## `__coverity_crypto_set_padding_parameter()`

```
void __coverity_crypto_set_padding_parameter(
                        void *cryptoContext,
                        const void *value,
                        const char *value_map_string
                    );
```

Sets the padding to use, interpreting `value` according to the `value_map_string`.

## `__coverity_crypto_set_ssl_protocol()`

```
void __coverity_crypto_set_ssl_protocol(
                        void *cryptoContext,
                        enum __coverity_crypto_SSLProtocol protocol
                    );
```

Sets the SSL protocol to use in the current
context.

This call initializes the protocol set.
