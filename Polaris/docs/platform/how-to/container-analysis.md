---
title: "Container Analysis"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/container-analysis.html"
content_id: "9ZmfvRxknA7x7HcsehuRnw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.350716+00:00"
content_hash: "01643a0a76b133f42562c168938522ce71e3bcdedbe2b423e36fdad3e4ceb793"
---

# Container Analysis

An overview of Container Analysis in Polaris.

Container Analysis enables teams to scan container images for open source risk, identifying vulnerable or license-encumbered components at the layer level. Results appear in the unified component inventory alongside findings from other SCA scan types (Package Manager, Signature Analysis, and Binary Analysis), so you can review, triage, and export a complete picture of your application's open source risk.

Container Analysis requires a Container Analysis entitlement, enabled at the organization level by an Organization Admin or Organization App Manager. See [Assign subscriptions to applications](assign-subscriptions-to-applications.md).

## Capabilities and limitations

Container Analysis:

- Runs from the Polaris UI or from Bridge CLI 4.5.0 or later.

  Note: See [Using SCA Container Scan with Bridge](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/f039b048ac944b4a6c77f5368c1fa991.topic) for more information.
- Is a standalone project type — Container Analysis projects cannot be combined with SAST & SCA or DAST projects.
- Does not support SCM integrations. Each test must be initiated manually.
- Accepts container image archives exported as .tar files using `docker save`. Uploads can be up to 10 GB per file.
- Identifies OS-layer and application-layer components, attributing each component to the container layer that introduced it.
- Results appear on the Components tab and Issues tab alongside other SCA findings.
- Triage and export workflows are consistent with other SCA tests. Container Analysis components are included in SBOM exports.
- CVE and BDSA data for detected components is updated automatically as the KnowledgeBase refreshes.

## Key concepts

Layer-level visibility
:   Container images are built in layers — typically a base OS layer, dependency layers, and application code layers stacked on top. Polaris attributes each detected component to the layer that introduced it. This helps you identify which layer is responsible for a vulnerable component so you can target the right layer when remediating risk (for example, updating the base image rather than an application dependency).

    After you run a Container Analysis test, you can view the container layers for each component on the Component Details tab, under Container Layers.

    Note: See View container layers for a component for more information.

Organizing test results
:   Each container in a project captures test results from a different image. Testing a new version of an image overwrites that container's results. At the project level, issues and components from all containers are combined, so total counts reflect all images in the project. To isolate results for a specific image, use the Container and Layer filters on the Issues and Components tabs.

`?.?` unknown version notation
:   When Polaris detects a component but cannot resolve its exact version, the version appears as `?.?` next to the component name (for example, `libssl ?.?`). CVEs and BDSAs can still be linked to components without versions. Components with an unknown version appear in SBOM exports with the version listed as unknown. If you know the correct version, you can edit the component to get more accurate vulnerability and license data. See [Edit a component](add-or-modify-components/edit-a-component.md).
