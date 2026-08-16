---
title: "Abstract interpretation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/abstract-interpretation.html"
content_id: "czGJeeF7LUV1E7ENWQHLcw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:34.274162+00:00"
---

# Abstract interpretation

Abstract interpretation is a general framework for doing program analysis. The core of
the analysis is an abstract store, which is a map from program variables to abstract
values. At one extreme, the abstract values could actually be concrete values, and then
we would have a real (concrete) interpreter. However, by abstracting the value space, we
enable the analysis of programs with loops or inputs. The choice of abstraction is
dictated by the property being checked.

For example, in an analysis that looks for occurrences of a call to fopen
and then a call to fclose, you might use the following rules:

- variable maps to 1 means fopen has been called
  but fclose has not.
- variable is unmapped (mapped to nothing) means either
  fopen has not been called, or else
  fclose has subsequently been called.

As another example, you might want to check that a negative value is never cast to
`unsigned`, and use a store with these rules:

- expression maps to 0 if it is negative.
- expression maps to 1 if it is negative or zero.
- expression maps to 2 if it is zero.
- expression maps to 3 if it is positive or zero.
- expression maps to 4 if it is positive.
- expression is unmapped if its sign is unknown

Note that these two examples not only use different abstract values (store ranges), but
they map *from* different constructs (variables vs. expressions, the store
domains). The choice of store domain is usually determined by concerns such as soundness
and completeness: a simple domain such as local variables will tend toward a sound
analysis (where a program bug implies a defect report), while a complex domain such as
expressions will tend towards a complete analysis (where a bug-free program implies no
defect report), though this characterization oversimplifies things.

In practice, it takes some experimentation to select a good store domain and range for
your particular properties of interest.
