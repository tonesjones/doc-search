---
title: "OpenShift: Create PostgreSQL databases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/openshift-create-postgresql-databases.html"
content_id: "Ba0F4mC1MbBzqXadKSCNVA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:00.416426+00:00"
---

# OpenShift: Create PostgreSQL databases

Red Hat OpenShift supports primary SQL databases as well as read-only SQL database
replicas. For information on databases in OpenShift, refer to Red Hat OpenShift
documentation, including the Red Hat OpenShift Data Foundation (ODF) managed service
document, [Red Hat OpenShift Data Foundation Managed
Service](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation_managed_service/2022-q2/html-single/introduction_to_red_hat_openshift_data_foundation_managed_service/index).

Important: Keep all database names handy; you will need
them when you configure the Helm keys.

At a minimum, you need one primary SQL instance to support a single Coverity Connect
cloud deployment, one primary SQL instance for each Coverity Connect instance.

Optionally, if you are deploying read-only replica PostgreSQL databases, in addition to
the single primary SQL database instance, you need one or more instances of read-only
replica SQL databases.
