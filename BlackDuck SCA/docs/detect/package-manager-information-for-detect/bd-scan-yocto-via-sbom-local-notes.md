---
title: "bd_scan_yocto_via_sbom (community tool, local notes)"
source_url: "https://github.com/blackducksoftware/bd_scan_yocto_via_sbom"
content_id: "local-bd-scan-yocto-via-sbom"
version: "1.4.3"
section: "Package Manager information for Detect"
scraped_at: "2026-08-19T00:00:00.000000+00:00"
local_addition: true
note: >
  This topic is NOT scraped from docs.blackduck.com. It documents a separate
  Black Duck-authored community/support utility hosted on GitHub
  (blackducksoftware/bd_scan_yocto_via_sbom), distinct from Detect's built-in
  BitBake detector described in bitbake-support.md. It is provided under the
  MIT license, for existing Black Duck SCA customers. Treat as a
  secondary/community reference, not official docs.blackduck.com
  documentation — cross-check against the GitHub README before relying on any
  flag not also confirmed there, since the tool evolves independently of the
  Detect/SCA doc release cycle.
---

# bd_scan_yocto_via_sbom (community tool, local notes)

> Source: https://github.com/blackducksoftware/bd_scan_yocto_via_sbom — not scraped
> from docs.blackduck.com. See frontmatter `note` field.

## Purpose

A Python utility that builds a more complete Black Duck SCA project for a
Yocto build than Detect's [BitBake detector](bitbake-support.md) can alone.
It generates an SPDX SBOM from the Yocto build and applies several
identification techniques, then uploads the result to Black Duck SCA.

## Why it exists — gaps in Detect's BitBake detector

Per the tool's README, Detect's BitBake detector "will only identify standard
recipes from OpenEmbedded.org" and does **not** cover:

- Modified or custom recipes
- Recipes moved to new layers, or with changed versions/revisions
- Custom kernel identification or kernel vulnerability mapping
- Copyright and deep license data
- Snippet or code scanning within custom recipes

`bd_scan_yocto_via_sbom` closes these gaps by:

- Generating an SPDX SBOM from build artifacts
- Cross-referencing recipes against the OpenEmbedded.org API to catch
  renamed/moved recipes
- Signature scanning unmatched packages
- Optional CPE lookups or custom component creation
- Applying locally-patched CVE data
- Optionally filtering kernel vulnerabilities based on actually-compiled
  kernel modules

## Installation

```bash
pip3 install bd_scan_yocto_via_sbom --upgrade
```

Or build from source:

```bash
git clone https://github.com/blackducksoftware/bd_scan_yocto_via_sbom
cd bd_scan_yocto_via_sbom
python3 -m build
pip3 install dist/bd_scan_yocto_via_sbom-1.0.X-py3-none-any.whl --upgrade
```

## Running

```bash
bd-scan-yocto-via-sbom PARAMETERS
```

or, if running from a clone without installing as a package:

```bash
python3 PATH_TO_REPOSITORY/run.py PARAMETERS
```

Minimum required parameters:

```bash
bd-scan-yocto-via-sbom \
  --blackduck_url BD_URL \
  --blackduck_api_token BD_API \
  -p BD_PROJECT \
  -v BD_VERSION \
  -t YOCTO_TARGET
```

## Key CLI flags

| Flag | Description |
|------|-------------|
| `--modes MODES` | Comma-delimited list from `ALL, DEFAULT, OE_RECIPES, IMAGE_MANIFEST, SIG_SCAN, SIG_SCAN_ALL, CVE_PATCHES, CPE_COMPS, CUSTOM_COMPS, KERNEL_VULNS`. Default (unspecified): `OE_RECIPES,SIG_SCAN,CVE_PATCHES` |
| `--oe_data_folder FOLDER` | Caches ~300MB of OpenEmbedded.org data for reuse across runs |
| `--max_oe_version_distance X.X.X` | Enables fuzzy version matching against OE data |
| `--recipe_report REPFILE` | Outputs a matched/unmatched recipe report |
| `--exclude_recipes` / `--exclude_layers` | Comma-delimited exclusion lists |
| `--filter_recipes_by_licenses EXPR` | Skip recipes matching license substrings (new in v1.4.3) |
| `--ignore_licenses` | Bypasses SPDX license validation for custom components |
| `--kernel_recipe RECIPE_NAME` | Override the default `linux-yocto` kernel recipe name |
| `--skip_bitbake` | Run without direct build access (requires `-l` and `--bitbake_layers_file`) |
| `--task_depends_dot_file FILE` | Process dev dependencies via `bitbake -g` output |
| `--unmap` | Unmap previous code locations on rescan (default: no unmap) |

## Prerequisites

- Yocto v2.1+
- Python 3.10+
- Black Duck SCA server 2024.7+ (note: this repo's minimum version is newer
  than the pinned corpus version footer would otherwise suggest checking —
  confirm against the current SCA server version in use)
- API token with Global Code Scanner + Global Project Manager roles (or
  equivalent project-level roles)
- Single-target BitBake configurations only — "Run this utility on one
  target at a time"
- SPDX-compliant license entries in manifest files (required for SBOM upload)

## Key limitations

- Custom components created via `--modes CUSTOM_COMPS` carry no
  vulnerability data and are effectively permanent — they "cannot be easily
  deleted from the BD server once created without deleting all projects
  where referenced"
- CPE-based matching only works for components with published CPEs, which
  generally requires the component to already have reported vulnerabilities
- The "Unmatched IDs" count shown in the BD project UI only reflects the
  first-stage `OE_RECIPES` scan — it should not be used to judge scan
  completeness if other modes were also run
- Running with `--skip_bitbake` disables signature scanning, CVE patching,
  and kernel vulnerability analysis
- Setting `--max_oe_version_distance` too high risks matching against older
  recipe versions with inaccurate vulnerability data

## When to use this vs. the BitBake detector

- Use Detect's [BitBake detector](bitbake-support.md) for a standard
  recipe/layer-level BOM of a Yocto image — it is the built-in, documented
  path and sufficient when your layers are all standard OpenEmbedded.org
  recipes.
- Reach for `bd_scan_yocto_via_sbom` when you need deeper coverage: custom
  or modified recipes, moved/relayered recipes, kernel-specific
  vulnerability filtering, copyright/license depth, or snippet scanning
  inside custom recipes — cases the BitBake detector's recipe-metadata walk
  does not reach.
- Neither tool inspects the actual C/C++ source compiled by a custom
  in-house recipe for vendored/copied OSS code the way the
  [Black Duck C/CPP tool](../../c-cpp-tool/black-duck-c-cpp-tool.md) does;
  that remains a separate, third option if source-level scanning of a
  specific recipe's build is needed.
