---
title: "Approved customer guidance: project size and scan capacity"
product: "blackduck-sca"
documentation_version: "2026.7"
guidance_status: "human-verified"
verified_by: "Tony"
verified_at: "2026-08-25"
source_type: "product-expert feedback; not scraped product documentation"
---

# Project size and scan capacity

Use this guidance when a customer asks whether Black Duck SCA has a strict
per-project size limit or how to handle a very large repository.

- Black Duck SCA has **not a strict per-project maximum**. Do not describe the
  10 GB statement in the project-creation documentation as a universal cap on an
  individual project.
- For a repository at or above **10-15 GB**, recommend chunking the scan into componentized modules or **subprojects** associated with a **single project version** for performance.
- Some legacy customers have a **capacity-scanning license**. For those
  entitlements, accumulated scan size is the relevant capacity measure. Direct
  the customer to the project version's **Settings > Scans** page to view usage.
- The separate, version-matched documentation page on code-size limits states
  that a configured license limit can block scanning or uploading after it is
  exceeded. Present that as entitlement-defined capacity, not as a universal
  maximum project size.
- Do not replace this customer guidance with an individual-scan size limit unless
  the customer specifically asks about that scan type.

## Customer-answer checklist

When responding to this type of question, keep all three distinctions visible:

1. State that there is **not a strict per-project maximum**.
2. Give the **10-15 GB** performance guidance and the option to use **subprojects** or componentized scans associated with a **single project version**.
3. Call out the separate, legacy **capacity-scanning license** case and its
   **Settings > Scans** usage view. Do not omit it merely because the customer
   did not state their entitlement.

## Evidence and boundaries

- Human product review supplied the absence of a universal strict per-project
  maximum, the 10-15 GB performance threshold, and the legacy
  capacity-scanning distinction.
- `docs/help-center/administering-black-duck/managing-your-code-size-limits.md`
  supports the license-defined capacity and **Settings > Scans** portions.
- `docs/help-center/about-project-version-boms/editing-a-project-version-bom/managing-subprojects.md`
  supports using subprojects to represent modules in a parent application's BOM.
