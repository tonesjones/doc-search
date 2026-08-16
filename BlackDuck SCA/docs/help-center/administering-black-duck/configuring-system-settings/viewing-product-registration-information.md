---
title: "Viewing product registration information"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-product-registration-information.html"
content_id: "72T3oKcyOFmbpYjliN_vgw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:10.175050+00:00"
---

# Viewing product registration information

The Product Registration page allows system administrators to manage and configure the
licensing and registration details for your Black Duck SCA
instance. This page is accessible from the Administration section of Black Duck SCA.

## Product Registration

The Product Registration section displays the current registration key associated
with your Black Duck SCA instance. This section includes the
following information:

- **Registration ID**: The unique key used to activate and register your
  Black Duck SCA instance, unlocking the features and
  modules included in your license.

  The **Refresh** button manually contacts the Black Duck SCA master registration server
  (`updates.suite.blackducksoftware.com`) to download the
  latest registration data for your instance. During a refresh, the Black Duck SCA instance uploads usage metrics and receives
  back the full registration payload, including:

  - License properties
  - Feature flags
  - Expiration dates
  - Resource limits

  This process occurs automatically approximately every 6 hours. However, the
  **Refresh** button allows an administrator to trigger it on demand —
  for example, immediately after a license change has been made by customer
  support, eliminating the need to wait for the next automatic cycle.

  Note: The Refresh button is disabled for air-gapped users.
- **Registration State:** An indicator showing whether the current registration key is
  valid, expired, or invalid.
- **Expiration Date:** The date on which the current registration key and associated
  license will expire.
- **Reset** button: Re-activates (re-claims) the registration key with the Black Duck SCA master registration server. This performs a
  full round-trip activation, which is useful if registration data has become
  corrupted or needs to be re-established from scratch.

  Note: The Reset button is disabled for air-gapped users.

## Registration features

- Number of users
- Number of projects
- Number of project versions
- Number of codebase KBs/MBs/GBs
- Number of scans
- Maximum scan size

## Licensed modules

- **AI Model Scanning**

  AI Model Scanning enables identification of AI models in scanning. AI models
  will appear within a project version's Bill of Materials and provide
  associated metadata.
- **Artifactory Integration**

  Artifactory Integration is a service that enables scanning of artifacts within a set of
  configured repositories to identify open source components, using data
  gathered by Component Scanning.
- **Black Duck Binary Analysis**

  Black Duck Binary Analysis (BDBA) is a service that provides enhanced interrogation of
  binaries to surface the open source components within open source. It also
  supports expanded file type support including various firmware formats,
  filesystem/disk images, installation formats and various compression and
  archive formats.
- **Black Duck Secure Container (BDSC)**

  Black Duck Secure Container scanning provides capabilities to identify components within
  container images, their layers and base images.
- **Black Duck Security Advisory**

  The Black Duck Security Advisory (BDSA) is a Black Duck-exclusive vulnerability data feed,
  sourced and curated by our Security Research team which is part of the Black
  Duck COSRI (Centre of Open Source Research & Innovation). A BDSA offers
  deeper coverage for a wider set of vulnerabilities than is available through
  the NVD (National Vulnerability Database), providing detailed vulnerability
  insight including severity, impact, exploitability metrics and actionable
  remediation guidance. The BDSA data for new vulnerabilities is reported an
  average of three weeks earlier than the NVD's reported data.
- **Component Scanning**

  Component Scanning automates the discovery and identification of OSS components in a scan to
  provide metadata such as license type, security vulnerabilities, and OSS
  project health for those components. Component scans can be linked to
  internal project versions to automatically generate BOMs.
- **Cryptography**

  Cryptography Management enables the display of cryptographic algorithms, and additional
  metadata, that are contained in open source components. This data is used to
  support compliance to security standards and legal export regulations.
- **License Management**

  License Management is the feature which allows Black Duck users to edit and
  maintain the data which can be used to create accurate and compliant open
  source notice files/reports at a Project/Release level.
- **Match as a Service**

  Match as a Service (MaaS) is a service that identifies OSS components, using data gathered
  by Component Scanning.
- **Notifications**

  Black Duck notifications alert your teams when vulnerabilities change or
  there are policy violations. Your organization can integrate with other
  platforms using the Notification API.
- **OSS Notices Report**

  The Notices Reports feature allows users to create notices (or attribution) reports for
  their projects. The notice files can then be included with the distribution
  or incorporated into documentation to satisfy the attribution obligation
  that exists in the vast majority of open source licenses.
- **Policy Management**

  The Policy Management feature enables companies to define rules to govern their use of open
  source components. With these rules, open source usage can be managed on an
  exception basis, i.e, as long as open source components meet the policy
  requirements their usage is allowed, thereby speeding time to market and
  freeing developers from a cumbersome approval process. Any open source
  components/versions that fail to meet policy are flagged, enabling a review
  process to determine if the use of the component should be allowed in the
  particular application.
- **Risk Management**

  Risk Management enables the identification, notification, and remediation of the security,
  license, and operational risks associated with the OSS components used in
  your internal projects.
- **SCM Integration**

  SCM Integration enables the configuration and authentication of Source Code Management (SCM)
  providers. It allows mapping, scanning, and management of SCM repositories
  in projects. The SCM integration feature must be enabled on your
  registration key for this to appear on the Product Registration list.
- **Snippets**

  This feature enables the option to invoke optimized scans of source files which find OSS
  usage at the file or code snippet level. These scans work in conjunction
  with a component scan to produce the best possible Bill of Materials (BOM)
  for a project. Once discovered, matches can be reviewed and added to a
  project BOM which pulls in the associated metadata for the component.
- **Vulnerability Exploitability eXchange (VEX)**

  Vulnerability Exploitability eXchange (VEX) documents are intended to communicate whether
  specific vulnerabilities in software components are exploitable in given
  product(s). This helps organizations prioritize their remediation efforts
  and gives better visibility of security risk for the associated products to
  customers.

## Updating your product registration

Your Black Duck license may restrict the number of users, projects,
and/or project versions. If you need more capacity, you can purchase a new license.
Once you receive a new license from Black Duck Software, enter the new
registration ID information in Black Duck to activate your
newly-licensed capacity.

1. Log in to Black Duck as a system administrator.
2. Click [image: image] .
3. Select **Product Registration** to open the Product Registration page.
4. Type your new registration key in the **Registration ID** field. Be sure
   that you accept the terms of the End User License Agreement.
5. Click **Save**.
