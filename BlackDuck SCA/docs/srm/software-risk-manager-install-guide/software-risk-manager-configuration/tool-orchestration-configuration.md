---
title: "Tool Orchestration Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/tool-orchestration-configuration.html"
content_id: "tsD7RqQnesA~1q1jmZZA0w"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:34.250477+00:00"
content_hash: "494e243d92ea8099dde4c1b32f78e4c4fce53e899d44ce78d5587dc49e643233"
---

# Tool Orchestration Configuration

When Software Risk Manager is deployed on a Kubernetes cluster, you can run orchestrated
analyses using the Software Risk Manager Tool Orchestration. If you have a
Software Risk Manager license that includes Tool Orchestration, enable the feature when
you run the [Helm Prep Wizard](https://github.com/codedx/srm-k8s).

## Analysis Cleanup

By default, Software Risk Manager will remove old analyses and related storage from
the tool service automatically. You can customize or disable this behavior with the
following options in the `codedx.props` file:

- `tws.storage.cleanup.enabled = true` - sets whether to enable
  automatic analysis cleanup [default: true].
- `tws.storage.cleanup.max-total-analyses = 100` - sets the
  maximum number of orchestrated analyses to keep; further analyses will cause
  the oldest to be deleted [default: 100].
- `tws.storage.cleanup.max-analyses-per-project = 5` - sets the
  maximum number of orchestrated analyses to keep *per-project*; further
  analyses will cause the oldest in the project to be deleted [default:
  5].

Note: Both successful and failed analyses count toward the "total" being
tracked.
