---
title: "Conventions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/conventions.html"
content_id: "4F8efYwRgozalyyHuN1qaA"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:37:13.478506+00:00"
---

# Conventions

This document uses the following code and command conventions.

Table 1. Code and command syntax conventions

| Convention | Purpose | Notes |
| --- | --- | --- |
| `cim.cimweb.exposeCommitPort: true` | Code or CLI commands that appear within a block of text. | monospace font |
| ${NS} | String variable. | See Table 2 for common variables. |
| ``` cim:   cimweb:     keystore:       enabled: true       certificateSecret: "coverity-ingress" ``` | Multi line code. | monospace font, indents |

This document contains the following commonly-used variables.

Table 2. Variables

| Variable name | Usage | Examples |
| --- | --- | --- |
| `${NS}` | Coverity namespace in Kubernetes cluster. | `cov-cnc` |
| `${RELEASE}` | Software release. | `2026.9.0` |
