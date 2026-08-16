---
title: "Installing Black Duck using Helm"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/installing-black-duck-using-helm.html"
content_id: "sjz7nhni_3G_PEJKHOhHzA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:32:59.131214+00:00"
---

# Installing Black Duck using Helm

A Helm chart describes a Kubernetes set of resources that are required for Helm to deploy Black
Duck. Black Duck supports Helm 3.5.4 and the minimum version of Kubernetes is 1.17.

Helm charts are available here: <https://repo.blackduck.com/cloudnative>

Click [here](https://github.com/blackducksoftware/hub/tree/master/kubernetes/blackduck) for instructions about installing Black Duck using
Helm. The Helm chart bootstraps a Black Duck deployment on a Kubernetes cluster using
Helm package manager.

## Migrating on Kubernetes with Helm

If you are upgrading from a PostgreSQL 9.6-based version of Black Duck, this
migration replaces the use of a CentOS PostgreSQL container with a
Black Duck-provided container. Also, the blackduck-init container is replaced with
the blackduck-postgres-waiter container.

On plain Kubernetes, the container of the upgrade job will run as root unless
overridden. However, the only requirement is that the job runs as the same UID
as the owner of the PostgreSQL data volume (which is UID=26 by default).

On OpenShift, the upgrade job assumes that it will run with the same UID as the
owner of the PostgreSQL data volume.
