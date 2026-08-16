---
title: "PostgreSQL database read replica setup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/postgresql-database-read-replica-setup.html"
content_id: "Z5rTMqa~18ogCD4r3xfIgg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:10.740180+00:00"
---

# PostgreSQL database read replica setup

The setup procedures define setup for only this feature.

Important: To support database read replicas, you need to
provide resources for the primary and replica storage, and for the Pgpool
container.

Important: Pgpool 4.6 supports backend SSL with
certificate verification (`verify-ca`) when CA certificates are
configured.

1. Create the PostgreSQL primary database and one or more read-only replica
   databases. See the appropriate section:platform-specific section:

   - For AWS: AWS: Create PostgreSQL databases
   - For Azure: Azure: Create PostgreSQL databases
   - For GCP: GCP: Create CloudSQL PostgreSQL databases
   - For OpenShift: OpenShift: Create PostgreSQL databases
2. Download the Bitnami Pgpool-II container image. See the section, Coverity container images as well as  [dockerhub pgpool](https://hub.docker.com/layers/bitnami/pgpool/4.5.3/images/sha256-df310233f90103dbb4dc6fa187bf5aca4ac65279745e209eeb95910a94657f80?context=explore).
3. Web application high availability (HA) must be enabled and configured. See Connect Web application high availability.
4. Optionally, create a `dbreadreplicas.yaml` Helm file. See the
   section, Create a dbreadreplica-values.yaml file.
5. Configure the `pgpool` Helm keys. See the section, Configure the cim.pgpool Helm keys.
6. Coverity Connect (CIM) must either be deployed.
7. Deploy PostgreSQL database read replicas. For an upgrade, Coverity Connect (CIM)
   must already be deployed. To deploy database read replicas, see the section,
   Deploy database read replicas.
