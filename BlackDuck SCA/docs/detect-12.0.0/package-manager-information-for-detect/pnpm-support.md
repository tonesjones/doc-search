---
title: "pnpm support"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pnpm-support.html"
content_id: "ZvBEQiFMwU7FXujOuBpCOA"
version: "12.0.0"
section: "Package Manager information for Detect"
scraped_at: "2026-10-04T23:33:21.154463+00:00"
content_hash: "29924f9444544420247a83cc7b3c15fe49f094543088be200f1e2a7463fe2386"
---

# pnpm support

## Related properties

Detector properties

## Overview

Detect runs the pnpm detector if it finds a pnpm-lock.yaml file in your project, and parses the file to obtain information on your project's dependencies.

To specify which types of dependencies you want Detect to exclude from the BOM (Dev and Optional dependencies) use the detect.pnpm.dependency.types.excluded property.

The pnpm detector extracts the project's name and version from the package.json file. If it does not find a package.json file, it will defer to a project name derived by git, from the project's directory, or defaults.
