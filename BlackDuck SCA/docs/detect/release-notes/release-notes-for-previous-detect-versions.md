---
title: "Release notes for previous Detect versions"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/release-notes-for-previous-detect-versions.html"
content_id: "Nv4kn99pLo6v81SA2pPkag"
version: "11.5.1"
section: "Release Notes"
scraped_at: "2026-08-08T23:43:58.673480+00:00"
---

# Release notes for previous Detect versions

## Version 11.4.2

### Resolved issues

- (IDETECT-5136) - Validate the `quack patch` output directory only if the Quack Patch feature is enabled; otherwise, skip validation to avoid errors.

## Version 11.4.1

### Dependency Updates

- Upgraded and released Nuget Inspector version 2.6.0

## Version 11.4.0

### New features

- Support for the Conda Tree–based detector has been added. For more details, see Conda Tree.
- Support for pnpm now extends to 10.32.1.
- NuGet Solution Native Inspector now supports .slnx files.
- Added support for Bazel 9.
- PIP Native Inspector now supports Setuptools version 82.0.0.
- npm detectors now allow for aliases to be used when specifying dependencies in the package.json file.
- Ivy CLI Detector, leveraging the `ivy:dependencytree` Ant task to extract direct and transitive dependencies for Ant + Ivy projects. For further information, see Ivy (Ant) support.
- Introduced the `detect.quack.patch.output` property to control the Quack Patch output information path. If not set, the current working directory will be used as the default.
- When Detect is integrated with Black Duck® SCA version 2026.4 or later, relevant Black Duck SCA server configuration details will be retrieved for use by Detect. With this release of Detect, the Black Duck SCA server administrator can choose to set the detect.blackduck.correlated.scanning.enabled property, which will be retrieved and used if the user has not specified this property locally.

  - In future releases the retrieval of additional Black Duck SCA server properties will be supported.

### Changed features

- The default output directory of the Quack Patch feature has been updated to use a `quack-patch` subdirectory of the present working directory.

### Resolved issues

- (IDETECT-5014) npm CLI detector now handles components that do not have a version specified, preventing those components from being silently dropped from results.
- (IDETECT-4980) When `detect.clone.project.version.latest` is set to true, an INFO-level log message will be written to identify the exact project version selected as the clone source.
- (IDETECT‑4979) Updated the NuGet Inspector to prevent duplicate components from being reported which end up unversioned in the BOM.
- (IDETECT‑5058) Improved the Poetry detector to eliminate errors encountered while parsing pyproject.toml.
- (IDETECT‑5013) Fixed an issue in the signature scan fallback logic when SCA Scan Service (SCASS) is intentionally bypassed.
- (IDETECT-4993) Fixed an issue where the Go Module Detector entered an infinite loop while scanning `go.mod` files containing circular dependencies.

### Dependency Updates

- Update tomlj library to version 1.1.1.

## Version 11.3.0

### New features

- The Bazel tool has been updated to support Bzlmod. It now supports both BZLMOD (MODULE.bazel) and WORKSPACE-based projects, performs automatic mode detection, and probes the dependency graph to determine which dependency sources are present. See Bazel support for details.
- With the addition of the `detect.cargo.included.features` and `detect.cargo.disable.default.features` properties, Detect now supports Cargo features and the inclusion or exclusion of dependencies as options. See Cargo for details.

  Note: This feature is supported for Cargo CLI Detector. Cargo Lockfile Detector will log a warning if these properties are provided.
- Add support for `environment.yaml` in Detect Conda CLI Detector.
- Component Location Analysis now supports locating dependency declarations that use version range operators for npm, Yarn, and PIP. See Component Location Analysis for details.

### Changed features

- The `detect.bazel.workspace.rules` property has been deprecated and will be removed in the next major release. It is replaced by `detect.bazel.dependency.sources`. If present in the configuration, the old property will be mapped to `detect.bazel.dependency.sources`. See Bazel support for migration details.

### Resolved issues

- (IDETECT-4960) Added support for Cargo features and optional dependencies in Cargo CLI Detector, allowing precise control over which features are included in the SBOM through cargo tree command flags. See Cargo for details.
- (IDETECT-4847) Clarified that the value of `detect.container.scan.file.path` should be a local .tar file path or HTTP/HTTPS URL for a remote .tar file.
- (IDETECT-4970) Fixed an issue where a `quack-patch` output directory was created despite the feature not being enabled.

### Dependency Updates

- Released and upgraded Component Locator version 2.4.2

## Version 11.2.1

### Dependency Updates

- Project Inspector version updated to 2024.12.2

## Version 11.2.0

### New features

- Detect now supports Rush Package Manager. For details and configuration information, see: Rush Detector
- Introducing Quack Patch: An AI-assisted code patching tool integrated into Detect to help developers generate code patches for vulnerable components. For more information, see: Quack Patch Documentation
- Control over which workspace members are included or excluded during scanning is made possible by the new `detect.cargo.included.workspaces` and `detect.cargo.excluded.workspaces` properties for Cargo Detector. See Cargo for details.
- When set to true (default: false), the new `detect.cargo.ignore.all.workspaces` property allows you to completely disable workspace support. See Cargo for more information.
- `detect.nuget.inspector.path` property has been added to specify a custom path to the NuGet Inspector.

### Resolved issues

- (IDETECT-4924) Resolved an issue where Impact Analysis Scan threw errors on malformed classes; it now handles them gracefully by logging a warning, skipping the affected classes, and adding them to the scan output.
- (IDETECT-4921) Fixed upload failures in proxied environments when SCASS is enabled.
- (IDETECT-4919) Added Cargo workspace support in Cargo detectors. Detect now identifies `[workspace]` in the root `Cargo.toml` and resolves dependencies across all members using the shared `Cargo.lock`. The "Additional_components" section has been removed from SBOMs for completeness.
- (IDETECT-4860) When Component Location Analysis is enabled, the metadata section of `component-source.json` will now contain a "dependencyTrees" field from Rapid/Stateless scan results.
- (IDETECT-4923) Fixed a bug during `pyproject.toml` parsing when project name could not be derived.
- (IDETECT-4903) Resolved an issue with Detect failing to capture transitive dependencies for the npm package `pdfjs-dist@4.8.69`.

### Dependency Updates

- Updated method-analyzer-core to 1.0.7
- Upgraded and released Nuget Inspector version 2.5.0
- Upgraded Detect Alpine Docker images to 3.23 to ensure continued security compliance.

## Version 11.1.0

### New features

- The Component Location Analysis feature has been extended to support the Cargo package manager.

### Changed features

- When using the `detect.excluded.detectors` property, any fallback Detectors will now we executed if the primary Detector is excluded. Previously, entire sets of Detectors would be excluded.

### Resolved issues

- (IDETECT-4874) Improved support for multibyte characters in project names, version names, and code location names during package manager scans.
- (IDETECT-4880) The `.bridge` directory will now be excluded by default from Detector and Signature Scans.
- (IDETECT-4897) Detect now looks for headers in a case-insensitive fashion when performing multipart binary uploads.
- (IDETECT-4707) The PIP Native Inspector now appropriately handles package names containing a dot character.
- (IDETECT-4864) The UV Detector now appropriately runs even if the optional field `[tool.uv] manage = true` is not specified.
- (IDETECT-4760) Any dependencies listed in a Gradle dependency tree as a `(c)` dependency constraint will no longer be identified as dependencies unless they also appear elsewhere in the tree.

## Version 11.0.0

### New features

- When enabled, the new detect.project.deep.license property sets the Deep License Data and Deep License Data Snippet fields when creating a project. This property can also be used to update existing projects when the detect.project.version.update property is set to true.
- The new detect.project.settings property takes as input a path to a JSON file. This file allows users to pass several existing `detect.project` properties as a single argument to Detect. Detect will parse the JSON file to obtain information relevant to creating or updating projects.
- The new detect.excluded.detectors property takes as input a comma-separated list of Detector names to exclude. This allows for greater control over selection of Detectors.
- Added support for capturing dependencies from the `go.mod` file via a new buildless detector named "Go Mod File" for Go projects.

  - Added a new property detect.go.forge to customize the Go registry URL used for fetching dependency information. Defaults to `https://proxy.golang.org`.
  - Added a new property detect.go.forge.connection.timeout to customize the connection timeout limit while connecting to the Go registry. Defaults to 30 seconds.
  - Added a new property detect.go.forge.read.timeout to customize the read timeout limit while fetching go.mod file of a dependency from Go registry. Defaults to 60 seconds.

### Changed features

- ReversingLabs Scans (`detect.tools=THREAT_INTEL`) has been removed.
- The `detect.threatintel.scan.file.path` property has been removed.
- The `detect.project.codelocation.unmap` property has been removed.
- The archived phase (`detect.project.version.phase=ARCHIVED`) has been deprecated.
- The efficiency of the Detector directory evaluation has been enhanced, resulting in the acceleration of certain scans.
- Detector directory evaluation has been made more efficient, resulting in some scans being faster.
- Support for `pyproject.toml` file has been added to PIP Native Inspector. For more details, please see Python Detector page
- Support for the following package managers have been extended:

  - pip: 25.2
  - pipenv: 2025.0.4
  - Setuptools: 80.9.0
  - uv: 0.8.15
  - Maven: 3.9.11
  - Conan: 2.20.1
  - NuGet: 6.8.1
  - GoLang: 1.25
  - RubyGems: 3.7.1
  - Gradle: 9.0.0
  - Yarn: 4.9.4
  - NPM: 11.5.2

### Resolved issues

- (IDETECT-4738) Corrected behavior of `detect.binary.scan.file.name.patterns` to be case-insensitive.
- (IDETECT-4802) Fix UV Lockfile Detector not generating BDIOs for projects with non-normalized names per Python requirements.
- (IDETECT-4806) Fixed UV detectors to handle dynamic versions and cyclic dependencies.
- (IDETECT-4751) Prevent server-side parsing errors by normalizing IAC Scan `results.json` contents before uploading to Black Duck SCA.
- (IDETECT-4799) When constructing the BDIO, ignore the Go toolchain directive, as it is the Go project's build-time configuration setting and not a module dependency.
- (IDETECT-4813) Fix Gradle Native Inspector to correctly identify projects with only `settings.gradle` or `settings.gradle.kts` file in the root directory.
- (IDETECT-4812) Gradle Native Inspector now supports configuration cache (refactored `init-detect.gradle` to add support for configuration cache in Gradle projects).
- (IDETECT-4845) With added support for extracting Python package versions from direct references [PEP 508 URIs](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers) in `pyproject.toml` files, Detect now correctly parses versions from wheel and archive URLs and VCS references for impacted detectors (Setuptools CLI, Setuptools Parse, and UV Lock detectors). When data is missing or badly formatted, detectors gracefully switch back to reporting only the package name.
- (IDETECT-4810) Exclude unnecessary directories when looking for the locations of dependency declarations to enhance performance when Component Location Analysis is enabled.
- (IDETECT-4724) Updated Yarn Detector to correctly identify components that were previously unmatched.
- (IDETECT-4850) Log a warning when unsupported `PROC_MACRO` dependency exclusion is attempted with the Cargo Lockfile Detector.
- (IDETECT-4591) The logic for enabling the IAC_SCAN tool has been updated to rely solely on detect.tools and detect.tools.excluded.
- (IDETECT-4786) `BDIO` uploads will no longer retry unnecessarily when the Black Duck SCA server returns a 412 (Precondition Failed), improving scan efficiency and avoiding timeouts.

### Dependency updates

- Upgraded and released Docker Inspector version 11.6.0.
- Upgraded and released Nuget Inspector version 2.3.2.

## Version 10.7.0

### New features

- Maven CLI Detector now accepts a custom pom.xml file name (matching the pattern *pom.xml) when provided via `detect.maven.build.command`.
- Signature Scan now supports ARM architecture with correctly packaged ARM JRE for Windows, Mac, Linux, and Alpine operating systems for Black Duck® SCA version 2025.7.0 or later.

  Note: To ensure Detect correctly identifies the system architecture on ARM-based systems, please install an ARM-specific Java runtime. This is necessary for accurate detection and proper functionality on ARM platforms.
- Support for Poetry is now extended to 2.1.4.
- Detect Docker Inspector air gap distribution JAR files are now digitally signed with Black Duck Software, Inc authority.
- Detect Nuget Inspector binaries for Windows are now digitally signed with Black Duck Software, Inc authority.

### Changed features

- Yarn workspace identification and processing has been made more efficient, resulting in some scans being faster.

### Resolved issues

- (IDETECT-3456) BOM components marked as "ignored" will no longer appear in Detect risk reports.
- (IDETECT-4781) Signature Scans will no longer fail if SCA Scan Service (SCASS) related IPs are blocked. A performance warning will be printed and a non-SCASS Signature Scan will be performed.
- (IDETECT-4759) Updated Detect UV Detector to prevent execution when the `toml` file does not have a `[tool.uv]` section with `managed = true` value, and to not return a success status unless a BDIO file is generated.
- (IDETECT-4746) Fixed Cargo Lockfile Detector incorrectly labeling transitive dependencies as direct dependencies.
- (IDETECT-4728) Rapid Scans using `BOM_COMPARE_STRICT` now show a clear message if the project version doesn’t exist, guiding users to run a full scan to create it.
- (IDETECT-4736) Gradle Native Inspector no longer appends `+FAILED` suffix to unresolved dependency versions in BDIO output.

### Dependency updates

- Upgraded and released Docker Inspector version 11.5.0.
- Upgraded and released Nuget Inspector version 2.3.1.
- Updated the Black Duck Software BDIO2 protobuf library to version 3.2.12 to resolve a security vulnerability in its Google Protobuf Java library.

## Version 10.6.0

### New features

- SCA Scan Service (SCASS) is a scalable solution for performing software composition analysis scans outside of the traditional Black Duck® SCA environment. This Detect release provides support for SCA Scan Service (SCASS) package manager and signature scans when deployed with Black Duck SCA version 2025.7.0 or later. For further information see [About SCASS](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/aboutScaScanService.html).

  - To learn more about the IP address configuration requirements for your deployments, refer to the IP notice above.
- A new property, detect.stateless.policy.check.fail.on.severities has been added, which will trigger Detect to fail the scan and notify the user if a policy violation matches the configured value. This property overrides the default "Blocker" and "Critical" severity settings that cause Detect scans to exit. This property applies to both Rapid and Stateless scans. Intelligent persistent scans, (when scan mode is not set to RAPID, STATELESS, or --detect.blackduck.scan.mode is explicitly set to INTELLIGENT and scan data is persisted), should continue using the detect.policy.check.fail.on.severities, property.
- Detect will now print the names of fatal policy violations at the Detect status stage if detect.policy.check.fail.on.names is configured.
- To provide greater control over Cargo dependencies reported in the BOM, a new property, `detect.cargo.dependency.types.excluded` has been added to allow exclusion of specific Cargo dependency types (`DEV`, `BUILD`) from scans. The default behavior (`NONE`) will include all dependency types.
- Node Package Manager (npm) scans now report optional dependencies. The `detect.npm.dependency.types.excluded` property has been extended to exclude optional dependencies if OPTIONAL is specified in the list of arguments.
- Black Duck® Detect will now provide an option to generate Black Duck® SCA risk report in a parseable (JSON) format. See Risk Report Generation for more details.
- Support for SBT is now extended to 1.11.3.

### Changed features

- To improve processing time when both PNPM and NPM detectors apply to a directory, only PNPM detector will execute, producing the same quality of results.

### Resolved issues

- (IDETECT-4657) - Additional logging has been added for occurances of Detect erroring out when loading a malformed Spring Boot config file.

  Note: A valid Spring Boot config file can be specified via the `--spring.config.location=""` parameter.
- (IDETECT-4700) – Fixed Rapid Scans reporting policy violations from previous full scans when run in BOM_COMPARE or BOM_COMPARE_STRICT mode.

### Dependency updates

- Upgraded and released Detect Docker Inspector version 11.4.0.

## Version 10.5.0

### New features

- Support for UV Package Manager has been added under UV Detector
- With the `detect.clone.project.version.name` parameter specified and `detect.project.version.update` set to true, Detect will now clone, scan, and update the cloned project via parameters such as `detect.project.version.phase`.
- Support for Java 21 has been added.
- If feasible, the most probable keys are recommended in place of invalid property keys that contain misspellings or malformations.

### Changed features

- Gradle inspector script no longer requires, or includes, Gradle dependencies. This applies to both non-air gap and air gap zip generation.
- Detect will now fail the scan if `detect.wait.for.results` is set to true and a scan is not properly included in the BOM.

### Resolved issues

- (IDETECT-4177) - Detect no longer requires that the X-Artifactory-Filename header is set when specifying an internally hosted version in Black Duck® SCA.
- (IDETECT-3512) - To prevent issues when Black Duck® SCA and Detect disagree on the full list of categories, Detect now sends an indicator specifying "all categories" when detect.project.clone.categories is set to ALL.
- (IDETECT-4606) - Support for the exclusion of dependency types in Detect Nuget Inspector now includes `project.assets.json` and `project.lock.json` files.
- (IDETECT-4209) - Detect no longer creates numerous access denied exceptions in Black Duck® SCA logs when a user does not have system administrator access.
- (IDETECT-4222) Detect now reports a failure status (FAILURE_BOM_PREPARATION) when BOM preparation fails in Black Duck® SCA.

### Dependency updates

- Upgraded and released Nuget Inspector version 2.2.0.
- Upgraded and released Docker Inspector version 11.3.0.
- Updated usage of Apache Commons BeanUtils to version 1.11.0.

## Version 10.4.0

### New features

- Support for Conda has been extended to 25.1.1.
- Cargo CLI Detector, leveraging `cargo tree` to extract direct and transitive dependencies, improving accuracy over the previous flat lockfile detection. This build-based detector is triggered for Cargo projects with a `Cargo.toml` file and requires Cargo version **1.44.0+**. For further information, see Cargo package manager support.
- Added property detect.cargo.path to allow user specification of a custom Cargo executable path.
- New `detect.pnpm.included.packages` and `detect.pnpm.excluded.packages` properties for pnpm provide increased control over what directories Detect scans under a pnpm project. See the pnpm property page for more information.

### Changed features

- If the URL configured for SCA Scan Service (SCASS) is inaccessible when Detect attempts a binary or container scan, Detect will retry the scan without using SCASS.

  - See Black Duck® SCA SCA Scan Service (SCASS) notice above for information pertaining to IP addresses that require allow listing.
- ReversingLabs Scans (`detect.tools=THREAT_INTEL`) has been deprecated.
- The `detect.threatintel.scan.file.path` property has been deprecated.
- Detect will now return a unique error code `code 16 - FAILURE_OUT_OF_MEMORY` when sub processes experience "Out of memory" issues.
- PIP Native Inspector now supports Python 3.12+.

### Resolved issues

- (IDETECT-4642) - Improved handling of pnpm packages that contain detailed version information in the pnpm-lock.yaml. Resolving Detect missing some packages through failure to link direct and transitive dependencies.
- (IDETECT-4641) - Improved Detect's Yarn detector to handle non-standard version entries for component dependencies.
- (IDETECT-4602 & IDETECT-4180) - Resolved Go dependency scan issue that resulted in transitive dependencies assigned to incorrect parent. (For further details on how the Go Mod CLI detector determines parents, please see GoLang support.)
- (IDETECT-4594) - Resolved Detect failing to handle duplicate keys in `package.json` files across npm, pnpm, Lerna, and Yarn projects.
- (IDETECT-4467) - Resolved an issue where Detect would exit with a 0 (zero) success code despite dependency requirements not being met for PIP Native Inspector.

  - The PIP Native Inspector will yield to other detectors when it cannot resolve an expected dependency from the PIP cache.

### Dependency updates

- Upgraded and released Detect Docker Inspector version 11.2.0.

## Version 10.3.0

### New features

- Added support for `ArtifactsPath` and `BaseIntermediateOutputPath` properties in Black Duck® Detect NuGet Inspector. See detect.nuget.artifacts.path for more details.
- SCA Scan Service (SCASS) is a scalable solution for performing software composition analysis scans outside of the traditional Black Duck® SCA environment. This Detect release provides support for the SCA Scan Service (SCASS) for Black Duck SCA version 2025.1.1 or later. For further information see [About SCASS](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/aboutScaScanService.html).

  - See IP address notice above for details on related IP configuration for your deployments.

### Resolved issues

- (IDETECT-4610) - Improved Detect's air gap for Gradle creation script to prevent unwanted JAR files from being included in the gradle subdirectory.
- (IDETECT-4611) - Updated Detect's air gap for Gradle creation script to remove reference to Integration Common library that is no longer a dependency.
- (IDETECT-3932) - Improved the exit code and error output generated when a duplicate project name is used in simultaneous scans.
- (IDETECT-4327) - Updated the Conan 2 detector to provide log entries in case of error.

### Dependency updates

- Upgraded and released NuGet Inspector version 2.1.0.
- Upgraded to rebranded Method Analyzer Core Library version 1.0.1 for Vulnerability Impact Analysis.

## Version 10.2.1

### Resolved issues

- (IDETECT-4560) - Update the FreeMarker Template Language (FTL) script used to build the Detect air gap zips to prevent inclusion of outdated JARs.

## Version 10.2.0

### New features

- The scanCLI `detect.blackduck.signature.scanner.csv.archive` property has been added for generating and uploading CSV files to Black Duck® SCA 2025.1.0 or later. If used in offline mode, the generated CSV files will be located in the Detect run directory in the csv folder.

  Note: This feature is only available for intelligent persistence scans.

### Changed features

- Use of the --detect.yarn.ignore.all.workspaces flag is not required for Yarn 4 projects, thus configuration parameters such as detect.yarn.dependency.types.excluded=NON_PRODUCTION can be employed.

### Resolved issues

- (IDETECT-4447) - ID strings of detected Yarn project dependencies are now correctly formed. Related warning messages have been improved to identify entries in the yarn.lock file that have not been resolved through package.json files and could not be resolved with any standard NPM packages.
- (IDETECT-4533) - Resolved an issue with Detect Gradle Native Inspector causing scans to hang indefinitely when submodule has the same name as the parent module.
- (IDETECT-4560) - Updated version of Jackson-Core (a transitive dependency) to address a vulnerability.

## Version 10.1.0

### New features

- npm lockfile and shrinkwrap detectors now ignore packages flagged as extraneous in the package-lock.json and npm-shrinkwrap.json files.
- Support added for Opam Package Manager via Opam Detector.
- New Gradle Native Inspector option to only process the root dependencies of a Gradle project. See detect.gradle.root.only for more details.

### Changed features

- npm version 1 package-lock.json and npm-shrinkwrap.json file parsing has been restored.
- The `detect.project.codelocation.unmap` property has been deprecated.
- Changed Black Duck® Detect's JAR signing authority from Synopsys, Inc. to Black Duck Software, Inc.

### Resolved issues

- (IDETECT-4517) - Detect now correctly indicates a timeout failure occurred when multipart binary or container scans timeout during an upload.
- (IDETECT-4540) - Multipart binary and container scans now correctly retry when authentication errors are received during transmission.
- (IDETECT-4469) - Eliminating null (`\u0000`) and replacement (`\uFFFD`) characters during the processing of Python requirements.txt files to ensure successful extraction of dependency information.

### Dependency updates

- Upgraded and released Detect Docker Inspector version 11.1.0.
- Upgraded to Project Inspector v2024.12.1.

## Version 10.0.0

Synopsys Detect has been renamed Black Duck® Detect with page links, documentation, and other URLs updated accordingly. Update any Detect documentation, or other bookmarks you may have. See the [Domain Change FAQ](https://community.blackduck.com/s/article/Black-Duck-Domain-Change-FAQ).

- As part of this activity, sig-repo.synopsys.com and detect.synopsys.com are being deprecated. Please make use of repo.blackduck.com and detect.blackduck.com respectively.

  - After March 2025, Detect script download details will only be available via detect.blackduck.com.
  - Detect 10.0.0 will only work when using repo.blackduck.com.

Note: It is recommended that customers continue to maintain sig-repo.synopsys.com, and repo.blackduck.com on their allow list until March 31st, 2025 when sig-repo.synopsys.com will be fully replaced by repo.blackduck.com.

### New features

- The npm package.json detector now performs additional parsing when attempting to find dependency versions. This can result in additional matches since versions like `^1.2.0` will now be extracted as `1.2.0` instead of as the raw `^1.2.0` string. In the case where multiple versions for a dependency are discovered, the earliest version will be used.
- Support for Python has now been extended with Pip 24.2, Pipenv 2024.0.1, and Setuptools 74.0.0.
- Support for npm has been extended to 10.8.2 and Node.js 22.7.0.
- Support for Maven has been extended to 3.9.9.
- Support for pnpm has been extended to 9.0.
- Support for BitBake is now extended to 2.8.0 (Yocto 5.0.3)
- Support for Nuget has been extended to 6.11.
- Support for GoLang is now extended to Go 1.22.7.
- Correlated Scanning is a new Match as a Service (MaaS) feature which correlates match results from Package Manager (Detector), and Signature scans when running Detect with Black Duck® SCA 2024.10.0 or later.

  - Correlation between scanning methods increases accuracy and provides for more comprehensive scan results.
    See the detect.blackduck.correlated.scanning.enabled property for more information

    Note: Correlated Scanning support is available for persistent Package Manager and Signature Scanning only.
- Detect now supports container scanning of large files via a chunking method employed during upload.

  Note: This feature requires Black Duck® SCA 2024.10.0 or later.

### Changed features

- The `logging.level.com.synopsys.integration` property deprecated in Detect 9.x, has been removed. Use `logging.level.detect` instead.
- The FULL_SNIPPET_MATCHING and FULL_SNIPPET_MATCHING_ONLY options for the `detect.blackduck.signature.scanner.snippet.matching` property deprecated in Detect 9.x, have been removed.
- The `.blackduck` temporary folder has been added to the default exclusion list.

### Dependency updates

- Updated jackson-core library to version 2.15.0 to resolve a security vulnerability.
- Upgraded and released Nuget Inspector version 2.0.0.
- Upgraded and released Detect Docker Inspector version 11.0.1

## Version 9.10.1

Notice: `sig-repo.synopsys.com` and `detect.synopsys.com` are being deprecated. Please make use of `repo.blackduck.com` and `detect.blackduck.com` respectively.

- After February 2025, Detect script download details will only be available via detect.blackduck.com.
- See the [Domain Change FAQ for the deprecation of sig-repo](https://community.blackduck.com/s/question/0D5Uh00000Jq18XKAR/black-duck-sca-and-the-impact-of-decommissioning-of-sigrepo).

  Important: It is essential to update to 9.10.1 before sig-repo is decommissioned.

Note: It is recommended that customers continue to maintain `sig-repo.synopsys.com`, and `repo.blackduck.com` on their allow list until February 2025 when `sig-repo.synopsys.com` will be fully replaced by `repo.blackduck.com`.

### Changed features

- Adds logic to pull necessary artifacts from the repo.blackduck.com repository. If this is not accessible, artifacts will be downloaded from the sig-repo.synopsys.com repository.

## Version 9.10.0

### Changed features

- The `logging.level.com.synopsys.integration` property has been deprecated in favor of `logging.level.detect` and will be removed in 10.0.0.

  Note: There is no functional difference between the two properties.
- Switched from Universal Analytics to Google Analytics 4 (GA4) as our phone home analytics measurement solution.
- In 9.9.0 the ability to perform multipart uploads for binary scans was added where related properties were not configurable at runtime. As of this release an optional environment variable setting the upload chunk size has been made available. This variable is primarily intended for troubleshooting purposes. See Environment variables.

### Dependency updates

- Detect Docker Inspector version updated to 10.2.1

## Version 9.9.0

### New features

- Detect now supports binary scanning of large files via a chunking method employed during upload. Testing has confirmed successful upload of 20GB files.

  Note: This feature requires Black Duck 2024.7.0 or later.

### Changed features

- When running Synopsys Detect against a Black Duck instance of version 2024.7.0 or later, the Scan CLI tool download will use a new format for the URL.

  - Current URL format: https://<BlackDuck_Instance>/download/scan.cli-macosx.zip
  - New URL format: https://<BlackDuck_Instance>/api/tools/scan.cli.zip/versions/latest/platforms/macosx

### Resolved issues

- (IDETECT-4408) - Remediated vulnerability in Logback-Core library to resolve high severity issues [CVE-2023-6378](https://nvd.nist.gov/vuln/detail/CVE-2023-6378) and [CVE-2023-6481](https://nvd.nist.gov/vuln/detail/CVE-2023-6481).

### Dependency updates

- Component Location Analysis version updated to 1.1.13
- Project Inspector version updated to 2024.9.0
- Logback Core version updated to 1.2.13

## Version 9.8.0

### New features

- Autonomous Scanning - this new feature simplifies default analysis of source and binary files by allowing Synopsys Detect to handle, and easily repeat, basic analysis decisions.
  See Autonomous Scanning for further information.

### Resolved issues

- (IDETECT-4315) A filter was added to prevent performance issues related to the Synopsys Detect API call that retrieves role information on startup.
- (IDETECT-4360) Resolved an issue with component location analysis failing with an index out of bounds exception when attempting to extract certain code substrings.

## Version 9.7.0

### New features

- Support for GoLang is now extended to Go 1.22.2.
- Synopsys Detect now allows exclusion of development dependencies when using the Poetry detector. See the detect.poetry.dependency.groups.excluded property for more information.
- Support has been added for Python package detection via [Setuptools](https://setuptools.pypa.io/en/latest/index.html), versions 47.0.0 through 69.4.2. See the Python Package Managers page for further details.
- Added Docker 25 and 26 support to Docker Inspector.

### Resolved issues

- (IDETECT-4341) The Poetry detector will now recognize Python components with case insensitivity.
- (IDETECT-3181) Improved Eclipse component matching implementation through better handling of external identifiers.
- (IDETECT-3989) Complete set of policy violations, regardless of category, now printed to console output.
- (IDETECT-4353) Resolved issue of including "go" as an unmatched component for Go Mod CLI Detector.

## Version 9.6.0

### New features

- ReversingLabs Scans - this new feature provides analysis of software packages for file-based malware threats.
- Component Location Analysis upgraded to certify support for location of components in Yarn Lock and Nuget Centralized Package Management files.
- Added support for Gradles rich model for declaring versions, allowing the combination of different levels of version information. See rich version declarations.

### Resolved issues

- (IDETECT-4211) Resolved an error handling issue with the scan retry mechanism when the git SCM data is conflicting with another already scanned project.
- (IDETECT-4263) Remediated the possibility of Detect sending Git credentials to Black Duck Projects API in cases when the credentials are present in the Git URLs.

## Version 9.5.0

### New features

- Synopsys Detect now includes the Maven embedded or shaded dependencies as part of the Bill of Materials (BOM) via the property --detect.maven.include.shaded.dependencies. See the detect.maven.include.shaded.dependencies property for more information.
- Synopsys Detect Maven Project Inspector now supports the exclusion of Maven dependencies having "<exclude>" tags in the pom file.
- Synopsys Detect Maven Project Inspector and Gradle Project Inspector honours effects of dependency scopes during dependency resolution.

### Dependency updates

- Upgraded Project Inspector to version 2024.2.0. Please refer to Maven, Gradle and Nuget documentation for more information on the changes.
  As of version 9.5.0 Synopsys Detect will only be compatible with, and support, Project Inspector 2024.2.0 or later.

## Version 9.4.0

### New features

- Nuget Inspector now supports the exclusion of user-specified dependency types from the Bill of Materials (BOM) via the Detect property --detect.nuget.dependency.types.excluded. See the detect.nuget.dependency.types.excluded property for more information.
- A new detector for Python packages has been added. The PIP Requirements File Parse is a buildless detector that acts as a LOW accuracy fallback for the PIP Native Inspector. This detector is triggered for PIP projects that contain one or more requirements.txt files if Detect does not have access to a PIP executable in the environment where the scan is run.

  - See PIP Requirements File Parse.
- To improve Yarn detector performance a new parameter is now available. The `--detect.yarn.ignore.all.workspaces` parameter enables the Yarn detector to build the dependency graph without analysis of workspaces. The default setting for this parameter is false and must be set to true to be enabled. This property ignores other Yarn detector properties if set.

  - See Yarn support.
- Support for BitBake is now extended to 2.6 (Yocto 4.3.2).
- Support for Yarn extended to include Yarn 3 and Yarn 4.

### Changed features

- Key-value pairs specified as part of the `detect.blackduck.signature.scanner.arguments` property will now replace the values specified elsewhere, rather than act as additions.

### Resolved issues

- (IDETECT-4155) Improved input validation in Component Location Analysis.
- (IDETECT-4187) Removed references to 'murex' from test resources.
- (IDETECT-4207) Fixed Nuget Inspector IndexOutofRangeException for cases of multiple `Directory.Packages.props` files.
- (IDETECT-3909) Resolved an issue causing ASM8 Error when running Vulnerability Impact Analysis.

### Dependency updates

- Released and Upgraded Nuget Inspector to version 1.3.0.
- Released and Upgraded Detect Docker Inspector to version 10.1.1.

## Version 9.3.0

### Changed features

- Any arguments that specify the number of threads to be used provided as part of the `detect.maven.build.command` Synopsys Detect property will be omitted when executing the Maven CLI.

### Resolved issues

- (IDETECT-4164) Improved Component Location Analysis parser support for package managers like Poetry that employ variable delimiters, for better location accuracy.
- (IDETECT-4171) Improved Component Location Analysis data validation support for package managers like NPM.
- (IDETECT-4174) Resolved an issue where Synopsys Detect was not sending the container scan size to Black Duck server, resulting in Black Duck's "Scans" page reporting the size as zero.
- (IDETECT-4176) The FULL_SNIPPET_MATCHING and FULL_SNIPPET_MATCHING_ONLY options, currently controlled via registration key, for the --detect.blackduck.signature.scanner.snippet.matching property are deprecated and will be removed in the next major release of Synopsys Detect.

### Dependency updates

- Updated Guava library from 31.1 to 32.1.2 to resolve high severity [CVE-2023-2976](https://nvd.nist.gov/vuln/detail/CVE-2023-2976).

## Version 9.2.0

### New features

- Support for pnpm is now extended to 8.9.2.
- Nuget support extended to version 6.2 with Central Package Management now supported for projects and solutions.
- Support for Conan is now extended to 2.0.14.
- Support for Go and Python added to Component Location Analysis.

### Changed features

- pnpm 6, and pnpm 7 using the default v5 pnpm-lock.yaml file, are being deprecated. Support will be removed in Synopsys Detect 10.

### Resolved issues

- (IDETECT-3515) Resolved an issue where the Nuget Inspector was not supporting "<Version>" tags for "<PackageReference>" on the second line and was not cascading to Project Inspector in case of failure.

### Dependency updates

- Released and Upgraded Nuget Inspector to version 1.2.0.

## Version 9.1.0

### New features

- Container Scan. Providing component risk detail analysis for each layer of a container image, (including non-Linux, non-Docker images). Please see Container Scan for details.

  Restriction: Your Black Duck server must have Black Duck Secure Container (BDSC) licensed and enabled.
- Support for Dart is now extended to Dart 3.1.2 and Flutter 3.13.4.
- Documentation for CPAN Package Manager and BitBucket Integration has been added.

### Changed features

- When Black Duck version 2023.10.0 or later is busy and includes a retry-after value greater than 0 in the header, Synopsys Detect will now wait the number of seconds specified by Black Duck before attempting to retry scan creation.

  - Synopsys Detect 9.1.0 will not retry scan creation with versions of Black Duck prior to 2023.10.0

### Resolved issues

- (IDETECT-3843) Additional information is now provided when Synopsys Detect fails to update and Synopsys Detect is internally hosted.
- (IDETECT-4056) Resolved an issue where no components were reported by CPAN detector.
  If the cpan command has not been previously configured and run on the system, Synopsys Detect instructs CPAN to accept default configurations.
- (IDETECT-4005) Resolved an issue where the location is not identified for a Maven component version when defined as a property.
- (IDETECT-4066) Resolved an issue of incorrect TAB width calculation in Component Locator.

### Dependency updates

- Upgraded Synopsys Detect Alpine Docker images (standard and buildless) to 3.18 to pull the latest curl version with no known vulnerabilities.
- Removed curl as a dependency from Synopsys Detect Ubuntu Docker image by using wget instead of curl.

## Version 9.0.0

### New features

- Support for npm is now extended to npm 9.8.1.
- Support for npm workspaces.
- Lerna projects leveraging npm now support npm up to version 9.8.1.
- Support for Gradle is now extended to Gradle 8.2.
- Support for GoLang is now extended to Go 1.20.4.
- Support for Nuget package reference properties from Directory.Build.props and Project.csproj.nuget.g.props files.

### Changed features

- The `detect.diagnostic.extended` property and the -de command line option, that were deprecated in Synopsys Detect 8.x, have been removed. Use `detect.diagnostic`, and the command line option -d, instead.
- The Ephemeral Scan Mode, that was deprecated in Synopsys Detect 8.x, has been removed in favor of Stateless Scan Mode. See the Stateless Scans page for further details.
- npm 6, which was deprecated in Synopsys Detect 8.x, is no longer supported.
- The detectors[N].statusReason field of the status.json file will now contain the exit code of the detector subprocess command in cases when the code is non-zero.
  In the case of subprocess exit code 137, the detectors[N].statusCode and detectors[N].statusReason fields will be populated with a new status indicating a likely out-of-memory issue.
- In addition to node_modules, bin, build, .git, .gradle, out, packages, target, the Gradle wrapper directory `gradle` will be excluded from signature scan by default. Use
  detect.excluded.directories.defaults.disabled to disable these defaults.
- Removed reliance on Synopsys Detect libraries for init-detect.gradle script to prevent them from being included in the Gradle dependency verification of target projects.

  Notice: Synopsys Detect 7.x has entered end of support. See the [Product Maintenance, Support, and Service Schedule page](https://sig-product-docs.synopsys.com/bundle/blackduck-compatibility/page/topics/Support-and-Service-Schedule.html) for further details.

### Resolved issues

- (IDETECT-3821) Detect will now capture and record failures of the Signature Scanner due to command lengths exceeding Windows limits. This can happen with certain folder structures when using the `detect.excluded.directories` property.
- (IDETECT-3820) Introduced an enhanced approach to NuGet Inspector for handling different formats of the `project.json` file, ensuring compatibility with both old and new structures.
- (IDETECT-4027) Resolved a problem with the npm CLI detector for npm versions 7 and later, which was causing only direct dependencies to be reported.
- (IDETECT-3997) Resolved npm package JSON parse detector issue of classifying components as RubyGems instead of npmjs.
- (IDETECT-4023) Resolved the issue of Scan failure if Project level "Retain Unmatched File Data" not set for "System Default".

### Dependency updates

- Released and Upgraded Project Inspector to version 2021.9.10.
- Released and Upgraded Nuget Inspector to version 1.1.0.
- Fixed EsotericSoftware YAMLBeans library version to resolve critical severity [CVE-2023-24621](https://nvd.nist.gov/vuln/detail/CVE-2023-24621)
