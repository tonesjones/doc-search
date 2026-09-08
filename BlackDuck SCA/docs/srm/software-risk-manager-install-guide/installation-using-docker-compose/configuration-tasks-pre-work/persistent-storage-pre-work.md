---
title: "Persistent Storage Pre-work"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/persistent-storage-pre-work.html"
content_id: "d4iiNFl0h1RDppCvjP4Rlw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:03.147580+00:00"
content_hash: "3cf3a5923dd78c3d1c13f915786fb64f468c806e7ab6dccbc9c51f61746d9dc7"
---

# Persistent Storage Pre-work

Software Risk Manager depends on one or more Docker volumes. When using [selinux](https://docs.docker.com/storage/bind-mounts/#configure-the-selinux-label), you must append `:Z` to volumes listed in
your Docker Compose file, including the default volumes and any extra volumes added during
configuration tasks.
