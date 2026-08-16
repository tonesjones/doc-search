---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "rnGWPuQgriA5LrvLt4t1TA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:12.986206+00:00"
---

# New and changed features

## Improved BOM import log

The BOM import log will now add any unmatched components without a PURL from an SBOM
import to the BOM Import Log so it’s visible and actionable. The error messages now
clearly indicate the reason why the particular component cannot be matched:

- If the PURL has no matches in the KnowledgeBase, the error message
  displayed is *Unable to map scanned component version to Black Duck
  project version because no mapping is present for the given external
  identifier*.
- If the PURL is invalid, the error message displayed is *Unable to map
  scanned component version to Black Duck project version because given
  external identifier is
  invalid*.
- If the PURL is missing, the error message displayed is *Unable to map
  scanned component version to Black Duck project version because no
  external identifier is
  provided*.

## Improved ReversingLabs scan results

Black Duck 2024.4.1 includes an enhancement to our ReversingLabs
malware scans. All malware scans will now include the specific malware threat name,
providing you with more detailed and precise information about detected threats, and
aims to enhance your ability to respond to security issues more effectively.

Please note, to take advantage of this new update, you must rerun the ReversingLabs
scan to see the new threat name in the scan results.

## Container versions

- blackducksoftware/blackduck-postgres:14-1.22
- blackducksoftware/blackduck-postgres-upgrader:14-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.12
- blackducksoftware/blackduck-cfssl:1.0.26
- blackducksoftware/blackduck-nginx:2024.4.1-RC
- blackducksoftware/blackduck-logstash:1.0.36
- blackducksoftware/bdba-worker:2024.3.0
- blackducksoftware/rabbitmq:1.2.37
- blackducksoftware/blackduck-authentication:2024.4.1
- blackducksoftware/blackduck-bomengine:2024.4.1
- blackducksoftware/blackduck-documentation:2024.4.1
- blackducksoftware/blackduck-integration:2024.4.1
- blackducksoftware/blackduck-jobrunner:2024.4.1
- blackducksoftware/blackduck-matchengine:2024.4.1
- blackducksoftware/blackduck-redis:2024.4.1
- blackducksoftware/blackduck-registration:2024.4.1
- blackducksoftware/blackduck-scan:2024.4.1
- blackducksoftware/blackduck-storage:2024.4.1
- blackducksoftware/blackduck-webapp:2024.4.1
