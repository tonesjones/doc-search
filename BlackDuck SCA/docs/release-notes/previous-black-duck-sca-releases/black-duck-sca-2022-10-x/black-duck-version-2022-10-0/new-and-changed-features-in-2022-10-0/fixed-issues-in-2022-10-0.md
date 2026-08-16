---
title: "Fixed issues in 2022.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.10.0.html"
content_id: "nGn2ibWyZfvbMDejXcTFww"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:26.391832+00:00"
---

# Fixed issues in 2022.10.0

The following customer-reported issues were fixed in this release:

- (HUB-29825). Fixed an issue where assigning the Global Security Manager to both
  Personal and Group overall Roles does not allow for remediate (grayed out) when
  the System Setting "Project Manager Role Settings > Security Manager" is
  disabled.
- (HUB-30488). Fixed an issue where the hierarchal BOM Tree could intermittently not
  show children components (Tree would not trickle down).
- (HUB-33274). Updated the REST API documentation to include "componentVersionName" and
  "componentVersion" for "BOM Component Representation".
- (HUB-33407). Fixed an issue where some users would receive a "You've exceeded
  your maximum amount of code you can scan" notification when they
  have unlimited codebase size.
- (HUB-33693). Fixed an issue where the uploaded source window in Snippet View
  might not display immediately.
- (HUB-33847). Fixed an issue when the clone categories field
  `cloneCategories` is not present in the body of a project
  creation request, all clone categories will be selected/enabled. In addition,
  when creating a project via the API the field
  `projectLevelAdjustments` defaults to 'true' when it is not
  present.
- (HUB-33922). Fixed an issue where only 7 days worth of job history was displaying in Admin > Diagnostics > Jobs when it should have been 30 days worth.
- (HUB-33945, HUB-34938). Fixed an issue where generating large HTML Vulnerability
  Reports in Black Duck for a project was crashing the application or taking much
  longer than expected. As part of the fix, we added a configurable
  `HUB_MAX_HTML_REPORT_SIZE_KB` property to manage HTML report
  downloads. This property will only affect HTML report viewing, not generation or
  downloading of any other report.
- (HUB-33972). Fixed an issue where string search/copyright search might not work
  with the OnPrem KB March data.
- (HUB-34085). Fixed an issue where sorting by name on the component management page
  was case sensitive.
- (HUB-34246). Fixed browser display issues related to the Project Version Comparison
  view.
- (HUB-34511). Fixed an issue where the project name of dependency scan could become
  unreadable characters when using Chinese characters.
- (HUB-34676). Fixed an issue where updating disabled custom fields could trigger BOM
  computation across all project versions.
- (HUB-34712). Fixed an issue where binary scan pods could get into a CrashLoopBackOff
  state due to the health check timeout settings for BDBA containers being out of sync
  with docker swarm and kubernetes (30 seconds). Also, the health check timeout is now
  customizable so that it can be customized:
  - For Kubernetes, use the following argument where ### is the value in
    seconds:

    `--set
    binaryscanner.timeout=`###
  - For Docker Swarm, provide the timeout value in the docker stack deploy
    command where ### is the value in seconds:

    ```
    BDBA_HEALTH_CHECK_TIMEOUT=### docker stack deploy -c docker-compose.yml -c sizes-gen03/10sph.yaml -c docker-compose.bdba.yml hub
    ```
- (HUB-34839). Added a postgres-upgrader section to
  `docker-compose.local-overrides.yml`.
- (HUB-34887). Fixed an issue for air-gapped environments where the phone-home call
  could hang for a long time, causing the system to misbehave when the registration
  service was unresponsive.
- (HUB-35110). Fixed the documentation inside `blackduck-config.env`
  for the default retention period of unmapped code locations.
- (HUB-35140). Fixed an issue where the comments on components with shared
  vulnerabilities comments were not origin-specific.
- (HUB-35184). Upgraded Zulu Java version to 11.0.16+8 to remediate vulnerabilities
  found in Black Duck 2022.4.2.
- (HUB-35196). Fixed an issue where using the Component/Component Version filter did
  not show Component name results.
- (HUB-35222). Fixed an issue where the "Affected projects" tab was not able to load
  pages when navigating through them for a specific vulnerability
  (CVE-2016-1000027).
- (HUB-35366). Fixed an issue where custom field values were not appearing in
  Component details screen.
- (HUB-35369). Fixed an issue when printing the Black Duck BOM pdf, the report would
  overlap at the edge of pages and would not list all the components correctly.
- (HUB-35407). Fixed an issue where custom fields with null values could cause the
  KbUpdateWorkflowJob-Component Version Update job to fail.
- (HUB-35524). Fixed user permissions issues when using the
  `/api/projects/<project_id>/versions/<version_id>/policy-rules`
  public endpoint.
- (HUB-35660). Fixed an issue with duplicate entry ids in the scan client which could
  cause an exit Code 70 - "java.util.ConcurrentModificationException" error.
