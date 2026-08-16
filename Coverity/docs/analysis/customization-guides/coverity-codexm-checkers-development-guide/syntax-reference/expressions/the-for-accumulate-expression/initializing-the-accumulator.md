---
title: "Initializing the accumulator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/initializing-the-accumulator.html"
content_id: "jgu6EDAFeH~WNzlQg48WkQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:31.774375+00:00"
---

# Initializing the accumulator

The value of `initial-expression` is typically the identity value for the accumulator's type.

- If the result of the loop (fold) operation is to be the sum of multiple additions, `initial-expression` will equal `0`.
- If the result is to come from a series of multiplicatIons, `initial-expression` will equal `1`.
- If the result is to be a set, `initial-expression` will equal the empty set, `[]`.
