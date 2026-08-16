---
title: "Deprecated C/C++ security primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deprecated-c/c-security-primitives.html"
content_id: "Hvur7mAPVJtEJL9x1NW2qA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:41.967156+00:00"
---

# Deprecated C/C++ security primitives

These primitives were deprecated in earlier releases of Coverity. Each section
describes an upgrade path from the earlier version.

## `__coverity_format_string_sink__( char *arg )`

**Deprecated:** This primitive has been deprecated as of Coverity 2019.09. It is
supported for backward compatibility only. Use
`__coverity_taint_sink__()` instead.

Indicates to the TAINTED_STRING checker that a function is a format string sink.

The following model code indicates that `custom_printf()` is a format
string sink with respect to its `format` argument:

```
void custom_printf(const char *format, ...) {
    __coverity_taint_sink__(format, FORMAT_STRING);
}
```

Note: This model is similar to the built-in Coverity model for the standard C-library
function `printf()`.

## `__coverity_secure_coding_function__( char *type, char *problem, char *alternative, char *risk )`

Indicates to the SECURE_CODING checker that a function should not be used.

Note: DEPRECATED in 7.5.0: The SECURE_CODING checker has been deprecated. As of release
2020.03, we recommend that you use CodeXM to implement custom checkers that can
identify *don't call* issues. See "Writing your own *Don't Call* checker" in the Coverity
CodeXM Checkers Development Guide.

The following model code indicates that at every call to
`outdated_copy_function()`, a warning appears informing the
developer that this function should be avoided and replaced with
`updated_copy_function()`. For example:

```
int outdated_copy_function(void *arg) {
    __coverity_secure_coding_function__("buffer overflow",
        "outdated_function makes no guarantee of safety.",
        "Use updated_copy_function() instead.",
        "VERY RISKY");
}
```

## `__coverity_tainted_data_argument__( void )`

**Deprecated:** This primitive is supported for backward compatibility only. Use
`__coverity_mark_pointee_as_tainted__()` instead.

Indicates to the TAINTED_SCALAR checker and the INTEGER_OVERFLOW checker that a
function taints its argument.

The following model code indicates that `custom_read()` taints its
argument `buf`:

```
void custom_read(int fd, void *buf) {
    __coverity_tainted_data_argument__(buf);
}
```

Note: Coverity models the POSIX `custom_read()` interface using a similar
stub function.

Use the following model as a guide for migrating
`__coverity_tainted_data_argument__()` usage to
`__coverity_mark_pointee_as_tainted__()` usage. This model
improves upon the previous by indicating the source of the tainted data (in this
case, the filesystem):

```
void custom_read(int fd, void *buf) {
    __coverity_mark_pointee_as_tainted__(buf, TAINT_TYPE_FILESYSTEM);
}
```

## `__coverity_tainted_data_return__( void )`

**Deprecated:** This primitive is supported for backward compatibility only. Use
`__coverity_mark_pointee_as_tainted__()` instead.

Indicates to the TAINTED_SCALAR checker and the INTEGER_OVERFLOW checker that a
function returns tainted data.

The following model code indicates that `packet_get_int()` returns
tainted data and should be tracked as such:

```
unsigned int packet_get_int() {
    return __coverity_tainted_data_return__();
}
```

Use the following model as a guide for migrating
`__coverity_tainted_data_return__()` usage to
`__coverity_mark_pointee_as_tainted__()` usage. This model
improves upon the previous by indicating the source of the tainted data (in this
case, the network):

```
unsigned int packet_get_int() {
    unsigned int ret;
    __coverity_mark_pointee_as_tainted__(&ret, TAINT_TYPE_NETWORK);
    return ret;
}
```

## `__coverity_tainted_data_sanitize__( void )`

**Deprecated:** This primitive has been deprecated as of Coverity 2019.09. It is
supported for backward compatibility only. Use
`__coverity_mark_pointee_as_sanitized__()` instead.

Makes the TAINTED_SCALAR checker treat the provided value as though it is
untainted.

The following model code indicates to the checker that it should no longer track
`s.x` (or `s.y`) as tainted if
`check_value()` returns `1`:

```
struct S { int x, y; };
int check_value(struct S *s) {
    int is_ok;
    if (is_ok) {
        __coverity_mark_pointee_as_sanitized__(s, OVERRUN);
        return 1;
    } else {
        return 0;
    }
}
```

Test code:

```
struct S { int x, y; };
void test() {
    int array[10];
    struct S s;
    read(0, &s, sizeof(s));
    if (check_value(&s)) {
        // no bug here
        array[s.x] = 1;
    } else {
        // TAINTED_SCALAR reported
        array[s.x] = 1;
    }
}
```

## `__coverity_tainted_data_sink__( void )`

**Deprecated:** This primitive is supported for backward compatibility only. Use
`__coverity_taint_sink__()` instead.

Indicates to the TAINTED_SCALAR checker and the INTEGER_OVERFLOW checker that a
function is a taint sink for an argument.

The following model code indicates that `custom_wfrite()` is a taint
sink for argument `count`:

```
void custom_write(int fd, const void *buf, size_t count) {
    __coverity_tainted_data_sink__(count);
}
```

Note: Coverity models the POSIX `write()` interface by using a similar
stub function.

Use the following model as a guide for migrating
`__coverity_tainted_data_sink__()` usage to
`__coverity_taint_sink__()` usage. This model indicates that
`custom_write()` is a taint sink (of type
`OVERRUN`) with respect to its argument
`count`:

```
void custom_write(int fd, const void *buf, size_t count) {
    __coverity_taint_sink__(&count, OVERRUN);
}
```

## `__coverity_tainted_data_transitive_return__( void )`

**Deprecated:** This primitive is supported for backward compatibility only. Use
`__coverity_tainted_data_transitive__()` instead.

Used by the TAINTED_SCALAR checker to model functions that transitively taint a
return value based on the taintedness of an argument, for example
`atoi`.

For example:

```
// if b was tainted, get_int returns tainted data
// get_int pulls an integer out of some buffer
int get_int(struct buffer *b) {
    return __coverity_tainted_data_transitive_return__(b->x);
}
```

Use the following model as a guide for migrating
`__coverity_tainted_data_transitive_return__()` usage to
`__coverity_tainted_data_transitive__()` usage:

```
// if b was tainted, get_int returns tainted data
// get_int pulls an integer out of some buffer
int get_int(struct buffer *b) {
    int r;
    __coverity_tainted_data_transitive__(r, b->x);
    return r;
}
```

## `__coverity_tainted_string_argument__( void )`

**Deprecated:** This primitive is supported for backward compatibility only. Use
`__coverity_mark_pointee_as_tainted__()` instead.

Indicates to the TAINTED_STRING checker that a function taints its argument.

The following model code indicates that `custom_string_read()` taints
its argument `s`:

```
char *custom_string_read(char *s, int size, FILE *stream) {
    __coverity_tainted_string_argument__(s);
    return s;
}
```

Use the following model as a guide for migrating
`__coverity_tainted_string_argument__()` usage to
`__coverity_mark_pointee_as_tainted__()` usage. The newer model
improves upon the previous one by indicating the source of the tainted data (in this
case, the filesystem):

```
char *custom_string_read(char *s, int size, FILE *stream) {
   __coverity_mark_pointee_as_tainted__(s, TAINT_TYPE_FILESYSTEM);
   return s;
}
```

## `__coverity_tainted_string_return_content__( void )`

**Deprecated:** This primitive is supported for backward compatibility only. Use
`__coverity_mark_pointee_as_tainted__()` instead.

Indicates to the TAINTED_STRING checker that a function returns a tainted string.

The following model code indicates that `packet_get_string()` returns
a tainted string:

```
void *packet_get_string() {
    return __coverity_tainted_string_return_content__();
}
```

Use the following model as a guide for migrating
`__coverity_tainted_string_return_content__()` usage to
`__coverity_mark_pointee_as_tainted__()` usage. The newer model
improves upon the previous one by indicating the source of the tainted data (in this
case, the network):

```
void *packet_get_string() {
    void *ret;
    __coverity_mark_pointee_as_tainted__(ret, TAINT_TYPE_NETWORK);
    return ret;
}
```

## `__coverity_tainted_string_sanitize_content__( void )`

**Deprecated:** This primitive has been deprecated as of Coverity 2019.09. It is
supported for backward compatibility only. Use
`__coverity_mark_pointee_as_sanitized__()` instead.

Indicates to the TAINTED_STRING checker whether a function can sanitize an
argument.

The following model code indicates that `s` will be sanitized for
sinks of type `PATH` when `custom_sanitize()` returns
`true`, but will not be cleansed in cases where the function
returns `false`:

```
bool custom_sanitize(const char *s) {
    bool ok_string;
    if (ok_string == true) {
        __coverity_mark_pointee_as_sanitized__(s, PATH);
        return true;
    }
    return false;
}
```

## `__coverity_tainted_string_sink_content__( char *arg )`

**Deprecated:** This primitive is supported for backward compatibility only. Use
`__coverity_taint_sink__()` instead.

Indicates to the TAINTED_STRING checker that a function is a taint sink with respect
to its argument.

The following model code indicates that `custom_db_command()` is a
tainted string sink with respect to its argument `command`:

```
void custom_putenv(const char *command) {
    __coverity_tainted_string_sink_content__(command);
}
```

Use the following model as a guide for migrating
`__coverity_tainted_string_sink_content__()` usage to
`__coverity_taint_sink__()` usage. The newer model indicates that
`custom_putenv()` is a taint sink (of type
`ENVIRONMENT`) with respect to its argument
`string`:

```
void custom_putenv(char *string) {
    __coverity_taint_sink__(string, ENVIRONMENT);
}
```

Note: Coverity models the standard C-interface function `putenv()` by
using a similar stub function:
