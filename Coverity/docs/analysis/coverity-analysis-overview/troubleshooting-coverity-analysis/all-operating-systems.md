---
title: "All operating systems"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/all-operating-systems.html"
content_id: "y5vyQdmx9Mg4RaUMCo6WCQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:30.973033+00:00"
---

# All operating systems

You might encounter the following issues if you use Coverity Analysis on all operating
systems.

`http_proxy`, `https_proxy`, and `no_proxy` environment variables
:   Analysis may fail or return inaccurate results when run on networks using HTTP client
    proxies. Specifically, issues are known to arise when the
    `http_proxy` or `https_proxy` environment
    variable is a machine name rather than an IP address, or when there are
    wildcards in the `no_proxy` environment variable.
