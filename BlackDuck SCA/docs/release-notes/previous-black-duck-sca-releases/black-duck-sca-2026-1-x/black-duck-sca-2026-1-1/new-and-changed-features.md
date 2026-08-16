---
title: "New and Changed Features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "tWrBJ4j~caErlX53RaaQ5A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:06.272846+00:00"
---

# New and Changed Features

## VEX Product ID and Filename Configuration

VEX reports now support configurable Product IDs and filenames to align with the CSAF
2.0 VEX specification. A VEX Product ID can be defined at the project level and is
used to populate both the VEX report filename and the document > tracking > ID field
in generated VEX reports.

- For single project version reports, the VEX Product ID is combined with the
  project version to form the filename and tracking ID
- For single project Global reports, the VEX Product ID is used as-is without
  appending the project version
- For multi-project Global reports, existing logic is used regardless of VEX
  Product ID configuration (multi-project support coming in a future
  release)

The VEX Product ID must be unique within a single Black Duck SCA instance. Uniqueness
across multiple instances cannot be guaranteed or enforced.

**Note:** Available only for customers with Vulnerability Exploitability eXchange
(VEX) enabled on their product registration.

## VEX Legal Disclaimer

VEX reports now support automatic inclusion of organization-level legal disclaimers.
Configure your legal disclaimer at the organization or project group level to define
terms and conditions for VEX document access. The disclaimer is automatically
included in all VEX reports when populated and cannot be excluded.

**Note:** Available only for customers with Vulnerability Exploitability eXchange
(VEX) enabled on their product registration.

## Updated Status Mappings

Updated
Black Duck SCA vulnerability status mappings for CSAF VEX reports:

- `NEW` status is now included in VEX reports and maps to
  `under_investigation`
- `MITIGATED` status now maps to
  `known_not_affected` with justification
  `inline_mitigations_already_exist` (changed from
  `FIXED`)

Updated
Black Duck SCA vulnerability status mappings for SPDX 3 reports:

- `NEW` status now maps to
  `underInvestigationFor`
- `MITIGATED` status now maps to `doesNotAffect`
  with justification `"security_justificationType":
  "inlineMitigationsAlreadyExist"`

Updated
Black Duck SCA vulnerability status mappings for CycloneDX reports:

- `NEW` status now maps to `in_triage`
- `MITIGATED` status now maps to `not_affected`
  with justification `protected_by_mitigating_control`

## Deprecation Notice: BDSA Auto Remediation Apply Functionality

The ability to immediately **Apply** BDSA Auto Remediation configuration changes
is deprecated and will be removed in release **2026.7.0**.

BDSA Auto Remediation configuration remains available, allowing administrators to
enable or disable the feature. However, going forward, auto remediation will only
apply to new and updated data changes rather than immediately applying to all
existing data when the configuration is changed.

Administrators should review and update any workflows that rely on this functionality
prior to upgrading.

## Container versions

- blackducksoftware/blackduck-postgres:16-2.7
- blackducksoftware/blackduck-postgres-upgrader:16-1.3
- blackducksoftware/blackduck-postgres-waiter:1.0.19
- blackducksoftware/blackduck-cfssl:1.0.35
- blackducksoftware/blackduck-nginx:2026.1.1
- blackducksoftware/blackduck-logstash:1.0.45
- blackducksoftware/bdba-worker:2025.12.5
- blackducksoftware/rabbitmq:1.2.49
- blackducksoftware/blackduck-authentication:2026.1.1
- blackducksoftware/blackduck-bomengine:2026.1.1
- blackducksoftware/blackduck-documentation:2026.1.1
- blackducksoftware/blackduck-integration:2026.1.1
- blackducksoftware/blackduck-jobrunner:2026.1.1
- blackducksoftware/blackduck-redis:2026.1.1
- blackducksoftware/blackduck-registration:2026.1.1
- blackducksoftware/blackduck-scanmatch:2026.1.1
- blackducksoftware/blackduck-storage:2026.1.1
- blackducksoftware/blackduck-webapp:2026.1.1
