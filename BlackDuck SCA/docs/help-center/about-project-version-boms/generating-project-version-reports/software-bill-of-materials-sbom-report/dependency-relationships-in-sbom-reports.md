---
title: "Dependency relationships in SBOM reports"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/dependency-relationships-in-sbom-reports.html"
content_id: "byf68HBqDszca28rFrDcrQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:54.804996+00:00"
---

# Dependency relationships in SBOM reports

Dependency relationships indicate how a component is intended to be included in the
project when this version is released. For example, if scanning identified development
tools in scanned code or a Docker image, the SBOM report will indicate that they will
not actually be included in the released version of the project.

See the table below for usage types and how they are defined in the SBOM report. Please
note that this applies only to SPDX 2.3 SBOM reports. CycloneDX SBOM reports do not
indicate the usage type in its `dependencies` section.

Table 1. Usage types

| Usage | SPDX relationship used | Description | **SPDX relationship comment** |
| --- | --- | --- | --- |
| Dynamically linked | `DYNAMIC_LINK` | Dynamically linked components that are part of the distribution package, such as with DLLs or JAR files.  For dynamically linked components that are not part of the distribution package, please choose "Prerequisite". | NONE |
| Statically linked | `STATIC_LINK` | A component that is not part of the source tree but linked into the project deliverable statically and distributed with your project. | NONE |
| Source code | `CONTAINS` | A component or snippet included in the project's source code directly. | NONE |
| Separate Work | `OTHER` | Intended for loosely-integrated components. Your work is not derived from the component. To be considered a separate work, your application has its own executables, with no linking between the component and your application. An example is including the free Acrobat PDF Viewer with your distribution media. | Separate Work |
| Prerequisite | `HAS_PREREQUISITE` | Run-time dependencies or dynamically linked components that are not part of the distribution package. | NONE |
| Merely Aggregated | `OTHER` | Intended for components that your project does not use or depend upon in any way, although they may be on the same media. For example, a sample version of an unrelated product included with your distribution. | Merely aggregated |
| Implementation of a Standard | `OTHER` | Intended for cases where you implemented according to a standard. For example, a Java spec request that ships with your project. | Implementation of a Standard |
| Dev. Tool / Excluded | `DEV_TOOL_OF` | Component will not be included in the released project. For example, a component that is used internally for building, development, or testing. Examples are unit tests, IDE files, or a compiler. | NONE |
| Unspecified | `OTHER` | The usage for this component has not yet been determined. You can use Unspecified to indicate that you need to investigate the usage of this component. | Unspecified |
