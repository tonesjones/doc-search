---
title: "Database requirements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/database-requirements.html"
content_id: "VuHFdFAf7FNzzd5chn6gzg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:30.623813+00:00"
---

# Database requirements

Black Duck uses the PostgreSQL object-relational database to store
data.

CAUTION:

Do not delete data from the Black Duck database
(bds_hub) unless directed to do so by a Black Duck Technical
Support representative. Be sure to follow appropriate backup procedures. Deletion of
data will cause errors ranging from UI problems to complete failure of Black Duck to start. Black Duck Technical
Support cannot recreate deleted data. If no backups are available, Black Duck will provide support on a best-effort basis.

Prior to installing Black Duck, determine whether you want to use
the database container that is automatically installed or an external PostgreSQL
instance.

Important: As of Black Duck 2026.7.0, Black Duck recommends PostgreSQL 18.x for new installs that use
external PostgreSQL. PostgreSQL 15.x is no longer supported for external PostgreSQL
instances. For users of the internal PostgreSQL container, PostgreSQL 16 is
provided.

Refer to:

- [PostgreSQL Version Upgrade Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic)
  for more information regarding supported PostgreSQL versions in Black Duck SCA.
- Configuring an external PostgreSQL instance for
  more information on setting up your own PostgreSQL instance.

Note: For PostgreSQL sizing guidelines, see the [Black Duck Hardware
Scaling Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic).
