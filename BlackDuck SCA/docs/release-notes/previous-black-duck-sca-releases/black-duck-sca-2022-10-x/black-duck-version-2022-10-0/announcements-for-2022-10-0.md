---
title: "Announcements for 2022.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-2022.10.0.html"
content_id: "_X7aD0oZFa8sBuxyU0n1cw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:24.018605+00:00"
---

# Announcements for 2022.10.0

## PostgreSQL 11 deprecation

Support for running Black Duck on PostgreSQL 11 has ended with the 2022.10.0 release.
Starting with this release, attempting to run Black Duck with PostgreSQL 11 will
generate an error and Black Duck will fail to start.

## PostgreSQL 13 container migration

Black Duck 2022.10.0 has migrated its PostgreSQL image from version 11 to version 13
and supports upgrading from versions using either the PostgreSQL 9.6 container
(versions 4.2 through and including 2021.10.x) or the PostgreSQL 11 container
(versions 2022.2.0 through and including 2022.7.x). During installation, the
`blackduck-postgres-upgrader` container will migrate the existing
database to PostgreSQL 13 and then exit upon completion.

Customers with non-core PG extensions are STRONGLY encouraged to uninstall them
before migrating and reinstall them after the migration completes successfully;
otherwise, the migration is likely to fail.

Customers with replication set up will need to follow the instructions in the
pg_upgrade documentation BEFORE they migrate. If the preparations described there
are not made, the migration will likely succeed, but the replication setup will
break.

Customers not using the Black Duck-supplied PostgreSQL image will not be affected.

**IMPORTANT:** Before starting the migration:

- Ensure that you have an extra 10% disk space to avoid unexpected issues
  arising from disk usage due to the data copying of system catalogs.
- Review root directory space and volume mounts to avoid running out of disk
  space as this can cause Linux system disruptions.

**For Kubernetes and OpenShift users:**

- On plain Kubernetes, the container of the upgrade job will run as root.
  However, the only requirement is that the job runs as the same UID as the
  owner of the PostgreSQL data volume.
- On OpenShift, the upgrade job assumes that it will run with the same UID as
  the owner of the PostgreSQL data volume.

**For Swarm users:**

- The migration is completely automatic; no extra actions are needed beyond
  those for a standard Black Duck upgrade.
- The `blackduck-postgres-upgrader` container MUST run as root
  in order to make the layout and UID changes described above.
- On subsequent Black Duck restarts,
  `blackduck-postgres-upgrader` will determine that no
  migration is needed and immediately exit.

## Database bds_hub_report deprecation

As stated in the release notes for Black Duck 2021.10.0, new installations of Black
Duck will no longer create the `bds_hub_report` database. We will be
deleting the `bds_hub_report` database in 2022.10.0.

Users wishing to save their `bds_hub_report` database can use the
`hub_create_data_dump.sh` script to dump the
`bds_hub_report` database if it exists.

## Notice of Black Duck KnowledgeBase IP Address Change Nov 2022

During the week of November 14th 2022 the Black Duck KnowledgeBase <https://kb.blackducksoftware.com> IP address will be changing. During the
week of the 14th, we will be updating the DNS to direct traffic to the new IP
addresses. For most customers, no action is required.

On-prem customers who use IP allow listing to communicate to the KB will need to
update their firewall, allow lists to include these new IP address. Customers who do
not use firewall rules to restrict traffic or IP allow listing will not be
affected.

For customers who use IP address, allow listing will need to add the following IP
addresses:

NAM (North America)

[kb-na.blackducksoftware.com](https://kb-na.blackducksoftware.com) : 34.160.126.173

EMEA (Europe, Middle East and Africa)

[kb-emea.blackducksoftware.com](https://kb-emea.blackducksoftware.com):
34.149.112.69

APAC (Asia Pacific, Asia and China)

[kb-apac.blackducksoftware.com](https://kb-apac.blackducksoftware.com):
34.111.46.24

This change will not affect the majority of customers which use DNS resolution, as
this will automatically handle the IP address update. Customers who are use IP
address whitelisting will need to add the three new IP address to their whitelist:
34.160.126.173, 34.149.112.69, 34.111.46.24.

The current IP address are included below for reference only:

NAM: 35.224.73.200

EMEA: 35.242.234.51

APAC: 35.220.236.106

We are making this change as part of our continued efforts to deliver a
highly available and secure KB.

Please [submit a support case](https://community.blackduck.com/s/contactsupport) if there
are questions or problems after the server migration.

## Upcoming system resource requirement for object storage service

The minimum system resource requirements to deploy the object storage service will
increase in Black Duck 2023.1.0. The object storage service will require
approximately an additional 1 cpu, 1GB of memory, and 10GB of disk space. Please
note that these requirements will change again in future releases.

## Documentation localization

The 2022.7.0 version of the UI, online help, and release notes have been localized to
Japanese and Simplified Chinese.
