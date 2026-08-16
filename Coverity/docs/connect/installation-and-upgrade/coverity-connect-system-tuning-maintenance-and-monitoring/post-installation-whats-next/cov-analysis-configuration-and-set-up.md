---
title: "cov-analysis configuration and set-up"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cov-analysis-configuration-and-set-up.html"
content_id: "~CKtBLshCgSLZH~r1ft6yw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:09.467068+00:00"
---

# cov-analysis configuration and set-up

The tasks mentioned below are described in full in the Coverity Analysis 2026.6.0 User and Administrator Guide.

*Generate a compiler configuration*
:   Before running your first code analysis, you typically generate a configuration
    of your native compiler.

*Enable analysis checkers*
:   Coverity runs checkers that detect specific types of issues in your source code.
    For example, the RESOURCE_LEAK checker finds many types of
    resource leaks from variables that go out of scope while "owning" a resource,
    such as freshly allocated memory. Checkers are classified by language and
    grouped by the types of problems that they detect.

*Create custom models to improve analysis results*
:   A custom model is a piece of source code that is written by a developer to
    replace the actual implementation of a function or method. Custom models can
    lead to a more accurate analysis by helping Coverity find more issues and
    eliminate false positive results.
