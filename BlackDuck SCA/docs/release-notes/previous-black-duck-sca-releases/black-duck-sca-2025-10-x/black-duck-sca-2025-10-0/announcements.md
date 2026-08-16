---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "_fYssX5GgSF2JdtWEXab5g"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:20.310501+00:00"
---

# Announcements

## Introduction of Match Review Process

With the Black Duck SCA 2025.10.x release, we are excited to introduce the Match
Review process. This new feature will add a Review tab to the Bill of Materials,
where certain items identified during scanning will be placed for further
evaluation.

After the upgrade, existing Project Versions' Bills of Materials will initially
appear unchanged. However, you will gain access to additional information about
unmatched items in the new Review tab. Upon rescanning a Project Version with the
updated software, you may notice some matches moving from the Bill of Materials to
the Review tab.

New Project Versions will immediately incorporate this feature, displaying relevant
scan contents in the Review tab right away. For more details, please refer to the
User Guide and Release Notes.

## Consolidation of Scan and Matchengine Containers

In the 2025.10.0 release, we have merged the `scan` and
`matchengine` containers into a single `scanmatch`
container. This change is part of our ongoing efforts to reduce resource
requirements for Black Duck SCA deployments, enhancing efficiency and
performance.

**NOTE**: Moving to the consolidated scanmatch container will require
transitioning to Gen05 SPH hardware configurations.

## PostgreSQL 17 Production Support Update

We would like to inform our users that we will not be providing production support
for PostgreSQL 17. Instead, we will be skipping PG 17 and redirecting our efforts
towards enhancing evaluation support for PostgreSQL 18. This decision reflects our
commitment to ensuring that our customers have access to the most stable and
effective database solutions. Thank you for your understanding as we strive to
improve your experience with our products.

## PostgreSQL container migration to version 16

With the release of Black Duck SCA 2025.10.0, the PostgreSQL image
will be upgraded to version 16. Customers who are not using the Black Duck-supplied PostgreSQL image will not be affected.

## End of Support for PostgreSQL 15

With the release of Black Duck SCA 2025.10.0, support for external
PostgreSQL 15 will be discontinued. For more information, please refer to the [PostgreSQL Version Upgrade Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic).

## Upgrade restrictions for PostgreSQL container users

For users of the Black Duck-provided PostgreSQL container, Black Duck SCA supports direct upgrades only from earlier versions
that use PostgreSQL 14 or 15 (specifically, version 2023.10.0 and later).

Upgrading from older Black Duck SCA versions (prior to 2023.10.0)
will require a multi-step process:

- From version 2021.10.0 and earlier: Upgrade from the currently installed
  version to 2023.7.x, then to 2025.7.x, and finally to 2025.10.0.
- From versions 2022.2.x through 2023.7.x (inclusive): Upgrade from the
  currently installed version to 2024.7.x, then to 2025.10.0.
