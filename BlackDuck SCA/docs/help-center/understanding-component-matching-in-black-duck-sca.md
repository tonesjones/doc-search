---
title: "Understanding component matching in Black Duck SCA"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/understanding-component-matching-in-black-duck-sca.html"
content_id: "xGu6qWj2Q~t~yHgI~Rt9zA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:13.335869+00:00"
---

# Understanding component matching in Black Duck SCA

Black Duck SCA uses sophisticated matching techniques to identify
components in your codebase. As customers increasingly use package manager-produced
SBOMs and other scanning methods, understanding how Black Duck
identifies and matches components becomes essential. This document explains our fuzzy
matching and match correlation capabilities, providing clarity on how components are
identified during package manager and SBOM import scans.

## Component Identification Process

Black Duck SCA employs a multi-layered approach to component
identification:

1. **Exact Matching**: First, we attempt to find an exact match for components
   based on their package URL (PURL) or other identifiers.
2. **Fuzzy Matching**: When exact matches aren't found, we employ fuzzy matching
   techniques to identify similar components.
3. **Match Correlation**: For scans using multiple techniques, we use match
   correlation to consolidate and improve results.

## Package URL (PURL) Matching Elements

Package URLs (PURLs) contain several elements that Black Duck
uses for matching. Below is a table showing which elements we consider mandatory for
accurate matching:

| PURL Element | Required for Matching | Notes |
| --- | --- | --- |
| Type | [image: image] | Package manager type (npm, maven, etc.) |
| Namespace | [image: image] | Organization or grouping |
| Name | [image: image] | Component name |
| Version | [image: image] | Component version |
| Architecture | [image: image] | Optional but considered when available |
| Epoch | [image: image] | Optional but considered when available |
| Qualifiers | [image: image] | Optional but considered when available |
| Subpaths | [image: image] | Optional but considered when available |

For detailed PURL specifications, refer to the [official PURL specification](https://github.com/package-url/purl-spec/tree/main).

## Fuzzy Matching Process

When exact matches aren't found during package manager or SBOM import scans, Black Duck employs fuzzy matching through the following
process:

1. **Component Name and Version Analysis**: We analyze variations of component
   names and versions.
2. **Namespace Flexibility**: We consider potential variations in
   namespaces.
3. **Version Normalization**: Version strings are normalized to account for
   different versioning formats.
4. **Knowledge Base Comparison**: The processed information is compared against
   our Knowledge Base to find the closest match.

For example, if an exact match for "org.example:library:1.0.0" isn't found, our fuzzy
matching might identify "org.example:library:1.0" or "org.example.library:1.0.0" as
potential matches.

## Match Correlation vs. Fuzzy Matching

It's important to understand the difference between these two techniques:

- **Fuzzy Matching**: Applies to a single scan type, looking for approximate
  matches when exact matches aren't found.
- **Match Correlation**: Combines results from multiple scan techniques (e.g.,
  signature scan and package manager scan) to provide more accurate
  identification.

To enable match correlation when using Detect, use the
`--detect.blackduck.correlated.scanning.enabled=true` option.

## Architectural Components Involved

The matching process involves several architectural components:

- **Knowledge Base (KB)**: Contains the comprehensive component information
  used for matching.
- **Match as a Service (MaaS)**: Handles the complex matching algorithms.
- **SCA Scan Service (SCASS)**: Coordinates scanning and initial
  processing.

Note: Fuzzy matching and match correlation features are not currently supported for
air-gapped (KB on-premise) installations.

## Ongoing Improvements

Component matching is an area of active development at Black Duck. We continuously refine our algorithms and processes to improve match accuracy.
We welcome customer feedback on matching results.

If you have questions about specific fuzzy or correlated matches, please submit a
support case through the standard process. Your feedback helps us improve our
matching capabilities.
