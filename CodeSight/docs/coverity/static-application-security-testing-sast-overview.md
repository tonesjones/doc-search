---
title: "Static Application Security Testing (SAST) overview"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/static-application-security-testing-sast-overview.html"
content_id: "xYr3aVcuvxJP1uT5Qvug8g"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.596245+00:00"
---

# Static Application Security Testing (SAST) overview

*Static application security testing* (SAST), also known as *static analysis,*
scans source code to check for quality issues, which can cause code to fail when it is executed,
and for security issues, which can leave code vulnerable to attack.

Resolving the issues reported by an SAST scan will increase your confidence in the reliability and security
of the software that you publish.

Code Sight supports two different SAST engines:

- Rapid Scan Static performs rapid scanning locally.
- Coverity Analysis performs comprehensive and detailed scanning that can be
  synchronized with a server.

Static analysis is a set of techniques for testing program code without executing the program,
as opposed to *dynamic analysis,* which tests code while it is running. Because of the time involved, dynamic analysis
can test only a sampling of the possible paths of a program’s execution.

Figure 1. Dynamic analysis of an execution tree
  
 [image: Dynamic analysis of an execution tree]

A dynamic analysis of code typically focuses on a particular issue, and typically has to do with program security: stress testing, penetration testing,
fuzz testing, and so on.

Static analysis, by contrast, can search for various kinds of issues, and it computes all possible execution paths.

Figure 2. Static analysis of an execution tree
  
 [image: Static analysis of an execution tree]

The ability to search all paths in an execution tree is one of the strengths of static analysis.

In a production environment, we recommend you use static analysis as one component of an overall testing
strategy, and combine it with appropriate types of dynamic analysis, so that the resulting code is as
robust and secure as possible.
