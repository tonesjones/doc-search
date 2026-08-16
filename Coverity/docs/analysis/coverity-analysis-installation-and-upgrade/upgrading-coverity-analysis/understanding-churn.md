---
title: "Understanding churn"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/understanding-churn.html"
content_id: "XA8k9ortHEW9sOQ21t8NJw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:19.230150+00:00"
---

# Understanding churn

Churn is a measure of change in defect reporting between two sequential Coverity Analysis
Feature releases (for example, 2017.07 and 2018.01).

For most programming languages, churn can be discovered through a two-step process:

1. Using the two Coverity Analysis releases to separately analyze the same code
   base.
2. Using Coverity Connect to triage the resulting CIDs into the following
   classifications: *False Positive* and *Bug*. Churn does not apply to the
   CIDs that have *Pending* or *Intentional* classifications.

**Churn formula:**

```
(New False Positives + Lost True Positives)/Total Number of CIDs
```

Note: Coverity expects the churn between contiguous Coverity Analysis releases to be less
than 5% for the following programming languages:

- C/C++
- C#
- Java
- JavaScript

- New False Positives (FPs): The number of CIDs that are reported by the more recent
  version of Coverity Analysis and that developers marked with an FP classification in
  Coverity Connect.
- Lost True Positives (TPs): The number of CIDs that are reported by the earlier
  version of Coverity Analysis and that developers marked with the Bug classification
  in Coverity Connect.
- Total Number of CIDs: The number of CIDs produced by the separate analyses. This
  total includes CIDs that are common to each version of Coverity Analysis and any
  unique CIDs from either version. Common CIDs are the result of defect merging in
  Coverity Connect.
