---
title: "The call-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-call-expression.html"
content_id: "4tFk7byR_WkJzK8fDlckuw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:25.517815+00:00"
---

# The call-expression

Calls a function, using the specified arguments.

## Syntax

The list of arguments is enclosed by parentheses ( `( )` ),
and arguments are separated by commas ( `,` ).

The number of arguments in the call must equal the number of arguments in the function-definition.
The arguments passed can be either named or unnamed.
If the name is specified, it is followed by a colon ( `:` ) and then by the value of that argument.

  
 [image: Syntax diagram, call-expression]   

```
call-expression ::=
    function-producing-expression
    '('       ( identifier ':' )? expression
        ( ',' ( identifier ':' )? expression )*
    ')'
```

The `function-producing-expression` specifies a function that has already been declared
(unless you use a forward-declaration).

## Details

If an argument is named, that name must be the same as the corresponding formal parameter in that function's definition.

It is an error to use an argument name that doesn't appear in the definition.
It is also an error to change the order of the arguments, whether or not you specify argument names.

For example, if a function is declared like this:

[image: CXM code follows]

```
    function func(first: int, second: int, third: int)
```

... it can be invoked like this (that is, not naming the arguments):

[image: CXM code follows]

```
    func(1, 42, 99)
```

... or like this (naming the arguments, in the right order):

[image: CXM code follows]

```
    func(first: 1, second: 42, third: 99)
```

... or even this (naming only one argument):

[image: CXM code follows]

```
    func(1, second: 42, 99)
```

... but the following is an error because reordering arguments is not permitted:

[image: CXM code follows]

```
    func(second: 42, first: 1, third: 99)
```
