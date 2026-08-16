---
title: "Store overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/store-overview.html"
content_id: "N9yxJS8cdATZjLsy99F1pQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:35.785046+00:00"
---

# Store overview

The store is the primary data structure for a flow-sensitive checker (a flow-insensitive
checker has no store). It is an approximation of a set of states that a real, running
program might be in. As the checker walks over the program's abstract syntax tree (one
function at a time), it simulates the program's behavior by changing the store in
response to program operations such as assignments and function calls.

The store is a map from abstract syntax trees denoting expressions (*AST nodes*) to
a pair consisting of an integer and an event sequence:

```
store : tree -> (int, event[])
```

The integer part of a mapping value is an *abstract value*. Whereas a real program
(typically) has an infinite state space of *concrete values*, a checker reduces
these down to a finite number of abstract values so that the checker can terminate. Much
of the art of checker design is in choosing the set of abstract values. Although the
examples in this manual are meant to suggest basic approaches, there are no hard and
fast rules about abstract domain design, so some experimentation is required.

The event sequence part of the mapping value is for defect reporting purposes. It
summarizes the sequence of abstract state transitions that have occurred for the mapped
expression, so that a user viewing the report can understand what the checker did when
it arrived at some conclusion. Note that an expression must be mapped to some abstract
value before events can be attached to it.

The Extend SDK API provides several macros for querying and manipulating the store, as
documented in the following sections.

For a detailed example of using the store, see Example: tracking the sign of expressions.
