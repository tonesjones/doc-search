---
title: "C# and Visual Basic reference-object primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-and-visual-basic-reference-object-primitives.html"
content_id: "tbFsbGKN35Ka0HNmYP8djQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:47.245186+00:00"
---

# C# and Visual Basic reference-object primitives

These primitives model operations that use reference objects.

## `Reference.Alias( System.Object to, System.Object from )`

Indicates that the object provided as the first parameter (`to`) is to
be considered an alias for the object provided as the second parameter
(`from`) To this extent, closing the object referred to in the
first parameter (`to`) is understood to close the object in the
second parameter (`from`). This is typically used to model a class
that contains, and properly manages, a member which also has open and close
semantics. Analysis understands that closing the containing class closes the
contained member as well.

Parameters:

`to`
:   The object aliased to another object

`from`
:   The object being aliased

See also:

- `Reference.Open( System.Object )`
- `Reference.Close( System.Object )`

## `Reference.Close( System.Object o )`

Indicates that the object provided is to be considered closed. A closed object should
have been previously opened. If `o` is a resource previously opened,
it no longer needs closing. Calls to this primitive are typically inserted where
closing of the resource is handled.

Parameters:

`o`
:   The object being closed

See also:

- `Reference.Open( System.Object )`

## `Reference.Escape( System.Object o )`

Indicates that the object given is considered to escape. An escaped object is no
longer tracked by analysis. The value passed in may or may not flow to, and be used
in, other parts of the program.

Parameters:

`o`
:   The object being escaped

## `Reference.EscapeNoClose( System.Object o )`

Indicates that the object given is considered to escape. An escaped object is no
longer tracked by analysis. The value passed in may or may not flow to, and be used
in, other parts of the program.

Parameters:

`o`
:   The object being escaped

## `Reference.Open( System.Object o )`

Indicates that the object provided (`o`) is a resource to be
considered open (and thus should be subsequently closed).

Parameters:

`o`
:   The object being opened

See also:

- `Reference.Close( System.Object )`
