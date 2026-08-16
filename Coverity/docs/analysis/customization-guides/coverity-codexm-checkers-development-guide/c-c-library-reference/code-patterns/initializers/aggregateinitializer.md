---
title: "aggregateInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aggregateinitializer.html"
content_id: "4n~Gn3cA8gzsgX2HqwVTdw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:55.401538+00:00"
---

# aggregateInitializer

Matches expressions used to initialize aggregate types such as structs or arrays.

## Properties

`aggregateInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `hasExplicitBraces` | `bool` | Whether the initializer is enclosed by braces ( `{}` ) in the source |
| `semanticIinitializerList` | `list<initializer>` | The list of initializers used to initialize the subobjects of the aggregate type |
| `syntacticInitializerList` | `list<initializer>` | The list of initializers used to initialize the subobjects of the aggregate type (at the syntactic level of a source program) |
| `tailInitializer` | `initializer?` | A tail initializer used to initialize the remaining objects of an aggregate, if one exists; `null` if there is no tail initializer |

**Inherits properties from:**

- astnode
- initializer

## Example

The following target source code matches `aggregateInitializer`:

  
 [image: C/C++ code follows]   

```
int x[3] = {1, 2};
```

Both `.semanticIinitializerList` and `.syntacticIinitializerListz`
contain two elements, which are
`expressionInitializer { .expression == intLiteral }`.
(In most cases no semantic and syntactic initializers are similar.)
The `.tailInitializer` is a zero initializer,
indicating the initializer that the compiler provides to fill out the initialization.

A similar aggregate initializer of a `struct` in target source:

  
 [image: C/C++ code follows]   

```
struct T {
    int x;
    int y;
}
T t { 2, 1, 3};
```

This following CodeXM pattern matches an aggregate initializer with exactly three elements:

  
 [image: CXM code follows]   

```
    pattern has3Initializers {
        aggregateInitializer as i 
            where i.syntacticInitializerList.length == 3
    };
```
