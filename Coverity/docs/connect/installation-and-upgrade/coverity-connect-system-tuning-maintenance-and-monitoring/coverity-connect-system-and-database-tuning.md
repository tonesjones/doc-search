---
title: "Coverity Connect system and database tuning"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-system-and-database-tuning.html"
content_id: "6MvDg5LP50ZECbjN5wDvjw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:11.395653+00:00"
---

# Coverity Connect system and database tuning

This chapter provides a series of recommendations that you can implement in your Coverity
Connect deployment to help the system run more efficiently and more reliably. This
section includes the following:

- Embedded PostgreSQL tuning parameters
- JVM tuning options (Java heap settings)

Note: If Coverity Connect is deployed in the cloud, refer to the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on Connect system and
database tuning.

For more information about the PostgreSQL settings mentioned in this chapter, or for
information about tuning your *external* database, see the PostgreSQL documentation
at <https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server>.

Tuning Coverity Connect and its related components is an iterative process that can vary
for different deployments. Each deployment is unique and might require further
customization to suit specific requirements. It is recommended to keep detailed records
of your tuning and configuration settings in case you need to revert your changes.

Note: After making tuning changes, you must restart the Coverity Connect application and database
for the changes to take effect. For more information, see Stopping and starting Coverity Connect.
