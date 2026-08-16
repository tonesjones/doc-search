---
title: "C/C++ security primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-security-primitives.html"
content_id: "dyLPapCOFrkmAX65DWQvtw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:41.222139+00:00"
---

# C/C++ security primitives

These primitives deal with security issues, chiefly involving potential sources or
sinks of tainted data.

## `__coverity_mark_pointee_as_sanitized__( void *ptr, enum TaintSinkType sinktype )`

Indicates to the following checkers that the specified value should be treated as
untainted:

- FORMAT_STRING_INJECTION
- OS_CMD_INJECTION
- PATH_MANIPULATION
- SQLI
- TAINTED_SCALAR
- TAINTED_STRING
- URL_MANIPULATION
- XPATH_INJECTION

The `SinkType` parameter specifies the type of sink that can now
safely accept the sanitized data. If `p` is not of this type, then
the primitive has no effect. These are the possible `SinkType`
values:

- `ALLOCATION`
- `ENVIRONMENT`
- `FORMAT_STRING`
- `GENERIC`
- `LOOP_BOUND_LOWER`

  A loop needs a lower bound check before being passed to this function.
- `LOOP_BOUND_UPPER`

  A loop needs an upper bound check before being passed to this function.
- `OS_CMD_ARGUMENTS`
- `OS_CMD_ARRAY`
- `OS_CMD_FILENAME`
- `OS_CMD_STRING`
- `OVERRUN`
- `PATH`
- `REGISTRY`
- `SQL`
- `TAINTED_SCALAR_GENERIC`
- `URL`
- `XPATH`

## `__coverity_mark_pointee_as_tainted__( void *ptr, enum TaintType taint_type )`

Indicates to the following checkers that a function either taints its argument or
returns tainted data; also indicates the source of the tainted data:

- INTEGER_OVERFLOW
- OS_CMD_INJECTION
- PATH_MANIPULATION
- SQLI
- TAINTED_SCALAR
- TAINTED_STRING
- XPATH_INJECTION

This primitive takes two parameters: a pointer and a taint type (which indicates the
source of the taint). Possible values for `taint_type` are:

- `TAINT_TYPE_HTTP`
- `TAINT_TYPE_NETWORK`
- `TAINT_TYPE_FILESYSTEM`
- `TAINT_TYPE_DATABASE`
- `TAINT_TYPE_CONSOLE`
- `TAINT_TYPE_ENVIRONMENT`
- `TAINT_TYPE_COMMAND_LINE`
- `TAINT_TYPE_SYSTEM_PROPERTIES`
- `TAINT_TYPE_RPC`
- `TAINT_TYPE_HTTP_HEADER`
- `TAINT_TYPE_COOKIE`

These values correspond to available trust options. For more information about trust
options, see the description of `TaintKind` in the Coverity 2026.6.0 Security Directives Reference.

The following model code indicates that `custom_string_read()` taints
its argument `s` and that the source of the tainted data is the
filesystem:

```
void custom_string_read(int fd, char *s) {
    __coverity_mark_pointee_as_tainted__(s, TAINT_TYPE_FILESYSTEM);
}
```

The following model code indicates that `packet_get_int()` returns
tainted data and that the source of the tainted data is the network:

```
unsigned int packet_get_int() {
    unsigned int ret;
    __coverity_mark_pointee_as_tainted__(&ret, TAINT_TYPE_NETWORK);
    return ret;
}
```

## `void __coverity_printf_function_valist__( void *data, const void *format, void *valist );`

Comparable to `__coverity_printf_function_varargs__()` (described next), but instead of using
the current function's `...` arguments, uses a `va_list` argument
(normally this should be of type `va_list`, but to avoid adding
compiler-specific code, this primitive uses a `void *` type).

## `void __coverity_printf_function_varargs__( void *data, const void *format )`

Indicates a `printf`-style function, writing to `data` (which can be
a buffer, a file descriptor, or similar object).
This argument is used for taint tracking.
If the call is not writing to anything that can be tracked, set `data` to `0`.

Objects to print are the current function's `...` arguments.

The `format` can be of type `const char *` or `const wchar_t *`.

## `void __coverity_scanf_function_valist__( const void *data, const void *format, void *valist )`

Comparable to the `__coverity_printf_function_valist__()` primitive (described above), but for `scanf()`.

## `void __coverity_scanf_function_varargs__( const void *data, const void *format )`

Comparable to the `__coverity_printf_function_varargs__()` primitive (described above), but for `scanf()`.

## `__coverity_string_length_function__( const char *str )`

Models invocations of the `strlen()` operator or functions that perform a
comparable string-length evaluation.

## `__coverity_string_null_argument__( char *s, size_t len )`

Indicates to the STRING_NULL checker that a function could assign an argument to a
character array without null-termination. For example:

```
void custom_packet_read(char *s, size_t length) {
    __coverity_string_null_argument__(s);
}
```

Attention:
In Coverity 2021.9.0 and earlier releases, this primitive accepted
only a single character-array argument.

If your code needs to support both versions of Coverity, you can create
a wrapper for the primitive that uses the `__COVERITY_VERSION__` macro,
as shown in the following example:

```
// Compatibility wrapper around __coverity_string_null_argument__():
static void ___coverity_string_null_argument(void *p, size_t len) {
    #if defined(__COVERITY_VERSION__) && __COVERITY_VERSION__ <= 2021090000
        // (In Coverity 2021.9.0 and older releases the primitive took just one argument.)
        __coverity_string_null_argument__(p);
        (void) len;
    #else
        __coverity_string_null_argument__(p, len);
    #endif
}
```

## `__coverity_string_null_return__( void )`

Indicates to the STRING_NULL checker that a function returns a character array that
is not null-terminated. For example:

```
char *custom_network_read() {
    return __coverity_string_null_return__();
}
```

## `__coverity_string_null_sink__( char *s )`

Indicates to the STRING_NULL checker that a function must be protected from strings
that are not null-terminated. For example:

```
void custom_string_replace(char *s, char c, char x) {
    __coverity_string_null_sink__(s);
}
```

## `__coverity_string_null_sink_vararg__( int arg_number )`

Indicates to the STRING_NULL checker that a function's arguments must be
protected from non-null-terminated strings.

The following model indicates that arguments beginning with the second argument must
be null-terminated before being passed to the `custom_vararg()`
function:

```
void custom_vararg(char *s, char *format, ...) {
    __coverity_string_null_sink_vararg__(2);
}
```

## `__coverity_string_size_return__( void )`

Indicates to the STRING_SIZE checker that a function returns a string of arbitrary
size and must be length-checked before use. For example:

```
string custom_string_return() {
    return __coverity_string_size_return__();
}
```

## `__coverity_string_size_sanitize__( void )`

Indicates to the STRING_SIZE checker that a function correctly sanitizes a
string's length.

In the following example, the `size_check()` function returns
`1` when the string has been sanitized with respect to its size,
and `0` otherwise:

```
int size_check(char *s) {
    int ok_size;
    if (ok_size == 1) {
        __coverity_string_size_sanitize__(s);
        return 1;
    } else {
        return 0;
    }
}
```

## `__coverity_string_size_sink__( char *s )`

Indicates to the STRING_SIZE checker that a function is a string size sink and must
be protected from arbitrarily large strings. For example:

```
void *custom_string_process(const char *s) {
    __coverity_string_size_sink__(s);
}
```

## `__coverity_string_size_sink_vararg__( int len )`

Indicates to the STRING_SIZE checker that a function's arguments must be
length-checked before being passed those arguments. For example:

```
void custom_vararg(char *s, char *format, ...) {
    __coverity_string_size_sink_vararg__(2);
}
```

## `__coverity_taint_sink__( void *ptr, enum TaintSinkType sinktype )`

Indicates to the following checkers that a function is a taint sink with respect to
its argument:

- FORMAT_STRING_INJECTION
- OS_CMD_INJECTION
- PATH_MANIPULATION
- SQLI
- TAINTED_SCALAR
- TAINTED_STRING
- URL_MANIPULATION
- XPATH_INJECTION

This primitive takes two parameters—a pointer and a taint sink type. Possible values
for the taint sink type are:

- `ALLOCATION`
- `ENVIRONMENT`
- `FORMAT_STRING`
- `GENERIC`
- `LOOP_BOUND_LOWER`
- `LOOP_BOUND_UPPER`
- `OS_CMD_ARGUMENTS`
- `OS_CMD_ARRAY`
- `OS_CMD_FILENAME`
- `OS_CMD_STRING`
- `OVERRUN`
- `PATH`
- `REGISTRY`
- `SQL`
- `TAINTED_SCALAR_GENERIC`
- `URL`
- `XPATH`

The following model code indicates that `custom_putenv()` is a taint
sink (of type `ENVIRONMENT`) with respect to its argument `string`:

```
void custom_putenv(char *string) {
    __coverity_taint_sink__(string, ENVIRONMENT);
}
```

Note: Coverity models the standard C-interface function `putenv()` by
using a similar stub function.

## `__coverity_tainted_data_transitive__( void *dest, const void *src )`

Used by a tainted data checker to a model function that propagates taintedness from
one argument to another.

The following model code indicates that `custom_copy()` will
transitively taint its `dest` argument, based on the tainted state of
its `src` argument (and only if `n != 0`).

```
void *custom_copy(void *dest, void *src, size_t n) {
    if (n != 0) {
        __coverity_tainted_data_transitive__(dest, src);
    }
    return dest;
}
```

Note: Coverity models the standard C-interface function `memcpy()` by
using a similar stub function.

## `__coverity_tainted_data_transitive_vararg_inbound__( unsigned position0, unsigned position1 )`

Indicates to the TAINTED_SCALAR checker that a function transitively taints one
argument if other arguments are tainted.

The following model code indicates that `custom_sprintf()`
transitively taints argument `0` if any argument from
`2` onward is tainted.

```
void custom_sprintf(char *str, const char *format, ...) {
    __coverity_tainted_data_transitive_vararg_inbound__(0,2);
}
```

Note: Coverity models the standard C-interface function `sprintf()` by
using a similar stub function.

## `__coverity_tainted_data_transitive_vararg_outbound__( unsigned position0, unsigned position1 )`

Indicates to the TAINTED_SCALAR checker that a function transitively taints arguments
if a specific argument is tainted.

The following model code indicates that `custom_sscanf()` transitively
taints arguments `2` and onward if argument `0` is
tainted:

```
void custom_sscanf(const char *str, const char *format, ...) {
    __coverity_tainted_data_transitive_vararg_outbound__(2, 0);
}
```

## `__coverity_tainted_unterminated_string__( void )`

To the STRING_NULL checker, indicates that a function returns a string that is not
null-terminated. To the TAINTED_STRING checker, indicates that a function returns a
tainted string.

## `__coverity_user_pointer__( char *arg )`

Indicates to the USER_POINTER checker that a function dereferences user-space
pointers.
