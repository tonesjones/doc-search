---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/examples.html"
content_id: "WDipwAhpBiLkMyhMq1ZuFg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:48.239526+00:00"
---

# Examples

Flag files with a line count greater than 1000:

```
> cov-count-lines --list l | awk '{if ($5 > 1000) print $0;}'
```

Report the line count for the Apache regcomp.c file:

```
> cov-count-lines --file /home/user/apache_1.3.33/src/regex/regcomp.c
```
