---
title: "Java and Kotlin cryptographic primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-and-kotlin-cryptographic-primitives.html"
content_id: "QOgs216NG05zHDP2REoe2w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:11.326873+00:00"
---

# Java and Kotlin cryptographic primitives

These are the primitives for modeling cryptography in Java or Kotlin source. The
primitives that reference `cryptoContext` alter the context object, to model
either setting up the cryptographic operation or performing it. *Note: User written models
for Kotlin are deprecated as of 2026.3.0.*

## `copy_parameters()`

```
public static native void copy_parameters(
                        Object obj,
                        Object fromObj
                    );
```

Copies parameters from `fromObj` to `obj`.

Can be used, for example, to copy the key size information that belongs to a key
object into the full cryptographic context.

## `output_final()`

```
public static native void output_final(
                        Object cryptoContext,
                        Object output
                    );
```

Models the generation of output, such as encryption or decryption, from the currently
specified context.

It is acceptable for `output` to be null if the output data is not
going to be used.

## `reset_input()`

```
public static native void reset_input(
                        Object cryptoContext
                    );
```

After this call, any previous input used with this context object no longer affects
its result.

## `set_algorithm()`

```
public static native void set_algorithm(
                        Object cryptoContext,
                        Algorithm alg
                    );
```

Sets the algorithm to use in the
current context.

## `set_algorithm_parameter()`

```
public static native void set_algorithm_parameter(
                        Object cryptoContext,
                        Object alg
                    );
```

Sets the current algorithm to a value not included in the standard enum.

## `set_blockmode()`

```
public static native void set_blockmode(
                        Object cryptoContext,
                        BlockMode bm
                    );
```

Sets the block mode to use in the
current context.

## `set_blockmode_parameter()`

```
public static native void set_blockmode_parameter(
                        Object cryptoContext,
                        Object bm
                    );
```

Sets the current block mode to a value not included in the standard enum.

## `set_default_ssl_protocols()`

```
public static native void set_default_ssl_protocols(
                        Object cryptoContext
                    );
```

Configures the cryptographic context object (such as a socket object) the default
behavior when negotiating TLS/SSL protocols. The default models both the newer TLS
and the older SSL protocols.

## `set_implementation()`

```
public static native void set_implementation(
                        Object cryptoContext,
                        Implementation impl
                    );
```

Sets the implementation to use in
the current context.

## `set_implementation_parameter()`

```
public static native void set_implementation_parameter(
                        Object cryptoContext,
                        Object impl
                    );
```

Sets the current implementation to a value not included in the standard enum.

## `set_keysize()`

```
public static native void set_keysize(
                        Object cryptoContext,
                        int keysize
                    );
```

Sets the key size to use in the current context.

The `keysize` value can be either a constant or a variable.

## `set_keysize_parameter()`

```
public static native void set_keysize_parameter(
                        Object cryptoContext,
                        Object keysize
                    );
```

Sets the keysize to a value that is not necessarily an integer.

## `set_operation()`

```
public static native void set_operation(
                        Object cryptoContext,
                        Operation operation
                    );
```

Sets the operation to use in the
current context.

## `set_operation_parameter()`

```
public static native void set_operation_parameter(
                        Object cryptoContext,
                        Object operation
                    );
```

Sets the current operation to a value not included in the standard enum.

## `set_padding()`

```
public static native void set_padding(
                        Object cryptoContext,
                        Padding pad
                    );
```

Sets the padding to use in the current
context.

## `set_padding_parameter()`

```
public static native void set_padding_parameter(
                        Object cryptoContext,
                        Object pad
                    );
```

Sets the current padding to a value not included in the standard enum.

## `set_ssl_protocol_parameter()`

```
public static native void set_ssl_protocol_parameter(
                        Object cryptoContext,
                        Object protocol
                    );
```

Sets the TLS/SSL protocol to use in the current context.

The value of `object` should be a string, either variable or
constant.

## `set_transformation()`

```
public static native void set_transformation(
                        Object cryptoContext,
                        String transformation
                    );
```

Specifies a string to use when performing a transformation.
