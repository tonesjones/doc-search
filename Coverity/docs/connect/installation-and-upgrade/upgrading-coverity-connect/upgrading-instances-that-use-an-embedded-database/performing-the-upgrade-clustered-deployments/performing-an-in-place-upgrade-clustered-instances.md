---
title: "Performing an in-place upgrade (clustered instances)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/performing-an-in-place-upgrade-clustered-instances-.html"
content_id: "pmXCls9xu_A0MCm52LnHjA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:34.073428+00:00"
---

# Performing an in-place upgrade (clustered instances)

This section describes how to perform an in-place upgrade on Coverity Connect clustered
instances (Coordinators and Subscribers) that use an embedded database.

To perform an in-place upgrade on a clustered instance that uses an embedded database:

1. Upgrade the instance using the installer. For details, see Performing an in-place upgrade (standalone instances).
2. (Perform this step on subscriber instances only) If the
   address of the Coordinator has changed as part of the upgrade, specify the new
   address of the Coordinator by editing the **`remoteconfig.coordinator`** property in the
   `cim.properties` file in the new installation directory.

   Note: You can start up a subscriber instance, test it,
   and shut it down even if the coordinator is not running. However, **do not start a subscriber** until you have finished
   the upgrade procedure for that subscriber.
3. Copy modifications from your old to your new `server.xml` file.

   If you made
   any modifications to the
   `<install_dir>/server/base/conf/server.xml` file of your
   existing installation (for example, if you modified the
   `keystoreFile` or `keystorePass` properties),
   copy those modifications to your new installation.

   Note: Copy only the modifications; do not overwrite the entire
   file.
