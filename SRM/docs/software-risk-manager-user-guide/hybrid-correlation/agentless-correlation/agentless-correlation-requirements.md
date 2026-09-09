---
title: "Agentless Correlation Requirements"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/agentless-correlation-requirements.html"
content_id: "nprwukXQ80VZNfY9qU6Xfg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:35.868785+00:00"
content_hash: "17a840f3333e415b5e5f5d465e73491ada63ace412bb3ea141d9f3df1b4856ff"
---

# Agentless Correlation Requirements

If Hybrid Correlation is enabled, Agentless Correlation is automatically applied for any
project with correlation enabled and with uploaded source code.

## Source Code

Agentless Correlation relies on the availability of source code to detect endpoints
and their locations within a codebase. From this alone, DAST and SAST results that
occur at an endpoint handling function can be correlated.

Only source code declaring and implementing endpoints are required. Source code for
dependencies and utility libraries are not necessary, unless they declare and
implement endpoints.

Endpoint detection is supported for a specific set of languages and web frameworks.
These are as follows:

- **Java**: JSPs, Servlets, Struts, Spring MVC
- **C#**: ASP.NET MVC, Web Forms
- **Ruby**: Rails
- **Python**: Django

Effectiveness of endpoint detection can vary depending on the use of plugins and
unconventional endpoint routing methods within the source code.

## Binaries

Binaries for your application can also be uploaded to improve Agentless Correlation.
If binaries are available, a call graph can be generated and explored to find code
paths to SASTs from a detected endpoint. All relevant binaries for your
application—the compiled application and its dependencies—should be uploaded with
debug symbols for the best results.

Hybrid Correlation through call graph analysis is supported for binaries on the
following runtime environments:

- JVM (Java, etc.)
- CLR (C#, etc.)
