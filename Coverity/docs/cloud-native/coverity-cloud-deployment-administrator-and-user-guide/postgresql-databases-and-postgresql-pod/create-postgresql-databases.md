---
title: "Create PostgreSQL databases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-postgresql-databases.html"
content_id: "o2wpKO0~u1wS~Cn9WE5Xbg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:57.812204+00:00"
---

# Create PostgreSQL databases

Each Coverity Connect instance in the Coverity cloud deployment must have an external
PostgreSQL database that it can access. Coverity Connect stores and manages analysis
data in the PostgreSQL database.

You can either create or migrate PostgreSQL database instances. To migrate an existing
database to the Coverity cloud environment, see Migrating a PostgreSQL database instance to the cloud.

PostgreSQL database instance(s) for Coverity Connect need to comply with the following
requirements:

- The Connect PostgreSQL database can be run anywhere – same region, different region,
  same data center, different data center, managed service – as long as the cloud
  instance of Coverity Connect, Scan Service, and Storage Service are able to access
  the database and are provided the connection parameters.
- The database must be accessible from the Kubernetes cluster in which Coverity
  Connect is deployed.
- Ensure that the database is co-located with the Coverity Connect instance as closely
  as possible, as this will enhance Coverity performance. For example, if the database
  is in a different zone from the Coverity Connect instance, or routes to a
  significantly different network, performance will degrade.
- Each instance of Coverity connect must have its own PostgreSQL database.
- For PostgreSQL database read-only replication support, you need one or more
  read-only replica PostgreSQL databases. For information on this feature, see
  Using PostgreSQL read replicas and Pgpool to balance database loads.

  Note: The PostgreSQL versions supported with Coverity 2026.6.0 all support PostgreSQL database read replicas and
  Bitnami Pgpool II. For supported PostgreSQL versions, see the section, Third-party software and platform support matrix.
- Black Duck recommends that you use DBaaS as offered by the
  cloud provider.
- The following cloud providers support PostgreSQL databases. In addition to the
  information in this section, refer to the following sections as well as the cloud
  provider's documentation for instructions to create a primary PostgreSQL database or
  optionally, replica databases:
  - Amazon AWS: See AWS: Create PostgreSQL databases.
  - Microsoft Azure: See Azure: Create PostgreSQL databases.
  - Google GCP: See GCP: Create CloudSQL PostgreSQL databases.
  - Red Hat OpenShift: See OpenShift: Create PostgreSQL databases.
- Cloud-managed databases (RDS, Cloud SQL, Azure) handle OpenSSL on the server.
- If you run pg_dump or pg_restore in customer-provided client containers outside the
  product, those containers must use Ubuntu 22+ or equivalent.
- Keep the database user name and password handy. You will need to configure
  `postgres` Helm key parameters for the service(s) to access the
  PostgreSQL database(s). providing these database values and access credentials.
- If you are deploying scan services in Kubernetes, you can optionally create a
  PostgreSQL database instance for Scan Service and/or a PostgreSQL database instance
  for Storage Service.
