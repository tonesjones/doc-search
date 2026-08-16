---
title: "classDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classdefinition.html"
content_id: "3prUe4atfRRgGojRu56YpA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:28.831235+00:00"
---

# classDefinition

Describes a target-language `class` (C++), `struct`, or `union`.

Note:
If a type is never used in a project (a code base), its definition might be elided from analysis.

## Properties

`classDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `declaredType` | `classType` | The associated `classType` record for this definition |
| `memberFunctionList` | `list<functionSymbol>` | A list of member functions in this class |
| `staticFieldList` | `list<globalVariableSymbol>` | A list of fields declared as `static` |
| `fieldList` | `list<fieldSymbol>` | A list of fields that are not static |
| `staticMemberFunctionList` | `list<functionSymbol>` | A list of the static member functions in this class |
| `parentList` | `list<classParent>` | A list of parent classes |
| `location` | `sourceloc` | The source-code location of the class definition |
| `byteSize` | `int` | The byte size of a class instance |
| `instantiatedFrom` | `classType?` | The class from which this class is instantiated; `null` if the class is not an instance |
| `specializationOf` | `classType?` | The class of which this class is a specialization; `null` if the class is not a specialization |
| `isFinal` | `bool` | `true` if the class is marked as `final` |
| `isPOD` | `bool` | `true` if the class is marked as POD (Plain Old Data) |
| `isStandardLayout` | `bool` | `true` if the class is a standard layout |
| `isTriviallyDefaultConstructible` | `bool` | `true` if the class is trivially default-constructible |
| `isTriviallyDestructible` | `bool` | `true` if the class is trivially destructible |
| `findBaseClass` | `function<testType>` | A function that invokes a callback function, which can be used as a predicate to find a particular base class—in other words, to test whether the class is a parent of the current class. See The base class properties. |
| `findMatchingBaseClass` | `function<testType>` | A function that invokes a pattern, which can be used as a predicate to find a particular base class—in other words, to test whether the class is a parent of the current class. See The base class properties. |

## Example

Given the following source-code snippet:

  
 [image: C/C++ code follows]   

```
struct T {
    static char c;
    int member;
};
```

... the pattern `classDefinition` matches
the definition of `struct T`:

[image: CXM code follows]

```
    for d in globalset allClasses {
    where d matches classDefinition as c :
        // ... And so on
};
```
