---
title: "SonarQube Support"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/sonarqube-support.html"
content_id: "7LWGmQsJD69HKm7H_voEmw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:40.264659+00:00"
content_hash: "4392f8982c99b43ff593bfc4cd239b632e1446733f6d6dc7d628bcdb44971f5a"
---

# SonarQube Support

When using SonarQube, there are two potential issues to be aware of. The first deals with
permissions; the second, listings.

## Permissions

Non-admin tokens may see permission-related issues when importing projects or when
running analyses. SRM performs permission checks during project import to prevent
the selection of items that cannot be accessed. Consequently, you should note the
following:

- These checks can greatly extend the runtime of project auto-import through
  the Integrations
  page.
- The additional requests can cause rate-limiting errors when accessing
  SonarQube.
- Projects that are successfully imported may later see analysis errors if the
  token has some permissions revoked at a later time.

However, if you are using an admin token, you can set
`sonarqube.permission-checks.enabled = false` in the SRM props
file to disable these permission checks during project import. (This will not affect
permission checks done during analysis.)

## Listings

SonarQube has an internal limit of 10,000 items when listing any sort of data from
their API. This affects lists of projects, bugs, hotspots, and so on.

When listing projects, SRM will stop once it reaches this internal limit, which can
prevent some projects from appearing. However, if an admin token is provided, SRM
will use an alternative method that will bypass the 10,000 project limit, allowing
SRM to show the full list of projects. Note: This ability to bypass the project
limit does not apply to any other data requested from SonarQube.

When listing issues during analysis, SRM mitigates this limit by using specific lists
like “critical bug issues in project X” instead of larger lists like “all issues in
portfolio Y.” Nevertheless, it’s still possible for these “specific” lists to exceed
the 10,000 project limit, in which case analysis will fail with an error.
