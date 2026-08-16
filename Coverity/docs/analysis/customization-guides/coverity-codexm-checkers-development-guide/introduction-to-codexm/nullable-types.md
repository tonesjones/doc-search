---
title: "Nullable types"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullable-types.html"
content_id: "kUnrnvCW01UosKY0YRNZgg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:32.605632+00:00"
---

# Nullable types

The type of certain pattern properties is said to be *nullable*.
This means that the property might return a value, or it might not.

If a property does not return a value, its value matches the CodeXM keyword `null`.
In this document, a nullable type is indicated by the name of the type the property *might* return,
followed by a question mark; for example, `int?`.

In checker code, a nullable type requires some special handling in order to avoid the error of
referencing the `null`.
The Handling null values section describes how to do this.
