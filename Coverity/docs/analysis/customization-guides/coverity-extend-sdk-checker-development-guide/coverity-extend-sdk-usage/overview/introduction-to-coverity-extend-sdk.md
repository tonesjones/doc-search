---
title: "Introduction to Coverity Extend SDK"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introduction-to-coverity-extend-sdk.html"
content_id: "v1No~xwNYKNx~BmeW7PS0w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:20.412909+00:00"
---

# Introduction to Coverity Extend SDK

Coverity Extend SDK is a framework for writing program analyzers (that is,
*checkers*) in C++ that support analyses of C/C++, Java, and C# applications.
Much of this framework is the same as that used by the checkers in Coverity
Analysis. The framework provides the following services:

- Basic front-end features: parsing, type checking and elaboration, abstract syntax
  construction, template instantiation, and linking across translation units.
- Facilities to inspect abstract syntax, using pattern matching.
- Mechanisms to traverse paths in the abstract syntax in execution order, prune
  false paths, and merge similar states to ensure termination in loops.
- Flexible checker state management for derivation of flow-sensitive
  properties.
- Output routines that work with the false path pruning (FPP) mechanism to ensure
  that defects are only reported in feasible paths.

What you must write is a description of a *state machine*, also known as an abstract
interpreter. This description specifies how the state transitions occur and which states
constitute errors. The Coverity Extend SDK framework then runs this state
machine over each function in the code that is undergoing analysis, collects the defect
(issue) reports (those produced in error states), and allows you to commit the reports
to Coverity Connect, where developers can learn about and triage the
issues.

Note: CodeXM is a language specifically designed for writing new checkers. If you have not already
invested in the Extend SDK, we strongly recommend you use CodeXM rather than the
mechanisms described in this manual. See Coverity
CodeXM Checkers Development Guide.
