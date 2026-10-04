---
title: "Restart the cim-web pod"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/restart-the-cim-web-pod.html"
content_id: "FJC9~5NYzYve9sqB7rHE9A"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:40.572849+00:00"
---

# Restart the cim-web pod

Note: Do not perform this step if you created proxy timeouts
annotations within the Helm chart.

After setting proxy timeouts in the NGINX configMap, in order to apply the new values and
override the default proxy timeout values, you must restart the cim web pod(s). For
example, use a `kubectl rollout restart`, or scale the
`cim` pod down then up using `kubectl scale`
commands.
