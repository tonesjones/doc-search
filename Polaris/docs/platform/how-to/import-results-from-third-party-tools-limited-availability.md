---
title: "Import results from third-party tools (limited availability)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/import-results-from-third-party-tools-limited-availability-.html"
content_id: "T9BQ4xhsYVUwctAFmzxLRQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:25.506748+00:00"
content_hash: "c10d6db5d4cbc6e1fc8c1033a0052c939e22f3e18ab72d6882d6d2573051ea30"
---

# Import results from third-party tools (limited availability)

Run external analysis tests to import SAST and SCA issue data from third-party tools into SAST & SCA projects in Polaris.

## Overview

You can import SAST and SCA issue data from a supported third-party tool by uploading a file that was exported from that tool to Polaris. This requires a subscription that permits external analysis tests.

Important: The ability to import results from third-party tools via file upload is available on a limited basis, and is not generally available. Please contact your account teams for more information.

Please note:

- Imports can only be run from the Polaris user interface, and run like other tests.
- SAST issues you import from third-party tools are subject to file and folder exclusion rules. See [Exclude files and folders from tests](exclude-files-and-folders-from-tests.md) for more information.
- Issues without a valid severity are ignored.
- You can upload one file (up to 2GB in size) for each external analysis test.
- Each file you upload can only include one type of issue data (SAST or SCA).
- Different file formats are accepted for different third-party tools. Find a list of third-party tools that generate results you can import into Polaris here: Supported third-party tools.
- Issues you import from third-party tools:
  - Appear on the Issues tab (Portfolio > select an application > select a project > Issues), but do not affect the Components or Licenses tabs.
  - Appear in reports and dashboards, but the components and licenses associated with issues you import do not.

## Import results from third-party tools

To import results from a third-party tool, follow these steps:

1. Go to Tests.
2. Select New Test.
3. Select an Application, select a Project, and select a Branch.
4. Under Third-Party Integration, select External Analysis (SAST or SCA).

   Note: Third-Party Integration only appears when you select an application linked to a subscription that permits external analysis tests.
5. Drag and drop the file you want to import into the Import Results zone, or select Browse Files to find the file to import on your file system.

   [image: Upload a file for an external analysis test.]   

   Note: You can upload one file (up to 2GB) for each external analysis test. Each file you upload can only include one type of issue data (SAST or SCA). Different file formats are accepted for different third-party tools. See Supported third-party tools for a full list of supported tools, along with accepted file formats for each.
6. Select Begin Test.

Monitor test progress on the Tests page (accessible from the left-hand navbar). Newer tests appear near the top of the page.

## View and manage issues imported from third-party tools

After you run an external analysis test, issues appear alongside the rest of the project's issues on the Issues tab. Use the Tool filter to view issues captured in different tools. Additional filters appear each time you import results from a new tool.   
 [image: Apply filters to view issues from third-party tools.]   

Issues you import from third-party tools can be triaged and exported (to CSV, JSON, or Jira) like other issues in Polaris, and are subject to issue policies and file and folder exclusion rules.

### Issue deduplication

Please note:

- Polaris deduplicates issues captured using the same third-party tool (if you run multiple external analysis tests to import results from Clang into a project, Polaris won't duplicate the same issue found in different external analysis tests that import results from Clang).
- Polaris does not deduplicate issues imported from different third-party tools in the same project (if the same issue is captured in external analysis tests using exports from Clang and Coverity, the issue appears twice on the Issues tab).
- Polaris does not deduplicate issues captured in external analysis tests from issues captured in other test types in the same project (if the same issue is captured in a SAST test run with Polaris and an external analysis test, the issue appears twice on the Issues tab).

### Triage information

Triage information—consisting of changes to an issue's triage status and the addition of triage comments—is included in SAST and SCA issue data imported from third-party tools.

You can find triage information for imported issues in the Issue History panel. Note that:

- Imported issues are attributed to a user in the third-party tool, or to "System" if user information is unavailable.
- Polaris does not link usernames in imported triage information to Polaris usernames, even if names or email addresses match.

**How is triage status determined?**

In SAST and SCA issues imported from third-party tools, the triage status is:

- Mapped from the third-party tool to the equivalent triage status in Polaris (see the mapping tables below).
- Marked as Not Triaged if triage information is unavailable.

The latest triage status is determined by the most recent triage event that occurred in either Polaris or the third-party tool. This means that older triage events you import from third-party tools may be added to an issue's history, without changing its most recent triage status.

See [View issue history](view-issue-history.md) for more information about viewing triage and detection history.

### Triage status mappings

When you import triage events from a supported third-party tool, the triage status is mapped from the tool to the equivalent status in Polaris. The following tables show the mappings used for supported SAST and SCA third-party tools. A hyphen indicates that an equivalent status value is unavailable or undefined in the third-party tool.

Table 1. Triage Status Mappings — SAST Tools to Polaris

| SAST Tools / Polaris Triage Status | Dismissed [Reason: Intentional] | Dismissed [Reason: False Positive] | To Be Fixed | Dismissed [Reason: Other, Comment: Issue marked as mitigated] | Dismissed [Reason: Other, Comment: Reported as fixed] | Not Triaged [Comment: Issue re-opened by tool] |
| --- | --- | --- | --- | --- | --- | --- |
| Android Lint | - | - | - | - | - | - |
| Software Risk Manager Custom Integration XML\* | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| Brakeman | - | - | - | - | - | - |
| Checkmarx (SAST) | NOT\_EXPLOITABLE / 1 | False Positive | URGENT / 3; CONFIRMED / 2 | - | - | - |
| Checkstyle | - | - | - | - | - | - |
| Clang | - | - | - | - | - | - |
| Clippy | - | - | - | - | - | - |
| CodePeer | not a bug | false positive | - | - | - | - |
| Coverity | Intentional, ignore | False Positive | - | - | - | - |
| CppCheck | - | - | - | - | - | - |
| DefenseCode ThunderScan | - | false positive | - | - | - | - |
| ErrCheck | - | - | - | - | - | - |
| error-prone | - | - | - | - | - | - |
| ESLint | - | - | - | - | - | - |
| Fortify | Suppressed, Not an Issue | - | Exploitable, Suspicious, Reliability Issue, Bad Practice | - | - | - |
| FxCop | - | - | - | - | - | - |
| Gendarme | - | - | - | - | - | - |
| GitLab Security | - | - | - | - | - | - |
| GoCyclo | - | - | - | - | - | - |
| GoLint | - | - | - | - | - | - |
| GoSec | - | - | - | - | - | - |
| HCL AppScan Source | - | noise | - | passed | fixed | reopened |
| HCL AppScan on Cloud (ASoC) | - | noise | - | passed | fixed | reopened |
| Helix QAC | - | - | - | - | - | - |
| IneffAssign | - | - | - | - | - | - |
| JLint | - | - | - | - | - | - |
| Microsoft Code Analysis | - | - | - | - | - | - |
| MobSF | - | - | - | - | - | - |
| MobFS Scan | - | - | - | - | - | - |
| NDepend | - | - | - | - | - | - |
| OCLint | - | - | - | - | - | - |
| Parasoft JTest / C++Test / dotTest | - | - | - | - | - | - |
| PHP\_CodeSniffer | - | - | - | - | - | - |
| PHPMD | - | - | - | - | - | - |
| PMD | - | - | - | - | - | - |
| Pylint | - | - | - | - | - | - |
| Rapid Scan SAST | - | - | - | - | - | - |
| SafeSQL | - | - | - | - | - | - |
| SARIF | - | - | - | - | - | - |
| SATE | - | - | - | - | - | - |
| Scalastyle | - | - | - | - | - | - |
| SCARF | - | - | - | - | - | - |
| SciTools Understand | - | - | - | - | - | - |
| Semgrep | - | - | - | - | fixed | - |
| SonarQube / SonarCloud | WON'T FIX, SAFE | FALSE POSITIVE | ACKNOWLEDGED | - | FIXED | REOPENED |
| SpotBugs / FindBugs | - | - | - | - | - | - |
| Staticcheck | - | - | - | - | - | - |
| TFLint | - | - | - | - | - | - |
| TruffleHog | - | - | - | - | - | - |
| Veracode | Accept the Risk | Potential False Positive | Reported to Library Maintainer | Mitigate by Design, Mitigate by Network Environment, Mitigate by OS Environment | - | - |
| Vet (go vet) | - | - | - | - | - | - |
| ZPA | - | - | - | - | - | - |

\* Importing SAST and SCA issue data from SRM is supported by using the SRM Custom Integration Analysis Tool (XML) only. See .

Table 2. Triage Status Mappings — SCA Tools to Polaris

| Component Tool / Polaris Triage Status | Dismissed [Reason: Intentional] | Dismissed [Reason: False Positive] | To Be Fixed | Dismissed [Reason: Other, Comment: Issue marked as mitigated] | Dismissed [Reason: Other, Comment: Reported as fixed] | Not Triaged [Comment: Issue re-opened by tool] |
| --- | --- | --- | --- | --- | --- | --- |
| Black Duck Binary Analysis | - | - | - | FD (feature disabled) | VP (vendor patched) | - |
| Software Risk Manager Custom Integration XML\* | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| Dependency-Check | - | - | - | - | - | - |
| GitLab Security | - | - | - | - | - | - |
| JFrog Xray | - | - | - | - | - | - |
| Retire.js | - | - | - | - | - | - |
| Snyk Open Source | Ignored | - | - | - | Patched | - |
| Veracode | Accept the Risk | Potential False Positive | Reported to Library Maintainer | Mitigate by Design, Mitigate by Network Environment, Mitigate by OS Environment | - | - |
| WPScan | - | - | - | - | - | - |

\* Importing SAST and SCA issue data from SRM is supported by using the SRM Custom Integration Analysis Tool (XML) only. See .
