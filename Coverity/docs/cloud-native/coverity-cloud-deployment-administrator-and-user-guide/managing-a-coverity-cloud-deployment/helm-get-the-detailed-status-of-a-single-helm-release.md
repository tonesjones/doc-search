---
title: "Helm - get the detailed status of a single Helm release"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/helm-get-the-detailed-status-of-a-single-helm-release.html"
content_id: "5LLIwXL5jXrb6lF1BL27dA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:19.349291+00:00"
---

# Helm - get the detailed status of a single Helm release

Using the following command, inspect the YAML file to determine whether it matches
expectations.

```
helm status -n "$NS" "$RELEASE" -o yaml
```
