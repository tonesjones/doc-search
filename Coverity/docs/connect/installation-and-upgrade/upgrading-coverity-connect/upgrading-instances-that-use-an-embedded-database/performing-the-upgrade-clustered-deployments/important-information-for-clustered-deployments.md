---
title: "Important information for clustered deployments"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/important-information-for-clustered-deployments.html"
content_id: "tI_39nQtMcdImXxPLAznVg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:32.819880+00:00"
---

# Important information for clustered deployments

Before upgrading a Coverity Connect instance in a clustered deployment, note the
following:

- **Upgrade the coordinator first.** You must upgrade the coordinator first and
  make sure that it is running properly before you upgrade any subscriber. After the
  coordinator is successfully upgraded, you can upgrade its subscribers in any
  order.
- **To upgrade the deployment by more than one major version (for example 8.6 to 2017.07), and
  at the same time keep the deployment in active use (except for downtime
  off-hours to perform the upgrade), stagger the coordinator upgrade with the
  subscriber upgrades.** When upgrading an active deployment, the Coverity
  Connect version on the coordinator cannot be allowed to get two major versions ahead
  of its subscribers. However, this is only applicable when the upgrade is planned to
  occur while the Coverity Connect deployment is in active use (except for a temporary
  suspension of activity across the deployment’s user base while the upgrade is
  performed). If the deployment is in active use and the upgrade spans two major
  versions, upgrade the coordinator to the next major version, then upgrade the
  subscribers to that version, then upgrade the coordinator to the second major
  version.

  To determine whether you are upgrading by more than one major
  version, refer to Table 1. In
  the x.y.z numbering, major versions have differing x.y from each other.

  In
  the yyyy.mm version numbering, different major versions have different
  yyyy.mm.
- **Staggering coordinator and subscriber upgrades is not required for inactive
  deployments.** When upgrading an inactive deployment, you can upgrade the
  coordinator several versions and then upgrade each subscriber several versions.
- **Upgrade instances, including their databases, independently of each other.** It
  is important for each Coverity Connect instance to upgrade its own PostgreSQL
  database. For example, you should not upgrade the database for Subscriber1 and then
  attempt to apply that database to other subscribers within the cluster.
- **Re-form trust relationships after upgrading.** Coverity Connect uses SSL to authenticate
  and encrypt communication between the Coordinator and Subscribers. The trust
  relationships define which Coverity Connect instances can participate in the
  cluster. If you make a copy of an instance, using an intermachine or
  backup-and-restore upgrade, both the copy and the original will be able to
  participate in the cluster, but the original should *not* be allowed to
  participate in the cluster. Having that duplication can damage the cluster. You must
  prevent that from happening by re-forming the trust relationships to exclude the
  original instance. For details, see "Post-upgrade manual setup" part of section
  "Setting
  up SSL certificates and TrustStores" in the Coverity Platform 2026.6.0 User and Administrator Guide.
