---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "c1OwJVyrCv8vT7TqG4eN9A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:21.911133+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-38966). Fixed an issue where policy evaluation could fail due to missing
  risk data involving the policy expression is Newer Versions Count.
- (HUB-40443). Fixed an aggregator function issue with policy violations
  discrepancies between UI and reports.
- (HUB-40666). Fixed an issue where license assignment might not update when the
  KbUpdate License Job finishes.
- (HUB-40690). Fixed issues arising with rabbitmq update which could cause false
  failure errors on Kubernetes.
- (HUB-40861). Fixed an issue where searching for components within Black Duck with
  a "dash" symbol and spaces were not returning results unless double spaced.
- (HUB-40975). Fixed an issue where attempting to bulk edit unmatched components
  could generate an error message (The application has encountered an unknown
  error).
- (HUB-41054). Fixed an issue where a project versions's source report could output
  duplicated entries.
- (HUB-41069). Fixed an issue where the Supplier field was not present on CycloneDX
  SBOM reports.
- (HUB-41281). Fixed an issue where components were being truncated when clicking
  the 'Print' button in BOM reports.
- (HUB-41295). Fixed an issue where the Create button was missing on the Create
  Custom Fields page when logged in as a non-System Administrator user.
- (HUB-41347). Fixed an issue where version-specific scan retention setting was
  available when the global setting was disabled.
- (HUB-41390). Fixed an issue where an error could occur when an excessive number
  of parameters is used with the /api/internal/dashboard-facts API request.
- (HUB-41396). Fixed an issue causing the Update KnowledgeBase Data job to fail to
  apply updates to BOMs with new or modified vulnerabilities. See the related
  announcement for more information.
- (HUB-41463). Fixed an issue where the BDBA worker log was not being captured from
  system logs.
- (HUB-41502). Updated the following SCAaaS component versions to resolve security
  vulnerabilities:

  | Component Name | Previous Version | New Version |
  | --- | --- | --- |
  | com.fasterxml.jackson.core:jackson-core | 2.13.3 | 2.14.1 |
  | com.fasterxml.jackson.core:jackson-databind | 2.13.3 | 2.13.4.2 |
  | com.google.code.findbugs:jsr305 | 2.0.3 | 3.0.1 |
  | com.google.guava:guava | 30.1.1-jre | 32.0.1-jre |
  | docker:basejrever | 2.0.13 | 2.0.21 |
  | docker:blackducksoftware/hub-docker-common | 1.0.6 | 1.0.7 |
  | docker:blackducksoftware/rabbitmq | 1.2.32 | 1.2.36 |
  | javax.inject:javax.inject | 1 | 1 |
  | javax.validation:validation-api | 1.1.0.Final | 2.0.1.Final |
  | org.springframework.boot:spring-boot-starter-amqp | 2.7.12 | 2.7.18 |
  | org.springframework.boot:spring-boot-starter-hateoas | 2.7.12 | 2.7.18 |
  | org.springframework.boot:spring-boot-starter-security | 2.7.12 | 2.7.18 |
  | org.springframework.boot:spring-boot-starter-test | 2.7.12 | 2.7.18 |
  | org.springframework.boot:spring-boot-starter-web | 2.7.12 | 2.7.18 |
