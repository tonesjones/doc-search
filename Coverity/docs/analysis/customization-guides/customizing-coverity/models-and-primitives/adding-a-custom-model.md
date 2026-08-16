---
title: "Adding a custom model"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-custom-model.html"
content_id: "O3VsJ_Z4UU7qfNl~AQ2KDw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:27.896217+00:00"
---

# Adding a custom model

A model file is a set of function stubs that is written in the target language. Each
stub is a *model* that indicates how the model behaves, and that might invoke
*modeling primitives* as instructions to the analysis engine.

When you have written the model source, you use the
`cov-make-library` command to create a model library file.

1. Create a new target-language source file.
2. Add one or more stub functions.

   Each function stub is the basis of a single model.
3. Complete each model by writing source code, possibly using modeling primitives
   to instruct Coverity how to treat the model during analysis.

   CAUTION:

   A model can use the numeric comparison operators, `<`, `<=`, `==`, `!=`,
   `>=`, and `>`, but models do not recognize arithmetic operators (for example, `+` and `-`)
   or bitwise operators (for example, `<<` and `>>`).
4. Invoke `cov-make-library` to compile the model into a user model library.

   Use `--model-file` to specify the custom model library source,
   and `--output-file` to specify the resulting library.
