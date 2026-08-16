---
title: "Viewing component version vulnerabilities"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-component-version-vulnerabilities.html"
content_id: "osEkhDx8Pg4b_nFPxlJ~SA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:21.432596+00:00"
---

# Viewing component version vulnerabilities

Use the component version page's **Vulnerabilities** tab to view the vulnerabilities
associated with specific component versions in Black Duck SCA. Understanding these
vulnerabilities helps you assess security risks and prioritize remediation efforts
effectively.

The information shown uses CVSS v3.x or CVSS v4.x scores, depending on which security risk
calculation you selected; by default CVSS v3.x scores are shown.

## **Accessing a component versions vulnerability page**

You can access a component version's vulnerability page through multiple
pathways:

- **From the Project Version Page**: Navigate to the Project Version page and click on a
  specific component listed under the **Components** tab to open its Component
  Version page. Then select the **Vulnerabilities** tab to view its associated
  vulnerabilities.
- **Using the Find Page**: Search for the component directly on the **Find** page by
  entering its name or other identifying details. Select the desired component
  from the search results to view its Component Version page. Then select the
  **Vulnerabilities** tab to view its associated vulnerabilities.

## Vulnerabilities list

  
 [image: Component Version Vulnerabilities tab]   

This Vulnerabilities list displays all identified vulnerabilities linked to the
component version which includes key details such as:

- **Vulnerability ID**: The unique identifier assigned to a specific
  security vulnerability. It serves as a reference point for tracking and
  managing vulnerabilities across various systems and databases. Formats for
  Vulnerability IDs include:

  - **CVE (Common Vulnerabilities and Exposures)**: Example:
    `CVE-2023-12345`. CVEs are standardized
    identifiers used globally to catalog publicly disclosed
    vulnerabilities.
  - **BDSA (Black Duck Security Advisory)**: Example:
    `BDSA-2023-4567`. BDSAs are proprietary
    identifiers used by Black Duck to provide
    enhanced information about vulnerabilities, including detailed
    analysis and remediation guidance.
- **Published**: The date when a vulnerability was officially disclosed or
  published by its source, such as the National Vulnerability Database (NVD)
  or a Black Duck Security Advisory (BDSA). This date marks when the
  vulnerability became publicly known and available for organizations to
  assess and address.
- **Overall Score**: The composite metric used to evaluate the severity and potential
  impact of a security vulnerability. It typically integrates various factors
  to provide a comprehensive view of the risk posed by the vulnerability.

## Viewing detailed vulnerability information

Select a vulnerability to expand more information about it:

  
 [image: Vulnerability details panel]   

- **Description**. A brief description of the vulnerabilities found for
  this component version.
- **Score Metrics**. See [Exploitability Metrics](https://www.first.org/cvss/v4-0/specification-document#Exploitability-Metrics) for
  more information.
- **Published**. The date this vulnerability was discovered and
  published.
- **Last Updated**. Date when a vulnerability for the component was last
  updated in Black Duck (such as updates from Black Duck KnowledgeBase, a user manually changing the associated
  vulnerability, and so on).
