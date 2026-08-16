---
title: "Fixed Issues in 2022.4.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.4.0.html"
content_id: "3JFWuKJSCJmZW9GhfLDMWw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:40.700181+00:00"
---

# Fixed Issues in 2022.4.0

The following customer-reported issues were fixed in this release:

- (HUB-33047). Fixed an issue where Null Pointer Exception errors occurring
  during the KbUpdateJob process could cause the job to progress very slowly
  or appear to be stuck.
- (HUB-32336). Renamed the Components filter on the BOM page to Component
  Versions to bring it in line with the actual functionality.
- (HUB-32316). Fixed an issue where the HUB_MAX_MEMORY environment variable to
  define maximum memory allocation pool for the JVM was left unset in docker
  registration container deployments.
- (HUB-32492). Fixed an issue where components with the MIT license could
  trigger a policy violation for "License Not Approved" and "License
  Unreviewed" in Rapid Scan, although MIT License is set as "Approved" in
  BlackDuck.
- (HUB-31839). Fixed an issue where the BDIO upload endpoint project and
  version values were not URL decoded.
- (HUB-32692, HUB-32672). Fixed an issue where if a component had multiple
  vulnerabilities, each with different vulnerability statuses, policy rules
  would not trigger a policy violation unless all the vulnerabilities for the
  component matched the selected policy rules.
- (HUB-31872). Fixed an issue where Rapid Scans did not validate the user
  permissions. If a scan finds a matching project version BOM but the user
  does not have permission - the scan will run without project version or BOM
  component data.
- (HUB-33231). Fixed an issue where sorting scans by scan size on the Scans
  page was not displaying the list in the correct order.
- (HUB-33096). Fixed an issue where filtering by license family may not display
  modified KnowledgeBase licenses correctly.
- (HUB-30463). Fixed an issue where the golang.org/x/sys component was not
  displaying in the Hub UI KnowledgeBase search.
- (HUB-31891). Fixed an issue where searching for the "Apache HTTP Server"
  component would link to the debian component page.
- (HUB-28406). Fixed an issue where sometimes a different number of
  vulnerabilities would be shown on the Security Tab and the Details Tab in
  some OSS component and versions.
- (HUB-32883). Fixed an issue where the accessTokenValiditySeconds setting's
  Max-Age and Expires fields did not align with the expiry value of the JSON
  Web Token (JWT).
- (HUB-32313). Fixed a performance issue with the REST API
  `/api/projects/<id>/versions/<id>/components`
  endpoint when dealing with a high package manager scan data load.
- (HUB-32571). Fixed an issue with how the namespace of origin was displayed
  inconsistently in the component version Copyrights tab and Black Duck notice
  reports (and BOM Security tab).
- (HUB-32949). Fixed an issue where having a user directly assigned to a
  Project Group and the same user assigned to a User Group that's also
  assigned to the Project Group would result in multiple project groups being
  returned by the API, resulting in a Detect failure.
- (HUB-33132). Fixed an issue where the dependency-paths API was consuming
  large amount of service memory and paging to disk.
- (HUB-33155). Fixed an issue where refreshes of HUB registration could stall,
  causing the jobrunner to hold a lock much longer than it should potentially
  resulting in blocked queries.
- (HUB-32010). Fixed an issue where when navigating through the Project Groups
  hierarchy, clicking a project within a subgroup could return the user back
  to the root project group.
- (HUB-32977). Fixed an issue where mixed case tags were not triggering policy
  rules as expected.
- (HUB-33305). Fixed an indentation issue in the
  `docker-compose.local-overrides.yml` file.
- (HUB-27940). Fixed an issue when deploying to EKS, without a minimum CPU
  resource specified, the pod will be allocated .25 (250m) CPU core causing
  bomengine/rabbitmq to not work.
- (HUB-33455). Fixed an issue where the link to the Vulnerability Detail Page
  for CVE-2022-23395 would go to a 404 Not Found error page.
- (HUB-32256). Fixed an issue where submitting an empty value for the custom
  signature level would generate an incorrect error message.
- (HUB-32800). Fixed an issue where the matchengine could restart or jobs could
  hang in jobrunner during bitbake/yocto scans due to very large numbers of
  matches per component in dependency tree resulting in OutOfMemory
  exceptions. See the New Component Dependency Duplication Sensitivity system
  property item in the New and Changed Features section above for more
  details.
- (HUB-33349). Fixed an issue where the webapp container needed a persistent
  volume named "`{{ .Release.Name }}-blackduck-webapp`" by
  default where "`Release.Name`" is typically
  "`hub`" or another label chosen at deployment time. In
  addition, some customers may have configured a custom persistent volume name
  by configuring the `persistentVolumeClaimName` in the webapp
  `values.yaml` overrides. These configurations, the
  persistent volume and the persistent volume claim, are no longer necessary
  and can be safely deleted.
- (HUB-32678). Fixed an issue where the default IP scan was not supporting the
  scan.cli argument `--matchConfidenceThreshold` to filter
  matched components.
- (HUB-29532). Fixed an issue where Linux distro package matching was broken
  when the rootfs path in an distro image was not starting at the root
  directory but at a subdirectory.
