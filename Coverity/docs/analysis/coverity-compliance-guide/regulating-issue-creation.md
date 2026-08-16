---
title: "Regulating issue creation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regulating-issue-creation.html"
content_id: "7cVrvrxyU3WZ8pGRs8TCFQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:41.402650+00:00"
---

# Regulating issue creation

Regulating issue creation is the process where you decide which findings to persist as
issues and how to prioritize those issues. You regulate issue creation using filtering
policies.

A filtering policy operates on all findings that match a specified two-part pattern, for
example, the set of findings located in the path src/main/c/lib
whose compliance type is defined by "MISRA C 2012".

Notice that the pattern consists of two sub-patterns, a Path Pattern and a Compliance
Pattern. The Path Pattern (src/main/c/lib, in our example)
specifies which findings the policy operates on according to the location of the source
files that contain the findings. The Compliance Pattern ("MISRA C 2012", in our example)
specifies which findings the policy operates on according to the compliance type of the
findings.

A filtering policy can have one or both of its sub-patterns specified. An unspecified
sub-pattern matches all findings. A filtering policy matches a finding only if both its
sub-patterns match the finding.

Note: Both the Path Pattern and Compliance Pattern are recursive. In other words, the set of
findings located in the path src/main/c/lib includes all findings
within all files in the lib directory and all its subdirectories.
In the same way, the set of findings whose compliance type is defined by MISRA C 2012
includes all findings whose compliance type is in the MISRA C 2012 standard. These
patterns can be more specific than those provided in the examples. For example, the Path
Pattern could specify a specific source code file. Likewise, the Compliance Pattern
could specify a specific rule or directive.

The filtering policy operates on findings by either including them or excluding them.
Included findings are persisted as issues on commit; excluded findings are not
persisted.

Coverity Compliance Filtering provides two types of filtering policies:

- **Blocking policies –** use these to exclude findings that are unimportant and
  that should be ignored (such as findings in third-party or generated code).
- **Scoring policies –** use these to score findings according to their level of
  priority (findings with a higher score are deemed higher priority). Findings
  whose score meets the threshold setting are persisted as issues; those below the
  threshold are excluded. You can view issue scores in Coverity Connect.

If a finding matches both a blocking and scoring policy, the blocking policy takes
precedence.
