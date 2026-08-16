---
title: "Mangled naming scheme: Java"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/mangled-naming-scheme-java.html"
content_id: "hNziQJFmKwQn_Vo7VIHClA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:05.120237+00:00"
---

# Mangled naming scheme: Java

Coverity uses a specialized grammar to mangle the names of Java identifiers
(`Identifier`), which include the names of packages, classes, fields,
methods, and so on. Table 1 provides
synopses of that grammar, and the code sample that
follows it provides the mangled name for several identifiers in the sample.

Table 1. Java Mangled name grammar

| Identifier type | Synopsis[*] |
| --- | --- |
| ClassName | { `Identifier "$"` } `Identifier` |
| MethodName | `Identifier` |
| FieldName | `Identifier` |
| PackageName | `Identifier` { `"." Identifier` } |
| MangledClassName | [ `PackageName "."` ] `ClassName` { `"`[ ]`"` } |
| MangledFieldName | `MangledClassName "." FieldName` |
| PrimitiveTypeName | `"boolean"` | `"char"` | `"float"` | `"double"` | `"byte"` | `"short"` | `"int"` | `"long"` |
| TypeName | `MangledClassName` | `PrimitiveTypeName` { `"`[ ]`"` } |
| ReturnTypeName | `TypeName` | `"void"` |
| ArgList | `TypeName` { `", " TypeName` } |
| MangledMethodName | `MangledClassName "." MethodName "("` [ `ArgList` ] `")"`  `ReturnTypeName` |

Note: [*]The synopses use the following syntax:

- Brackets for a sequence that is optional: [ ]
- Curly braces for a sequence that can be omitted or repeated: { }
- Pipes for a sequence that must match exactly one of the options:
  `"x"` | `"y"` |
  `"z"`

The comments in the following code sample list the
mangled names of classes, fields, methods, and other items in a sample Java class.

```
// (c) 2017, Black Duck Software, Inc. All rights reserved worldwide.
package p;
class Outer {                // p.Outer[1]
    int i = 24;              // p.Outer.i[2]
    String str = "s";        // p.Outer.str
    // The following "virtual" function is created to
    // initialize all non-static member fields:
    //   p.Outer.instance_field_initializations()void[3]
    static final int a = 1;  // p.Outer.a
    static int b = 2;        // p.Outer.b
    static {
        b = 777;
    }
    // The following "virtual" function is created to do
    // all the static initializations for this class:
    //   p.Outer.clinit()void
    Outer() {                     // p.Outer.init()void
        int localVar = 4;         // localVar[4]
    }
    int foo(int i, int j) {       // p.Outer.foo(int, int)int
        return 21;
    }
    void printme(String s) {      // p.Outer.printme(java.lang.String)void[5]
        System.out.println(s);    // java.io.PrintStream.println(java.lang.String)void
    }
    class Inner {                 // p.Outer$Inner[6]
        int field = 1;            // p.Outer$Inner.field
        int bar(int i, int j) {   // p.Outer$Inner.bar(int, int)int[7][8]
            return 22;
        }
    }
    void testAnonClass(String s) {      // p.Outer.testAnonClass(java.lang.String)void
        final String capturedLocal = s; // capturedLocal
        Inner anonymousInstance =
            new Inner() {               // p.Outer$1[9]
                // The constructor that is generated for an anonymous class
                // takes the containing class instance as an argument:
                //   p.Outer$1.init(p.Outer)void
                //
                // In addition, a synthetic field called "this$0" is
                // created to refer to the containing class instance.
                // And synthetic fields called val$var_name are created
                // for any captured local variables from the containing class.
                public String getS() {     // p.Outer$1.getS()java.lang.String
                    Outer myParent =       // myParent
                        Outer.this;        // this$0
                    return capturedLocal;  // val$capturedLocal[10]
                }
            };
    }
}
```

- [1]: If a class is declared within a package, then its mangled class name is
  always prepended with its package name. Examples: `java.lang.String`,
  `Package.ClassA`
- [2]: Class field names are always prepended with the full class name and the
  package name, if any. Example: `Package.ClassA.field`
- [3]: A few special methods are created automatically (if applicable) for each class:
  - init - A class constructor.
  - clinit - A method containing all the static initializers
    for a class.
  - instance_field_initializations - A method containing the
    initializers for non-static member fields.
- [4]: Local variable names do not require any mangling. The package and class
  names are not prepended for local variables.
- [5]: Unless a type is one of the primitive types (such as boolean, char, or
  int), its mangled type name includes the package it belongs to. Example:
  `java.lang.String`
- [6]: Nested class names are denoted with `$`. Example:
  `Package.Outer$Inner1$Inner2`
- [7]: The return type for a method is located at the end of the mangled name,
  rather than at the beginning. Example:
  `Package.ClassA.printString(java.lang.String)void`. Otherwise,
  mangled method names are very readable (especially compared to mangled C
  functions).
- [8]: When matching the mangled name of a method, be careful to notice the space
  between arguments. For example, attempting to match the name
  `foo(int,int)void` will not result in a match. You must use the
  following, instead: `foo(int, int)void`
- [9]: Anonymous classes have no real name, so they are assigned numbers. The
  numbers are assigned arbitrarily and you should not depend on their appearance in a
  particular order. For the purpose of name mangling, anonymous classes are treated as
  nested classes. Example: `Package.Outer$1`
- [10]: There are two kinds of synthetically-created variables, and they are both
  related to the way that an anonymous class captures values from its enclosing class
  or method.
  - `this$0` - Pointer to the enclosing class instance.
  - `val$original_variable_name` -
    Captured local variables. When a final local variable is used inside an
    anonymous class, this name is used to refer to it.

Note: Also note that Java class constructors have different mangled names than C++
constructors. For example, compare the C++ name `CClass::CClass()` to the
Java name `JavaClass.init`.
