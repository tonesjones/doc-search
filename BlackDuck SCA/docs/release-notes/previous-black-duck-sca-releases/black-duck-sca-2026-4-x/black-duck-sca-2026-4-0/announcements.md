---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "8jZCd62u6uffwYQK8qVIgw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:58.356876+00:00"
---

# Announcements

## End of Support for BD SCA Embedded Web Help

We are announcing the upcoming end of support for the Black Duck SCA embedded web help with Black Duck SCA 2026.7.0. As part of this transition, documentation
will be moving to a new URL and IP address.

For customers using air-gapped Knowledge Bases, a PDF help document will be provided
going forward as an alternative resource.

Please note that the documentation container will reach its end of life, and we
encourage all users to prepare for this change.

## Chainguard Container Image Support

Black Duck SCA Secure Container now supports Chainguard
container images, helping organizations that rely on commercially maintained
containers reduce risk, eliminate noise, and move faster. By combining Chainguard’s
curated component inventory and vulnerability intelligence with Black Duck SCA’s industry‑leading analysis, customers get more
accurate results with fewer false positives, faster access to security fixes, and
less manual triage for developers and security teams. The result is quicker
patching, lower exposure to vulnerabilities, and more time spent delivering secure
software instead of tracking down issues.

## Preliminary PostgreSQL 18 support

Black Duck SCA 2026.4.0 introduces preliminary support for
PostgreSQL 18 as an external database. This support is for **testing purposes
only**, and **production use is not supported** at this time. Customers can
evaluate PostgreSQL 18 in non-production environments to assess compatibility ahead
of future full support.

**NOTE**: Starting with PostgreSQL 18, data page checksums are enabled by default
when initializing a new cluster. If you are upgrading from a previous PostgreSQL
version using `pg_upgrade`, you’ll need to add the
`--no-data-checksums` option to `initdb` when
initializing the PostgreSQL 18 cluster.

## Retroactive PostgreSQL 17 support

With the release of Black Duck SCA 2026.4.0, we are pleased to
announce retroactive support for PostgreSQL 17 as an external database. This support
is intended for production use, allowing customers to leverage PostgreSQL 17 in
their environments. Customers are encouraged to upgrade to PostgreSQL 17 to benefit
from the latest features and enhancements.

## Update to `default_statistics_target` Setting in Black Duck SCA 2026.4.0

With the migration to Black Duck SCA 2026.4.0, the
`default_statistics_target` setting for PostgreSQL will be
increased to 250, provided that it is not already set to a higher value.

**Important Considerations:**

- For users utilizing external PostgreSQL instances, the change may fail to
  apply if the `bds_hub` database is not owned by the
  `blackduck` database user or if the
  `blackduck` user lacks administrative privileges. Should
  this failure occur, it will not impede the migration process and may go
  unnoticed by the user.
- Users operating with the Black Duck-provided PostgreSQL container are not
  affected by these conditions, and no additional action is required.

**Verification Steps for External PostgreSQL Users:** To confirm whether the new
value has been successfully applied, connect to the `bds_hub`
database and execute the following command:

```
SHOW default_statistics_target;
```

If the returned value is below 250, it can be updated using the following
command:

```
ALTER DATABASE bds_hub SET default_statistics_target = 250;
```

Please note that the migration process sets this value specifically for the
`bds_hub` database. As a result, queries checking the system-wide
setting may not reflect this change, even if the update was successfully applied for
`bds_hub`.
