---
title: "Internet Access"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/internet-access.html"
content_id: "rq97IlVOjXAixw3kgiZhSQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:20.320849+00:00"
content_hash: "d216186f6240dd3cc936ca5b87ef9f5d3f9fd6cc9e44c1b2779f59ccb4caed84"
---

# Internet Access

Software Risk Manager uses internet access in the background for some activities, such as
keeping tool data up-to-date and periodically checking for a new Software Risk Manager
release.

Software Risk Manager does not require internet access; however, to insure full
functionality, internet access is highly recommended.

To disable background internet access by Software Risk Manager, add
`codedx.offline-mode = true` in your properties file
(`codedx.props`). The default is `false`. Note that
this will not disable any internet access that may occur as a result of user action or
configuration settings, such as *Tool Connector*, *Git*, or *Issue
Tracker* configurations.

When internet access is enabled, Software Risk Manager will perform the following
actions:

- Update notifications - Software Risk Manager will periodically check for newer
  versions and display an update notification when one is available.
- Dependency-Check updates - Dependency-Check will periodically download updates
  from the [National Vulnerability Database](https://nvd.nist.gov/), the [Retire.js repository](https://raw.githubusercontent.com/Retirejs/retire.js/master/repository/jsrepository.json), or reach out to
  [Maven
  Central](https://search.maven.org/) while scanning Java dependencies (this aids in the dependency
  identification process, to cut down on both false positive and false negative
  results). If Software Risk Manager is in offline mode, this may lead to lower
  quality results when running Dependency-Check as a bundled tool.
- Secure Code Warrior - Unless noted elsewhere, Software Risk Manager will reach
  out to any URLs belonging to the `securecodewarrior.com`
  domain.

## Dependency-Check External Access

The base paths below are external resources that Dependency-Check may attempt to
access during analyses or updates. If Software Risk Manager is not running in
offline mode, ensure that all of the following paths are accessible to allow normal
operation:

- https://jeremylong.github.io/DependencyCheck/current.txt
- https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.gz
- https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-%d.json.gz (where %d is a
  year)
- https://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.gz
- https://repository.sonatype.org/service/local/
- https://search.maven.org/solrsearch/select
- https://search.maven.org/remotecontent?filepath=
- https://repo1.maven.org/maven2/
- https://ossindex.sonatype.org
- https://registry.npmjs.org/-/npm/v1/security/audits
- https://raw.githubusercontent.com/Retirejs/retire.js/master/repository/jsrepository.json

Note: The first resource
(https://jeremylong.github.io/DependencyCheck/current.txt) is not necessary for
proper operation; however, Dependency-Check will occasionally attempt to access it
to check the latest release version number.

## Software Risk Manager External Access

To see the latest Software Risk Manager version:
https://service.codedx.com/updates/latestVersionData.json

## Secure Code Warrior External Access

For Software Risk Manager Secure Code Warrior integration, Software Risk Manager will
attempt to reach out to a number of URLs that belong to the
`securecodewarrior.com` domain. If Software Risk Manager is not
running in offline mode and Secure Code Warrior functionality is enabled, ensure
that the domain `securecodewarrior.com` (and all subdomains) are
accessible to allow normal operation.
