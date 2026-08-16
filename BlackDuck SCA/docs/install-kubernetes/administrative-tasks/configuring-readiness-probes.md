---
title: "Configuring readiness probes"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-readiness-probes.html"
content_id: "_jDJgogmrXd7BxeN_l5uvg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:20.993699+00:00"
---

# Configuring readiness probes

You can enable or disable the readiness probes by editing the following boolean flags in
`values.yaml`:

```
enableLivenessProbe: true
enableReadinessProbe: true
enableStartupProbe: true
```
