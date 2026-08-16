---
title: "Terminology"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/terminology.html"
content_id: "fSUFYkAWpV0sSfvX18whew"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:31.628977+00:00"
---

# Terminology

issue
:   A uniquely identifiable software problem found by Coverity Static Analysis. This
    corresponds to the `MergedDefect` concept in the SOAP API. Triage
    records are attached to issues.

issue occurrence
:   An instance of an issue. Each issue has one or more issue occurrences. An issue
    occurrence corresponds to the `DefectInstance` concept in the
    SOAP API, and the "defect occurrence" concept in Coverity Static Analysis.

key
:   A parameter that identifies which of several items in a collection is to be
    used. The value is usually stable, in the sense that it does not vary among
    Connect instances or across time. A column key is a key identifying a column,
    for example. Further, column key "cid" identifies the column whose value is a
    Coverity CID.

standard attribute
:   An attribute that associates a standard with an issue type. These appear on the
    **Standard Attributes** panel of the Coverity Connect GUI.

    *Built-in
    standard attributes* are those provided in a default Coverity Connect
    installation. *Custom standard attributes* are those configured after
    installation.

triage attribute
:   An attribute that associates a value with an issue. These can be displayed on
    the **Triage** panel of the Coverity Connect GUI.

    *Built-in triage
    attributes* are those provided in a default Coverity Connect
    installation. *Custom triage attributes* are those configured after
    installation.
