---
title: "Configuration Tasks (Pre-work)"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuration-tasks-pre-work-.html"
content_id: "9DRL8mPKd1iigO0WyoQHPw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:02.536034+00:00"
content_hash: "5f266b797789cf3c16b68151164fefdd908281183f9bafe4fc806e7db07824c7"
---

# Configuration Tasks (Pre-work)

The following sections specify configuration tasks that might apply to your deployment.
Pre-work tasks require updates to your Docker Compose file.

- If you are *not* using an external database, you will edit
  `docker-compose.yml`.
- If you are using an external database, you will edit
  `docker-compose-external-db.yml` instead.

For more information, see the following sections:

- Persistent Storage Pre-work
- External Web Database
  Pre-work
- Trust Certificates Pre-work
- HTTPS Pre-work
