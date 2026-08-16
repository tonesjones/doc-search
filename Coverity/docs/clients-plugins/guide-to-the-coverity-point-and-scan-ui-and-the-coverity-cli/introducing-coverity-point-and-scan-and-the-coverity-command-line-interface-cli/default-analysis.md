---
title: "Default analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/default-analysis.html"
content_id: "2riyLExw2GDvGmcrhPhoww"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:45.277270+00:00"
---

# Default analysis

The Point and Scan UI and the Coverity CLI run the analysis with a set of
analysis options that is based on what was captured. By default, the Coverity CLI unconditionally passes the following option to
`cov-analyze`:

- `--recommended-security-checkers`

Note: If any checker configuration or custom analysis arguments are specified in the
configuration file, then this option will not be passed to `cov-analyze`.

For more information, see Checker configuration
and Web app security configuration.
