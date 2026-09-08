---
title: "JFrog Xray Support"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/jfrog-xray-support.html"
content_id: "7F2wpJX8xB0a7eClPUsK9A"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:39.062695+00:00"
content_hash: "e123ab6198d0995de8b9419fe018fd5318a453c78b3e62d143ca53b3a9af571a"
---

# JFrog Xray Support

Software Risk Manager imports results from JFrog Xray using its built-in Reports feature, which collects a list of vulnerabilities
for all scanned artifacts that match the specified filters. While this data includes the list of vulnerabilities and the affected
artifacts, it does not include a list of the scanned artifacts.

If a new version of an artifact is uploaded and scanned by JFrog Xray,
and if it is found to have zero vulnerabilities, that artifact may not have any entries in the report and vulnerabilities from older versions
of the artifact may still be present. While SRM *does* track the list of affected artifacts through the "JFrog Impacted Artifacts" field on individual
results, the existence of findings in the scanned
project gives a false impression of its state and makes it harder to tell which vulnerabilities are still present in the most recent
artifacts of interest.

Requests by SRM for the Build report type automatically include a filter to only fetch results for the latest build. However, Repository
reports do not have this option, which necessitates detection and filtering by SRM to determine the latest version and its associated results.

When the JFrog Xray connector is configured to use Repository reports, SRM can perform a variety of additional checks to discover the
most recent version of each affected artifact. The types and number of checks done will depend on which options are selected in the connector
configuration form.

## Detecting the "Latest Version"

The strategy for detecting the "latest version" depends on the "Latest Version Search Method" dropdown field, which has the following options:

- **None**. All results from the report are ingested.
- **Report Only**. Finds the most recent artifact versions present in the Xray report.
- **Active Search**. Uses the JFrog Xray API to find the most recent version of each affected artifact.

The "None" option may be used if you are interested in vulnerabilities across all versions of the affected artifacts. The "Report Only"
option may be used if you expect the scanned artifacts to always contain at least some vulnerabilities. The "Active Search" option may
be used if you expect at least some scanned artifacts to be completely free of vulnerabilities.

When a "latest version" is detected, its artifact ID and file path are recorded and used as a filter on the list of vulnerabilities
in the JFrog Xray report.

## Finding the "Latest Version" within a Report

When using the contents of the Xray report to detect the most recent version, SRM will take each affected artifact ID and split it
on its last `:` (colon) character. Text up to this character will be used as the package
ID, and text after that character will be used as the package version.

Note: This logic is also used to filter for specific versions when "Version Filtering Mode" is set to "Text Pattern."

SRM will take each artifact ID, its file path, and scan time for the artifact, and group this information together based on the parsed
package ID. For each group, the entry with the most recent scan time will be used as the "latest version" for the given package ID.

## Finding the "Latest Version" via JFrog Xray API

When using the Active Search method, SRM will use the [Scans List - Get Package Versions](https://jfrog.com/help/r/jfrog-rest-apis/scans-list-get-package-versions) API to find the most recent version
for each affected artifact. This requires detecting the correct package ID for the artifact, which is the most time-intensive
part of this process.

For each file name found in the JFrog Xray report, SRM will make a request to the [Scans List - Get Artifacts](https://jfrog.com/help/r/jfrog-rest-apis/scans-list-get-artifacts) API, filtering to
the file name and a creation time of ±1 hour of its scan date. If an entry is found with a matching file path, it will be associated with
the entry's `packageId` for later reference.

For any artifacts whose package ID was not resolved, SRM will create a set of "candidate" package IDs based on the artifact ID. While JFrog artifact
IDs do have a standard format, it's not guaranteed that the IDs will be "fully formed." For example, there may be an RPM artifact with an artifact ID
of `rpm://7:rpm-python:7:4.11.3-43.el7`, or it may present the artifact as `rpm://rpm-python:4.11.3-43.el7` depending on
the Artifactory configuration. The candidate package IDs for an artifact ID will be permutations of a subset of the artifact ID, for example
`7:rpm-python:7, rpm-python:7, rpm-python`.

SRM combines the list of known package IDs and candidate IDs and uses the `Get Package Versions` API for each package ID.
SRM collects pages of package versions and, for each artifact associated with the tested package ID, checks for an API response which
matches the artifact ID and file path. This ensures that SRM is reading from the correct list of package versions for a given artifact. SRM
will collect these pages until all associated artifacts are resolved, or the received versions are older than the oldest artifact associated with
the tested package ID. For artifacts that were matched, their latest version is set to the most recent entry from the beginning of the list of
versions provided by the JFrog Xray API.

SRM continues querying for package versions of each potential package ID, updating its list of associated unresolved artifacts, until a latest version
is discovered for all artifacts or all options are exhausted. For remaining artifacts that have a known package ID but an unresolved version, SRM
uses the scan date from the JFrog Xray report to find the most recent version. For artifacts with an unresolved version **and** do not have a known package ID,
their results will be included without filtering.

This process gives SRM an updated list of "latest artifacts" to filter by. SRM then reads the JFrog Xray report and only ingests results for artifacts
whose artifact ID and file path exist in this list.

## Optimization Options for "Active Search" Detection

The Active Search detection method attempts to ensure that the latest detected version is correct. This can involve many requests to the JFrog Xray
API and significantly lengthen analysis times. You can use the "Latest Version Search Optimizations" dropdown field to let SRM make certain assumptions,
which will reduce the amount of API requests to JFrog Xray.
This field has the following options:

- **Accurate**. The full search process is performed as previously described.
- **Pre-Filter**. SRM will use the "Report Only" filtering before making any API requests, reducing
  the number of requests to `Get Artifacts` and, potentially, `Get Package Versions`.
- **Optimistic**. In addition to the Pre-Filter optimization, this option assumes that each package ID candidate is a match for each associated artifact
  (without confirming their existence in the list of package versions) and immediately returns the first package version in the list. This
  reduces the number of requests to `Get Package Versions`.

It is typically safe to enable "Optimistic" filtering for the following package types:

- Docker
- Maven
- NPM
- Go
- Composer
- NuGet
- PyPi
- Conan

It is recommended to start with the "Accurate" optimization to get a baseline set of results
and confirm that other optimization options are consistent with that baseline.
