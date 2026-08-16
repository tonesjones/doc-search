---
title: "AWS: Create PostgreSQL databases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-create-postgresql-databases.html"
content_id: "OqBvZJKbzKzM10f~Vnhg9A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:58.456682+00:00"
---

# AWS: Create PostgreSQL databases

The following guidance uses the AWS Management Console to create AWS RDS databases.

Important: Keep all database names handy; you will need
them when you configure the Helm keys.

## AWS: creating the primary PostgreSQL database

Create the AWS RDS primary database instance as described in the AWS documentation:
[Creating an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)

Important: In AWS, we support only RDS.

## AWS: creating read-only replica PostgreSQL databases

Optionally, if you are deploying read-only replica PostgreSQL databases:

1. Create one or more AWS RDS read replica database instance(s) of the primary
   database instance as described in the AWS documentation: [Creating a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Create.html)

   See also the Amazon RDS documentation:  [What is Amazon Relational Database
   Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide)

   Important:

   You must create an Aurora read replica. Select Create Aurora
   read replica. Aurora is a modified version of Postgres
   that contains its own load balancing solution.

   See also:

   - [Amazon Aurora DB
     clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html)
   - [Replication with Amazon
     Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html)
2. Continue with confguring the read-only replica PostgreSQL databases as described
   in Using PostgreSQL read replicas and Pgpool to balance database loads.
