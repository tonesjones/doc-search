---
title: "Commit configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/commit-configuration.html"
content_id: "cdllGV6zKBFqClC_fGsfTg"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:04.652080+00:00"
---

# Commit configuration

Use this configuration to specify where to commit results.
One of the values shown in this table must be provided.

| Key | Type | Description |
| --- | --- | --- |
| `connect` | Connect configuration | The Coverity Connect configuration to use when committing defects to a Connect server. |
| `local-only` | Boolean | If `true`, analysis results will only be committed to the local filesystem, as specified by the Local configuration settings.  Default: `false` |
| `local` | Local configuration | A local configuration to use when saving defects to your local file system. |
