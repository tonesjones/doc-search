---
title: "Project size and scan capacity in SCA 2026.7"
product: "blackduck-sca"
documentation_version: "2026.7"
guidance_status: "documentation-reconciled"
verified_by: "Tony and version-matched product documentation"
verified_at: "2026-09-22"
source_type: "2026.7 Black Duck SCA documentation"
---

# Project size and scan capacity

The 2026.7 [Creating a project](../../BlackDuck%20SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md) page states that projects or applications are limited to 10GB of Managed Code base. It does not explain how that quantity is measured or whether the statement applies to every scan mode. Do not restate it as a universal limit on repository size or on each scan.

For large Signature Scanner scans, [Scanning best practices](../../BlackDuck%20SCA/docs/scanning-best-practices/scanning-best-practices-2.md) distinguishes two thresholds:

- Splitting a scan may help when the scanned project is larger than 1 GB or has more than 10,000 files. This is a recommendation, not a hard limit, and the page excludes package-manager-only scans from that advice.
- An individual scan has a stated 5 GB size limit. The page says an error appears if the scan exceeds it.

For large repositories, split Signature Scanner work into smaller scans and map them to the same project version to aggregate the results. If modules need separate management, map scans to separate project versions and assemble a parent BOM with [subprojects](../../BlackDuck%20SCA/docs/help-center/about-project-version-boms/editing-a-project-version-bom/managing-subprojects.md).

The [code-size limits](../../BlackDuck%20SCA/docs/help-center/administering-black-duck/managing-your-code-size-limits.md) page describes a separate license-defined capacity. Once the licensed limit is exceeded, Black Duck blocks scans or uploads. The project version's **Settings** > **Scans** page shows scan sizes. Do not confuse this entitlement limit with either the Managed Code base statement or the individual-scan limit.

Earlier product-expert feedback suggested splitting around 10–15 GB and said there is no universal strict per-project maximum. The cited 2026.7 pages do not establish those claims. Keep them out of a documentation-grounded answer unless separately verified for the customer's scan mode and entitlement.
