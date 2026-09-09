---
title: "Understanding Data Normalization"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/understanding-data-normalization.html"
content_id: "Syz_z_ikO8wDWgEMUsx4SQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:56.315139+00:00"
content_hash: "a7a3ab5851fb1d0224165014303fd0e3b4d742e75f472562c9d700c2d758c0df"
---

# Understanding Data Normalization

In broad terms, data normalization can be understood as the process of ordering,
structuring, and simplifying the reported data that makes up a result. The purpose is to
make it easier to determine if different data points refer to the same item. In other
words, the correlation process does not evaluate the raw data provided by a result;
instead, the evaluation is based on a normalized representation of that data.

Data that is displayed on the Findings page is the normalized representation of the
available data. To view the raw data, you can open the specific finding and inspect the
results attached to it.

Software Risk Manager performs the following normalizations:

- File paths*
- URL paths: Query parameters and anchors are stripped from URLs.*
- Component info: Component (package) names and versions are collected and stored
  as-is. CPE strings and certain package format strings (e.g., maven, npm) are
  parsed to collect this information, if available.
- Hosts: IP addresses, FQDNs, MAC addresses, NetBIOS names, and hostnames are
  collected when available, and the existence of a result that ties any of these
  values will lead to the values being associated as the same host. (For example,
  if a single result reports a vulnerability and specified
  `10.0.0.9` and `PRODENV` hostname, these two
  identifiers would be combined to the same normalized host.)

* Normalization involving paths will compare the structure of the available paths to
discover overlaps and determine the correct location of a file with respect to the known
structure. If a user uploads source code, the paths from the source code are used as the
normalized path. If the source code isn't uploaded, the normalized path becomes the most
specific path shared by all of the paths. For example, the paths
`src/main/test.java` and `main/test.java` would be
normalized to the same, most-specific path, which is `main/test.java`,
because `src/` is not shared between them. Base paths that are common
across all inputs may be stripped.
