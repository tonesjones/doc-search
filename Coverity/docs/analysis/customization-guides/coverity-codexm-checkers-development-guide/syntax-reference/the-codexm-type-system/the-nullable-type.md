---
title: "The nullable-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-nullable-type.html"
content_id: "m2QBVBmkXapKGkPsugDKTg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:06.313327+00:00"
---

# The nullable-type

When a property is not specified, that property is `null`.
If there is a possibility of this occurring, the property's type is said to be *nullable*.

CodeXM code indicates a nullable type by appending a question mark
( `?` )
to the name of the underlying non-nullable type.

For example, a function in the target language might return an integer value or it might not.
The pattern for that function includes a property named `.returnValue`.
The type for `.returnValue` would be
`int?`.

## Syntax

[image: image]

```
nullable-type ::=
    type'?'
```

## Details

If a value is `null`,
you cannot use it in an operation and a pattern cannot match it.
Your checker code needs to detect occurrences of `null`
and avoid referencing them.
There are two ways to do so:
by using the keyword `NonNull`,
or by using the null-coalescing operator ( `??` ).

The keyword `NonNull` matches only non-null values.
You can use it with matches to avoid illegally referencing
`null`, as shown in
the following sample code:

[image: CXM code follows]

```
    myNullableValue matches NonNull as myNonnullableValue
```

The null-coalescing operator works a bit differently:
It replaces `null` with a default non-nullable value that
you can specify. The following is an example of code that uses `??`:

[image: CXM code follows]

```
    myNullableValue ?? someDefaultValueIfNull
```

An expression, such as a function, that accepts a nullable type will also accept an object that is `null`.

For further information, see Handling null values.
