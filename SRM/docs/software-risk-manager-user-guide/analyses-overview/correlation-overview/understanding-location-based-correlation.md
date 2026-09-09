---
title: "Understanding Location-based Correlation"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/understanding-location-based-correlation.html"
content_id: "jIDapoXTXHdzOmoVfTTNJA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:56.915563+00:00"
content_hash: "40cedcde318305db02a435614424ca5b444a9e11c57d5140d71a2cdcb25ef7b6"
---

# Understanding Location-based Correlation

Location data is essential for correlation. Results that have the same location type and
value might be candidates for correlation, depending on the location type.

Location types are as follows:

- File, Logical paths: Line ranges must at least overlap. Results without a line
  range will only be correlated with other results without a line range, and
  vice-versa. Column ranges are ignored.
- URL paths: The "Element" for both results must match exactly. An "Element"
  refers to the type and name of the part of the request that was indicated as
  vulnerable. If a result indicates that the query parameter "user" is vulnerable,
  that result will only correlate with other results with an Element of "Query
  Parameter ('user')".
