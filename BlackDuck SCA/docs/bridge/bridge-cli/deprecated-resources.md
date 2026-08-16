---
title: "Deprecated resources"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/deprecated-resources.html"
content_id: "w5zWAv2oq7bEe0nsJd~4iw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:31.002253+00:00"
---

# Deprecated resources

## Overview

The following resources have been changed. The old resources have been deprecated. All changes are backwards-compatible and will remain so until 6 months from the deprecation date, after which they will no longer work. The Bridge CLI will also issue a deprecated warning for that duration.

## September, 2025

| Deprecated resource name | New resource name |
| --- | --- |
| coverity.automation.prcomment | coverity.prcomment.enabled |
| coverity.prcomment.impacts |

## August, 2025

| Deprecated resource name | New resource name |
| --- | --- |
| polaris.assessment.mode=SOURCE_UPLOAD | polaris.test.sca.location=remote polaris.test.sast.location=remote |

## March, 2025

These resources are now sunset and removed in Bridge CLI v4.0.

| Deprecated resource name | New resource name |
| --- | --- |
| blackduck.url | blackducksca.url |
| blackduck.token | blackducksca.token |
| blackduck.install.directory | detect.install.directory |
| blackduck.scan.full | blackducksca.scan.full |
| blackduck.scan.failure.severities | blackducksca.scan.failure.severities |
| blackduck.fixpr.filter.severities | blackducksca.fixpr.filter.severities |
| blackduck.fixpr.maxCount | blackducksca.fixpr.maxCount |
| blackduck.fixpr.useUpgradeGuidance | blackducksca.fixpr.useUpgradeGuidance |
| blackduck.automation.fixpr | This is removed |
| blackduck.fixpr.enabled | blackducksca.fixpr.enabled |
| blackduck.automation.prcomment | blackducksca.automation.prcomment |
| blackduck.download.url | detect.download.url |
| blackduck.reports.sarif.create | blackducksca.reports.sarif.create |
| blackduck.reports.sarif.severities | blackducksca.reports.sarif.severities |
| blackduck.reports.sarif.groupSCAIssues | blackducksca.reports.sarif.groupSCAIssues |
| blackduck.reports.sarif.issues | blackducksca.reports.sarif.issues |
| blackduck.reports.sarif.file.path | blackducksca.reports.sarif.file.path |
| blackduck.search.depth | detect.search.depth |
| blackduck.config.path | detect.config.path |
| blackduck.args | detect.args |
| blackduck.policy.badges.create | blackducksca.policy.badges.create |
| blackduck.policy.badges.maxCount | blackducksca.policy.badges.maxCount |
| blackduck.waitForScan | blackducksca.waitForScan |
