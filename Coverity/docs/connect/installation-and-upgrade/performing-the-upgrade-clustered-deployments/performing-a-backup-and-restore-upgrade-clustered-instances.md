---
title: "Performing a backup-and-restore upgrade (clustered instances)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/performing-a-backup-and-restore-upgrade-clustered-instances-.html"
content_id: "YWjYPgaCWaAehnJH1cw4bQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:34.683554+00:00"
---

# Performing a backup-and-restore upgrade (clustered instances)

This section describes how to perform a backup-and-restore upgrade on Coverity Connect
clustered instances (Coordinators and Subscribers) that use an embedded database.

Note: After using the installer to perform a backup-and-restore upgrade on an instance, you need
to update SSL certificates and truststores. For details, see "Setting up SSL
certificates and TrustStores" in the Coverity Platform 2026.6.0 User and Administrator Guide.

To perform a backup-and-restore upgrade on a clustered instance that uses an embedded
database:

1. Upgrade the instance using the installer. For details, see Performing a backup-and-restore upgrade (standalone instances).
2. (Perform this step on subscriber instances only) If the
   address of the Coordinator has changed as part of the upgrade, specify the new
   address of the Coordinator by editing the **`remoteconfig.coordinator`** property in the
   `cim.properties` file in the new installation directory.

   Note: You can start up a subscriber instance, test it,
   and shut it down even if the coordinator is not running. However, **do not start a subscriber** until you have finished
   the upgrade procedure for that subscriber.
3. Update SSL certificates and truststores as needed. For details, see "Setting
   up SSL certificates and TrustStores" in the Coverity Platform 2026.6.0 User and Administrator Guide.
