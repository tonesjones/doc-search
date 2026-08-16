---
title: "Simple checker vs. checker with store"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/simple-checker-vs.-checker-with-store.html"
content_id: "B2NvBDRCSFogGANuB36DYw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:33.626924+00:00"
---

# Simple checker vs. checker with store

The `simple` checker type (where `simple` is the second
argument to `START_EXTEND_CHECKER`) is stateless. It is not sensitive to
the order in which it encounters AST fragments. In the program analysis literature this
is known as a *flow-insensitive analysis*.

In contrast, the `int_store` checker type is stateful. It has a
*store*, which is a map from ASTs to values. This map can be used to implement
an abstract interpreter, a concept explained in the next section. This is called
*flow-sensitive* analysis and is what makes the Extend SDK so powerful.
