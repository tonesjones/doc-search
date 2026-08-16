---
title: "Filters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/filters.html"
content_id: "oEgiRHjy0BD0dG1vA0nmaA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:22.106101+00:00"
---

# Filters

You use filters to specify the scope of the issues and issue-related data that you want
to display. Filters vary according to the View type (for example, Issues: By
Snapshot, Functions, or
Snapshots) that you are using.

By default, Coverity Connect displays some filter data in columns of the same name. For
example, many View types display a Total column in their views,
by default. You can select other columns to display them in the view (see Columns).

Table 1. Filters

| Filter | Description | View Types |
| --- | --- | --- |
| Action | Recommended action. See Action. | Issues: By Snapshot, Issues: Project Scope |
| Acyclic Path Count (APC) | Estimated number of execution paths through the function. See Acyclic Path Count. | Functions |
| Acyclic Path Count - Statements only (APC-S) | Estimated number of execution paths through the function, disregarding branches within a statement. See Acyclic Path Count. | Functions |
| Analysis Time | Time that it took to analyze the code that underlies the snapshot. Example: `01:16:46` | Snapshots |
| Backedge Count | Number of back edges in the control flow graph. | Functions |
| Blank Lines | Number of blank lines in the source code. | Files, Components, Snapshots, Trends |
| Block Count | Number of blocks in the control flow graph. | Functions |
| Build Time | Time that it took to build the source code that underlies the snapshot. | Snapshots |
| CALLING | Number of distinct functions that call the analyzed function. **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |
| CALLS | Number of distinct functions that the analyzed function invokes.  The following count as functions:   - Overloaded operators (each overload counts as a separate   function) - Constructors - Destructors - "operator new" - "operator delete" - Virtual calls (only the function being called virtually   counts)   The following do not count as functions:   - Indirect calls - Function pointer calls   **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |
| Category | Issue category. | Issues: By Snapshot, Issues: Project Scope, Checkers |
| CCM | Cyclomatic complexity metric, which is the number of linearly independent paths in the function body. | Functions |
| Checker | Name of the checker that discovered the issue. You can quickly select all filters by enabling the Select All field. | Issues: By Snapshot, Issues: Project Scope, Checkers |
| CID | The CID of the issue. | Issues: By Snapshot, Issues: Project Scope |
| Classification | Classification of the issue. See Classification. | Files, Issues: By Snapshot, Issues: Project Scope |
| Code Lines (LOC) | Number of lines of code in the project.[1] | Files, Components, Snapshots, Trends |
| COMF | Comment density (the number of comments per statement).  Note: The number of comments is calculated by counting the comments within the function body and then adding 1 if there are comments before the function body. This number is then divided by the number of statements within the function body to arrive at a value for COMF.  A value of `-1` indicates that an actual value has not been calculated. | Files, Functions |
| Comment Lines | Number of lines in the code that contain comments. Uncommented code or code that has too few comments can lead to issues when other developers attempt to modify it. | Files, Components, Snapshots, Trends |
| Comparison | Comparison indicates whether an issue is present in the snapshot(s) specified in the view's field in the comparison scope. You can choose from one of the following options:  - Present - The CID exists in at least one of the comparison   snapshots. - Absent - The CID does not exist in any of the comparison   snapshots. | Issues: By Snapshot, Issues: Project Scope |
| Component | Component name. For example, the component in which the issue, file, or function is found. | Issues: By Snapshot, Issues: Project Scope,Files, Functions,Components |
| Count | Number of issue occurrences. For example, see the Occurrences tab in Figure 1. | Issues: By Snapshot |
| CWE | [Common Weakness Enumeration](http://cwe.mitre.org/) (CWE) identifier for software weaknesses, which include issues such as resource leaks, cross-site scripting vulnerabilities (XSS), null pointer dereferences, and so on. | Issues: By Snapshot, Issues: Project Scope |
| CYCLE | Number of call graph recursions over one or more functions. **Note:** A value of `-1` indicates that an actual value has not been calculated. | Files |
| Date | Date when the snapshot was committed to Coverity Connect. Date of the trend record. Example: `2012-09-09 20:09:19.136` | Snapshots, Trends |
| Description | Snapshot description. | Snapshots |
| Dismissed | Number of dismissed issues. | Files, Functions, Components, Checkers, Owners, Trends |
| Duration(ms) | Duration of test in milliseconds. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Tests |
| External Reference | An internal identifier used by your company to track the issue. See Ext. reference. | Issues: By Snapshot, Issues: Project Scope |
| File | Name of the file in which the issue, file, or function is found. | Issues: By Snapshot, Files, Functions |
| File Count | Number of files in the snapshot. | Snapshots |
| First Detected | Date when the issue was first detected. | Issues: By Snapshot, Issues: Project Scope |
| First Detected By | Value that helps identify the process by which an issue was initially reported to Coverity Connect: Snapshot (for issues initially reported through a commit process that yields a snapshot), Preview (for issues initially reported through a preview process, which does not produce a snapshot, for example, when Coverity Desktop invokes `cov-run-desktop`), API (for issues initially reported through a special, rarely used process). In each case, a CID for the issue is created. Note: Preview issues that a developer fixes before pushing code changes to the source code repository will never have (or need) a snapshot. Preview issues left unfixed before they are pushed to the repository will typically undergo the server-based analysis and commit process. Therefore, these issues will receive a snapshot in Coverity Connect *after* they were initially reported, and it will be possible to triage the associated CIDs and see events related to them in the source code browser (from an Issues: By Snapshot view that lists the CID).  Whether fixed or left unfixed prior to the push to the source code repository, issues will be be identified as Preview issues if they were initially reported through a preview process. | Issues: Project Scope |
| First Snapshot (column only - not a filter) | ID of the snapshot in which the issue was first detected. | Issues: By Snapshot, Issues: Project Scope |
| First Snapshot Date | Specified range of dates in which one or more issues was first committed. | Issues: By Snapshot, Issues: Project Scope |
| First Snapshot Description (column only - not a filter) | Description of the snapshot in which the issue was first detected. | Issues: By Snapshot, Issues: Project Scope |
| First Snapshot Stream (column only - not a filter) | Stream in which the issue was first detected. | Issues: By Snapshot, Issues: Project Scope |
| First Snapshot Target (column only - not a filter) | Target platform of the snapshot in which the issue was first detected. | Issues: By Snapshot, Issues: Project Scope |
| First Snapshot Version (column only - not a filter) | Version number of the snapshot in which the issue was first detected. | Issues: By Snapshot, Issues: Project Scope |
| Fix Target | Target milestone for fixing an issue, such as a release or version. See Fix target. | Issues: By Snapshot, Issues: Project Scope |
| Fixed | Number of fixed issues. | Files, Components, Checkers, Owners, Trends |
| Forwardedge Count | Number of forward edges in the control flow graph. | Functions |
| Function | The name of the function that contains the issue. | Issues: By Snapshot |
| Function Count | Number of functions in the source code that underlies the snapshot. | Snapshots |
| Function Merge Name[2] | Internal function name used as one of the criteria for merging separate occurrences of the same software issue, with the result that they are identified by the same CID. | Issues: By Snapshot |
| GOTO | Number of `goto` statements in the function. **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |
| Halstead Effort | Estimated effort required to modify a program based on empirical findings by Halstead. In general, the less effort required, the easier it should be to modify the program. | Functions |
| Halstead Errors | Estimate that relates program errors to the number of operands used. In general, the more operands used, the more prone to error the program is. Estimate is based on empirical findings by Halstead. | Functions |
| Has analysis summaries | Indicates if analysis summaries are included in the snapshot. | Snapshots |
| ID | Snapshot ID. | Snapshots |
| Impact | Issue impact as determined by Coverity Connect: High, Medium, Low, Audit. | Issues: By Snapshot, Issues: Project Scope, Checkers |
| Inspected | Number of inspected  issues. | Trends |
| Issue Density | Number of unresolved (outstanding) issues per 1000 lines of code. | Files, Components, Trends |
| Issue Kind | Quality, Security, Test, or Various issue. | Issues: By Snapshot, Issues: Project Scope |
| Language | Programming language associated with the defect. | Issues: By Snapshot, Issues: Project Scope, Files, Functions |
| Last Failure | Date when test last failed. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Tests |
| Last Impacted | This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. Date of the most recent snapshot in which the function was either changed directly by a developer (resulting in a modification of its syntactic structure) or affected by a direct change elsewhere in the code base that affects the behavior of the function. Examples include changes to the items called by the function or to the global variables used by the function. | Functions |
| Last Modified | This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. Date of the most recent snapshot in which the function was modified. Last modification date is computed from SCM data and is taken to be the most recent date on which any of the source code lines belonging to the function were modified. | Functions |
| Last Run | Date when test was last run. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Tests |
| Last Snapshot (column only - not a filter) | ID of the snapshot in which the issue was last detected. | Issues: By Snapshot, Issues: Project Scope |
| Last Snapshot Date[4] | Specified range of dates in which one or more issues was last detected. | Issues: By Snapshot, Issues: Project Scope |
| Last Snapshot Description (column only - not a filter) | Description of the snapshot in which the issue was last detected. | Issues: By Snapshot, Issues: Project Scope |
| Last Snapshot Stream (column only - not a filter) | Stream in which the issue was last detected. | Issues: By Snapshot, Issues: Project Scope |
| Last Snapshot Target (column only - not a filter) | Target platform of the snapshot in which the issue was last detected. | Issues: By Snapshot, Issues: Project Scope |
| Last Snapshot Version (column only - not a filter) | Version number of the snapshot in which the issue was last detected. | Issues: By Snapshot, Issues: Project Scope |
| Last Success | Date when test last passed. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Tests |
| Last Triaged | Date when the issue was most recently triaged. | Issues: By Snapshot |
| Legacy | Searches for issues by the Legacy attribute. Options are:   - False - True - Various | Issues: By Snapshot, Issues: Project Scope |
| LEVEL | Maximum nesting depth of control flow structures such as `do`, `for`, `if`, `switch`, `try`, and `while`. **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |
| Line Count | Number of lines of code. | Functions |
| Merge Extra | Internal property used as one of the criteria for merging occurrences of an issue. | Issues: By Snapshot |
| Merge Key | Internal signature used to merge separate occurrences of the same software issue and identify them all by the same CID. | Issues: By Snapshot |
| Name | Test name. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Tests |
| New | Number of new issues. | Files, Functions, Components, Checkers, Owners, Trends |
| Newly Detected | Issues that were not in the previous snapshot. | Components, Checkers, Snapshots |
| Newly Eliminated | Issues from the previous snapshot that are no longer present. | Components, Checkers, Snapshots |
| Number of Unique Operands | Number of unique operands in the program | Functions |
| Number of Unique Operators | Number of unique operators in the program | Functions |
| Outstanding | Number of unresolved (outstanding) issues. | Files, Functions, Components, Checkers, Owners, Trends |
| Owner | User or group name of the issue owner.[3] | Issues: By Snapshot, Issues: Project Scope, Owners |
| Owner Name | Name of the issue owner. | Issues: By Snapshot, Issues: Project Scope, Owners |
| PARAM | Number of function arguments. **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |
| Policy Coverage | Policy Coverage. This filter was applicable only with Coverity Connect projects that included Test Advisor datadata, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Files, Functions, Components |
| Policy Covered Lines | Number of lines covered by tests according to your Test Advisor policy. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Files, Functions, Components |
| Policy Uncovered Lines | Number of lines not covered by tests according to your Test Advisor policy. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Files, Functions, Components |
| Raw Coverage | Raw coverage. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Files, Functions, Components |
| Raw Covered Lines | Number of lines covered by tests as reported by the coverage tool. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Files, Functions, Components |
| Raw Uncovered Lines | Number of lines not covered by tests as reported by the coverage tool. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Files, Functions, Components |
| Resolved | Number of dismissed and fixed issues. See resolved issues. | Trends |
| RETURN | Number of return points within the function. **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |
| Severity | Severity of the issue. See Severity. | Issues: By Snapshot, Issues: Project Scope |
| Score | Issue score. The score is assigned by a compliance scoring policy. For more information, see "Using scores to prioritize development tasks" in the Coverity Compliance Guide. | Issues: By Snapshot |
| Standard: Hyundai Coding Standard C | Identifies the Hyundai Coding Standard C rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: Hyundai Coding Standard Cost of Implementation | Cost of remediating the issue occurrence. Pertains only to issues that result from the violation of Hyundai Coding Standard C, C++, or Java rules. | Issues: By Snapshot, Issues: Project Scope |
| Standard: Hyundai Coding Standard C++ | Identifies the Hyundai Coding Standard C++ rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: Hyundai Coding Standard Java | Identifies the Hyundai Coding Standard Java rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: Hyundai Coding Standard Likelihood | Likelihood of an occurrence of the issue manifesting. Pertains only to issues that result from the violation of Hyundai Coding Standard C, C++, or Java rules. | Issues: By Snapshot, Issues: Project Scope |
| Standard: Hyundai Coding Standard Severity | Severity of the issue. Pertains only to issues that result from the violation of Hyundai Coding Standard C, C++, or Java rules. | Issues: By Snapshot, Issues: Project Scope |
| Standard: AUTOSAR C++14 | Identifies the AUTOSAR C++14 coding-standard rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: CERT C | Identifies the SEI CERT C coding-standard rule or recommendation violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: CERT C++ | Identifies the SEI CERT C++ coding-standard rule or recommendation violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: DISA STIG V4R3 | Identifies the DISA-STIG V4R3 coding-standard rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: DISA STIG V4R10 | Identifies the DISA-STIG V4R10 coding-standard rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: DISA STIG Severity | Identifies the severity of the issue according to the DISA-STIG Standard | Issues: By Snapshot, Issues: Project Scope |
| Standard: DISA STIG V5 | Identifies the DISA-STIG V5 coding-standard rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: ISO TS17961 2016 | Identifies the ISO/IEC TS 17961:2013/Cor1:2016 coding-standard rule violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: MISRA Category | Number of MISRA issues that fall into these selected categories:   - Mandatory: no guidelines are violated. - Required: justification required. - Advisory: guidance provided. - None: MISRA does not apply. | Issues: By Snapshot, Issues: Project Scope |
| Standard: OWASP Mobile Top Ten 2016 | Identifies the OWASP Mobile Top Ten 2016 software vulnerability category violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: OWASP Web Top Ten 2017 | Identifies the OWASP Web Top Ten 2017 software vulnerability category violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: OWASP Web Top Ten 2021 | Identifies the OWASP Web Top Ten 2021 software vulnerability category violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| Standard: PCI DSS 2018 | Identifies the PCI DSS 2018 coding-standard requirement violated by the issue. | Issues: By Snapshot, Issues: Project Scope |
| State | Test state. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Tests |
| Status | Status values:   - New: Issues that are classified as   Unclassified. - Triaged: Issues that are classified as   Pending,   Bug, or   Untested. - Dismissed: Issues that are classified   as Intentional, False   Positive, Tested   Elsewhere, or No Test   Needed, and that are present in the latest   snapshot. - Absent Dismissed: Issues classified as   Intentional, False   Positive, Tested   Elsewhere, or No Test   Needed, that were present an earlier   snapshot but are absent from the latest snapshot. - Fixed: Issues that do not occur in the   latest snapshot are assigned this status by Coverity   Connect.   Coverity Connect automatically tracks the status of issues based on the state of an issue: For example, Coverity Connect assigns the status New if the analysis discovers a new issue in the latest snapshot. If you change the classification of an issue, Coverity Connect updates the status to reflect the change. For example, if you change the classification to Bug, the status is updated as triaged. If an identical issue exists in more than one stream, Coverity Connect unifies them. This attribute is not displayed in the Triage pane. | Issues: By Snapshot |
| STMT | Number of statements in the function. **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |
| Stream | Stream name. You can choose to include or exclude matching names. | Snapshots |
| Streams | The Streams filter is useful if you need to perform a search for issues in a subset of streams in your project.  Enter a full or partial stream name in the menu to select streams that you want to examine. You can select multiple streams, one at a time.  Specify the scope of the software issues that you want to include in the search results:   - Any: CIDs that have ever occurred in   any of the selected streams. - All: Only those CIDs that have ever   occurred in all of the selected streams at one time or   another. | Issues: By Snapshot |
| Suite | Name of the test suite. This filter was applicable only with Coverity Connect projects that included Test Advisor data, and is no longer valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. | Tests |
| Target | Target platform as specified by:  - In the Target attribute in a    Snapshots    view. - The `--target` option to the `cov-commit-defects` command when   committing the snapshot to Coverity Connect. For more   information about the `cov-commit-defects`   command, see the Coverity 2026.6.0 Command Reference. | Snapshots |
| Total | Total number of issues. | Components, Checkers, Owners, Trends |
| Total Detected | Total number of issues detected in the snapshot. | Snapshots |
| Total Number of Operands | Total number of operands in the program | Functions |
| Total Number of Operators | Total number of operations in the program | Functions |
| Triaged | Number of triaged issues. | Triaged column: Files, Functions,, Components, Checkers, Owners, Trends |
| Type | Issue type. For example, Resource leak, Out-of-bounds write. | Issues: By Snapshot, Issues: Project Scope, Checkers |
| Version | The version of the most recent commit to any of the streams in the project. The version is specified by the `--version` option to the `cov-commit-defects` command. For more information, see Coverity 2026.6.0 Command Reference. | Snapshots |
| VOCF | Language scope.  This value is calculated as follows:  VOCF = (N1 + N2) / (n1 + n2)  where:   - N1 = Total number of operators in the function - N2 = Total number of operands in the function - n1 = Number of different operators in the function - n2 = Number of different operands in the function   For the purposes of calculating VOCF (vocabulary frequency), the following conditions apply:   - Assignment using `=` counts as 1 operator.  When used to initialize a variable, `=` does   not count as an operator. For example, the count for   `int x = 10` includes 1 operand but 0   operators. - A compound assignment (`+=`,   `-=`, and so on) counts as 2   operators. - Accessing a structure, a pointer, and an access passed by   reference are counted as 1 operator. - The comma operator (for example `(1, 2)`) is   counted as 2 operators.  The operands on either side of the comma might include   operators of their own. - A cast is counted as 1 operator. - Array access using `[]` is counted as 1   operator per dimension specified.  The array variable is counted as 1 operand and each parameter   enclosed in brackets (`[]`) is counted as 1   operand. - The parentheses (`()`) used in a function call   count as 1 operator. - A function can be an operand. - The `sizeof()` operator is counted as 1   operator.  In addition to `sizeof()` itself, the operand   it is called on might include operators of its own.   **Note:** A value of `-1` indicates that an actual value has not been calculated. | Functions |

- [1] Number of lines of code in the source code files within the scope of a
  given node of a hierarchy. Does not include lines fully composed of comments or blank
  lines in the source code. However, any line that includes both code and a comment counts
  as a line of code.
- [2] Separate instances of software issues (issue occurrences) receive
  the same CID if they are found by the same checker and have
  the same Merged Function Name and Merge
  Extra property. These instances share the same Merge
  Key.
- [3] You can use the <User> token on the
  Owner filter to return only software
  issues assigned to whichever user is currently logged in. See
  Relative user
- [4] See Grammar for time filter usage for
  information about how CIDs are returned for date filters.
