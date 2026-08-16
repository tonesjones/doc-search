---
title: "Statically tuning an external Connect PostgreSQL database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/statically-tuning-an-external-connect-postgresql-database.html"
content_id: "YMcHrY0n_z7QJ2u3D68Mjw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:15.394671+00:00"
---

# Statically tuning an external Connect PostgreSQL database

Database tuning optimizes and homogenizes the performance of a database. The tuning
process updates database configuration parameters based on hardware resources of the
database instance. To perform static tuning, you must provide the PostgreSQL
distribution and hardware resource definitions through the Kubernetes job deployment
environment.

Note: You can perform a static tuning periodically as needed to tune
your PostgreSQL database.

The container images and scripts used to perform the tuning are bundled in the tools
image that is downloaded and installed during the Coverity cloud depoyment process.

This chapter describes how to create a yaml file that specifies tuning parameters and
points to the script file, and how to statically tune an external Coverity Connect
PostgreSQL database.

To statically tune an external PostgreSQL database:

1. Create a tuning yaml file which defines the tuning container job and provides tuning
   values. See Creating a tuning job yaml file.
2. Run the tuning. See Run a database tuning job.
3. Verify the tuning status. See Monitor the logs.
4. If the tuning completes successfully, restart the database. See Restart the database.
