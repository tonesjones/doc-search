---
title: "Hosted vs Air-gapped KnowledgeBase"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/hosted-vs-air-gapped-knowledgebase.html"
content_id: "R83H9cEy4LN57W8deig~tQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:25.317481+00:00"
---

# Hosted vs Air-gapped KnowledgeBase

Notice: This is a non-exhaustive list and any feature not explicitly listed may
not be available for air-gapped KnowledgeBase installations.

## Core features & scanning techniques

| Feature | Included in Hosted | Included in Air-gapped | Notes |
| --- | --- | --- | --- |
| Policies | [image: image] | [image: image] | The Policy Management feature enables you to create rules to govern your use of open source components. With policy rules, open source usage can be managed on an exception basis – as long as open source components meet the policy requirements their usage is allowed. Any open source components/versions that fail to meet your policy rules are flagged, enabling you to review and determine if the use of the component should be allowed in the particular application. |
| Signature scanning | [image: image] | [image: image] | Signature scanning scans an arbitrary file system directory or archive and matches to known components in the Black Duck KnowledgeBase. The core concept behind component scanning and discovery is the ability to compare the signatures of artifacts in the repository with the signatures of all OSS components in the Black Duck KB and quickly recognize a match. |
| Package manager scanning | [image: image] | [image: image] | Uses the project's package manager to derive the hierarchy of dependencies known to that package manager. |
| Snippet scanning | [image: image] | [image: image] | Snippet matching is beneficial to managing legal risk and detecting possible license infringement. A snippet match occurs when a portion of code in your file matches code in one or more KnowledgeBase files. |
| Binary scanning | [image: image] | [image: image] | Binary scanning identifies the open-source security, compliance, and quality risks in the software libraries, executables, and vendor-supplied binaries in use within your codebase. |
| Black Duck Secure Container scans | [image: image] | [image: image] | When scanning a container using this feature, Black Duck creates a new type of project that manages a new container scan. The container project displays the aggregated BOM and risk, but it also provides a way to view risk layer by layer, specifically adding support for components that are added or removed on a layer. |
| Vulnerabilities | [image: image] | [image: image] | Vulnerability information, triaging and management features are available in Black Duck. |
| Real time updates | [image: image] | [image: image] | Update of the hosted KB is done in real-time so new vulnerabilities or components appears continuously. With an air-gapped KB, new vulnerabilities and components only appear when the KB update is performed. |

## License text and copyright text

| Feature | Included in Hosted | Included in Air-gapped | Notes |
| --- | --- | --- | --- |
| Template license text | [image: image] | [image: image] | Each license comes with a template version of the license. |
| Local license text scan | [image: image] | [image: image] | The license search feature to search for license text in your projects. This helps with the reconstruction of the specific custom license text which might be contained in the project source files. See License Detection for more information. |
| Local copyright text scan | [image: image] | [image: image] | By enabling detection of copyright data when scanning code, users focused on license compliance can reduce license compliance risks by detecting and managing open source software and proprietary copyrights statements.  With this feature, Black Duck performs a search for copyright string text and displays the text found in the Source tab. See Copyright Detection for more information. |
| Actual license text | [image: image] | [image: image] | Black Duck KnowledgeBase provides the actual license text contained in each version of every component. No big data is shipped with air-gapped KnowledgeBase. |
| Full copyrights | [image: image] | [image: image] | Black Duck manages copyright statements by the origin name/ID for a component version. Using this feature makes it easier for you to include the full list of copyright holders for the open source components you use in your notices file report. No big data is shipped with air-gapped KnowledgeBase. |
| Deep License data | [image: image] | [image: image] | Black Duck displays declared licenses for the components in your BOM. However, deep licenses (also known as sub-licenses or embedded licenses) may also exist in your open source components. Deep license data is not enabled by default. No big data is shipped with air-gapped KnowledgeBase. |

## Cloud scanning services & specific match features

| Feature | Included in Hosted | Included in Air-gapped | Notes |
| --- | --- | --- | --- |
| SCA Scan Service | [image: image] | Coming in 2026 | SCA Scan Service (SCASS) is a scalable solution for performing software composition analysis scans outside of the traditional Black Duck SCA environment. SCASS supports Package Manager and Signature Scans, making it a versatile choice for various scanning needs. |
| Match as a Service (MaaS) | [image: image] | [image: image] | Match as a Service (MaaS) is a cloud service that identifies OSS components, using data gathered by Component Scanning. MaaS moves the matching logic from the Black Duck server to the KB server for efficiency. |
| Scan correlation | [image: image] | [image: image] | Correlated Scanning is a scanning method which allows different matching technologies to scan the same application target and correlate results together to perform more accurate component and component version matching. |
| AI Model Scanning | [image: image] | [image: image] | AI Model Scanning enables organizations to maintain visibility into the AI models they use, monitor associated risks, and ensure compliance with relevant policies. |

## External integrations

| Feature | Included in Hosted | Included in Air-gapped | Notes |
| --- | --- | --- | --- |
| SCM Onboarding | [image: image] | [image: image] | SCM repository auto-scanning allows Black Duck to check daily for any changes such as commits, pushes, or merges in the repository branch mapped to your SCM projects and perform scans if changes were made. |
| Artifactory Integration | [image: image] | [image: image] | BD SCA can be integrated with Artifactory to scan the assets for OSS. Artifactory Integration automatically blocks downloads from scanned Artifactory Repositories that have a Black Duck Policy Violation. |

## Other features

| Feature | Included in Hosted | Included in Air-gapped | Notes |
| --- | --- | --- | --- |
| Stateless signature scanning | [image: image] | [image: image] | Stateless Scan is a scan mode that does not create or use any permanent storage within Black Duck, thus there is no bill of material (BOM) stored. It is used to quickly find policy violations within the designated scan target. |
| Auto BOM re-computation (components) | [image: image] | [image: image] | When the KnowledgeBase (KB) is updated, Black Duck automatically refreshes vulnerability and component information. For air-gapped KB deployments, this refresh is not automatic—projects must be re-scanned or scans manually unmapped and remapped after KB updates to trigger a data refresh. |
