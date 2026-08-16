---
title: "C/C++ resource-management primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-resource-management-primitives.html"
content_id: "rIljj5gmdfdousHIUWPp1g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:40.472558+00:00"
---

# C/C++ resource-management primitives

These primitives deal chiefly with allocating and releasing memory.

Note:
The standard C library and the corresponding directory structure categorize these
operations as "generic" functions.

## `__coverity_alloc__( unsigned size )`

Models a function that returns a dynamically allocated block of memory. The
function's only argument determines its size. The RESOURCE_LEAK checker uses
this primitive to identify which pointers refer to memory that must be freed.
SIZE_CHECK and OVERRUN use it to determine if the allocated size is correct.

For an example, see the function `malloc()` in the file
<install_dir>/library/generic/libc/all/all.c.

## `__coverity_alloc_nosize__( void )`

Models a function that returns a dynamically allocated block of memory without size
information. Used when you are looking for RESOURCE_LEAK errors but are not
interested in buffer overruns.

For an example, see the function `fopen()` in the file
file.c.

## `__coverity_close__( int handle )`

Closes a handle. Used to model file handle allocation for the RESOURCE_LEAK and
USE_AFTER_FREE checkers.

## `__coverity_commutative_operation__(void *)`

Indicates that modifications to the argument in the function where this is called should be considered commutative,
and *will not* cause the POINTER_NONDETERMINISM checker to report an iteration defect.

**Usage example:**

```
class X {
    Y &getY() {
        // Lazy initialization is commutative
        __coverity_commutative_operation(this);
        if (!y) {
            y = new Y;
        }
        return *y;
    }
    Y *y = nullptr;
};
```

## `__coverity_delete__( void *ptr )`

Models a call to operator delete[]. In addition to memory
deallocation semantics, this will cause an error if
`__coverity_new_array__` allocated this memory. The DELETE_ARRAY
checker uses this primitive.

## `__coverity_delete_array__( void *ptr )`

Models a call to operator delete[]. In addition to memory
deallocation semantics, this will cause an error if
`__coverity_new__()` allocated this memory. The DELETE_ARRAY
checker uses this primitive.

## `__coverity_escape__( void *ptr )`

Models a function that saves its argument (for example, in a global variable) so it
can be freed later. The analysis will not report a resource leak on such an argument
once it escapes.

## `__coverity_free__( void *ptr )`

Frees its argument. Indicates to the USE_AFTER_FREE and RESOURCE_LEAK checkers that a
pointer is freed. For an example, see the function `free()` in
<install_dir>/library/generic/libc/all/all.c.

## `__coverity_mark_as_afm_allocated__`

Models a function that marks the passed handle/pointer as a resource that can only be
deallocated by a matching deallocator. This tracks the allocation for the
ALLOC_FREE_MISMATCH checker. This primitive accepts a
handle/pointer parameter and a common string (usually the name of the deallocator)
that indicates the pairing.

## `__coverity_mark_as_afm_freed__`

Models a function that marks the passed handle/pointer as a resource that can only be
allocated by a matching deallocator. This tracks the deallocation for the
ALLOC_FREE_MISMATCH checker. This primitive accepts a
handle/pointer parameter and a common string (usually the name of the allocator)
that indicates the pairing.

## `__coverity_negative_sink__( int val )`

Models a function that cannot take a negative number as an argument. Used in
conjunction with other models to indicate that negative arguments are invalid. For
example, see the `size` argument in
<install_dir>/library/generic/libc/all/all.c.

## `__coverity_new__( unsigned size )`

Models a call to operator new[]. In addition to memory allocation
semantics, this will cause an error if `__coverity_delete_array__()`
later frees this memory. The DELETE_ARRAY checker uses this primitive.

## `__coverity_new_array__( unsigned size )`

Models a call to operator new[]. In addition to memory allocation
semantics, this will cause an error if `__coverity_delete__()` later
frees this memory. The DELETE_ARRAY checker uses this primitive.

## `__coverity_open__( void )`

Creates a handle that needs to be closed. Used to model file handle allocation for
the RESOURCE_LEAK and USE_AFTER_FREE checkers.

## `__coverity_panic__( void )`

Models a function that ends the execution of the current path.

For an example, see the function `abort()` in the file
killpath.c.

## `__coverity_read_buffer_bytes__( const void *buf, unsigned size );`

Indicates that a buffer is read up to a given size in bytes. Mainly affects the
OVERRUN, ARRAY_VS_SINGLETON, and UNINIT checkers.

## `__coverity_read_buffer_elements__( const void *buf, unsigned size );`

Indicates that a buffer is read up to a given size specified in elements. The element
type is determined by the type of the expression before the cast to `void
*`. Mainly affects the OVERRUN, ARRAY_VS_SINGLETON, and UNINIT
checkers.

## `__coverity_stack_alloc__( unsigned size )`

Indicates stack-based allocation, as in `alloca()`. For use with the
OVERRUN checker.

## `__coverity_stack_depth__( unisigned max_memory )`

Indicates to the STACK_USE checker that the function and its callees should not use
more memory (in bytes) than specified by the constant integer
`max_memory`. This feature is useful for situations
where threads are created with different stack sizes. The primitive should be used
in the thread entry-point function.

Note:
This primitive is called from your source code, not from model source.

You need to declare this primitive in your code at the top of the tree for which you
intend to specify a limit. For example, you might add the following to a
coverity.h header file:

```
#ifdef __COVERITY__
#ifdef __cplusplus
extern "C"
#endif
void __coverity_stack_depth__(unsigned long);
#else
#define __coverity_stack_depth__(x) 0
#endif
```

Then you can include the declaration in a file that contains a thread entry function.
The call to `__coverity_stack_depth__()` must appear in your source.
It can appear anywhere within the function that uses it. Only one call to
`__coverity_stack_depth__()` per function is allowed. For
example, threadentry.c:

```
#include "coverity.h"

// ...

void thread_entry() {
    __coverity_stack_depth__( MAX_THREAD_STACK_BYTES );

    // Implement thread entry

}
```

## `__coverity_use_handle__( void )`

Indicates the invalid use of a handle if the handle has been previously closed. Used
to model file handle allocation for the RESOURCE_LEAK and USE_AFTER_FREE
checkers.

## `__coverity_write_buffer_bytes__( void *buf, unsigned size );`

Indicates that a buffer is written up to a given size, specified in bytes. Mainly
affects the OVERRUN, ARRAY_VS_SINGLETON, and UNINIT checkers.

## `__coverity_write_buffer_elements__( void *buf, unsigned size );`

Indicates that a buffer is written up to a given size, specified in elements. The
element type is determined by the type of the expression, `buf`,
before the cast to `void *`. Mainly affects the OVERRUN,
ARRAY_VS_SINGLETON, and UNINIT checkers.

## `__coverity_writeall__( void )`

Indicates that all contents of a variable are overwritten. This includes all fields
if the variable is a structure, or simply the variable's value if it is
not.

For an example, see the function `memcpy()` in the
mem.c file.
