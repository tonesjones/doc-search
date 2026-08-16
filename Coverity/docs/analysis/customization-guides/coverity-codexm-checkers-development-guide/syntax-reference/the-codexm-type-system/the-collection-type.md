---
title: "The collection-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-collection-type.html"
content_id: "ACCrR8wn_GWw5_NJgPU3HQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:01.004439+00:00"
---

# The collection-type

A `collection-type` object can be either a
`set` or a `list`.

All members of a `set` or a `list` share the same base type.

## Syntax

  
 [image: Syntax diagram, collection-type]   

```
collection-type ::=
    ( 'set' | 'list' )
    '<' non-nullable-type '>'
```

The `non-nullable-type` is the base type of the collection.
As the EBNF name implies, it cannot be nullable: See The nullable-type.

## Details

The members of a `set` or a `list`
do not need to be unique (for sets, this is different from the usual mathematical stipulation).

The main difference between a
`set` and a `list`
is that the members of a `list` have a particular order,
while the members of a `set` do not.
This difference does have implications for the way these two types of collections behave, as the following points explain:

- You can use a `list` anywhere you might use a
  `set`, but the reverse is not true.
- With a `list`, you can use an
  element-access-expression (which works like an index to an array)
  to specify particular member items;
  for example, `myList[3]`.

## Properties

A few properties apply to sets, to lists, or to both.

`.contains` (sets and lists)
:   Specifies a single parameter, `item`.
    Returns `true` or `false`,
    depending on whether the set or list contains the specified item.

    For a set, `item` can be either a literal value, or a pattern.
    If `item` is a literal, then
    `contains()` simply uses the equals operator
    ( `==` ) to make the comparison;
    otherwise, it uses the `matches` operator.
    See The matches-expression.

`.empty` (sets and lists)
:   Returns `true` if the set or list is empty,
    `false` if the collection contains members.

`.length` (lists only)
:   Returns the length of the list.

`.sub` (lists only)
:   The `.sub` property specifies two parameters,
    `start-index` and `sub-length`.
    It returns a subset of the list, beginning with the item specified by `start-index` and containing
    `sub-length` elements.

    - The `start-index` is zero-based.
    - If `start-index` is less than zero
      or greater than the length of the list, the result is an empty list.
    - If there are fewer than `sub-length` elements in
      the specified range, the list returned is truncated to those elements that
      are available.
    - If `sub-length` is less than zero, `.sub`
      returns a sublist that begins at `start-index` and ends at `sampleList.length+sub-length`.
      For example, `sampleList.sub(0, -1)` returns `sampleList` with its last element removed.
      If the result of a negative `sub-length` would equal or be less than
      `start-index`, the result is an empty list.

    Here are some examples of using `.sub`:

    `[0, 1, 2].sub(1, 2)` returns `[1, 2]`.

    `[0, 1, 2].sub(1, 4)` returns `[1, 2]`.

    `[0, 1, 2].sub(1,1)` returns `[1]`.

    `[0, 1, 2].sub(0, -1)` returns `[0, 1]`.

    `[0, 1, 2, 3].sub(1, -1)` returns `[1, 2]`.

    `[0, 1, 2, 3].sub(1, -4)` returns `[]`.

    `[0, 1, 2].sub(-1, 2)` returns `[]`.
