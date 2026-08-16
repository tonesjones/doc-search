---
title: "C# and Visual Basic cryptographic primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-and-visual-basic-cryptographic-primitives.html"
content_id: "Zjx0jVG35EWGxcAjBWCRTg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:10.589348+00:00"
---

# C# and Visual Basic cryptographic primitives

These are the primitives to model cryptography in the .NET languages, C# and Visual
Basic. The primitives that reference `cryptoContext` alter the context
object, to model either setting up the cryptographic operation or performing it.

## `copy_parameters()`

```
public static extern void copy_parameters(
                        object cryptoContext,
                        object *fromObj
                    );
```

Copies parameters from `fromObj` into
`cryptoContext`.

Can be used, for example, to copy the key size information that belongs to a key
object into the full cryptographic context.

## `output_final()`

```
public static extern void output_final(
                        object cryptoContext,
                        object output
                    );
```

Models the generation of output, such as encryption or decryption, from the currently
specified context.

It is acceptable for `output` to be null if the output data is not
going to be used.

## `reset_input()`

```
public static extern void reset_input(
                        objectcryptoContext
                    );
```

After this call, any previous input used with this context object no longer affects
its result.

## `set_algorithm()`

```
public static extern void set_algorithm(
                        object cryptoContext,
                        Algorithm alg
                    );
```

Sets the algorithm to use in the
current context.

## `set_algorithm_parameter()`

```
public static extern void set_algorithm_parameter(
                        object cryptoContext,
                        object alg
                    );
```

Sets the current algorithm to a value not included in the standard enum.

## `set_blockmode()`

```
public static extern void set_blockmode(
                        object cryptoContext,
                        BlockMode bm
                    );
```

Sets the block mode to use in the
current context.

## `set_blockmode_parameter()`

```
public static extern void set_blockmode_parameter(
                        object cryptoContext,
                        object bm
                    );
```

Sets the current block mode to a value not included in the standard enum.

## `set_default_ssl_protocols()`

```
public static extern void set_default_ssl_protocols(
                        object cryptoContext
                    );
```

Configures the cryptographic context object (such as a socket object) the default
behavior when negotiating TLS/SSL protocols. The default models both the newer TLS
and the older SSL protocols.

## `set_implementation()`

```
public static extern void set_implementation(
                        object cryptoContext,
                        Implementation impl
                    );
```

Sets the implementation to use in
the current context.

## `set_implementation_parameter()`

```
public static extern void set_implementation_parameter(
                        object cryptoContext,
                        object impl
                    );
```

Sets the current implementation to a value not included in the standard enum.

## `set_input()`

```
public static extern void set_input(
                        object cryptoContext,
                        object input
                    );
```

Sets the input to use in the current context.

## `set_keysize()`

```
public static extern void set_keysize(
                        object cryptoContext,
                        int keysize
                    );
```

Sets the key size to use in the current context.

The `keysize` value can be either a constant or a variable.

## `set_operation()`

```
public static extern void set_operation(
                        object cryptoContext,
                        Operation operation
                    );
```

Sets the operation to use in the
current context.

## `set_operation_parameter()`

```
public static extern void set_operation_parameter(
                        object cryptoContext,
                        object operation
                    );
```

Sets the current operation to a value not included in the standard enum.

## `set_padding()`

```
public static extern void set_padding(
                        object cryptoContext,
                        Padding pad
                    );
```

Sets the padding to use in the current
context.

## `set_padding_parameter()`

```
public static extern void set_padding_parameter(
                        object cryptoContext,
                        object pad
                    );
```

Sets the current padding to a value not included in the standard enum.

## `set_ssl_protocol_parameter()`

```
public static extern void set_ssl_protocol_parameter(
                        object cryptoContext,
                        object protocol
                    );
```

Sets the TLS/SSL protocol to use in the current context.

The value of `object` should be a string, either variable or
constant.

## `set_transformation()`

```
public static extern void set_transformation(
                        object cryptoContext,
                        string transformation
                    );
```

Specifies a string to use when performing a transformation.
