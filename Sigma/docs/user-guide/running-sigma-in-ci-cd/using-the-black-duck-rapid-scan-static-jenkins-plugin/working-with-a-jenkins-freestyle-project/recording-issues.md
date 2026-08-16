---
title: "Recording Issues"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/recording-issues.html"
content_id: "kIdFo~6rCoKX~DgwQOcRSw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:22.026820+00:00"
---

# Recording Issues

To record issues using the Post Build Action, you must specify the `--format
jenkins` command line option to the analyze command. For
example:

```
--config config/sigma-config.yml --policy config/sigma-policy.yml analyze --format jenkins
```

If you use a different format option, the Warnings Next Generation plugin will not be
able to parse the results in the sigma-results.json file Sigma
produces.
