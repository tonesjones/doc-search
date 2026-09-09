---
title: "Project Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/project-configuration.html"
content_id: "nKMoGgqkUtd81NDDpzCi0A"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:43.025397+00:00"
content_hash: "b483c9d549a5b8135958d9fa3552160953bcebb88fa941e1aa16dea4bb743725"
---

# Project Configuration

The following properties can be used to configure Software Risk Manager project behavior:

- `project.default-branch-name` [default: 'main'] - The name to use for
  the default branch when creating new projects.
- `project.scan-coverage.include-parent-projects` [default: false] - Decides
  whether or not to include child projects which are also parent projects in the
  scan coverage calculation.
