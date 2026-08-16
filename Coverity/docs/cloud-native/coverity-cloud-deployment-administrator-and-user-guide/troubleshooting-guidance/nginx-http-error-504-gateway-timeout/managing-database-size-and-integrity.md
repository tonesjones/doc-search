---
title: "Managing database size and integrity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-database-size-and-integrity.html"
content_id: "LG4nCogFL9gloH3JxKdQsw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:52.151779+00:00"
---

# Managing database size and integrity

The larger your PostgreSQL database, the greater the need to maintain the database for
efficiency and performance. Maintaining the database will also help avoid error 504
proxy timeouts. For a complete list of database management tools and procedures, see
Managing Connect PostgreSQL database size and integrity. The following list points to a few
significant database management tools:

- You must statically tune your database to align with your resources. See Statically tuning an external Connect PostgreSQL database.
- Run database cross reference deduplication to reduce database size and increase
  performance. See the chapter: Coverity Connect administration and
  subsection: Database cross-reference deduplication within the
  document Coverity Platform 2026.6.0 User and Administrator Guide.
- Disable and truncate ETL data during a database migration to reduce database size
  and increase performance. See the chapter: Coverity policy manager
  administration and subsection: Truncating ETL data within
  the document Coverity Platform 2026.6.0 User and Administrator Guide.
- Run database vacuum. To help maintain the database size and increase database
  performance, you can run the “vacuum full analyze” command in “maintenance mode”
  to reclaim space. If performed on a large database, this can take hours to
  complete.

We recommend enabling and monitoring metrics. See Metrics. Monitoring
metrics and usage helps you verify whether you’ve set everything properly, and helps
guide decisions.

Note: See the connect_commit_executor_size metric for
commitPoolThreads.
