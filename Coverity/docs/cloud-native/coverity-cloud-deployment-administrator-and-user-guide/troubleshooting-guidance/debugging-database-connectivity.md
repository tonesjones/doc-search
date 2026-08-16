---
title: "Debugging database connectivity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/debugging-database-connectivity.html"
content_id: "xhCp1jLIvE28uSquKnDDow"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:41.436609+00:00"
---

# Debugging database connectivity

You can use the `pg_isready` command to check the connection status of a
PostgreSQL server:

```
pg_isready --dbname=dbname --host=hostname --port=port --username=username
```

`pg_isready` returns:

- 0 - if the server is accepting connections normally.
- 1 - if the server is rejecting connections (for example, during startup).
- 2 - if there was no response to the connection attempt.
- 3 - if no attempt was made (for example, due to invalid parameters).

```
siguser@coverity:~$ /opt/Coverity/cov-platform-linux64-2021.9.0/postgres/bin/pg_isready -h 127.0.0.1 -d cim -p 5432 -U cim
127.0.0.1:5432 - accepting connections
```
