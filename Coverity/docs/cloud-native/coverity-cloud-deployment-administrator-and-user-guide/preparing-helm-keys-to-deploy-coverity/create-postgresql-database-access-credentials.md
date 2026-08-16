---
title: "Create PostgreSQL database access credentials"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-postgresql-database-access-credentials.html"
content_id: "8Qq9KiWhnUZP5~obCdgOpg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:31.917958+00:00"
---

# Create PostgreSQL database access credentials

All services (Connect, Scan Service, Storage Service) need to be able to access either a
common PostgreSQL database or separate databases created for each service. The services
need privileges to create and modify tables and perform CRUD operations on table rows in
the PostgreSQL database. To create PostgreSQL access credentials, you can use either
method:

- Create secret(s) as described in Creating secret(s) for PostgreSQL access then configure Helm keys as described in Specify PostgreSQL credentials using secrets.
- Specify PostgreSQL host, port, username, and password credentials in the Helm
  chart as described in Specify PostgreSQL credentials in the Helm chart.
