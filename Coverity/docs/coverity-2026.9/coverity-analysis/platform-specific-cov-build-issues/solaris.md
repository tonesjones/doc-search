---
title: "Solaris"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/solaris.html"
content_id: "VtC4XGR8c1wjnheRBVGcPw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:27.574101+00:00"
---

# Solaris

The `cov-build` command fails if the build command, such as
`make`, is a setuid executable. To run the
`cov-build` command, you can turn off the setuid bit with the
following command:

```
> chmod u-s path/build_command
```
