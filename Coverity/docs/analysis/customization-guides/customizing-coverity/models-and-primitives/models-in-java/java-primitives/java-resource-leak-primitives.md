---
title: "Java resource-leak primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-resource-leak-primitives.html"
content_id: "LaMpsxqfK3pQTcGt9jtxUg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:01.979669+00:00"
---

# Java resource-leak primitives

These primitives deal chiefly with allocating and releasing memory.

## `void alias( java.lang.Object to, java.lang.Object from )`

Indicates that `to` refers to the same resource as `from`.
In other words, after calling this method, closing `to` is sufficient to close `from`.

## `void close( java.lang.Object o )`

Indicates that if `o` is a resource, it no longer needs closing.
Calls to this primitive are typically inserted in code where closing of the resource is handled.

## `void open( java.lang.Object o )`

Marks `o` as containing an allocated database connection that needs to be closed.

## `void open_db( java.lang.Object o )`

Marks `o` as containing an allocated resource that needs to be closed.
