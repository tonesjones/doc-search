---
title: "The function-definition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-function-definition.html"
content_id: "oBLjmtQ6KGPxci9JcfjQmw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:15.876812+00:00"
---

# The function-definition

CodeXM allows you to define functions that can evaluate specific expressions, allowing you to give a descriptive name to what otherwise might be a complicated expression.
This helps readability and allows you to use that expression in more than one place.

## Syntax

A function declaration is introduced by the keyword `function`
and an identifier that names the function.
This is optionally followed by generic type IDs, and then by at least one formal parameter that has a name and an explicit type.
The return type of the function can optionally be specified, and then an arrow delimiter ( `->` ) introduces the
expression that defines the body of the function.

  
 [image: Syntax diagram, function-definition]   

```
function-definition ::=
    'function' identifier
        ( '<'       type-parameter-identifier
                 ( ',' type-parameter-identifier )*
          '>' )?
          '('          parameter-identifier ':' type
                 ( ',' parameter-identifier ':' type )*
          ')' (':' type)? '->' expression
```

Each `type-parameter-identifier` is a generic placeholder for an actual type (see below).
This identifier can be used within the parameter list as if it were a known type.
It can also be used as the function's return type,
or in any portion of the expression that the function evaluates.
When present, these identfiers appear immediately after the function name.
Generic type identifiers are enclosed by angle brackets
( `<` and `>` )
and separated by commas ( `,` ).

Each `parameter-identifier` is an identifier for a formal, explicitly typed parameter.
Each parameter name must be unique to the function.
Named parameters are enclosed by parentheses ( `(` and `)` )
and separated by commas ( `,` ).
Each named parameter has an associated type.

Each parameter's type must be one of the following:

- A type that is native to CodeXM or that has previously been defined in this CodeXM (.cxm) file
- A type defined by an included language library or an included .cxm file
- A `type-parameter-identifier` specified in this function definition

## Details

Because CodeXM is a functional (rather than procedural) language, a function cannot generate side effects:
For example, a function cannot set variables that persist beyond the scope of the function call itself.

A function can be recursive: The function's name and type are accessible within the body of the function, enabling it to call itself.

For an example of recursive function use,
see Defining CodeXM functions.
