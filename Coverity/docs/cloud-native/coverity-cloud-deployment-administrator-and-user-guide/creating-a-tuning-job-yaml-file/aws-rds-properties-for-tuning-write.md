---
title: "AWS RDS properties for tuning-write"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-rds-properties-for-tuning-write.html"
content_id: "4~C1VHM7F5iFSYQUfCS1mA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:18.696914+00:00"
---

# AWS RDS properties for tuning-write

If the PostgreSQL database is on AWS-RDS and if you are performing a tuning-write, set
`<POSTGRES-DISTRO>`, authentication, and authorization as
follows.

## POSTGRES-DISTRO

If the PostgreSQL database is on AWS-RDS, set `<POSTGRES-DISTRO>`
to `'rds'`.

## Authentication

Provide the access key and secret key using environment variables
`AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`.

For the `AWS_REGION` environment variable, provide the region
where the database is located.

## Authorization

Provide the following required permissions for AWS-RDS to perform the tuning
write.

Note: This authorization is not required with
tuning-suggest.

| Action | Required Permissions |
| --- | --- |
| Get a description of a DB instance to check the instance status. | `rds:DescribeDBInstances` |
| Create a custom DB parameter group. | `rds:CreateDBParameterGrouprds:AddTagsToResource` |
| Modify the DB parameter group. | `rds.ModifyDBParameterGroup` |
| Modify the DB instance, associating the custom DB parameter group. | `rds:ModifyDBInstanceiam:PassRole` |

## DBParameterGroupFamily

The `DBParameterGroupFamily` parameter specifies the parameter group
family when tuning an AWS RDS database.

A database cluster parameter group acts as a container for engine configuration
values that are applied to one or more database instances. Database cluster
parameter groups apply only to Multi-Availability Zone database (Multi-AZ DB)
clusters. In a Multi-AZ DB cluster, the database cluster parameter group settings
apply to all of the database instances in the database cluster. The default database
parameter group for the database engine and database engine version is used for each
database instance in the database cluster. For more information about parameter
groups, refer to:

- <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/parameter-groups-overview.html>

Using the `AWS_DB_PARAMETER_GROUP_FAMILY` environment variable,
specify the database parameter family. This family is based on the PostgreSQL
version of the database instance from the RDS console.

Note: If you pass an empty key value, by default the database
family is considered `postgres14`. Do not pass the empty key value.
Also, if you expect the environment variable to be empty, remove the key.
