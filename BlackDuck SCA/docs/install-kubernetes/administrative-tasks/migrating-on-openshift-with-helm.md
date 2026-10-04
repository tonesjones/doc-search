---
title: "Migrating on OpenShift with Helm"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/migrating-on-openshift-with-helm.html"
content_id: "9k0P1SFflyA1UF8kt__5oQ"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.520596+00:00"
content_hash: "fb66ac67bc40f60eecb74c07e33cb0f90942e9daaaa3e8180a8ce0c1b97c92fd"
---

# Migrating on OpenShift with Helm

If you are upgrading from a PostgreSQL 9.6-based version of Black Duck, this migration replaces the use of a CentOS PostgreSQL container with a Black Duck-provided container. Also, the blackduck-init container is replaced with the blackduck-postgres-waiter container.

On plain Kubernetes, the container of the upgrade job will run as root unless overridden. However, the only requirement is that the job runs as the same UID as the owner of the PostgreSQL data volume (which is UID=26 by default).

On OpenShift, the upgrade job assumes that it will run with the same UID as the owner of the PostgreSQL data volume.
