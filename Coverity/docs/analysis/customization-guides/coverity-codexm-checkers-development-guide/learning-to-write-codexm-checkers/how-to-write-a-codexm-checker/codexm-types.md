---
title: "CodeXM types"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/codexm-types.html"
content_id: "N~A5LGjK~8K8LT2h8qPjrQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:45.555403+00:00"
---

# CodeXM types

Like many programming languages, CodeXM is strongly typed.
The types that the CodeXM language supports, such as integers (`int`) or strings (`string`), are likely to be familiar to you.

In many cases, however, when you declare a variable you don't need to use the name of the type: The type is inferred from the declaration syntax.
For example, the following code snippet shows implicit typing:

[image: CXM code follows]

```
    let i = 5;
```

... In this example, `i` is clearly an integer whose value is 5, so it has the type `int`.

You *can* specify a type explicitly. To do so, use a colon ( `:` ), as shown in the following code snippet:

[image: CXM code follows]

```
    let s  : string = "foo"  in
        // Some logic that expects a string named s
```

Types are described fully in the Syntax reference. These are some of the widely used ones:

`bool`
:   A Boolean whose value is either `true` or `false`.

`int`
:   An integer value; can be positive or zero.
    (CodeXM treats a minus sign ( `-` ) as applying a negation operation to a positive integer.)

`string`
:   A sequence of characters. A string literal is enclosed in double quotes; for example, `"orange"`.

`list<type>`
:   An ordered collection of values; for example, `let myList = list [ 1, 2, 4 ];`.
    The values in a list must all be of the same type.

    You can access a particular list element by using an array subscript operator;
    for example, `myList[0]` designates the first element in `myList`. Lists are indexed starting from zero.

    A list also has a `.length` property that holds the number of elements in that list.
    For example, `myList.length` equals 3.

`set<type>`
:   Similar to a list, but the elements are not ordered. (Because of this, they can't be indexed.)

    Unlike the mathematical notion of a set, a CodeXM set can have duplicate entries.

`enum<literal>`
:   An unordered collection of literal identifiers; for example, `` let myDecision = { `yes`, `no`, `maybe` } ``.

    The literals in an `enum` are similar to strings: They can contain any characters, including white space, and are enclosed in back-ticks.
