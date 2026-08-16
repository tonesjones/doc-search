---
title: "Java iterator primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-iterator-primitives.html"
content_id: "5ugXgo2HbNg5VB_qi6g43g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:07.203076+00:00"
---

# Java iterator primitives

These primitives model the behavior of iterators.

## `void model_iterable_mutate( java.lang.Object iterable )`

The `iterable` value is an *iterator*, or any object that can return an iterator, that is being modified in such a way
as to be incompatible with subsequent uses of any iterator instances that have already be obtained from this iterator.

## `void model_iterable_union( java.lang.Object to, java.lang.Object from )`

Marks `to` as being equivalent to `from`.
Put another way, iterators associated with `from` are also associated with `to`.
This allows for classes like `Map` to have any *iterators* returned from `Map.keySet` and `Map.entrySet`
tracked as iterators associated with the original `Map`.

## `void model_iterator_return( java.lang.Object iterator, java.lang.Object iterable )`

The first parameter, `iterator`. is an *iterator* being returned from the second parameter, `iterable`.

## `void model_iterator_use( java.lang.Object iterator )`

The parameter, `iterator`, is an *iterator* that is being used in a way that will fail if the *iterable* from which it came
has changed in such a way as to invalidate this *iterator*.

## `void model_map_put( java.lang.Object map )`

The parameter `map` is a `Map` (or similar object) that is being modified by an operation such as `Map.put`,
which doesn't necessarily invalidate iteration if the key is already present.
