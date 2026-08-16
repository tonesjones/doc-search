---
title: "Configuring HUB_MAX_MEMORY setting"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-hub_max_memory-setting.html"
content_id: "h1KzyMDaqFkJKkgZLNYTkA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:21.550441+00:00"
---

# Configuring HUB_MAX_MEMORY setting

The configuration parameter `HUB_MAX_MEMORY` is automatically set for
relevant containers in Kubernetes-based deployments. The value is computed as a
percentage of the memory limit, with 90% being the default.

In the gen04 deployment sizings, the `maxRamPercentage` controls the
percentage used; the values for this setting were chosen so that
`HUB_MAX_MEMORY` has the same values as before.
