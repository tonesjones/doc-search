---
title: "Inspecting pod logs for errors"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/inspecting-pod-logs-for-errors.html"
content_id: "CT~ZxXZbeOydNiS8J8KZ0A"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:39.870603+00:00"
---

# Inspecting pod logs for errors

Look for errors in the following logs:

- Coverity Connect pod: `${RELEASE}-cim-webapp-XXX`
  - tls-sidecar: `/var/log/nginx/access.log`
  - tls-sidecar: `/var/log/nginx/error.log`
  - cim-webapp: `stdout`
