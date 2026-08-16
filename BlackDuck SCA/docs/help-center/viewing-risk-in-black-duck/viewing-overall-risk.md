---
title: "Viewing overall risk"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-overall-risk.html"
content_id: "SD97TfbopzgpNOpjfVoZrA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:17.863361+00:00"
---

# Viewing overall risk

## Project level

The **Watching**, **My Projects**, and saved search dashboards show the overall risk
across all projects where you are a project team member.

  
 [image: image]   

Click here for more information
about using this page to understand security vulnerabilities associated with your
projects.

## Project version level

Risk information for a specific project version is shown on the project version's
**Components** tab.

  
 [image: Components tab]   

Also known as the BOM page, this tab shows all type of risks associated with each component in
the project version's BOM.

## Component version level

Risk information for a specific component version is shown in the **Security** tab.

[image: Component version Security tab]

Additionally, if a component version's origin has been flagged with further Component
Intelligence risks, you can click the menu button found at the end of the
component's row [image: Menu button] and select **Insights** to view the component version's Insights
page.

[image: Insights page]

On this page, you can view a component version's insights:

**Capabilities**: Native functionality offered by the component. Capabilities currently
detectable:

- Network Communications: The software component possesses the ability to
  communicate over the network.
- System Operation: The software component possesses the ability to execute system
  level commands.
- Cryptography: The software component possesses the ability to secure
  communications.
- Serialization: The software component possesses the ability to convert data
  structures to byte streams.
- File System Access: The software component possesses the ability to interact
  with the local file system.
- Compression: The software component possesses the ability to compress data.
- Security operations (Sanitizers & Validators): The software component
  possesses the ability to sanitize and/or validate input data.

**Information Leak**: Detected valid IPv4/6 addresses including domains identified within
the codebase.

**Pre/Post Installation**: Various component configuration findings and observations.
Observations may signify security and/or operational concerns.

## Understanding the types of risk

There are three types of risk being assessed across all projects, project versions, and
component versions:

- **Security Risk**. Project and project version security risk is based on the
  vulnerabilities associated with the components that comprise the project and
  the project version's BOM. Component version security risk is based on the
  vulnerabilities associated with the versions in use in projects.

  Vulnerabilities are linked to components by the CVE numbers, as reported in
  the National Vulnerabilities Database (NVD) maintained by NIST or by Black Duck Security Advisories (BDSA) numbers.

  Note that the security risk values shown use CVSS v3.x or CVSS v4.x scores, depending on
  which security risk calculation you selected; by default, CVSS v3.x
  scores are shown.

  Possible risk categories are Critical, High, Medium, Low, and None.
- **License Risk**. Refers to the legal and compliance challenges that arise from using
  licensed software. These risks include failing to meet license obligations,
  dealing with conflicting licenses, and unintentionally exposing proprietary
  code.

  License risk is assigned one of four categories of overall risk: High,
  Medium, Low, and None.

  Click here for more information on how license risk for a component is
  determined.
- **Operational Risk**. Operational risk is based on a combination of
  factors: (1) the strength of the component community, including the number
  of contributors and the level of commit activity; and (2) the number of
  newer versions of the component that are available than the one that is
  currently in use.

  There are four categories of operational risk are High, Medium, Low, and None.
