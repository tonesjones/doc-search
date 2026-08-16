---
title: "Transitioning from Synopsysctl to helm chart deployments"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/transitioning-from-synopsysctl-to-helm-chart-deployments.html"
content_id: "frs93tIq4gkmNsDbPU_gTA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:24.445602+00:00"
---

# Transitioning from Synopsysctl to helm chart deployments

As Black Duck evolves, we are transitioning from using synopsysctl
to Helm charts for managing Kubernetes deployments. Helm charts provide a more
standardized and flexible approach to deploying, upgrading, and maintaining Black Duck in Kubernetes environments.

In this guide, we recommend a fresh installation, as upgrading existing deployments may
pose risks due to volume naming conventions and other configuration differences.

Important: Before beginning the transition process, ensure you back up your
databases and any other critical data. This step is essential to prevent data loss in
case of unexpected issues arising during the transition. Always verify the integrity of
your backups before proceeding.

We strongly recommend deploying Black Duck in a test environment
before proceeding with production. This allows you to validate the process and identify
potential issues. The test environment can be a dedicated test instance or a temporary
instance cloned from your production environment.

## Internal or external database

If using an external database, you can configure the new installation to connect to
the existing database, provided only one Black Duck instance
communicates with it at any given time. Alternatively, you can create a new database
and perform a backup and restore of your existing data.

If using an internal database, you must back up the current database and restore it
to the new instance.

## Transition process

1. Back up the database from the production environment.
2. Deploy a fresh installation of Black Duck using Helm in a new
   namespace.

   Note: If using an external database, configure the new installation to point
   to the existing external database during deployment.
3. Verify that the Black Duck instance is running correctly.
4. Restore the database using the production backup (for both internal or
   external databases).
5. Perform thorough testing to ensure functionality and data integrity.
6. If performing a dry-run, and it is successful, repeat the steps above
   after stopping the production instance and updating the DNS routing or
   load balancer to point to the new instance.
