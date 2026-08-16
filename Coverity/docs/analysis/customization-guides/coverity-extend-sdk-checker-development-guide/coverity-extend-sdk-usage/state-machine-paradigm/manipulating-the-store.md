---
title: "Manipulating the store"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/manipulating-the-store.html"
content_id: "TQ_ZqbehydQdIs7fUAeYcQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:35.558534+00:00"
---

# Manipulating the store

The store is a map from expressions to integer values:

```
store : expression -> integer
```

Some of the common functions that are used
to manipulate the map are described next. For a full listing, see The store.

## SET_STATE(t, v)

Map expression tree `t` to `v`. Any prior mapping is
removed.

## GET_STATE(t, v)

Retrieve the mapping for `t`. If it exists,
GET_STATE returns true and stores the value in
`v`. Otherwise, GET_STATE returns false and
`v` is undefined.

## MATCH_STATE(t, v)

Return true if `t` is mapped to `v`.

## CLEAR_STATE(t)

Remove any mapping for
`t`.

## COPY_STATE(dst, src)

First, `CLEAR_STATE(dst)`. Then, if `src` is mapped,
copy its mapping to `dst`.

## FOREACH_IN_STORE(t, v)

Using a loop, bind `t` and `v` to all of the
(`expression tree`, `value`) pairs in the store.
The bindings are retrieved in an undefined order. The store should not be modified
during the iteration.
