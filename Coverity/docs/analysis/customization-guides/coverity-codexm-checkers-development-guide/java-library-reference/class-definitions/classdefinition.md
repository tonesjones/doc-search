---
title: "classDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classdefinition.html"
content_id: "k~Sskyc3kW6m8Xke908UQg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:11.798991+00:00"
---

# classDefinition

Describes a Java `class`, `interface`, `enum`, or code annotation.

## Properties

`classDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `annotations` | `list<codeAnnotation>` | Any annotations specified for this class |
| `declaredType` | `classType` | The type of the class |
| `fieldList` | `list<fieldSymbol>` | A list of the symbols for each non-static field in the class |
| `location` | `sourceloc` | The location of this class in the source code |
| `memberFunctionList` | `list<functionSymbol>` | A list of the symbols for each non-static member function |
| `parentList` | `list<classParent>` | A list of parent classes |
| `staticFieldList` | `list<staticVariableSymbol>` | A list of the symbols for each static field in the class |
| `staticMemberFunctionList` | `list<functionSymbol>` | A list of the symbols for each static member function |
| `findBaseClass` | `function<testType>` | A function that invokes a callback function, which can be used as a predicate to find a particular base class—in other words, to test whether the class is a parent of the current class. See The base class properties. |
| `findMatchingBaseClass` | `function<testType>` | A function that invokes a pattern, which can be used as a predicate to find a particular base class—in other words, to test whether the class is a parent of the current class. See The base class properties. |
