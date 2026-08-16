---
title: "Mangled naming scheme: C#"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/mangled-naming-scheme-c-.html"
content_id: "Jgignm7~h5p2IKi3epFTZw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:04.390551+00:00"
---

# Mangled naming scheme: C#

Coverity uses a specialized grammar to represent the names and signatures of C# types,
fields, methods, and so on. The rules for C# name mangling are as follows:

- Nested namespaces are separated by a period: `System.Data`
- Types directly contained by a namespace are separated by a period:
  `System.Math`
- Types represented by special keywords, such as int or void, are represented
  by their equivalent fully-qualified system types:
  `System.Int32`
- Array types are represented as in C#, by appending brackets containing zero
  or more commas: `System.Char[,]`
- Nested types are separated by a solidus:
  `OuterClass/InnerClass`
- Unconstructed generic types and methods are represented by appending a
  backtick and the generic arity (the number of type parameters) to the
  mangled type or method name:
  `` System.Collections.Generic.Dictionary`2 ``
- Constructed generic types are represented by appending to the mangled type
  name a comma-separated list of mangled type arguments in angle brackets:
  `` System.Collections.Generic.Dictionary`2System.Int32,System.String ``
- Type members other than nested types are separated from their containing type
  by a double colon: `MyClass::myField`
- Method names are followed by first, a parenthesized, comma-separated list of
  mangled formal parameter types (ote that the comma is not followed by a
  space), and second, the mangled return type:
  `System.Math::Sin(System.Double)System.Double`
- Class constructors, instance constructors and destructors are treated as
  void-returning methods named .cctor,
  .ctor, or .dtor respectively:
  `System.Object::.ctor()System.Void`
- Property accessors are represented as though they were methods; the property
  name is prepended with `get_` or `set_` as
  appropriate: `System.String::get_Chars()System.Char[]`

  Similarly, event accessors are represented as though they were methods; the
  property name is prepended with `add_` and
  `remove_` as appropriate.
- Indexers are treated as though they were methods; the indexer name is
  `get_Item` or `set_Item` as appropriate:
  `System.String::get_Item(System.Int32)System.Char`
- User-defined operators are treated as though they were methods named
  `op_Addition`, `op_LogicalNot`. The full
  list is as follows:

  |  |  |
  | --- | --- |
  | != | op_Inequality |
  | < | op_LessThan |
  | > | op_GreaterThan |
  | <= | op_LessThanOrEqual |
  | >= | op_GreaterThanOrEqual |
  | * | op_Multiply |
  | / | op_Division |
  | % | op_Modulus |
  | + | op_Addition / op_UnaryPlus |
  | - | op_Subtraction / op_UnaryNegation |
  | << | op_LeftShift |
  | >> | op_RightShift |
  | & | op_BitwiseAnd |
  | | | op_BitwiseOr |
  | ^ | op_ExclusiveOr |
  | ! | op_LogicalNot |
  | ~ | op_OnesComplement |
  | ++ | op_Increment |
  | -- | op_Decrement |
  | operator true | op_True |
  | operator false | op_False |
  | implicit operator type | op_Implicit |
  | explicit operator type | op_Explicit |
- Formal type parameters are represented using the name of the parameter.
- Unsafe pointer types have a `*` appended to the mangled
  name.

For example: the mangled name of the method in:

```
namespace N
{
  class O<T>
  {
    class I<U, V>
    {
      void M<W>(L<W> w, int[] i) {}
    }  
  }
  class L<X> {}
  }
```

Would be:

```
N.O`1/I`2::M`1(N.L`1<W>,System.Int32[])System.Void
```
