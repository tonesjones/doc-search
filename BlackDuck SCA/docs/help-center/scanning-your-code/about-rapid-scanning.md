---
title: "About Rapid Scanning"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-rapid-scanning.html"
content_id: "5XDFLC8D~R7ZNsbOxpL~eQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:32.174604+00:00"
---

# About Rapid Scanning

Black Duck's Rapid Scanning provides a way for developers to quickly determine if the
versions of open source components included in a project violate corporate policies
surrounding the use of open source. Using Black Duck Detect, Rapid Scanning
quickly returns results as it only employs package manager scanning and does not
interact with the Black Duck server database. Use Rapid Scanning when you need quick
feedback and when persisting the data in Black Duck is not necessary.

Using Rapid Scanning enables you to run thousands of scans while eliminating the need to
deploy additional instances of Black Duck. It provides you with actionable results (such
as failing the build) that can be used without a project version or without access to
Black Duck's user interface.

Results are printed as part of Black Duck Detect's normal log-style output. If there are
policy violations, the output from Rapid Scanning lists the components with at least one
policy violation, providing information such as the component name, version, component
identifier, and policy name so that you can easily determine the component that is
violating a policy.

Note that you can use a Black Duck Detect property to save the results as a
.`json` file, as described below.

When a policy violation is found, the developer can:

- replace the triggering component with a component that does not violate
  policies.
- obtain an exception for the violation with the policy being modified to exclude
  the violating component. currently,
  that exclusion is global, but by GA (and possibly by 2021.4.0) it can be
  made project specific.

For Rapid Scanning:

- Ensure that the user running Rapid Scanning has the ability to invoke Black Duck Detect.
- Ensure that your Black Duck system meets the system requirements needed to run
  Rapid Scanning.
- Create policy rules that will be triggered when a scan violates the rule. While policy rules are not
  required to run Rapid Scans, Rapid Scans only reports policy violations, and
  therefore are necessary for the successful use of Rapid Scanning.

  Policy rules can apply to all projects or a subset of projects.

  To use Rapid Scan to fetch all vulnerabilities regardless of policies, simply
  create a single policy, setting the condition severity >=0.

  Supported policy conditions are:

  Component properties:

  - Component (all versions or a specific version)
  - Component Approval Status
  - Component Modified
  - Component Modification
  - Component Purpose
  - Component Usage
  - Component Version Approval Status
  - Match Type
  - Newer Version Count
  - Review Status
  - Unknown Component Version

  Licenses:

  - Licenses (Declared)
  - License Expiration Date (Declared)
  - License Family (Declared)
  - License Risk
  - License Status (Declared)
  - Unfulfilled License Terms

  Operational:

  - Component Release Date
  - Commits in the past year
  - Contributors in the past year

  Vulnerabilities

  - Critical Severity Vulnerability Count
  - High Severity Vulnerability Count
  - Medium Severity Vulnerability Count
  - Low Severity Vulnerability Count
  - Highest Vulnerability Score
  - Published Date
  - Vendor Fix Date
  - Workaround
  - Solution
  - CWE IDs

  Custom Fields:

  - Component custom fields
  - Component version custom fields
  - Project custom fields
  - Project version custom fields

  Supported vulnerability conditions are:

  - Overall Score
  - CWE IDs
  - Solution Available
  - Workaround Available
  - Exploit Available
  - Reachable from Source
  - Remediation Status
  - RCE (Remote Code Execution)

  All other policy conditions are silently ignored.

  Upgrade guidance information is not used as policy conditions, however it is
  returned as part of Rapid Scan results separately to the policy violations
  output.

  Note that the severity of the policy rule determines how Black Duck Detect reacts to violations. Black Duck Detect treats violations of Blocker
  and Critical policies as errors; if any such violations are found, Black Duck Detect prints error messages and terminates with a non-zero
  exit code (so that builds can be failed if desired). For all other policy
  severities, Black Duck Detect treats violations as warnings; Black Duck Detect will print warning messages, but they alone will not
  cause Black Duck Detect to terminate with a non-zero exit code.
- Use Black Duck Detect 8.0 and later.
- Enable Rapid Scanning in Black Duck Detect by including these properties:
  - **--detect.blackduck.scan.mode="RAPID"**

  Refer to the [Black Duck Detect](https://docs.blackduck.com/p/detect) documentation for more information
  about these properties.
- If **--detect.cleanup=false** is set, the raw JSON response from the Black
  Duck server will be saved as
  `<DETECT_OUPUT_PATH>/runs/<timestamp>/scan/<project_name>_<project_version>_BlackDuck_DeveloperMode_Result.json`.
- Any other Black Duck Detect properties that affect package manager scans
  are also applicable to Rapid Scanning.
- If a project and/or version is specified, but does not exist, policies will still
  be evaluated.
- Rapid Scanning will not create projects if they do not already exist, which is
  the opposite of what occurs when running other types of scans.
- For projects with complex builds, and especially when such projects use Gradle,
  the runtime of Rapid Scanning is frequently dominated by the runtime of the
  package manager when it is invoked to report the project's dependencies.
- A new job, CollectScanStatsJob, collects scan statistics which are shown on the
  **usage: rapid scan completion** section on the System Information
  page.
- Caching is used extensively. If any of the following values are changed, it may be
  up to 15 minutes for those changes to be reflected in Rapid Scanning results:
  - Component Approval Status
  - Component Custom Fields
  - Component Modified
  - Component Modification
  - Component Purpose
  - Component Usage
  - Component Version Approval Status
  - Component Version Custom Fields
  - Match Type
  - Project Custom Fields
  - Project Name
  - Project Version Name
  - Project Tags
  - Project Version Custom Fields
  - Review Status
  - Unfulfilled License Terms

  You can override the Rapid Scanning caching interval by setting the value in
  the `blackduck.rapidscan.policy.cache.interval.mins` environment
  variable in the `blackduck-config.env` file.
- If a code location was previously scanned with a traditional scan where Black Duck
  Detect created a project for it, a subsequent rapid scan of the same code
  location will be associated with that project even if no project was explicitly
  provided.
- The following default values are used in evaluations if the project version is not
  known or the component is not found in the BOM.
  - Dynamically Linked for Component Usage
  - Not Reviewed for Review Status
  - File Dependency for Match Type
  - False for Component Purpose, Component Modified, Component Modification,
    and Component Terms Unfulfilled

## Scan Custom Config File

The policy overrides config will be ingested by Black Duck through a custom config
YAML file that a developer could check-in to SCM alongside other build config files.
Detect or CodeSight would then archive that file and scan header file and upload
through the "Initialize Scan With Custom Config" endpoint when creating a scan.

  
 [image: image]   

Each policy override must apply to a list of specific components, on a specific
version (e.g. component1 + version1) or on all versions (e.g. component2).

The endpoint to initialize a rapid scan with a custom config is:

```
POST /api/developer-scans
```

```
Consumes: application/vnd.blackducksoftware.developer-scan-1-ld-2-yaml-1+zip
```

This endpoint's request body is a zipped archive of the custom config YAML file
and the bdio header file.

## BOM Comparison Modes

By using the `X-BD-RAPID-SCAN-MODE` header or detect option
`detect.blackduck.rapid.compare.mode` and providing it one of the
values below, you can change the Rapid Scan mode.

Set the compare mode of rapid scan:

- `ALL`: The default operation. It will evaluate policy rules
  that are `RAPID` or (`RAPID` and
  `FULL`). When the header is absent, this is the default
  behaviour.

- `BOM_COMPARE`: Will evaluate policy rules like the
  `ALL` option, but will now evaluate differently based on
  the type of policy rule modes. When the policy rule is
  (`RAPID` and `FULL`) it will behave like
  `BOM_COMPARE_STRICT` but if the policy rule is only
  (`RAPID`) it will evaluate the result of the rapid scan
  against the policy ignoring results in the BOM.

- `BOM_COMPARE_STRICT`: Will only evaluate policy rules that are
  (`RAPID` and `FULL`). Policy violations
  are compared to the existing project version BOM. If the policy violation
  was already known and visible in the BOM (active or overridden) it is not
  part of the rapid scan positive result, it will still be part of the full
  result following existing restrictions.

In order to run either of the `BOM_COMPARE` modes there must be an existing
project version in HUB.

## Enabling full results data for BOM support

You can configure Rapid Scan to provide a full results format to include data points for BOM
support. To do so, set the following environment variable:
`BLACKDUCK_RAPID_SCAN_EXTENDED_DATA=true`. The additional data
points include:

|  |  |  |
| --- | --- | --- |
| - componentDescription - Homepage link - OpenHub link - Declared License definition | - Release date - Meta links to component id component version id and component version origin URIs - External namespace - Package URL | - SPDX license ID - Source (NVD or BDSA) - Match type |
