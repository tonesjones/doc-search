---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "ldwd0042hObTbdXHiIGzkg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:39.710879+00:00"
---

# New and changed features

## New MFA secret expiration

Black Duck now enforces a time-to-live (TTL) period for MFA
secrets, ensuring they expire after two minutes or when a new secret is requested
via the API. IF a user attempts to set up MFA with an expired or invalidated secret,
a 401 UNAUTHORIZED error will be returned with an appropriate message. The
expiration time is configurable for flexibility.

## New BDSA vulnerability tags

Black Duck now includes two new BDSA vulnerability tags to help
further classify and assess remote code execution risks:

- **Potential Remote Code Execution**: Flags vulnerabilities that may lead
  to remote code execution under specific conditions but are not conclusively
  confirmed.
- **Remote Code Execution Requiring User Input** : Indicates the
  vulnerability requires user interaction through a user interface to exploit
  remote code execution.

## New policy rule expressions for component and vulnerability age

Black Duck now supports two new policy rule expressions that
allow users to define rules based on the age of the components or published
vulnerabilities:

- **Component Release Age**: Evaluates the number of days since a component
  was released. Useful for avoiding newly released components or prioritizing
  mature libraries.
- **Published Age**: Evaluates the number of days since a vulnerability was
  published. This can help identify components affected by recently disclosed
  vulnerabilities.

Both expressions accept a number value in days and compare it against the current
date. These additions provide more flexibility when creating time-based risk
policies.

💡 *This feature was suggested by customers. [BD-I-13](https://bdsi-sca.ideas.aha.io/ideas/BD-I-13)*

## Added support for supplying external database credentials via predefined secret

Black Duck now supports passing database credentials via
user-managed Kubernetes secret when using an external PostgreSQL instance. This
allows customers to avoid storing plaintext credentials in the
`values.yaml` file.

- A new Helm chart setting, `useHelmChartDbCreds`, has been
  added. It is enabled `true` by default, preserving the
  existing behavior where the Helm chart creates the
  `<name>-blackduck-db-creds` secret using values
  defined in `values.yaml`.
- Setting this value to `false` allows users to manually create
  and manage their own `<name>-blackduck-db-creds`
  secret.
- The user-provided secret must contain the following keys:

  - `HUB_POSTGRES_ADMIN_PASSWORD_FILE`
  - `HUB_POSTGRES_USER_PASSWORD_FILE`
- If the custom secret is invalid or missing, the deployment will fail. The
  system will not fall back to passwords in `values.yaml`.

For more details and examples, see the Kubernetes installation guide.

💡 *This feature was suggested by customers. [BD-I-7](https://bdsi-sca.ideas.aha.io/ideas/BD-I-7)*

## Added support for Ubuntu 22.04 and 24.04, ending support for Ubuntu 20.04

Starting in Black Duck 2025.4.0, Ubuntu 22.04 and 24.04 are now
supported.

As Ubuntu 20.04 reaches end of life on May 31, 2025, Black Duck
will remove support for this version in 2025.7.0. Customers using Ubuntu 20.04
should plan to upgrade to a supported version to ensure continued compatibility.

## Added support for Docker 26.x

Black Duck now supports Docker version 26.x. This update ensures
compatibility with the latest Docker runtime environments and aligns with current
container platform standards.

## Added PURL filter to BOM component's Origin ID tab

Users can now filter the Origin IDs for a BOM component using PURLs (Package URLs).
This enhancements makes it easier to locate and distinguish component identifiers
based on standardized package references, improving traceability and SBOM
navigation.

## Enhanced Vulnerabilities tab for LTS project versions

The Vulnerabilities tab for LTS project versions now includes several updates to
improve usability and visibility into risks:

- **New Risk Profile bar** – A visual summary displays the total number of
  vulnerabilities by severity (Critical, High, Medium, Low), helping users
  quickly assess the overall security posture of the project version.
- **New search bar and expanded filter** – Users can now:

  - Use the search bar to find specific vulnerabilities by ID, component
    name, or keyword.
  - Filter vulnerabilities by CWE Tags, Overall Score, Remediation
    Status, Security Risk, and Vulnerability Tags.

## Improved flexibility when importing SBOMs

Black Duck has relaxed strict field requirements when importing
SBOM files, improving usability and reducing import errors:

- For CycloneDX reports, if the component name metadata is missing from the
  report, the import will now succeed. The filename of the SBOM will be used
  as the scan name in place of the missing metadata.
- For CycloneDX and SPDX reports imported from a BOM project version Scan page,
  if the report is already mapped to a different project version and the user
  has permission to access that project version, the error message now clearly
  displays the conflicting project name and version name, making it easier for
  users to identify and resolve mapping issues.

  This behavior applies only when importing from the BOM project version Scan
  page. When importing from the Global Scans page, existing scans with the
  same name are still replaced automatically—this behavior has not
  changed.

  There is no change in behavior if the user does not have permission to view the other
  project version.

## Improved performance during bulk policy rule edits

To reduce system load during policy rule editing sessions, Black Duck now limits the number of policy rule messages
published to the BOM queue. Previously, a message was published every time a policy
rule was saved, even in rapid or bulk editing sessions. This could lead to excessive
message generation and downstream performance impacts.

With this update, message publication is intelligently reduced during clustered
policy rule edits, helping to improve overall system responsiveness and reduce
contention on shared resources such as RabbitMQ and PostgreSQL.

## Updated policy violation notification logic

The notification logic for policy violations has been updated to reduce unnecessary
alerts. Now, if a user overrides a policy rule violation and the component is later
determined to be not in violation, no notification will be sent. Previously, a
"policy violation cleared" notification was still triggered, even though the
violation had already been overridden.

## Updated Users & Groups page display

The Users & Groups page has been updated to display only a user's Global Roles in
the Roles column. Previously, this column included roles assigned at the project and
group level which lead to duplication in some cases. This update provides a clearer,
more accurate view of each user's global access within Black Duck.

## Restored file match edits for unmatched binary package manager scan results

In a previous release, binary file match edits were removed for binary scans to
address performance issues and improve usability. However, this unintentionally
disabled file match edits for unmatched binary package manager scan results, leaving
no way to resolve them. This update restores source file edits for these unmatched
results, allowing users to properly manage and adjust them.

## Minimum supported browser versions

- Safari Version 16.5
- Chrome Version 113 (x86_64)
- Firefox Version 112 (64-bit)
- Microsoft Edge Version 113 (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:15-2.2
- blackducksoftware/blackduck-postgres-upgrader:15-2.3
- blackducksoftware/blackduck-postgres-waiter:1.0.16
- blackducksoftware/blackduck-cfssl:1.0.32
- blackducksoftware/blackduck-nginx:2025.4.0
- blackducksoftware/blackduck-logstash:1.0.41
- blackducksoftware/bdba-worker:2025.3.0
- blackducksoftware/rabbitmq:1.2.44
- blackducksoftware/blackduck-authentication:2025.4.0
- blackducksoftware/blackduck-bomengine:2025.4.0
- blackducksoftware/blackduck-documentation:2025.4.0
- blackducksoftware/blackduck-integration:2025.4.0
- blackducksoftware/blackduck-jobrunner:2025.4.0
- blackducksoftware/blackduck-matchengine:2025.4.0
- blackducksoftware/blackduck-redis:2025.4.0
- blackducksoftware/blackduck-registration:2025.4.0
- blackducksoftware/blackduck-scan:2025.4.0
- blackducksoftware/blackduck-storage:2025.4.0
- blackducksoftware/blackduck-webapp:2025.4.0
