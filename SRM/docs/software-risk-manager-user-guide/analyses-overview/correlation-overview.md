---
title: "Correlation Overview"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/correlation-overview.html"
content_id: "LOwf~~7xnx9CF2dY5ANsMA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:55.128100+00:00"
content_hash: "6e6b5439eccaa5332fdb23f1853e3049b7a86d94d6832b8f13d403fb4f5ed508"
---

# Correlation Overview

Correlation is the process Software Risk Manager uses to evaluate data returned by any
combination of supported AppSec tools to determine which, if any, of the
results reported by the various tools refers to the same issue. When
matching results are found, Software Risk Manager correlates those results and creates a
single finding for that issue. Software Risk Manager does this by looking at the data
provided for each result; although, in some cases, the correlation process
will factor in the detection method as well (e.g., Static vs. Dynamic
results).

Correlation involves various processes that check for data within results that
would suggest whether results should be correlated. The output is a
per-result set of associations, where each association indicates whether to
allow or deny correlation. At the end of this process, the correlation
decisions for all results are used to determine which results have enough
evidence to be grouped into the same finding. (For more information, see
Analysis Correlation Options.)

The correlation process includes the following elements:

- Rule Sets
- Data
  Normalization
- Location-based Correlation
- Component
  Correlation
- Hybrid
  Correlation
- InfraSec
  Correlation
- Location-less Correlation
