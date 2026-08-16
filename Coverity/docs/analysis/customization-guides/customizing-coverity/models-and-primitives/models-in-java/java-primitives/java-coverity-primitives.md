---
title: "Java Coverity primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-coverity-primitives.html"
content_id: "TQEokMgGq~4viPtIT308qQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:05.560694+00:00"
---

# Java Coverity primitives

These primitives have to do with Coverity modeling in general.

## `void escape( java.lang.Object o )`

Indicates that the value of the parameter `o` might or might not flow to and be used in other parts of the program.

## `void killpath()`

Kills a path. You can use this to mark methods that exit the Java Virtual Machine (JVM)ߝfor example, `System.exit()`—or to explicitly mark infeasible paths.

## `boolean nondet()`

Models a nondeterministic choice in the analysis.
Checkers will explore both paths of the branch, making no assumptions about the conditional.

## `<T> T unknown()`

Models an unknown value of any type `T`.
The analysis will treat the return value as it would the return value from an unknown, unimplemented, or native method.
