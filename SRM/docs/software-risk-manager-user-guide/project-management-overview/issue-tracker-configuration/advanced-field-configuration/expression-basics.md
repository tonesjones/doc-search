---
title: "Expression Basics"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/expression-basics.html"
content_id: "p5U6FsUvksRz~3ejVknOwQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:16.008914+00:00"
content_hash: "4831002c1e20b4f5f9892878976dc489dae0abfd9255923286e693072f811374"
---

# Expression Basics

The template engine will use the text you provide as-is, but it will treat anything
inside pairs of double braces {{ }} as an expression to be evaluated using the active
finding or findings. Software Risk Manager defines five basic data objects that can be
used in the template expressions:

- `allFindings` - An array of all of the active findings ordered
  first by the severity then by finding ID.
- `finding` - The first element in `allFindings`
  (i.e., for multiple-finding issues, this will be the finding with the highest
  severity and lowest finding ID); this field is most useful for single-finding
  issues.
- `common` - An abstract finding containing any field whose value
  is shared by all of the findings in `allFindings`, containing the
  same fields enumerated below for finding objects; any value not shared by all
  findings will be reported as `null`.
- `project` - An object containing information about the
  project.
- `trackerType` - The type of issue tracker that the template is
  being generated for (`"jira"`, `"azure"`,
  `"servicenow"`, `"github"` or `"gitlab"`).

These objects can be used to construct expressions containing data from the active
findings. For
example,

```
Finding {{finding.id}} has {{finding.severity.name}} severity
```

will, when applied to a Software Risk Manager finding with ID 1 and High severity,
produce the following
text:

```
Finding 1 has High severity
```

## Code Block Format

Each issue tracker has its own markup language and may require special syntax when
you create pre-formatted code blocks.

**Jira:** Use `{code}` before and after the code
block.

```
{code} {{{requestBody}}} {code}
{code} {{{responseBody}}} {code}
```

**ServiceNow:** Use `[code]<code>` before the code block and
`</code>[/code]` after the code
block.

```
[code]<code> {{{requestBody}}} </code>[/code]
[code]<code> {{{responseBody}}} </code>[/code]
```

**Azure DevOps**, **GitHub** and **GitLab** (triple backticks): Use ```` ``` ````
before and after the code block.

```
```
{{{requestBody}}}
```
```
{{{responseBody}}}
```
```

## Finding Objects

The following fields are available on all finding objects (each element in the
allFindings array, finding, and common). Fields marked as being optional can be
omitted or set to null, all other fields will be present. The only exception to this
rule is the common object, where any value not shared by all findings will be set to
null regardless of whether it is optional or not.

- `id` - The ID of the Software Risk Manager Finding.
- `link` - A fully qualified URL pointing to the Software
  Risk Manager details page for this finding; must be wrapped to prevent
  html-escaping, for example `{{{finding.link}}}`.
- `triageStatus` - The finding's Triage Status,
  e.g. "Fixed" or "Ignored".
- `findingStatus` - The finding's Finding Status,
  e.g. "New" or "Existing".
- `assignee` - The name of the user that is assigned to the finding
- `firstSeenOn` - The date the finding was first seen, as text
  in `MM/dd/yyyy` format.
- `firstSeenOnDate` - The date the finding was
  first seen in ISO 8601 extended format; suitable for use with the
  `{{formatDate}}` and `{{formatDateTime}}`
  template helpers.
- `triageTime` - The date and time the finding's triage
  status was updated in ISO 8601 extended format; suitable for use with
  the `{{formatDate}}` and `{{formatDateTime}}`
  template helpers.
- `closeTime` - The date and time the finding's triage
  status was set to a closed status (i.e., Ignored, False Positive, Fixed,
  Mitigated, or Gone), in ISO 8601 extended format; suitable for use with
  the `{{formatDate}}` and `{{formatDateTime}}`
  template helpers.
- `fixByDate` - The Fix By Date of the finding in
  `yyyy-MM-dd` format.
- `detectionMethod` - An object representing the manner in
  which the finding was discovered.

  - `id` - An identifier for the detection method.
  - `name` - The name of the detection method (e.g.
    "Static Analysis").
- `detection` - A helper object containing booleans for some
  pre-defined detection methods.

  - `isDast` - True if the finding is a DAST
    finding.
  - `isSast` - True if the finding is a SAST
    finding.
  - `isComponent` - True if the finding is a Component
    Analysis finding.
  - `isHybrid` - True if the finding is a Hybrid
    finding.
  - `isInteractive` - True if the finding is an IAST
    finding.
  - `isThreatModel` - True if the finding is a Threat
    Modeling finding.
  - `isNetwork` - True if the finding is a Network
    Security finding.
  - `isDatabase` - True if the finding is a Database
    Analysis finding.
  - `isContainer` - True if the finding is a Container
    Analysis finding.
  - `isCloudInfrastructure` - True if the finding is a
    Cloud Infrastructure Analysis finding.
- `detectedBy` - The list of tools that detected the
  finding, in text form.
- `descriptor` - An object describing the type of
  finding.

  - `id` - An identifier for the descriptor.
  - `code` - A unique identifier for the
    descriptor.
  - `name` - A human-friendly name for the
    descriptor.
  - `type` - The type of descriptor; possible values
    can include the following:

    - `rule` - This finding represents one or
      more results that matched a rule in the current *Rule
      Set*.
    - `tool-code` /
      `observed-tool-code` - This finding
      directly represents a result from a tool.
    - `manual-entry` - This finding was manually
      entered.
    - `cve-group` - This finding was created to
      represent a group of CVEs.
  - `hierarchy` - The hierarchy of the type of
    finding, corresponding with the nesting represented in the
    *Type* filter on the *Findings* page; this is an
    array of strings, with `name` as the last
    element.
- `cwe` - An optional object representing the CWE associated
  with the finding.

  - `id` - The CWE ID associated with the finding.
  - `name` - The name of the CWE.
- `location` - The location where the finding has been
  identified.

  - `lines` - An object representing the line number
    range on which the finding is present, if available; uses the
    format `{start: <Number>, end:
    <Number>}`.
  - `line` - The line number of the location, if
    available, in text form (e.g., `'3-5'` or
    `'100'`).
  - `columns` - An object representing the start and
    end columns of the finding's location, if available; uses the
    format `{start: <Number>, end:
    <Number>}`.
  - `column` - The column number of the location, if
    available (e.g., `'12-44'` or
    `'440'`).
  - `path` - An object representing the location's
    path:

    - `path` - The full path of the
      location.
    - `pathType` - The type of the path (e.g.,
      `url` or `file`).
    - `shortName` - A shortened version of
      `path`; this is the value that is
      displayed on the findings table for the finding.
    - `hasSource` - A boolean value reflecting
      whether Software Risk Manager has a source file for the
      given location.
- `element` - An optional object representing the element
  impacted by the finding:

  - `name` - The name of the element.
  - `shortName` - An abbreviated version of the
    `name`.
  - `type` - The type of the element.

    - `keyword` - A computer-friendly
      description of the element type (e.g., "query-string" or
      "http-header").
    - `name` - A human-friendly description of
      the element type (e.g., "Query String" or "HTTP
      Header").
- `severity` - An object representing the effective Software
  Risk Manager severity value for the finding
  (`severityOverride` if specified, otherwise
  `severityDefault`):

  - `key` - A numeric representation of the severity;
    higher is more severe.
  - `name` - The name of the severity (e.g.,
    "Critical" or "Info").
- `severityDefault` - An object (in the same format as
  `severity` above) representing the severity of the
  finding as calculated by Software Risk Manager; this is the severity
  that is used if an override is not specified.
- `severityOverride` - An optional object (in the same
  format as `severity` above) representing the
  user-specified severity override for the finding, if provided.
- `descriptions` - An object containing the general and
  contextual descriptions for the finding:

  - `general` - The general description for the
    finding; corresponds to the description shown at the top of the
    Details page.

    - `format` - An indication of the
      description's format (e.g., `'text'`,
      `'markdown'`, or
      `'html'`).
    - `content` - The content of the description
      in the specified format.
  - `contextual` - The contextual description for the
    finding, if one is specified; this is in the same format as the
    `general` description above.
- `metadata` - An object containing metadata available for
  the finding; each key in the object is the metadata field name, and the
  value is the value for that field.
- `trainingLink` - A fully qualified URL pointing to a
  Secure Code Warrior training module if available. NOTE: you are required
  to wrap this field in an extra pair of curly braces to prevent html
  escaping of the URL (`{{{trainingLink}}}`, for
  example).
- `mostRecentAnalysis` - An object representing the last
  successfully completed analysis that either generated or updated the
  finding.

  - `id` - The ID of the analysis.
  - `projectId` - The ID of the Software Risk Manager
    Project this finding is on.
  - `state` - The state of the analysis, can be one
    of: `Created`, `Queued`,
    `Running`, `Failed`,
    `Complete`.
  - `createdBy` - The object representing the user who
    created the analysis.

    - `id` - The ID of the user.
    - `name` - The name of the user.
  - `creationTime` - When an analysis was created.
  - `startTime` - When an analysis started.
  - `endTime` - When an analysis ended.
  - `name` - The name of the analysis (note that this
    value is blank by default unless explicitly set).
- `sourceSnippet` - An object representing a snippet of code
  the finding occurs in.

  - `lines` - A list that contains the lines of source
    code for the snippet.
  - `startLine` - The line number from the source file
    corresponding with the first element of the list.
- `branch` - An object containing information about the
  branch the issue is associated with.

  - `id` - The id of the Software Risk Manager
    branch.
  - `name` - The name of the Software Risk Manager
    branch.
- `branches` - An array containing the branches this finding appears on.
- `results` - An array of all of the results (ingested from
  tools and manually entered) on the finding, corresponding with the
  *Evidence* section of the details page, ordered first by the
  severity and then by result ID. Each entry contains:

  - `id` - The ID of the Software Risk Manager
    Result.
  - `firstSeenOn` - The date the result was
    first seen in ISO 8601 extended format; suitable for use with the
    `{{formatDate}}` and `{{formatDateTime}}`
    template helpers.
  - `isManual` - A boolean indicating if the result
    was manually entered.
  - `detectionMethod` - An object representing the
    result's detection method (in the same format as the Finding
    `detectionMethod` above).
  - `tool` - An optional string representing the tool
    name (always present for tool results, but optional for manual
    results).
  - `severity` - An object representing the result's
    reported severity (in the same format as the Finding
    `severity` above).
  - `cwe` - An optional object representing the
    result's reported CWE (in the same format as the Finding
    `cwe` above); note that the result's
    `cwe` may be different from the finding's
    `cwe`, due to correlation based on rule
    sets.
  - `descriptor` - An object describing the type of
    result (in the same format as the Finding
    `descriptor` above).
  - `location` - An optional object representing the
    raw location reported by the result:

    - `rawDisplayPath` - The full display path,
      as reported by the tool; this will be
      `null` for manually entered
      results.
    - `pathObject` - An object representing the
      result's reported path (in the same format as the
      Finding `location.path` above); this path
      represents the normalized version of the path as
      understood by Software Risk Manager, and therefore may
      be slightly different from
      `rawDisplayPath`.
    - `lines` - An optional `{ start:
      <Number>, end: <Number> }` object for
      the result's reported line numbers, if specified.
    - `columns` - An optional `{ start:
      <Number>, end: <Number> }` object for
      the result's reported column numbers, if specified.
  - `descriptions` - An object containing the general
    and contextual descriptions for the result.

    - `general` - A description object
      describing general information about the result (in the
      same format as the Finding description objects
      above).
    - `contextual` - A description object
      containing specific contextual data reported by the tool
      or manual entry (in same format as the Finding
      description objects above).
  - `metadata` - An object containing tool-specific
    metadata; keys in this object are a [camel case](https://en.wikipedia.org/wiki/Camel_case) version of
    the name shown in the *Evidence* section of the details
    page - some (non-exhaustive) examples are as follows:

    - `ContinuousDynamicVulnerabilityId` - The Continuous Dynamic (formerly WhiteHat)
      Vulnerability ID (for Continuous Dynamic tool results).
    - `cvssV3` - The CVSS V3 score (typically
      for component analysis results).
    - `cpe` - The CPE of the associated
      component (typically for component analysis
      results).
    - `veracodeFlawId` - The Veracode Flaw ID
      (for Veracode tool results).
    - `sonatypeThreatLevel` The Sonatype Threat
      Level (for Sonatype tool results).
    - `prismaCloudComputeTwistlockDistro` The
      distro of the image scanned (for Prisma Cloud Compute
      [Twistlock] results).
  - `httpMetadata` - An object containing the values
    associated with the result's HTTP Activity; similarly to
    `metadata`, the keys in this object are camel
    case and corresponds with the values displayed in the
    *Metadata* section for each HTTP variant on each
    associated result - for example:

    - `ContinuousDynamicAttackVectorId` -
      `["123", "456", "789"]` for a result
      with three Continuous Dynamic Attack Vectors with the IDs
      123, 456, and 789.
  - `cves` - An array of CVEs associated with the
    finding, in text form (each element in the array is a string in
    the format `CVE-YYYY-NNNN`).
  - `vulnerabilities` - An array of vulnerability IDs
    (e.g., CVE and BDSA) associated with the finding, in text form
    (each element in the array is a string in the vulnerability
    format, such as `BDSA-YYYY-NNNN` for BDSAs and `CVE-YYYY-NNNN` for
    CVEs).
  - `variants` - An object containing the values
    associated with the result's request & response HTTP
    Activity.

    - `requestData` - Formatted info for an HTTP
      request as seen in the "Raw Request Data" for a Result
      (does not include request body).
    - `responseData` - Formatted info for an
      HTTP response as seen in the "Raw Response Data" for a
      Result (does not include response body).
    - `requestBody` - The body of the
      corresponding HTTP request.
    - `responseBody` - The body of the
      corresponding HTTP response.
  - `hostInfo` - An object containing the values
    associated with the result's Host Info.

    - `formattedHostname` - A formatted list of
      Host Names.
    - `formattedFqdn` - A formatted list of
      FQDN.
    - `formattedIp` - A formatted list of IP
      Addresses.
    - `formattedMac` - A formatted list of MAC
      Addresses.
    - `formattedNetBios` - A formatted list of
      NetBIOS Names.
    - `formattedOs` - A formatted list of
      Operating Systems.
    - `formattedPorts` - A formatted list of
      Ports in the form of
      `[Port][Protocol][State]`.
    - `formattedEnvironment` - A formatted list
      of Environments.
    - `formattedHostInfo` - Full formatted Host
      Info using all previously listed items.

## Project Object

- `id` - The ID of the Software Risk Manager Project.
- `name` - The name of the project.
- `metadata` - An array of value objects entered via the Project Metadata
  dialog.

  - `name` - The name of the metadata field.
  - `value` - The value entered for the field.
  - `valueId` - For "dropdown" fields, the choice ID.
