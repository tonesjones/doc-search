---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "HDRFmlQVT03pTagYRD2ePA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:33.666769+00:00"
---

# Announcements

## Security Advisory for curl and libcurl (CVE-2023-38545, CVE-2023-38546)

Black Duck is aware of the security issue relating to curl and libcurl which was
disclosed by the maintainer and original creator of the project on October 3, 2023.

CVE-2023-38545 impacts curl versions 7.69.0 through and including 8.3.0 and addresses
a buffer overflow flaw that impacts both libcurl and the curl command line tool. The
overflow can occur during a SOCKS5 handshake. If the handshake is slow, a
user-supplied, unusually long hostname may not be resolved, and instead be copied
into a target buffer for which it may exceed the allocated size. Heap-based buffer
overflows such as these are known to lead to crashes, data corruption, and even
arbitrary code execution.

CVE-2023-38546 is associated with a cookie injection flaw, but curl maintainers
suggest that the series of conditions that must be met makes the likelihood of
exploitation low. The versions impacted by this vulnerability are 7.9.1 through and
including 8.3.0. Upgrading to curl 8.4.0 resolves the issue. Users are also advised
to call curl_easy_setopt(cloned_curl, CURLOPT_COOKIELIST, "ALL"); after every call
to curl_easy_duphandle();.

We believe that there is limited exposure to Black Duck’ products, services and systems.
To the extent we have had exposure, we have upgraded to the latest version of curl
to remediate the situation.

For more information, please visit:

- [Preparing for critical libcurl and curl vulnerabilities (CVE-2023-38545)](https://www.blackduck.com/blog/critical-libcurl-curl-vulnerabilities.html)
- [How to respond to the curl and libcurl vulnerabilities](https://www.blackduck.com/blog/curl-libcurl-vulnerabilities-response.html)

## PostgreSQL 14 container migration

Black Duck 2023.10.0 supports upgrading from versions using either the PostgreSQL 11
container (versions 2022.2.0 through and including 2022.7.x) or the PostgreSQL 13
container (versions 2022.10.0 through and including 2023.7.x). During installation,
the `blackduck-postgres-upgrader` container will migrate the existing
database to PostgreSQL 14 and then exit upon completion.

Customers with non-core PG extensions are STRONGLY encouraged to uninstall them
before migrating and reinstall them after the migration completes successfully;
otherwise, the migration is likely to fail.

Customers with replication set up will need to follow the instructions in the
pg_upgrade documentation BEFORE they migrate. If the preparations described there
are not made, the migration will likely succeed, but the replication setup will
break.

Customers not using the Black Duck-supplied PostgreSQL image will not be affected.

**NOTE:** Starting with 2023.10.0, Black Duck will only support direct upgrades
from Black Duck versions that use the PostgreSQL 11 or PostgreSQL 13 containers
(i.e., all Black Duck versions between 2022.2.0 and 2023.7.x inclusive). Users of
the Black Duck-provided PG container upgrading from older Black Duck versions (i.e.,
all Black Duck versions prior to 2022.2.0) will require a 2-step upgrade: upgrade to
2023.7.x and then upgrade to 2023.10.x.

**IMPORTANT:** Before starting the migration:

- Ensure that you have an extra 10% disk space to avoid unexpected issues
  arising from disk usage due to the data copying of system catalogs.
- Review root directory space and volume mounts to avoid running out of disk
  space as this can cause Linux system disruptions.

**For Kubernetes and OpenShift users:**

- On plain Kubernetes, the postgres-upgrader init container within the
  PostgreSQL pod will run as root. However, the only requirement is that the
  container runs as the same UID as the owner of the PostgreSQL data
  volume.
- On OpenShift, the postgres-upgrader init container assumes that it will run
  with the same UID as the owner of the PostgreSQL data volume.

**For Swarm users:**

- The migration is completely automatic; no extra actions are needed beyond
  those for a standard Black Duck upgrade.
- The `blackduck-postgres-upgrader` container MUST run as
  root.
- On subsequent Black Duck restarts,
  `blackduck-postgres-upgrader` will determine that no
  migration is needed and immediately exit.

## End of support for PostgreSQL 13

Support for PostgreSQL 13 has ended with Black Duck 2023.10.0.
Please refer to the [PostgreSQL Upgrade
Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic) page for more information.

## End of life for Black Duckctl

As of the 2023.7.0 release, Black Duckctl will no longer be supported and there will be
no more updates. Documentation for Black Duckctl can be found at <https://github.com/blackducksoftware/hub/tree/master/kubernetes/blackduck>.

Please note that this announcement was accidentally left out of the Black Duck
2023.7.0 release notes.

## Upgrade restrictions for PostgreSQL container users

Black Duck 2023.10.0 now only support direct upgrades from Black Duck versions that
use the PostgreSQL 11 or PostgreSQL 13 containers (i.e., all Black Duck versions
between 2022.2.0 and 2023.7.x inclusive). Users of the Black Duck-provided PG
container upgrading from older Black Duck versions (i.e., all Black Duck versions
prior to 2022.2.0) will require a 2-step upgrade: upgrade to 2023.7.x and then
upgrade to 2023.10.x.

## Documentation localization

The 2023.7.0 version of the UI have been localized to Japanese and Simplified
Chinese. The localized formats for the online help and release notes will be
available in an upcoming release.
