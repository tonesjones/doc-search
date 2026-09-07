---
title: "File permissions"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/file-permissions.html"
content_id: "PRWfrzoPrw5kJTshA2sHKA"
version: "12.0.0"
section: "Package Manager information for Detect"
scraped_at: "2026-09-07T21:16:02.221289+00:00"
---

# File permissions

When using Docker Inspector, Detect must be run in an environment configured so that files created
by Docker Inspector are readable by all. On Linux, this means an appropriate umask value
(for example, 002 or 022 will work). On Windows, this means that the Detect
output directory must be readable by all.

Docker image tarfiles passed to Detect via the *detect.docker.tar* property must be readable by all.
