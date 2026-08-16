---
title: "Binary Analysis"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/binary-analysis.html"
content_id: "5z2yLiNk690AYG5Xcqcv~w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:18.984975+00:00"
content_hash: "93a5e40aedd920cdbc5fcb6b175825b5725be1dedfce9cbe58f740e6e32095b7"
---

# Binary Analysis

An overview of Binary Analysis in Polaris.

Binary analysis enables users to identify open source risk in compiled software where source code is not available. This delivers a more complete Software Bill of Materials (SBOM) and improves visibility for managing risk across the full software lifecycle.

Binary analysis requires:

- Concurrent SCA Binary Test entitlement (alone or bundled with other types of tests).
- Bridge CLI 4.2.1 or above.

## Capabilities and limitations

Binary Scanning:

- Run binary scans directly from the CI pipeline or the Polaris UI.
- Manual tests only:
  - No SCM Integrations.
  - No automatic configurations to run every time there is an SCA scan.
  - A new test must be created with binary (not source code) files uploaded.
  - Uploads can be up to 10 GB and one binary file or a ZIP or tar file of multiple binary files.
- To view multiple binaries in a branch view, ZIP/tar the multiple binaries into one binary archive and test.
- Binary files can be included in projects or have their own projects but binary scans are run standalone and cannot be run at the same time as package/signature scans.
- Results appear in the component list and issue view alongside other SCA findings.
- Triage and export workflows are consistent with other SCA tests.
- Unlike other SCA scans, binary scans of compiled executables/libraries often generate component names, but may be unable to identify the exact version/origin. In this case, a “?.?” is after the component name. Edit the component (see [Edit a component](add-or-modify-components/edit-a-component.md)) if you know the version, to get a more complete and accurate vulnerability and license information.

**Security Data Included in Results**

Binary scans surface the following security data in Polaris:

- NVD CVE data with enhanced data from Black Duck Security Advisories (BDSA).
- Component Origins: Additional vulnerability streams like Linux distribution backport patches, Node.js and NuGet.
- Operational risk information (update guidance and transitive upgrade guidance).

  Note: Operational risk data powered by OpenHub is captured in results but not yet displayed in the Polaris UI.

**Data Not Shown**

The following data will not be displayed in Polaris at this time:

- Component Intelligence
- Rapid static scan (SAST)
- Knowledgebase encryption algorithm references

## How to view binary analysis results

To isolate binary analysis results from other test results:

- Filter issues by **Tool Type**.
- Filter components by **Match Type**.
- Go to the project's **Issues** tab and click an issue to see full CVE and BDSA data.
- Export or view results in Dashboards and Reporting (for example, binary results are included in the SBOM and Issue Summary Report).
