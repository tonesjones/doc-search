---
title: "Sizing PostgreSQL pod RAM"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sizing-postgresql-pod-ram.html"
content_id: "crp1jbnQ~oUDVQWScDztAQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:06.927339+00:00"
---

# Sizing PostgreSQL pod RAM

As a guideline, you can size the PostgreSQL pod RAM to support the PostgreSQL database as
15% of the total PostgreSQL database size. This provides padding for related resources
and for some database growth. About 5%-6% database growth is built into the 15%. You
should regularly monitor memory consumption and modify resources as needed.

Important:

You must run static database tuning whenever you upgrade resources, and periodically
to tune for performance. Refer to Statically tuning an external Connect PostgreSQL database.

The following examples calculate RAM size using the 15% formula described above:

- For a 100 GB database, provide 15 GB RAM (100 x .15).
- For a 500 GB database, provide 75 GB RAM (500 x .15).

The default recommended RAM size is 32 GB.

Since RAM is available in powers of 2 (16 GB, 32 GB, 64 GB, 128 GB, 256 GB), specify your
RAM and plan to resize accordingly. These sizes provide the following PostgreSQL
support:

Table 1. RAM support of PostgreSQL

| RAM size | PostgreSQL database support |
| --- | --- |
| 16 GB | up to 106 GB |
| 32 GB (default) | up to 213 GB |
| 64 GB | up to 426 GB |
| 128 GB | up to 853 GB |
| 256 GB | up to 1.7 TB |
