---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "nUyItmukHkPXQbH3a8V2GA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:50.843402+00:00"
---

# New and changed features

## New SCA Scan Service for Package Manager and Signature Scans

Black Duck now offers the SCA Scan Service (SCASS), a scalable
solution for performing software composition analysis scans outside of the
traditional Black Duck SCA environment. SCASS supports Package
Manager and Signature Scans, making it a versatile choice for various scanning
needs.

This services provides significant benefits for both on-premise and hosted
customers:

- On-premise customers: Resource requirements for non-specialized scanning are
  greatly reduced, steamlining infrastructure needs.
- Hosted customers: Cloud Infrastructure efficiency improves with dynamic scaling
  based on overall scan demand, enhancing performance and reducing operational
  overhead.

SCASS also enables Correlated Scanning, a new feature that leverages SCASS to enhance
match results by combining insights from multiple scanning techniques.

Additionally, SCASS delivers faster delivery of scanning bug fixes, independent of
Black Duck release cycles. While scan results are stored
transactionally, this streamlined service enhances the flexibility and scalability
of scanning across platforms.

Please note, this feature must be enabled on your product registration key to take
advantage of the service. With SCASS, you can simplify resource management and enjoy
a more scalable scanning experience. Contact your Black Duck
representative to learn more.

## New sorting feature in LTS vulnerability view

The LTS vulnerability view now includes sorting capabilities, allowing you to
organize vulnerabilities by the following criteria for improved navigation and
analysis:

- Vulnerability ID (default)
- Affected Components, the first component in the list
- Overall Score
- Remediation Status

## New URL field added to Project Settings page

A new URL field has been added to the Project Settings page to define the homepage
value in an SBOM when a project version is used as a component in a parent project.

- The URL field is used as the Homepage in an SBOM if enabled in the template.
- The field is empty for new projects unless cloned from one with a
  pre-populated URL.
- The same URL applies to all project versions; it cannot be overridden at the BOM
  Component level.

## Match confidence for package manager matches removed from BOM

Match confidence scores for package manager matches are no longer included in the
Bill of Materials (BOM). This update reflects the inherent accuracy of package
manager matches, where ambiguity is unlikely. Match confidence continues to be
applied for other types of component matches.

## Merged Kubernetes and Openshift install guides

The previously separate installation guides for Kubernetes and Openshift have been
merged into a single, unified guide. This streamlined documentation simplifies the
installation process by consolidating all relevant instructions in one place. Please
note that the Swarm install guide is still maintained as a separate document.

## Updated maximum upload size change for binary and container scans

Starting in Black Duck 2024.10.0, customers can now increase the
maximum upload size for binary and container scans from the default of 5 GB to 100
GB by adjusting the `BINARY_UPLOAD_MAX_SIZE` environment variable.
The documentation has been updated to reflect this new configuration change.

## Container versions

- blackducksoftware/blackduck-postgres:15-1.8
- blackducksoftware/blackduck-postgres-upgrader:15-1.1
- blackducksoftware/blackduck-postgres-waiter:1.0.14
- blackducksoftware/blackduck-cfssl:1.0.30
- blackducksoftware/blackduck-nginx:2024.10.1
- blackducksoftware/blackduck-logstash:1.0.39
- blackducksoftware/bdba-worker:2024.9.1
- blackducksoftware/rabbitmq:1.2.41
- blackducksoftware/blackduck-authentication:2024.10.1
- blackducksoftware/blackduck-bomengine:2024.10.1
- blackducksoftware/blackduck-documentation:2024.10.1
- blackducksoftware/blackduck-integration:2024.10.1
- blackducksoftware/blackduck-jobrunner:2024.10.1
- blackducksoftware/blackduck-matchengine:2024.10.1
- blackducksoftware/blackduck-redis:2024.10.1
- blackducksoftware/blackduck-registration:2024.10.1
- blackducksoftware/blackduck-scan:2024.10.1
- blackducksoftware/blackduck-storage:2024.10.1
- blackducksoftware/blackduck-webapp:2024.10.1
