---
title: "Project size and scan capacity in SCA 2026.7"
product: "blackduck-sca"
documentation_version: "2026.7"
guidance_status: "user-observed-and-documentation-reconciled"
verified_by: "Tony, SCA v2026.7.0 Product Registration screenshot, and version-matched documentation"
verified_at: "2026-09-22"
source_type: "user-provided SCA UI screenshot and 2026.7 documentation"
---

# Project size and scan capacity

Limits depend on the customer's license. The user-provided SCA v2026.7.0 **Product Registration** screenshot shows **Unlimited Codebase Size** and **Maximum of 21.00 GB scan size per Scan** for this sandbox. These values describe this registration, not every customer.

The 2026.7 [Creating a project](../../BlackDuck%20SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md) page states that projects or applications are limited to 10GB of Managed Code base. That number does not match the sandbox's registration. Do not present it as a universal project limit.

For large Signature Scanner scans, [Scanning best practices](../../BlackDuck%20SCA/docs/scanning-best-practices/scanning-best-practices-2.md) distinguishes two thresholds:

- Splitting a scan may help when the scanned project is larger than 1 GB or has more than 10,000 files. This is a recommendation, not a hard limit, and the page excludes package-manager-only scans from that advice.
- The page states a 5 GB individual-scan limit. The sandbox's registration instead shows 21.00 GB per scan. Check the customer's registration before treating either number as their limit.

For large repositories, split Signature Scanner work into smaller scans and map them to the same project version to aggregate the results. If modules need separate management, map scans to separate project versions and assemble a parent BOM with [subprojects](../../BlackDuck%20SCA/docs/help-center/about-project-version-boms/editing-a-project-version-bom/managing-subprojects.md).

The [code-size limits](../../BlackDuck%20SCA/docs/help-center/administering-black-duck/managing-your-code-size-limits.md) page says Black Duck blocks scans or uploads after a licensed code-size limit is exceeded. Check **System Settings** > **Product Registration** for the customer's licensed limits. The project version's **Settings** > **Scans** page shows scan sizes.

Earlier product-expert feedback suggested splitting around 10–15 GB. Treat that as performance advice, not a product limit or a substitute for the customer's registration.
