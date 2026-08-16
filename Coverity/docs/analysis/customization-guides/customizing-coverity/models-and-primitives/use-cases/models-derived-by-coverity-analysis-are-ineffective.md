---
title: "Models derived by Coverity Analysis are ineffective"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-derived-by-coverity-analysis-are-ineffective.html"
content_id: "mKyCZLRMjGhVjgu4ndn6CQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:27.213919+00:00"
---

# Models derived by Coverity Analysis are ineffective

Sometimes a model that Coverity Analysis derives is not correct.
This can cause false positive reports.

A model that Coverity Analysis derives might diverge from the actual
behavior of the original function. Usually this happens because of the complexity of the
modeled function: There is a limit to the precision of compile-time analysis. In cases
like this you can improve the accuracy of analysis, and reduce the number of false
positives, by replacing the derived model with a custom model that more accurately
describes the behavior of the function.
