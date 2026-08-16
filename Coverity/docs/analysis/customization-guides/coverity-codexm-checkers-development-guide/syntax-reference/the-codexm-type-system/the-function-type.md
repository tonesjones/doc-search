---
title: "The function-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-function-type.html"
content_id: "fk0o3LbNzfT6y47rFUZVHw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:03.284396+00:00"
---

# The function-type

When you define a
function, the function has an implicit type.

The implicit function type has three components:

- The fact that it is a function
- Its parameters
- Its return type

You can also define a particular `function-type`.
You can specify a function type as the type of another function's argument:
doing so enables you to pass functions as arguments.

## Syntax

A function type declaration is similar to a `function-definition`,
but it doesn't specify a function name,
and instead of an expression to evaluate it simply declares the name of the new type.

  
 [image: Syntax diagram, function-type]   

```
function-type ::=
    'function'
        (
            '<'       type-parameter-identifier
                   ( ',' type-parameter-identifier )*
            '>'
        )?
        '('
                         parameter-identifier ':' type
                   ( ',' parameter-identifier ':' type )*
        ')'
        '->' type
```

Each `type-parameter-identifier` is a generic placeholder for an actual type.
This identifier can be used within the parameter list as if it were a known type, the return type,
or any portion of the expression the function evaluates.

Each `parameter-identifier` is an identifier for an explicitly typed parameter.
Each parameter name must be unique to the function.

Each parameter's type must be one of the following:

- A type that is native to CodeXM or that has previously been defined in this CodeXM (`.cxm`) file
- A type defined by an included language library or an included `.cxm` file
- A `type-parameter-identifier` specified in this `function-type` declaration

## Example

A function that accepts a single integer parameter and returns a Boolean value can be written as follows:

[image: CXM code follows]

```
    function(int) -> bool
```

Once declared, the function type can be used in other functions; for example, to specify the type of parameter that the function accepts, as in
the following code sample:0

[image: CXM code follows]

```
    function( function(int) -> bool ) -> bool
```

In the following example, a filter function from a CodeXM library takes a function and a set of values, then applies that function to the values
in the set and returns a filtered list:

[image: CXM code follows]

```
    function filter<T>( predicate: function(T) -> bool, s: set<T> ) : list<T>
```
