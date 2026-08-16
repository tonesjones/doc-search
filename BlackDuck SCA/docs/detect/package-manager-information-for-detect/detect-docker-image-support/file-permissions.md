---
title: "File permissions"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/file-permissions.html"
content_id: "PRWfrzoPrw5kJTshA2sHKA"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:56.693185+00:00"
---

# File permissions

When using Docker Inspector, Detect must be run in an environment configured so that files created
by Docker Inspector are readable by all. On Linux, this means an appropriate umask value
(for example, 002 or 022 will work). On Windows, this means that the Detect
output directory must be readable by all.

Docker image tarfiles passed to Detect via the *detect.docker.tar* property must be readable by all.
