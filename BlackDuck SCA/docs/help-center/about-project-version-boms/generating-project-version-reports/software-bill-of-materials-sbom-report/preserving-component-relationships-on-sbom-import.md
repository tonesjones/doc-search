---
title: "Preserving Component Relationships on SBOM Import"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/preserving-component-relationships-on-sbom-import.html"
content_id: "KNtp_OJfr4VKrxOXF3bGaw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:56.316299+00:00"
---

# Preserving Component Relationships on SBOM Import

Black Duck SCA now preserves component relationships when importing SBOM
(Software Bill of Materials) reports. This enhancement ensures that dependency
information from imported SBOMs is retained and can be accurately reproduced when
generating new SBOM reports from your project versions.

## Why This Matters

[CISA SBOM minimum requirements](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf) mandate that
SBOMs include dependency relationship information. These relationships document how
software components are included in your application, enabling you to:

- Build accurate dependency graphs showing direct and transitive dependencies
- Perform comprehensive vulnerability impact analysis
- Conduct thorough license compliance assessments
- Document backported or forked software components

According to CISA guidelines, the Dependency Relationship element reflects how a
given software component was included in the target software. The inclusion
relationship ("includes" or "included in") supports the capability to build a
dependency graph and explicitly documents when components are derived from or are
descendants of other software.

## How It Works

When you import an SBOM report into Black Duck SCA, the system
now:

1. **Preserves Relationship Data**: Component relationships from the original
   SBOM are stored and maintained within Black Duck.
2. **Supports Multiple Relationship Types**: The system recognizes and maps
   various SPDX relationship types to Black Duck SCA usage
   types, including:

   - Dynamic and static linking
   - Source code containment
   - Prerequisites
   - Development tools
   - And more
3. **Handles Complex Scenarios**: The implementation accounts for:

   - Components with multiple parent dependencies
   - Merging relationships when multiple scans are mapped to the same project
     version
   - Preventing duplicate relationships within imported SBOMs
4. **Maintains Compatibility**: Existing functionality, including scan
   unmapping and purge operations, continues to work as expected.

## Configuration

Preserving component relationships on SBOM import is disabled by default. To
enable this feature, you must configure the following setting:

```
blackduck.scan.sbom.preserve.relationships=true
```

Once this configuration is set, Black Duck SCA will automatically
preserve relationship data from imported SBOM reports.

## SPDX Relationship Type Mappings

Black Duck SCA automatically maps SPDX relationship types to internal
usage types to ensure accurate representation:

Table 1. SPDX v2 Mappings

| SPDX v2 RelationshipType | Black Duck SCA Usage mapping |
| --- | --- |
| `DYNAMIC_LINK` | `DYNAMICALLY_LINKED` |
| `STATIC_LINK` | `STATICALLY_LINKED` |
| `CONTAINS` | `SOURCE_CODE` |
| `HAS_PREREQUISITE` | `PREREQUISITE` |
| `DEV_TOOL_OF` | `DEV_TOOL_EXCLUDED` |
| `OTHER` | Determined from the possible `RelationshipType` Comment:   - `SEPARATE WORK` →   `SEPARATE_WORK` - `MERELY AGGREGATED` →   `MERELY_AGGREGATED` - `IMPLEMENTATION OF A STANDARD` →   `IMPLEMENTATION_OF_A_STANDARD` - `UNSPECIFIED` →   `UNSPECIFIED` |
| All other types default to `DYNAMICALLY_LINKED` | |

Table 2. SPDX v3 Mappings

| SPDX v3 RelationshipType | Black Duck SCA Usage mapping |
| --- | --- |
| `HAS_DYNAMIC_LINK` | `DYNAMICALLY_LINKED` |
| `HAS_STATIC_LINK` | `STATICALLY_LINKED` |
| `CONTAINS` | `SOURCE_CODE` |
| `HAS_PREREQUISITE` | `PREREQUISITE` |
| `OTHER` | Determined from the possible `RelationshipType` Comment:   - `SEPARATE WORK` →   `SEPARATE_WORK` - `MERELY AGGREGATED` →   `MERELY_AGGREGATED` - `IMPLEMENTATION OF A STANDARD` →   `IMPLEMENTATION_OF_A_STANDARD` - `UNSPECIFIED` →   `UNSPECIFIED` |
| `USES_TOOL` with lifecycle `DEVELOPMENT` | `DEV_TOOL_EXCLUDED` |
| All other types default to `DYNAMICALLY_LINKED` | |
