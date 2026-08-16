---
title: "Tool error detection"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tool-error-detection.html"
content_id: "ZbNWTdqkLTwBrSTFwFLRlw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:40.098434+00:00"
---

# Tool error detection

As in the case of all static code analysis tools, Coverity might report *False
Positives*, which are issues that are not actual errors in the context of the
relevant code. In addition, the tool might be subject to *False Negatives*, which
are undiscovered, and therefore unreported, issues that are present in the code.

- The degree of confidence that a False Positive can be identified by the user is
  high (TD1).
- The degree of confidence that a False Negative can be identified by the user is
  low (TD3).

Examples of False Negatives are discussed in various sections of Customizing Coverity, such as in "Primitives for
modeling sources of untrusted (tainted) data" and "Model for methods to which
tainted data must not flow (sinks)".
