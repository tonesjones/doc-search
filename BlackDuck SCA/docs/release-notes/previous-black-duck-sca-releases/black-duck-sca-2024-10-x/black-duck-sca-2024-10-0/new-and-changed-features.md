---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "kddWwni6poiNmKkWqbmV7g"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:54.300355+00:00"
---

# New and changed features

## New Multi-Factor Authentication (MFA) feature

Black Duck 2024.10.0 now includes a new Multi-Factor
Authentication (MFA) feature, providing enhanced security for user accounts. With
MFA enabled, users will authenticate using a MFA token, SMS or app based
verification code for the second layer of verification. This additional step helps
ensure that only authorized users can access the system, further safeguarding
sensitive data.

## New Correlated scanning

A new scanning method has been added to Black Duck 2024.10.0 which
correlates match results from Package Manager and Signature scans to enhance
results. By integrating the strengths and compensating for the weaknesses of
different scanning methods, Correlated Scanning effectively reduces false positives
and version spray. The correlation between these scanning methods ensures more
accurate and comprehensives results.

Black Duck 2024.10.0 supports correlation between single
signature scans and one/many package manager scan results only. Using it with other
scan types is not recommended.

## New Origin IDs tab added to Component version page

A new Origin IDs tab has been added to the Component version page. This tab lists all
known external IDs and Package URLs (PURLs) associated with a specific component
version, providing more detailed visibility into the origins of each component.

## New file adjustment simplification

The file adjustment process has been simplified to use path-based adjustments instead
of signature-based adjustments. This change improves user experience, enhances
performance, and removes obstacles to advancing signature-based component matching
in the KnowledgeBase. For example, if the same file, directory, or archive appears
in multiple locations (e.g., in different code locations mapped to the same project
version), only one instance will be adjusted.

## New session token invalidation after logout

This new feature allows session token to be invalidated after a user logs out of the
system. This enhances security by ensuring that tokens cannot be reused after
logout. However, this feature is not enabled by default. To activate it,
administrators must configure the `blackduck-config.env` file and set
the `JWT_BLOCK_LIST_CHECK` variable to `true`.

## Updated external authentication configuration location

The external authentication configuration pages for SAML and LDAP have been moved
from Admin → System Settings → User Authentication to Admin → Integrations →
External Authentication.

In addition, the User Authentication page has been renamed to Local Authentication to
reflect its updated functionality.

## Updated support for multiple container scans to a single project version

We have enhanced the system to allow multiple container scans to be mapped to a
single project version. Previously, only one container scan could be mapped per
project version. This enhancement provides greater flexibility in managing and
analyzing your codebase across different containers. The following are valid
combinations of scans (code locations) that can be mapped to single project
version:

- Any combination of non-container scans mapped to project version.
- One or many container scans mapped to project version.
- One or many container scans along with one or many IaC/Malware scans mapped to the
  same project version.

All other combinations of mapped code locations are invalid and the scan process will
fail if the mapping of corresponding code location will result in invalid
combination.

As part of this update, a migration will be required to change how container names are
constructed. Previously, container names were derived from their code location.
Moving forward, they will be generated from the URI of the container tar file, as
provided in the BDIO file.

## Added vulnerability remediation for LTS projects

Long-term support (LTS) projects now support setting the remediation status for
vulnerabilities, helping teams track and document the resolution process for
vulnerabilities within their projects.

## Updated rate limiting configuration

Rate limiting has been disabled by default in Black Duck to
enhance overall system performance. If needed, rate limiting can still be manually
re-enabled by setting the `BLACKDUCK_USE_HEAP_RATE_LIMITING`
environment variable to `ON`.

## Minimum supported browser versions

- Safari Version 16.1
- Chrome Version 107 (x86_64)
- Firefox Version 106 (64-bit)
- Microsoft Edge Version 107 (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:15-1.8
- blackducksoftware/blackduck-postgres-upgrader:15-1.1
- blackducksoftware/blackduck-postgres-waiter:1.0.14
- blackducksoftware/blackduck-cfssl:1.0.30
- blackducksoftware/blackduck-nginx:2024.10.0
- blackducksoftware/blackduck-logstash:1.0.39
- blackducksoftware/bdba-worker:2024.9.1
- blackducksoftware/rabbitmq:1.2.41
- blackducksoftware/blackduck-authentication:2024.10.0
- blackducksoftware/blackduck-bomengine:2024.10.0
- blackducksoftware/blackduck-documentation:2024.10.0
- blackducksoftware/blackduck-integration:2024.10.0
- blackducksoftware/blackduck-jobrunner:2024.10.0
- blackducksoftware/blackduck-matchengine:2024.10.0
- blackducksoftware/blackduck-redis:2024.10.0
- blackducksoftware/blackduck-registration:2024.10.0
- blackducksoftware/blackduck-scan:2024.10.0
- blackducksoftware/blackduck-storage:2024.10.0
- blackducksoftware/blackduck-webapp:2024.10.0
