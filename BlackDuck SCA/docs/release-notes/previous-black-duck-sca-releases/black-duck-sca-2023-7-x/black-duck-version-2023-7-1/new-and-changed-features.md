---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "dvKsUdeLCCcoC9aEnqYaPg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:45.138590+00:00"
---

# New and changed features

## New Artifactory configuration management

You can now manage your Artifactory Integration configurations within the Black Duck
UI. To do so, log in as a Integration Manager user, click the Admin button, and then
select Integrations.

As a result, a number of environment properties have been removed and are now
configurable in the Black Duck UI. The following properties have been removed:

- `BLACKDUCK_SCAAAS_ARTIFACTORY_ANNOTATE_VIOLATING_POLICY_RULES`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_EXCLUDE_FILETYPES`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_HOST`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_IGNORE_SSL`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_INCLUDE_FILETYPES`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_PORT`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_REPOSITORIES`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_DOCKER_REPOSITORIES`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_SCAN_REPORT_ENABLED`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_SCAN_REPORT_REPOSITORY`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_SCHEME`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_SEARCHER_ADAPTIVE_QUEUE`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_SEARCHER_QUEUE_SIZE`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_SEARCHER_SCHEDULE_DELAY`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_TOKEN`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_UPDATED_WINDOW_HOURS`
- `BLACKDUCK_SCAAAS_ARTIFACTORY_URI_PATHBLACKDUCK_SCAAAS_FAILED_COUNT`
- `BLACKDUCK_SCAAAS_FAILED_TIMEOUT_HOURS`
- `BLACKDUCK_SCAAAS_MANAGER_SEARCHER_QUEUE_THRESHOLD_HIGH`
- `BLACKDUCK_SCAAAS_MANAGER_SEARCHER_QUEUE_THRESHOLD_LOW`
- `BLACKDUCK_SCAAAS_PROCESSING_TIMEOUT_HOURS`
- `BLACKDUCK_SCAAAS_SEARCHER_CUTOFF_DATE`
- `BLACKDUCK_SCAAAS_REPOSITORY_TYPE`

## New Docker image/container for Artifactory Integration service

A new Docker image/container has been added for use with Artifactory Integration.
Hosted Black Duck customers must have Artifactory Integration enabled with their
registration key before deploying this image/container.

## New SCA Engine properties for Artifactory Integration

The following `environs` properties must now be added to Black Duck's
`values.yaml` file in order for Black Duck and
sca-engine-as-a-service to talk to each other:

```
BLACKDUCK_SCA_ENGINE_SCHEME:
BLACKDUCK_SCA_ENGINE_HOST:
BLACKDUCK_SCA_ENGINE_PORT:
```

**NOTE**: While these properties must be added to the `values.yaml`
file, their values are not required to be set immediately and can be left blank as
in the example above. The value of `BLACKDUCK_SCA_ENGINE_HOST`
changes based on what you plan to name the sca-engine-as-a-service deployment.

## New user roles

New user roles have been added to the list of overall roles:

- Integration Manager: This role grants the ability to manage all
  integrations.
- Lightweight BOM Code Scanner: This role grants administration privileges to a
  Lightweight BOM.
- Lightweight BOM Project Manager: This role grants administration privileges to a
  Lightweight BOM Project.
- Lightweight BOM Project Version Manager: This role grants administration
  privileges to a Lightweight BOM Project Version.

## Updated full snippet scanning functionality

With increased usage of snippet scanning we are starting to see performance and
scalability issues with snippet scanning. To help mitigate these issues, we are
implementing tactical restrictions and optimizations to manage the throughput and
reduce redundant re-work for snippet matching:

- Reduced the allowed range of maximum snippet file size to 1 - 4MB (from 1 -
  16MB)
- Changed the default value of maximum snippet file size to 1MB (from 2MB)

In addition, full snippet scanning options must now be activated on your registration
key. Affected Detect parameters are:

[detect.blackduck.signature.scanner.snippet.matching](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/62c4c406cd41875f23cf0a8c2848be66.topic)

- `FULL_SNIPPET_MATCHING`
- `FULL_SNIPPET_MATCHING_ONLY`

## Container versions

- blackducksoftware/blackduck-postgres:13-2.27
- blackducksoftware/blackduck-authentication:2023.7.1
- blackducksoftware/blackduck-webapp:2023.7.1
- blackducksoftware/blackduck-scan:2023.7.1
- blackducksoftware/blackduck-jobrunner:2023.7.1
- blackducksoftware/blackduck-cfssl:1.0.20
- blackducksoftware/blackduck-logstash:1.0.32
- blackducksoftware/blackduck-registration:2023.7.1
- blackducksoftware/blackduck-nginx:2.0.47
- blackducksoftware/blackduck-documentation:2023.7.1
- blackducksoftware/blackduck-upload-cache:1.0.45
- blackducksoftware/blackduck-redis:2023.7.1
- blackducksoftware/blackduck-bomengine:2023.7.1
- blackducksoftware/blackduck-matchengine:2023.7.1
- blackducksoftware/blackduck-webui:2023.7.1
- blackducksoftware/blackduck-storage:2023.7.1
- blackducksoftware/bdba-worker:2023.6.0
- blackducksoftware/rabbitmq:1.2.28
