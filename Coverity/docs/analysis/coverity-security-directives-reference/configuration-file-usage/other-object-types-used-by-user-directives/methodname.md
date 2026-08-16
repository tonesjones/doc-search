---
title: "MethodName"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/methodname.html"
content_id: "T3WobBO8PpbpdluSGHyG7Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:25.188746+00:00"
---

# MethodName

**Used by these objects:**
`MethodCallSpecifier`, `MethodSet`

A `MethodName` value describes the mangled name for a method.

The mangled method name uses the non-generic types of the arguments and return
values.

- Unconstrained type variables are replaced with `java.lang.Object`
  (Java) or `System.Object` (C#).
- Constrained type variables are replaced with their upper bound.

**Java:**

For Java, mangled method names follow the grammar below (using regex-style notation):

```
method_name  ::= class_name "." method "(" arg_list? ")" return_type
method       ::= identifier

class_name   ::= ( package "." )* class ( "$" inner_class )*
package      ::= identifier
class        ::= identifier
inner_class  ::= identifier

arg_list     ::= ( arg_type ", " )* arg_type
arg_type     ::= type

return_type  ::= type | "void"

type         ::= array_type | class_name | "boolean" | "byte" | "short" | "char" | 
                 "int" | "long" | "float" | "double"
array_type   ::= type "[]"
```

An `identifier`
[non-terminal](https://en.wikipedia.org/wiki/Terminal_and_nonterminal_symbols) is a valid source code
identifier.

Constructors have the string `<init>` for the method identifier and
`void` for the `return_type`.

**.NET:**

For C# and Visual Basic, mangled method names follow the grammar below (using regex-style
notation):

```
method_name  ::= class_name "::" method "(" arg_list? ")" return_type
method       ::= identifier generic_arity?

class_name   ::= ( namespace "." )* class ( "/" inner_class )*
namespace    ::= identifier
class        ::= identifier generic_arity?
inner_class  ::= identifier generic_arity?

arg_list     ::= ( arg_type "," )* arg_type
arg_type     ::= type

return_type  ::= type | "System.Void"

type         ::= array_type | class_name
array_type   ::= type "[]"

generic_arity::= "`" [0-9]+
```

Constructors have the string `.ctor` for the method identifier and
`System.Void` for the `return_type`. For example:

```
NS.Foo::.ctor()System.Void
```

Static constructors have the string `.cctor` for the method identifier and
`System.Void` for the `return_type`. For example:

```
NS.Foo::.cctor()System.Void
```

Note: Primitive names are converted to the corresponding fully qualified class name; for
example:

```
bool  -> System.Boolean
byte  -> System.Byte
sbyte -> System.SByte
```

.
