---
title: "New and Changed Features in Version 2020.12.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2020.12.0.html"
content_id: "qOipeXQkpuTtwjH3aKtubA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:22.321004+00:00"
---

# New and Changed Features in Version 2020.12.0

## New containers and changes to system requirements

There are two additional containers: BOM Engine and RabbitMQ (now a required
container) for the 2020.12.0 release.

The minimum system requirements to run a single instance of all containers are:

- 6 CPUs
- 26 GB RAM for the minimum Redis configuration; 29 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching
- 250 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

The minimum hardware that is needed to run Black Duck with Black Duck Binary Analysis are:

- 7 CPUs
- 30 GB RAM for the minimum Redis configuration; 33 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching
- 350 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

Note: An additional CPU, 2 GB RAM, and 100 GB of free disk space will be needed for every
additional binaryscanner container.

## Password configuration

Users with the Super User role can now set password requirements for *local*
Black Duck accounts. If enabled, Black Duck ensures that the new password meets your
requirements and also rejects passwords that are considered weak, such as
"password", "blackduck", or a user's username or email address.

Super Users can:

- define the minimum password length.
- define the minimum number of character types for the password. Possible
  character types are lowercase letters, uppercase letters, numbers, or
  special characters.
- select whether to enforce the password requirements on current users when
  they log in to Black Duck.

By default, *password requirements are enabled* and have these settings:

- The minimum password length is eight characters.
- Only one character type is required.
- Password requirements are not enforced on current users when logging in to
  Black Duck.

## License enhancements

So that you can successfully manage license risk, Black Duck now gives you the
ability to create new or edit existing multi-license scenarios for the components in
your BOM.

## Vulnerability Impact Analysis enhancements

- A new project version report,
  `vulnerability_matches_date_time.csv`, has been added.
  It lists the component, vulnerability data, and vulnerability impact analysis
  data for each component potentially reached by a vulnerability. This report has
  the following columns:
  - Component name
  - Component id
  - In use
  - Component version name
  - Version id
  - Channel version origin
  - Origin id
  - Origin name id
  - Vulnerability Id
  - Vulnerability source
  - CVSS Version
  - Security Risk
  - Base score
  - Overall score
  - Solution available
  - Workaround available
  - Exploit available
  - Called Function
  - Qualified Name
  - Line Number

- A new table, vulnerability method matches
  (`vulnerability_method_matches`), has been added to the
  report database. It has the following columns:
  - `id`. ID.
  - `project_version_id`. UUID of the project version
    where the reachable vulnerability appears.
  - `vuln_source`. Source of the vulnerability. For
    vulnerability impact analysis, the value is BDSA.
  - `vuln_id`. Vulnerability ID, such as
    BDSA-2020-1234.
  - `qualified_name`. Name of the class the function is
    called on.
  - `called_function`. Name of the vulnerable function
    call in your code that makes the vulnerability reachable.
  - `line_number`. Line number in your code where the
    vulnerable function is called.
- The vulnerability reports (vulnerability remediation report, vulnerability
  status report, and the vulnerability update report) now have a new column,
  "Reachable", added to the end of the report, to denote whether the security
  vulnerability is reachable (true) or not reachable (false).

## BOM computation information

Black Duck now provides detailed information on the status of the computation of the
project version BOM.

The new **Status** indicator (replacing the Components indicator) in the project
version header in the Black Duck UI provides the current status of the BOM and
notifies you of the state of the processing of BOM events. For more information, a
new BOM Processing Status dialog box lists the events that are pending, processing,
or have failed.

Black Duck also provides the ability to configure the frequency of the BOM event
cleanup job (VersionBomEventCleanupJob) which clears those BOM events that might be
stuck because of processing errors or topology changes.

## Policy enhancements

- Policy management now provides the ability to create policy rules based on these
  custom fields:
  - Component custom fields for Boolean, Date, Drop Down, Multiple
    Selections, Single Selection, and Text field types.
  - Component version custom fields for Boolean, Date, Drop Down,
    Multiple Selections, Single Selection, and Text field
    types.

- You can now distinguish between declared and deep (embedded) license data when
  creating policy rules for these conditions:
  - License
  - License expiration date
  - License family

  Note:

  Any existing policy rules using these license conditions will now
  only apply to declared licenses. You must create a separate policy rule
  for deep (embedded) licenses for these license
  conditions.

## Report enhancements

The vulnerability reports (vulnerability remediation report, vulnerability status
report, and the vulnerability update report) that were previously only available at
the global or project level are now available for project versions.

## Configuration of snippet file size

You can now modify the default maximum file size that will be scanned for snippets
and select a value from 1MB to 16MB.

## HUB-26086Configuration of the clean up of unmapped code locations

Black Duck purges unmapped code location data every 365 days. You can disable this
feature, such that unmapped code location data is not purged, or set the retention
period to a lower number of days if you scan regularly and want to discard the data
frequently.

## Access tokens

The options for the scope of user access tokens are now Read or Read and Write.

## Supported browser versions

- Safari Version 14.0.1 (14610.2.11.51.10)
- Chrome Version 87.0.4280.88 (Official Build) (x86_64)
- Firefox 83.0 (64-bit)
- Internet Explorer 11 11.630.19041.0

  Note that support for Internet Explorer 11 is deprecated and Black Duck will be
  ending support for Internet Explorer 11 starting with the Black Duck 2021.2.0 release.
- Microsoft Edge 87.0.664.60 (Official build) (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:1.0.16
- blackducksoftware/blackduck-authentication:2020.12.0
- blackducksoftware/blackduck-webapp:2020.12.0
- blackducksoftware/blackduck-scan:2020.12.0
- blackducksoftware/blackduck-jobrunner:2020.12.0
- blackducksoftware/blackduck-cfssl:1.0.1
- blackducksoftware/blackduck-logstash:1.0.8
- blackducksoftware/blackduck-registration:2020.12.0
- blackducksoftware/blackduck-nginx:1.0.26
- blackducksoftware/blackduck-documentation:2020.12.0
- blackducksoftware/blackduck-upload-cache:1.0.15
- blackducksoftware/blackduck-redis:2020.12.0
- blackducksoftware/blackduck-bomengine:2020.12.0
- blackducksoftware/bdba-worker:2020.09-1
- blackducksoftware/rabbitmq:1.2.2

## Japanese language

The 2020.10.0 version of the UI, online help, and release notes has been localized to
Japanese.
