---
title: "Sizing PostgreSQL pod resources"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sizing-postgresql-pod-resources.html"
content_id: "kYLQDBh0ly4~9wHTFFSXmQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:05.607316+00:00"
---

# Sizing PostgreSQL pod resources

This section provides resource sizing guidance for the PostgreSQL pod.

The PostgreSQL pod for Coverity Connect needs to comply with the following
requirements:

- For PostgreSQL pod memory and CPU requirements, refer to PostgreSQL pod minimum resource requirements
- For PostgreSQL pod memory sizing, refer to Sizing PostgreSQL pod RAM.

  Important: To calculate the amount of RAM
  required by a cloud implementation of Coverity to support an external PostgreSQL
  database, refer to Sizing PostgreSQL pod RAM.
- Enable TLS communication between Coverity Connect and PostgreSQL as described in
  Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS.
