---
title: "Importing Scan Results"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/importing-scan-results.html"
content_id: "Hj2vsrRPmP2A2iEWNSgWuA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:37.655873+00:00"
content_hash: "c97128945578200073ed4405734c640497a477f9a10fe56f3395f633dc8428e6"
---

# Importing Scan Results

Software Risk Manager supports importing the results of commercial and open source
application security testing tools as well as a couple of generic tool result listing
formats. The list of supported tools for scan imports includes the built-in ones
mentioned in the previous section. If one of the tools you want to import is not
supported, please [let us know](https://community.blackduck.com/s/). However, in the meantime, you can convert your
data to the generic *SRM Input XML* format. The schema definition for this format
and an example can be accessed via the download icon in the Software Risk Manager
header.

Note: Some tools will output empty files if no results were found, which cannot be
detected by Software Risk Manager as any particular format. For more information on
empty or undetected tool results, see Empty/Undetected Tool
Results.

## Supported Tools

Software Risk Manager supports various tools and tool types, including the following:

- SAST tools
- DAST tools
- IAST tools
- Mobile tools
- InfraSec tools
- Threat Modeling tools
- Component tools
- Container tools
- Cloud Infrastructure tools
- Bug Bounty tools
- Infrastructure as Code (IaC)
- Web Application Firewall (WAF)
- Security Technical Implementation Guide (STIG)

## Additional Support for Selected Tools

Software Risk Manager also provides additional support for the following tools:

- AppDetective Pro
- AppSpider
- Aqua
- CodeSonar
- Dynatrace
- Helix QAC
- Parasoft
- Prisma Cloud Compute (Twistlock)
- SARIF
- SBOM Files

## SAST Tools

Software Risk Manager supports the following [SAST](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **42Crunch:** a *Tool Connector* for Security Audit scans.
- **Android Lint:**
  `.xml` and `.zip`.
- **Armorize CodeSecure:**
  `.xml`.
- **Brakeman** is a built-in scanner; `.json` is also
  supported.
- **Checkmarx:**
  `.xml` and a *Tool
  Connector*.
- **Checkmarx One:** a *Tool
  Connector*.
- **Checkstyle** is a built-in scanner; `.xml` is also
  supported.
- **Clang:**
  `.zip` containing one or more `.html` or
  `.plist.html` (CodeChecker) files. (Clang outputs one
  HTML file per checked source file.)
- **Clippy (user-installed)** is a built-in scanner; `.json`
  is also supported.
- **CodePeer:**
  `.csv` reports.
- **CodeSonar-Scrape:** see the *CodeSonar-Scrape utility* section for details.
- **Continuous Dynamic (formerly WhiteHat):** a *Tool Connector*.
- **CppCheck** is a built-in scanner; v2 `.xml` is supported
  as well.
- **Coverity:**
  `.json` using the `cov-format-errors` command
  line tool. For example: `cov-format-errors --dir /tmp/idir
  --json-output-v10 file.json`. When Scan Farm is configured,
  Coverity is available as a built-in tool.
- **Coverity on Polaris:** a *Tool
  Connector*.
- **Coverity Connect:** a *Tool
  Connector*.
- **DefenseCode ThunderScan:**
  `.json` report and a *Tool
  Connector*.
- **ErrCheck:** plain-text (e.g., `.txt`) with console
  output redirected to a file.
- **error-prone:** plain-text such as `.txt`.
- **ESLint** is a built-in scanner; `.json` is also
  supported.
- **Fortify:**
  `.fpr`.
- **Fortify Software Security Center:** a *Tool
  Connector*.
- **FxCop (user-installed)** is a built-in tool; `.xml` is
  also accepted.
- **Gendarme** is a built-in tool (not available in containerized
  deployments such as Docker Compose or Kubernetes); `.xml` is
  also supported.
- **GitHub Advanced Security (Code Scanning):** a *Tool
  Connector*.
- **GitLab Security:**
  `.json` and `Report .zip`.
- **GoCyclo:** plain-text (e.g., `.txt`) with console output
  redirected to a file; it may contain build errors.
- **GoLint:** plain-text (e.g., `.txt`) with console output
  redirected to a file; it may include build errors
- **GoSec:**
  `.json` when using the `-fmt json` flag.
- **HCL AppScan Source:**
  `.ozasmt`.
- **HCL AppScan on Cloud (ASoC):**
  `.xml` and a *Tool
  Connector*.
- **Helix QAC:**
  `.csv` report containing Helix QAC Rule Compliance results;
  see the *Helix QAC Support* section for
  more information.
- **IneffAssign:** plain-text (e.g., `.txt`) with console
  output redirected to a file.
- **JLint:** plain-text such as `.txt`.
- **JSHint** is a built-in tool; plain-text such as `.txt`
  is supported.
- **Microsoft Code Analysis** log files containing [Roslyn](https://docs.microsoft.com/en-us/visualstudio/code-quality/install-net-analyzers?view=vs-2019) analyzer results from
  MSBuild or Visual Studio as `.txt` files. Additionally, a
  copy/pasted `.tsv` output from the Error List table in Visual
  Studio with `Entire Solution` analysis enabled, which must
  contain the `Code`, `Description`,
  `Line`, and `File` (or
  `Path`) columns, and may optionally include the
  `Column` column. Furthermore, rules from the `Code
  Cracker` and `Security Code Scan` Roslyn
  analyzers, which are in the `.tsv` and `.txt`
  file formats as previously described.
- **MobSF:**
  `.json` where the JSON is generated by exporting a JSON file
  using the API, api/v1/report_json.
- **MobSF Scan:**
  `.json`.
- **NDepend:**
  `.xml` file containing NDepend Rule Results.
- **OCLint:**
  `.xml`.
- **Orca Security:** a *Tool
  Connector*.
- **Parasoft JTest/C++Test/dotTest:**
  `.xml`; please see the *Parasoft Support* section for more information.
- **PHP_CodeSniffer** is a built-in tool; `.xml` is also
  supported.
- **PHPMD** is a built-in tool; `.xml` is also supported.
- **PMD** is a built-in tool; `.xml` is also supported.
- **Pylint** is a built-in tool; `.json` is also supported.
- **Polaris:** a *Tool Connector*.
- **Rapid Scan SAST:**
  `.json`.
- **SafeSQL:** plain-text (e.g., `.txt`) with console output
  redirected to a file.
- **SARIF**
  `.json` format in compliance with SARIF v2.1.0 schema; please
  see the *SARIF Support* section for more
  information.
- **SATE:**
  `.xml` format for NIST’s Static Analysis Tool Exposition V
  (SATE V).
- **Scalastyle** is a built-in tool; `.xml` is also
  supported.
- **SCARF:**
  `.xml` for SWAMP Common Assessment Result Format.
- **SciTools Understand:**
  `.csv` report containing SciTools Understand analysis
  results.
- **Semgrep:**
  `.json` and a *Tool
  Connector*.
- **Snyk Code:** a *Tool
  Connector*; `.json` is supported.
- **Software Risk Manager XML:** for cases where you have data from a
  custom tool or from a tool that isn’t supported by Software Risk Manager,
  you can convert the output to the Software Risk Manager
  `.xml` format and input that directly for analysis. XML
  schemas and examples are provided via the download icon in the Software Risk
  Manager header.
- **SonarQube/SonarCloud:** a *Tool
  Connector*.
- **SonarQube Generic Issue Import Format:**
  `.json`.
- **SpotBugs/FindBugs** is a built-in scanner; `.xml`
  outputs are also accepted.
- **Staticcheck:**
  `.json` when using the `-f json` flag, with
  its console output redirected to a file.
- **TFLint:**
  `.json` file in compliance with SARIF format when using the
  `-f sarif` format option with `tflint` command.
  Software Risk Manager currently allows importing TFLint results in SARIF
  format only. The `-f` (or `--format`) option
  can be used to generate the SARIF formatted console output, which can then be
  redirected to a file, for example:
  `tflint -f sarif <file or directory>`.
- **TruffleHog:**
  `.json` file with repository scan results.
- **Veracode:** either the `.zip` files generated when
  exporting XML results, or the `.xml` files contained within
  them. Additionally, Veracode is a *Tool
  Connector*.
- **Vet:**
  `.json` from `go vet` by using the
  `-json` flag, with console output redirected to a file.
  It may include build errors.
- **ZPA:**
  `.json` using the `zpa-cli` command line tool,
  with the `sq-generic-issue-import` output-format.
- **Other source zip archives:**
  `.zip` (zipped source archives display contextual source for
  findings on the *Finding Details* page).

## DAST Tools

Software Risk Manager supports the following [DAST](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **Acunetix Desktop:**
  `.xml` where the XML is generated by selecting Scans, then
  Select Scan, then WAF Export, and then XML.
- **Acunetix 360:** a *Tool
  Connector*.
- **AppSpider Vulnerability Summary:**
  `VulnerabilitiesSummary.xml`; see the *AppSpider Support* section for more
  information.
- **Arachni:**
  `.json`.
- **APIsec:** a *Tool
  Connector*.
- **API Security Platform(ApiSec)** : a *Tool
  Connector*.
- **Burp Suite:**
  `.xml`when the Base64 encoding option is selected; consider
  using our Burp Suite plugin to send results directly to Software Risk
  Manager.
- **Continuous Dynamic (formerly WhiteHat):** a *Tool Connector*.
- **Defensics Fuzz Test:**
  `super-summary.xml`.
- **Dynatrace:** a *Tool Connector* (Attack data only).
- **Fortify WebInspect:**
  `.xml` when these options are selected: File, then Export,
  then Scan Details. In the Settings section, choose *Full* from the
  "Details:" dropdown menu and click Export.
- **HCL AppScan Standard:**
  `.xml`.
- **HCL AppScan on Cloud (ASoC):**
  `.xml` and a *Tool
  Connector*.
- **Imperva:** a *Tool Connector*.
- **Invicti Standard** (formerly Netsparker): `.xml`.
- **Invicti Enterprise** (formerly Netsparker Enterprise):
  *Vulnerabilities List*
  `.xml` report and a *Tool
  Connector*.
- **Invicti Application Security Platform:** a *Tool
  Connector*.
- **OWASP ZAP:**
  `.xml`; consider using our OWASP ZAP
  add-on to send results directly to Software Risk Manager.
- **Qualys WAS:** a *Tool Connector*.
- **Polaris:** a *Tool Connector*.
- **Rapid7 InsightAppSec:** a *Tool
  Connector*.
- **Rapid7 InsightVM:** a *Tool
  Connector*.
- **Rapid7 Nexpose:**
  `.xml` generated with the XML Export or XML Export 2.0
  reports. See Rapid7 Nexpose [Working with report formats](https://docs.rapid7.com/nexpose/working-with-report-formats/) and
  [Report templates and sections](https://docs.rapid7.com/nexpose/report-templates-and-sections/) for
  more information.
- **Black Duck Managed Services Platform:**
  `.xml` report and a *Tool
  Connector*.
- **Tenable.io Web App Scanning:** a *Tool
  Connector*.
- **Tinfoil API:** a *Tool
  Connector*.
- **Tinfoil Web:** a *Tool
  Connector*.
- **Trustwave App Scanner:** a *Tool
  Connector*.
- **Veracode:**
  `.xml` and `.zip`. Additionally, Veracode is a
  *Tool
  Connector*.
- **WPScan:**
  `.json`.
- **sqlmap output** - Sqlmap does not provide a suitable output format; to
  that end [we've developed a fork of sqlmap](https://github.com/codedx/sqlmap), which has
  flags for exporting in the Software Risk Manager Custom XML format.

## IAST Tools

Software Risk Manager supports the following [IAST](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **Checkmarx:** a *Tool Connector*.
- **Contrast:** a *Tool Connector*.
- **HCL AppScan on Cloud (ASoC):**
  `.xml` and a *Tool
  Connector*.
- **NowSecure Workstation:**
  `.json`.
- **Q-MAST:** a *Tool Connector*.
- **Black Duck Seeker:** a *Tool
  Connector*.

## Mobile Tools

Software Risk Manager supports the following [Mobile](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **Data Theorem Mobile Secure:** a *Tool
  Connector*.
- **HCL AppScan on Cloud (ASoC):**
  `.xml` and a *Tool
  Connector*.
- **MobSF:**
  `.json` where the JSON is generated by exporting a JSON file
  using the API, api/v1/report_json.
- **MobSF Scan:**
  `.json`.
- **NowSecure:** a *Tool Connector*.
- **NowSecure Workstation:**
  `.json`.

## InfraSec Tools

Software Risk Manager configured with the InfraSec add-on supports the following
[Infrastructure](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **AppDetective Pro:**
  `.xml`
  *Check Results* reports; please see the *AppDetective Pro Support* section
  for more information on report requirements.
- **Tenable Nessus:**
  `.nessus`.
- **Tenable.io:** a *Tool Connector*.
- **Tenable.sc:** a *Tool Connector*.
- **Rapid7 Nexpose:**
  `.xml`.
- **NMap:**
  `.xml` that contains vulnerability information associated
  with scripts written using the NMap Scripting Engine.
- **Qualys VM:**
  `.xml` generated with Scan-Based and Host-Based report
  templates and a *Tool Connector*. Before generating a report with a
  Host-Based report template, ensure that "Vulnerability Details" and at least
  one subsection are checked by navigating to the Display tab, in the "Edit
  Scan Report Template" window, and looking under "Include the following
  detailed results in the report."
- **Qualys VMDR:** a *Tool
  Connector*.
- **Qualys CS:**
  `.csv` of "images" or "container" scans.
- **SCAP:**
  `.xml` file containing the SCAP tool's scan results.

## Threat Modeling Tools

Software Risk Manager supports the following Threat Modeling tools and import
formats:

- **IriusRisk:** a *Tool Connector*.
- **Microsoft Threat Modeling Tool 2016:**
  `.htm` reports and `.tm7` files. Note:
  `.htm` reports will include images of the diagram and
  interaction for each finding.
- **SD Elements:** a *Tool
  Connector*.

## Component Tools

Software Risk Manager supports the following Component tools and import formats:

- **Black Duck Binary Analysis:** a *Tool
  Connector*, `.csv` and `.json`
  are supported. Note: CSV files can be created via Export > Vulnerabilities as CSV > Comma separator, and JSON files are only available through API using the `GET api/product/{ productId }` endpoint.
- **Black Duck SCA:** When Scan Farm is configured, Black Duck is available
  as a built-in tool. Also accessible as a *Tool
  Connector.*
- **CAST Highlight:** a *Tool
  Connector.*
- **Checkmarx One:** a *Tool
  Connector.*
- **Checkmarx OSA:** a *Tool
  Connector.*
- **Continuous Dynamic (formerly WhiteHat):** a *Tool
  Connector*.
- **Dependency-Check** is a built-in scanner; `.xml` is also
  supported.
- **Dependency-Track** a *Tool
  Connector.*
- **Dynatrace:** a *Tool Connector* (Vulnerability data with no related
  container images only).
- **GitHub Advanced Security (Dependabot)** a *Tool
  Connector.*
- **GitLab Security:**
  `.json` and `Report .zip`.
- **HCL AppScan on Cloud (ASoC):**
  `.xml` and a *Tool
  Connector*.
- **JFrog Xray:** a *Tool Connector*, `.json` is supported
- **Mend:** a *Tool Connector.*
- **NeuVector:** a *Tool Connector.*
- **Orca Security:** a *Tool
  Connector*.
- **Polaris:** a *Tool Connector.*
- **Retire.js** is checked by Dependency-Check; if run externally,
  `.json` is supported.
- **Snyk Open Source:** a *Tool
  Connector*, `.json` is supported.
- **Snyk License Compliance Management:** a *Tool
  Connector*, `.json` is supported.
- **Sonatype Nexus:** a *Tool
  Connector.*
- **Veracode:**
  `.xml` and `.zip`. Additionally, Veracode is a
  *Tool
  Connector*.
- **WPScan:**
  `.json`.

## Container Tools

Software Risk Manager supports the following [Container](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **Anchore:** a `.json` file generated using
  `anchore-cli image vuln {image-name} all`.
- **Aqua Enterprise:** a *Tool
  Connector*.
- **Check Point CloudGuard:** a *Tool
  Connector* (Vulnerability data only).
- **Dynatrace:** a *Tool
  Connector* (Vulnerability data with related container
  images only).
- **GitLab Security:**
  `.json` and `Report .zip`.
- **Grype:** a `.json` file with container image/filesystem
  results.
- **Google SCC:** a *Tool
  Connector*.
- **Harbor:** a `.json` or `.csv` Harbor
  vulnerability report.
- **NeuVector:** a *Tool Connector.*
- **Orca Security:** a *Tool
  Connector*.
- **Snyk Container:** a *Tool
  Connector*, `.json` is supported.
- **Prisma Cloud Compute (Twistlock):** a *Tool
  Connector*, a `.json` file generated with
  `twistcli`, or one of the downloadable Twistlock CSVs in
  the Images, Scans, or Hosts format (the Connector is strongly recommended);
  please see the *Twistlock
  Support* section for more information.
- **Trivy:** a `.json` file with container image results
  (other scan types are not yet supported).

## Cloud Infrastructure Tools

Software Risk Manager supports the following [Cloud Infrastructure](https://www.blackduck.com/integrations.html#logoWall6) tools and import
formats:

- **Prisma Cloud (RedLock):** a *Tool
  Connector* (Alert data only), a `.csv` file of
  Alerts downloaded from Prisma Cloud UI, or a `.json` file
  from the Prisma Cloud REST API ["List Alerts V1"](https://api.docs.prismacloud.io/reference#get-alerts) endpoint.
- **AWS Security Hub:**
  `.json` and a *Tool
  Connector*.
- **Azure Security Center:** a `.csv` file by clicking
  'Download CSV report' from the 'Recommendations' page in Microsoft Defender
  for Cloud.
- **Check Point CloudGuard:** a *Tool
  Connector* (Posture Finding data only).
- **Wiz:** a *Tool Connector.*
- **Google SCC:** a *Tool
  Connector*.
- **Microsoft Defender for Cloud:** a *Tool
  Connector.*

## Bug Bounty Tools

Software Risk Manager supports the following [Bug Bounty](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **Hacker One:** a *Tool Connector*.

## Infrastructure as Code (IaC) Tools

Software Risk Manager supports the following [Infrastructure as Code](https://www.blackduck.com/integrations.html#logoWall6) tools and import
formats:

- **Checkmarx One:** a *Tool
  Connector.*
- **Checkov:**
  `.json`.
- **Orca Security:** a *Tool
  Connector*.

## Web Application Firewall (WAF) Tools

Software Risk Manager supports the following [Web Application Firewall](https://www.blackduck.com/integrations.html#logoWall6) tools and import
formats:

- **Imperva:** a *Tool Connector*.

## Security Technical Implementation Guide (STIG) Tools

Software Risk Manager supports the following [STIG](https://www.blackduck.com/integrations.html#logoWall6) tools and import formats:

- **STIG:** `.ckl` and `.cklb` format checklist results exported
  by any common STIG tool.

## AppDetective Pro

When generating a *Check Results Report* in AppDetective Pro, you will be given
options for which fields to include. For best results, we recommend including every
field. However, at a minimum, the following fields are required:

- Check Category
- Summary
- Overview
- Fix Information
- CVE
- References
- Links
- Vulnerability
- Description
- Show Occurrences

If any of these required fields are excluded, you will receive an error when
uploading the report to Software Risk Manager and analysis of the file will not be
allowed.

## AppSpider

Software Risk Manager accepts the `VulnerabilitiesSummary.xml` file
from AppSpider. This file is output as part of the report generation process within
AppSpider.

**To generate a report and locate the summary XML file:**

1. Run a new scan or open an existing scan in AppSpider.
2. Generate a report by clicking the Generate Report button on the scan
   toolbar.
3. Locate the generated report on disk (the default location is
   Documents/AppSpider/Scans).

   The
   `VulnerabilitiesSummary.xml` file in the report
   folder is the file that should be uploaded to Software Risk Manager for
   analysis.

## Aqua SaaS Configuration

Software Risk Manager supports Aqua SaaS Configuration. For more information, click
here.

## CodeSonar

The preferred means of importing CodeSonar result into Software Risk Manager is to
use the CodeSonar *Tool
Connector*. However, in situations where the machine running
Software Risk Manager and the machine running CodeSonar cannot communicate with each
other, the *CodeSonar-Scrape* utility can bridge the gap.

*CodeSonar-Scrape* is a command-line utility that you can use to generate a Zip
file that Software Risk Manager understands as CodeSonar results. You provide it the
URL of your CodeSonar server, the name of the project you want to import into
Software Risk Manager, and optionally your username and password. SRM will find all
of the "warnings" associated with that project and download them into a Zip file,
which you can then upload to Software Risk Manager. Results imported in this manner
will include descriptions (tracing) information and links back to CodeSonar's hub
for warning details and category documentation. Detailed instructions for this tool
can be found in the *CodeSonar-Scrape User Guide*. If you need CodeSonar-Scrape
or have questions, [please contact us](https://community.blackduck.com/s/).

## Dynatrace

Software Risk Manager supports data ingestion via the Dynatrace *Tool
Connector*.

Connector authentication is performed with an access token. The user should have both
the `Read security problems` and `Read attacks` scopes
for this token.

## Helix QAC

Software Risk Manager supports the importation of Helix QAC rule compliance reports
(.csv). The instructions below show how to use the Helix QAC GUI to create a rule
compliance report on your local machine that you can upload to SRM.

**To generate a rule compliance report from the Helix QAC GUI:**

1. Click Report from the main menu and use the dropdown list to select which
   project or files to use.
2. Click the "Report Type" field and select "Rule Compliance Report" from the
   dropdown list.
3. Confirm the output location and the name of the report in the location and
   name fields.

   You can either use the default settings or enter new values
   in the respective fields.
4. Click OK.

   The report will be generated and placed in the selected output
   folder.

You can now upload the Helix QAC rule compliance report to SRM.

For more information about Helix QAC, visit Perforce.com.

## JFrog Xray Support

Software Risk Manager imports results from JFrog Xray using its built-in Reports
feature, which does not include a list of the scanned artifacts. This may cause
resolved vulnerabilities to still appear in SRM. For more information, click here.

## Parasoft Support

Software Risk Manager accepts the XML SATE reports generated by Parasoft tools, which
can be generated using both the GUI and CLI. For more information, click here.

## Prisma Cloud Compute (Twistlock)

Software Risk Manager supports data ingestion via the Prisma Cloud Compute
(Twistlock) *Tool
Connector* and CSV/JSON files. The tool connector is **strongly
recommended** due to limitations in CSV export1 and JSON
ingest2.

Connector authentication is performed with a username and password. The user should
have the `monitorImages` (Compute -> Monitor) permission at a
minimum. The recommended built-in role is `DevSecOps`. The connector
will validate that the given user has the necessary permission during
configuration.

The connector offers several options for filtering images. Verifying any of these
options will state the number of images matched. This result is based only on the
filter being verified. During analysis, all filters will be combined.

The connector may ingest vulnerabilities from Deployed, Registry, and CLI image
scans. Each particular image type can be toggled during configuration. Filters will
be applied to all selected scan types, where applicable. Not all filters can be
applied to CLI image scans. Fields inapplicable to CLI images will be noted in their
descriptions within the connector configuration page.

1Downloading CSVs from the Prisma Cloud Compute UI will not download all
results, only those visible on the current page. Full CSVs can be downloaded by
interacting with the REST API at `api/v1/images/download`, which
requires a separate API authentication step against
`api/v1/authenticate`. (Navigating to this endpoint with a
browser will typically fail, regardless of authentication within the Prisma UI.)

2Analyzing JSON results in Software Risk Manager will archive any previous
Twistlock JSON results as a standard part of archival behavior. If multiple images
are being scanned with Twistlock, the scans for all images must be uploaded together
in order for all of their results to persist after analysis.

### Base Image Scanning

Twistlock allows filtering (exclusion) of base image vulnerabilities when
retrieving results, which is exposed as the option *"Exclude base image
vulns"* in the connector config page.

Note: Twistlock [requires](https://docs.paloaltonetworks.com/prisma/prisma-cloud/21-04/prisma-cloud-compute-edition-admin/vulnerability_management/base_images.html) the base image to be in one
of its [configured registries](https://docs.paloaltonetworks.com/prisma/prisma-cloud/21-04/prisma-cloud-compute-edition-admin/vulnerability_management/registry_scanning.html), and the base
image must have been previously scanned:

To define your base images, go to **Defend > Vulnerabilities > Images > Base
images**. The base images you define must reside in your registry and they
must be scanned to exclude their vulnerabilities from scan reports.

### Missing Image Data

Twistlock may temporarily report image data as "missing," even though it may
reappear in subsequent analyses. Results for these images will be missing once
the analysis completes. Such missing data will be reported as a warning on the
Analysis page and in the Visual
Log.

## SARIF

Software Risk Manager strictly supports the v2.1.0 SARIF spec as outlined [here](https://github.com/oasis-tcs/sarif-spec/tree/master/Documents/CommitteeSpecifications/2.1.0) and detailed [here](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html). New formats will be added
explicitly; support for v2.1.0 does not imply support for v2.1.1, and so on.

Note: All ingested SARIF results will be detected as "SAST," regardless of whether a
"Container Analysis" tool generated it.

### Limitations

Software Risk Manager support for SARIF currently does not include the following
notable features:

- External properties files
- Inline external properties
- JSON pointers/SARIF-URI schemes
- Suppressions
- Text/code/artifact snippets
- Localization data
- Details of tool/converter invocation
- Version control "provenance" information
- Location references to binary files
- Graph information
- Stack traces
- Tool notifications

### Results with Multiple Locations

SARIF results containing multiple locations will be split into duplicate results,
one for each location. If multiple `codeFlows` are specified and
none have a sink matching the result location, the `codeFlow`
sinks will be treated as the effective locations, and the result will similarly
be split. This may cause a mismatch between the location reported by the SARIF
result and the location used by Software Risk Manager.

## SBOM Files

Software Risk Manager supports the following [SBOM](https://ntia.gov/SBOM) import formats:

- **CycloneDX:**
  `.xml` and `.json`
- **SPDX:**
  `.spdx` and `.json`

Note: Uploading and analyzing SBOM files will not result in any new findings. The
purpose of importing SBOM files is to provide a single place to retrieve SBOMs and
to store them.
