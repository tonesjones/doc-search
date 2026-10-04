---
title: "Modeling primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/modeling-primitives.html"
content_id: "Bb13HdovDFR7fWbCQP_AkA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:03.672160+00:00"
---

# Modeling primitives

A model can employ either existing library functions or *modeling primitives*.
Each language that supports modeling has its own set of primitives to use.

Each primitive implements a single state transition or a single action within the analysis.
Because of this, the effect of a primitive is independent of any other primitive.
The list of modeling primitives for a particular language (or set of languages) represents
the scope of behaviors that a static analysis can understand.
