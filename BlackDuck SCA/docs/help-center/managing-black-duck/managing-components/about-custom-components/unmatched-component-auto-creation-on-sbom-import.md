---
title: "Unmatched component auto-creation on SBOM import"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/unmatched-component-auto-creation-on-sbom-import.html"
content_id: "7q8Go3CH4iMJp2MAH2uYxg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:14.898122+00:00"
---

# Unmatched component auto-creation on SBOM import

In an SBOM
management workflow, the SBOM is the input and all of the components included in the
SBOM need to be persisted in the SBOM management solution so that visibility isn't lost,
regardless if there is a match to the KnowledgeBase. This feature provides the option to
automatically populate unmatched
components in the BOM with
custom components of the same name
in an SBOM import.

To use unmatched component auto-creation:

1. Log in to Black Duck SCA.
2. Click [image: image] .
3. Click the **Upload File** button and select either **SBOM-SPDX** or
   **SBOM-CycloneDX**.
4. Upload the SBOM
   file(s).
5. Check the **Unmatched Component Auto-Creation** checkbox at the bottom of the
   Upload SBOM dialog box.
6. Map the scan to a
   project or create a new project for the scan.

Important: Components in the SBOM import must have an associated package URL
(PURL) in order to be automatically populated in the BOM.

Tip: Unmatched components will automatically use the default license as
configured in the System Settings.

## Viewing auto-populated components in the BOM

Once your scan is mapped to a project, you can view the BOM by clicking the project's
name in the **Mapped To** column of the Scans page or by navigating to the
project on the Dashboard. Unmatched components that have been auto-populated will be
included in the BOM report and can be found by using the Source/Type → Custom
component filter on the project version page.
