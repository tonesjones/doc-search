---
title: "SAST Tools Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/sast-tools-mapping.html"
content_id: "025dKTDuw7AILhqZ9t4Wlw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:46.459239+00:00"
content_hash: "83c5c0fb076a128fa3e25c1a4b7b7f3f909f811ab1a06f4a206c574c6bb4dae6"
---

# SAST Tools Mapping

The tables below show the severity and triage status mappings for all of the SAST tools that
are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager status
shown at the top of each column. (A blank cell indicates that an equivalent status value is
unavailable or undefined.)

## Severity Mapping

Table 1.

| SAST Tools | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **Android Lint**1 |  | Security | Correctness; Correctness: Messages, Fatal; Correctness: Messages, Error; Internationalization, Fatal; Internationalization, Error; Bi-directional Text, Fatal; Bi-directional Text, Error | Correctness: Messages Warning, Performance | Usability, Topography; Usability, Icons; Usability; Accessibility; Internationalization, Warning; Bi-directional Text, Warning |  |
| **Armorize CodeSecure** |  | HIGH | MEDIUM | LOW |  |  |
| **Brakeman** |  |  |  |  |  |  |
| **Checkmarx (SAST)** | 4 | High / 3 | Medium / 2 | Low / 1 | Info / 0, Information | Unspecified, Unknown |
| **Checkmarx One (SAST)** | CRITICAL | HIGH | MEDIUM | LOW | INFO |  |
| **Checkstyle** |  |  |  |  |  |  |
| **Clang** |  |  |  |  |  |  |
| **Clang (CodeChecker)** | CRITICAL | HIGH | MEDIUM | LOW | STYLE |  |
| **Clippy** |  | error | warning | note / failure-note | help | none |
| **CodePeer** |  | high | medium | low |  |  |
| **CodeSonar-Scrape**2 |  | Red | Yellow | Green |  |  |
| **Continuous Dynamic (formerly WhiteHat) - (Legacy Rating System)** | urgent, critical | high | medium | low | informational, note |  |
| **Continuous Dynamic (formerly WhiteHat) - (Advanced Rating System)** | Critical | High | Medium | Low | Note |  |
| **CppCheck** |  | error | performance, warning | portability, style | information | none |
| **Coverity** | Very High / Critical | Major / High | Moderate / Medium | Minor / Low | Audit, Very Low |  |
| **Coverity On Polaris** | critical | high | medium | low | audit |  |
| **42Crunch** | 5 | 4 | 3 | 2 | 1 |  |
| **DefenseCode ThunderScan** | critical | high | medium | low | informational |  |
| **ErrCheck** |  |  | all |  |  |  |
| **error-prone** |  |  |  |  |  |  |
| **ESLint** |  |  |  |  |  |  |
| **Fortify**3 | impact >= 2.5 and likelihood >= 2.5 | impact >= 2.5 | likelihood >= 2.5 | likelihood < 2.5 and impact < 2.5 |  |  |
| **Fortify Software Security Center***** | impact >= 2.5 and likelihood >= 2.5 | impact >= 2.5 | likelihood >= 2.5 | likelihood < 2.5 and impact < 2.5 |  |  |
| **Gendarme** |  |  |  |  |  |  |
| **GitLab Security** | critical | high | medium | low | informational |  |
| **GoCyclo** |  |  |  | all |  |  |
| **GoLint** |  |  |  |  |  |  |
| **GoSec** |  | HIGH | MEDIUM | LOW |  |  |
| **HCL AppScan Source** | critical | high | medium | low | informational |  |
| **HCL AppScan on Cloud (ASoC)** | critical | high | medium | low | informational |  |
| **Helix QAC** |  | 7 (Undefined behavior), 8 (Language constraints) | 3 (Important issue), 4 (Local criteria), 5 (Data flow analysis), 6 (Portability) | 2 (Minor issue) | 0 (Information), 1 (Obsolete message), 9 (Error) |  |
| **IneffAssign** |  |  |  | all |  |  |
| **JLint** |  |  |  |  |  |  |
| **JSHint** |  |  |  | all |  |  |
| **Microsoft Code Analysis** |  |  |  |  |  |  |
| **MobSF** |  | dangerous, insecure, high | medium, warning |  | normal, signature, info, good |  |
| **MobFS Scan** |  | ERROR | WARNING |  | INFO |  |
| **NDepend** | Critical | High | Medium | Low | Info |  |
| **OCLint** |  |  |  |  |  |  |
| **Orca Security (Secret Scans)** | CRITICAL | HIGH | MEDIUM | LOW | INFO |  |
| **Parasoft JTest / C++Test / dotTest** |  | Level 1: Severe Violation; Level 2: Possible Severe Violation | Level 3: Violation | Level 4: Possible Violation; Level 5: Informational |  |  |
| **PHPMD** |  | 1, 2 | 3 | 4, 5 |  |  |
| **PMD** |  | 1, 2 | 3 | 4, 5 |  |  |
| **Polaris** | critical | high | medium | low | informational |  |
| **Pylint** |  |  |  |  |  |  |
| **Rapid Scan SAST** | critical | high | medium | low | informational |  |
| **SafeSQL** |  | all |  |  |  |  |
| **SARIF** | severe / critical | high / error | medium / moderate | low / warning | note / info / informational |  |
| **SATE** |  | 1, 2 | 3 | 4, 5 |  |  |
| **Scalastyle** |  |  |  |  |  |  |
| **Scan@Source** | critical | high | medium | low | informational |  |
| **SCARF** |  |  |  |  |  |  |
| **Semgrep** |  | high | medium | low |  |  |
| **Snyk Code** | critical | high | medium | low |  |  |
| **SonarQube / SonarCloud** | BLOCKER / CRITICAL | MAJOR / HIGH | MEDIUM | MINOR / LOW | INFO |  |
| **SpotBugs / FindBugs** |  | 1 | 2 | 3 |  |  |
| **Staticcheck** |  |  |  |  |  |  |
| **TruffleHog** | Verified = true; Verified = false AND Detector name = Oauth, AWS, or Heroku | Verified = false AND Detector Name = PrivateKey | Verified = false AND Detector Name = Generic Secret |  |  | Verified = false AND Detector Name = Unspecified |
| **Veracode** |  | 4 | 3 | 2 | 1 |  |
| **Vet** |  |  |  |  |  |  |

1. Android Lint evaluates risk based on both a category and a severity level. Categories
are indicated by an asterisk.

2. CodeSonar reports risk through a combination of a ranking formula and an analysis
warning system (red, yellow, green). Software Risk Manager uses the red, yellow, and green
statuses to map to high, medium, and low, respectively.

3. Fortify reports risk by creating scores for “impact” and “likelihood.” The combination
of these scores is then mapped to the Software Risk Manager severity levels.

## Triage Status Mapping

Table 2.

| SAST Tools | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| --- | --- | --- | --- | --- | --- | --- |
| **Android Lint** |  |  |  |  |  |  |
| **Armorize CodeSecure** |  |  |  |  |  |  |
| **Brakeman** |  |  |  |  |  |  |
| **Checkmarx (SAST)** | NOT_EXPLOITABLE / 1 | False Positive | URGENT / 3; CONFIRMED / 2 |  |  |  |
| **Checkmarx One (SAST)** | NOT_EXPLOITABLE; PROPOSED_NOT_EXPLOITABLE |  | URGENT; CONFIRMED |  |  |  |
| **Checkstyle** |  |  |  |  |  |  |
| **Clang** |  |  |  |  |  |  |
| **Clang (CodeChecker)** | intentional | false_positive, suppress | confirmed |  |  |  |
| **Clippy** |  |  |  |  |  |  |
| **CodePeer** | not a bug | false positive |  |  |  |  |
| **CodeSonar-Scrape**** |  |  |  |  |  |  |
| **Continuous Dynamic (formerly WhiteHat)** | accepted, out of scope | Invalid, false |  | open, mitigated |  |  |
| **CppCheck** |  |  |  |  |  |  |
| **Coverity** | Intentional, ignore | False Positive |  |  |  |  |
| **Coverity On Polaris** | DISMISSED INTENTIONAL, DISMISSED OTHER | FALSE POSITIVE | TO BE FIXED |  |  |  |
| **42Crunch** |  |  |  |  |  |  |
| **DefenseCode ThunderScan** |  | false positive |  |  |  |  |
| **ErrCheck** |  |  |  |  |  |  |
| **error-prone** |  |  |  |  |  |  |
| **ESLint** |  |  |  |  |  |  |
| **Fortify***** | Suppressed, Not an Issue |  | Exploitable, Suspicious, Reliability Issue, Bad Practice |  |  |  |
| **Fortify Software Security Center***** | Suppressed, Not an Issue |  | Exploitable, Suspicious, Reliability Issue, Bad Practice |  |  |  |
| **Gendarme** |  |  |  |  |  |  |
| **GitLab Security** |  |  |  |  |  |  |
| **GoCyclo** |  |  |  |  |  |  |
| **GoLint** |  |  |  |  |  |  |
| **GoSec** |  |  |  |  |  |  |
| **HCL AppScan Source** |  | noise |  | passed | fixed | reopened |
| **HCL AppScan on Cloud (ASoC)** |  | noise |  | passed | fixed | reopened |
| **Helix QAC** |  |  |  |  |  |  |
| **IneffAssign** |  |  |  |  |  |  |
| **JLint** |  |  |  |  |  |  |
| **JSHint** |  |  |  |  |  |  |
| **Microsoft Code Analysis** |  |  |  |  |  |  |
| **MobSF** |  |  |  |  |  |  |
| **MobFS Scan** |  |  |  |  |  |  |
| **NDepend** |  |  |  |  |  |  |
| **OCLint** |  |  |  |  |  |  |
| **Orca Security (Secret Scans)** |  |  |  |  |  |  |
| **Parasoft JTest / C++Test / dotTest** |  |  |  |  |  |  |
| **PHPMD** |  |  |  |  |  |  |
| **PMD** |  |  |  |  |  |  |
| **Polaris** | dismissed (any other reason) | dismissed (false positive) | to-be-fixed |  |  |  |
| **Pylint** |  |  |  |  |  |  |
| **Rapid Scan SAST** |  |  |  |  |  |  |
| **SafeSQL** |  |  |  |  |  |  |
| **SARIF** |  |  |  |  |  |  |
| **SATE** |  |  |  |  |  |  |
| **Scalastyle** |  |  |  |  |  |  |
| **Scan@Source** |  |  |  |  |  |  |
| **SCARF** |  |  |  |  |  |  |
| **Semgrep** |  |  |  |  | fixed |  |
| **Snyk Code** | ignored |  |  |  |  |  |
| **SonarQube / SonarCloud** | WON'T FIX, SAFE | FALSE POSITIVE | ACKNOWLEDGED |  | FIXED | REOPENED |
| **SpotBugs / FindBugs** |  |  |  |  |  |  |
| **Staticcheck** |  |  |  |  |  |  |
| **TruffleHog** |  |  |  |  |  |  |
| **Veracode** | Accept the Risk | Potential False Positive | Reported to Library Maintainer | Mitigate by Design, Mitigate by Network Environment, Mitigate by OS Environment |  |  |
| **Vet** |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.
