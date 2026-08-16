---
title: "ClassName"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classname.html"
content_id: "T3ulaSSZE7nOqJ1bRUw~zg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:13.498391+00:00"
---

# ClassName

**Used by these objects:**
`AnnotationSet`, `ClassSet`,
`MethodCallSpecifier`

A `ClassName` value describes the mangled name for a class type.

The mangled name uses the fully qualified name of that type, without including any
generic type arguments.

**Java**

For Java, mangled type names follow the grammar below (using regex-style notation):

```
class_name   ::= ( package "." )* class ( "$" inner_class )*
package      ::= identifier
class        ::= identifier
inner_class  ::= identifier
```

An `identifier`
[non-terminal](https://en.wikipedia.org/wiki/Terminal_and_nonterminal_symbols) is a valid source-code
identifier.

**Visual Basic**

For C# and Visual Basic, mangled type names follow the grammar below (using regex-style
notation):

```
class_name   ::= ( namespace "." )* class ( "/" inner_class )*
namespace    ::= identifier
class        ::= identifier generic_arity?
inner_class  ::= identifier generic_arity?
generic_arity::= "`" [0-9]+
```
