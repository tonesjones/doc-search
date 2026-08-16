---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "iDCqDMgFxz4rZbvqDbps6A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:53.654149+00:00"
---

# Announcements

## Black Duck SCA is now part of Black Duck, a fully independent entity from Synopsys

With this update, you will notice branding changes, including the new Black Duck
logo. For more information please see [Black Duck takes flight](https://www.blackduck.com/blog/our-new-beginning-as-black-duck.html).

Additionally, we have launched a new website and community portals. Please update any
Black Duck documentation and bookmarks you have saved. For details on the new URLs
please see [Black Duck Domain Change FAQ](https://community.blackduck.com/s/article/Black-Duck-Domain-Change-FAQ).

As part of this process, sig-repo.synopsys.com is being phased out. Please switch to
using repo.blackduck.com. We recommend keeping sig-repo.synopsys.com on your allow
list until February 2025, when it will be completely replaced by
repo.blackduck.com.

## Introducing ceiling-based rate limiting policies

Starting in Q1 2025, we will begin rolling out ceiling-based rate limiting policies.
This change is expected to have minimal impact initially, and will likely be
introduced first for Black Duck Hosted customers.

- Black Duck will be closely monitoring this rollout and
  will take necessary actions for customers that do hit the ceiling
  threshold.
- Customers with high API traffic load may experience rate limiting under heavy
  usage scenarios. If you encounter `HTTP 429 - Too Many
  Requests` responses, we strongly recommend implementing a
  strategy to reduce API traffic when building custom API integration
  applications.

## Java Development Kit (JDK) upgraded to version 17

Black Duck 2024.10.0 has been updated to use JDK 17, upgrading
from JDK 11. This upgrade brings enhanced performance, improved security, and
long-term support, ensuring a more robust and future-ready environment for both the
hosted and on-prem products.

Users and developers working with both versions should ensure their environments are
compatible with JDK 17 to take full advantage of this update.

## Upcoming deprecation of BDIO1

Please note that the BDIO1 format of BDIO files will be deprecated starting with the
2025.1.0 release. Detect version 8 and later utilize BDIO2+, while only unsupported
versions of Detect continue to use BDIO1.

BDIO (Black Duck I/O) files are JSON-based files that store scan results, including
open source components, dependencies, vulnerabilities, and licenses in a project.
They enable efficient data transfer between Black Duck scanners and the platform for
further analysis and integration into development workflows.

For customers running earlier versions of Black Duck that still
use BDIO1, we will continue to support it in those versions. If you modify BDIO1
files, these modifications will remain compatible with Black Duck versions 2024.10.0 or earlier. However, when upgrading to Black Duck version 2025.1.0 or later, you will need to update
your modifications to work with BDIO2, BDIO3, or newer versions.

There are no changes to BDIO2 and BDIO3 support; both will continue to be fully
supported.

## End of support for PostgreSQL 14

With the 2024.10.0 release, Black Duck drops support for
external PostgreSQL 14. Please refer to the [PostgreSQL Version Upgrade Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic) page for more
information.

## Upgrade restrictions for PostgreSQL container users

For users of the Black Duck-provided PostgreSQL container, Black Duck 2024.10.0 only supports direct upgrades from earlier
versions of Black Duck that use the PostgreSQL 13 or 14
containers (2022.10.0 to 2024.7.x inclusive).

Upgrading from older Black Duck versions (prior to 2022.10.0) will
require a 2-step upgrade:

1. Upgrade to Black Duck 2023.7.x.
2. Upgrade to Black Duck 2024.10.x.

## PostgreSQL container migration to version 15

Black Duck migrates its PostgreSQL image to version 15 with the
2024.10.0 release. Customers not using the Black Duck-supplied
PostgreSQL image are not affected.

## Regarding binary scanning performance metrics

This guidance offered on the [Black Duck Hardware Scaling Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) is
valid when binary scans are 20% or less of the total scan volume (by count of
scans). The performance testing metrics should be used as guideline for scaling the
server. Not all binaries that are of a certain size are the same in that the number
of layers of extraction and the number of identified components found within the
binary can require more or less resources than what was determined in the
performance tests.
