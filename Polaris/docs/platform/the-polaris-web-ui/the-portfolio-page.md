---
title: "The Portfolio page"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/the-portfolio-page.html"
content_id: "c_jSfXixeYNgmRN7tBwf2A"
product_key: "polaris-platform-latest"
section: "The Polaris web UI"
scraped_at: "2026-08-12T19:55:44.698812+00:00"
content_hash: "56eb32441b4fc4db314e3e9370942f6abaab654e989f8141aed904d373f1b48f"
---

# The Portfolio page

The **Portfolio** page and its sub-pages (The Application page, The Project page) allow you to create and manage applications and projects.

## The Portfolio page

View and manage the applications in your portfolio.

Table 1. Portfolio

|  |  |
| --- | --- |
| [image: portfolio] | |
| [image: portfolio filter icon] Filter | Filter applications by label. In the left panel, select one or more labels to filter the table to show only applications with the applied label(s). Note: See [Create and manage labels](../how-to/create-and-manage-labels.md) for more information. |
| + Create | Create applications:  - New Application(s): Create an application. Note: See Create an application for more information. - New Application(s) with SCM (only available for customers with concurrent subscriptions): Create one or more applications (and projects) using repositories in your SCM. Note: See [Connect Polaris to Multiple SCM Repositories](../how-to/connect-polaris-to-multiple-scm-repositories.md) for more information. |
| Search by Name | Search applications by name. |
| Table fields | Lists all applications in your portfolio. For each application, view:  - The application's risk score Note: Risk scores only appear when the risk scoring feature is enabled. See [Risk scoring in Polaris](../how-to/risk-scoring-in-polaris.md) for more information. - The quantity of projects - The subscriptions available in the application - The total quantity of issues - Per-severity issue quantities - The quantity (sum) of policy violations captured in the most recent test of a default branch in any of the application's projects - The latest completed test (including test type) of a default branch in any of the application's projects   Note: Issue quantities in the Total Issues and severity columns do not include dismissed issues (via issue triage or issues dismissed due to components triaged as excluded).  Note: Quantities in the Total Active Policy Violations ( [image: portfolio policy icon] ) column may include dismissed issues. See Monitor policy on the Portfolio page for more information on the policy values in this table. Click an application name to open the Application page (see "Portfolio Application Page" below). Click on the ellipse icon to select:   - Move projects in application: Move all the projects in this application to a different application. See [Move projects between applications](../how-to/move-projects-between-applications.md) for more information. - Settings: Open the application's settings. - Delete: Delete the application. Note: All of the application's projects, branches, and test data will be deleted. |

## The Application page

View and manage the projects in an application.

### Projects tab

Lists all projects and descriptions in the application.

Table 2. Application > Projects

|  |  |
| --- | --- |
| [image: ui application] | |
| Filter | Filter projects by label. In the left panel, select one or more labels to filter the table to show only projects with the applied label(s). See [Create and manage labels](../how-to/create-and-manage-labels.md) for more information. |
| + Create | Create projects:  - New Project(s): Create a SAST & SCA project, or a DAST project. - New Project(s) with SCM (only available for customers with concurrent subscriptions): Create multiple SAST & SCA projects using repositories in your SCM. Note: See [Connect Polaris to Multiple SCM Repositories](../how-to/connect-polaris-to-multiple-scm-repositories.md) for more information. |
| Test Type | Filter projects by type. |
| Table fields | View all the projects in your application. Hover over project names to see the programming languages detected in the latest SAST test, displayed as approximate percentages (for example, JavaScript 74.33%, HTML 24.2%, Makefile 1.47%). Note: If one or more languages are detected that cannot be scanned (given the test mode), and 90% or more of the code cannot be scanned, a warning [image: icon test metrics error] icon appears next to the project name, indicating an alternative testing method is required to fully analyze the source. Typically, this occurs when a language in your source files can only be tested from your CI system using Black Duck Bridge.  For each project, view:   - The policy status of the most recent test of each project's default branch - The project's name and default branch - The project's type - The total quantity of tests run - The total quantity of issues - Per-severity issue quantities - The quantity of policy violations captured in the most recent test of each project's default branch - The latest completed test (including test type) of each project's default branch - Repository type   Note: Issue quantities in the Total Issues and severity columns do not include dismissed issues (via issue triage or issues dismissed due to components triaged as excluded).  Note: Quantities in the Total Active Policy Violations ( [image: portfolio policy icon] ) column may include dismissed issues. See Monitor policy on the Portfolio page for more information on the policy values in this table.  Click a project name or issue quantity to open the Project page (see "Portfolio Project Page" below) and view issues in the Project. When you click an issue quantity in a severity column, only issues matching the severity you select appear on the Project page.  Click on the ellipse icon to select:   - New Test: Test the project (see [How to test from the web UI](../how-to/how-to-test-from-the-web-ui.md)). - Move project: Move this project to a different application. See [Move projects between applications](../how-to/move-projects-between-applications.md) for more information. - Settings: Open the project's settings. - Delete: Delete the project. Note: All the project's branches and test data will be deleted. |

### Settings tab

Manage settings for applications.

Table 3. Application > Settings

|  |  |
| --- | --- |
| [image: ui application settings] | |
| General | Change the name and description of the application. Apply or remove labels. Change the application's automatic branch deletion setting. |
| Members | Give users or groups access to the application. Control what different users can do with roles. |
| Subscriptions | View DAST, SAST, and SCA subscriptions applied to the application. |
| Licenses | Enable or disable deep license data on an application level. |
| Integrations | Manage your SCM connections and Fix Pull Request settings within an application. |
| Analysis | Here you can:  - Manage an application's file and folder exclusion rules. - Customize event-based test automation for your application (if part of an onboarded SCM repositories) including types of tests and block merge. See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md) for more information. - Customize SAST Analysis settings for application. - Customize SCA Analysis settings for application. |
| Triage | Here, you can:  - Enable or disable triaging issue severity, unless this feature has been locked by your Organization Administrator. When enabled, users can change severity levels when triaging issues in the application's projects. See [Ways to triage issues in Polaris](../how-to/ways-to-triage-issues-in-polaris.md) for more information. - Manage an application's approval workflow—see [Set up triage approval workflows](../how-to/set-up-triage-approval-workflows.md) for more information. |

## The Project page

Different information appears on the Project page, depending on the type of project (SAST & SCA or DAST) you open.

- SAST & SCA project:
  - Branch dropdown
  - Project Test Details
  - Summary tab
  - Issues tab
  - Components tab
  - Licenses tab
  - Tests tab
  - Branches tab
  - Settings tab
- DAST project:
  - Project Test Details
  - Issues tab
  - Tests tab
  - DAST Profiles tab
  - Settings tab

### Branch dropdown

Use the branch dropdown (available while using the Summary, Issues, Components, Licenses, and Tests tabs) to view results for different branches in your project (SAST & SCA projects only).

  
 [image: ui portfolio branch]

### Project Test Details

Select the Project Test Details [image: icon project test details] icon — at the top-right, under your user profile — to view the latest tests run against the project.

Note: In SAST & SCA projects, Project Test Details is available while using the Issues, Components, and Licenses tabs — and shows the latest tests run on the current branch. In DAST projects, Project Test Details is only available while using the Issues tab.

  
 [image: project test details]   

Note: If one or more languages are detected in the latest SAST test that cannot be scanned (given the test mode), and 90% or more of the code cannot be scanned, a warning [image: icon test metrics error] icon appears next to Project Test Details, indicating an alternative testing method is required to fully analyze the source. Typically, this occurs when a language in your source files can only be tested from your CI system using Black Duck Bridge.

### Summary tab

Use the charts on the Summary tab to track the quantity of SAST and SCA issues in a branch over time, and the average age of outstanding (unresolved) issues with different severities.

Table 4. Application > Project > Summary

|  |  |
| --- | --- |
| [image: ui summary tab] | |
| Issues Over Time | A chart that shows the quantity of detected and absent SAST and SCA issues in each test of a branch over time (by default, 30 days). Includes issues imported from third-party tools, when available. Note: Issues captured in different SCA tests (package manager, signature analysis or binary analysis) are tracked separately.  Each point on the chart represents a test. Hover over a point to view the test's completed date and time, and the quantity of detected or absent issues.  Important: Points on the chart are static and represent completed SAST, SCA, or external analysis tests. A test's detected issue quantity includes all the issues detected in the test, even if the issues were detected in earlier tests and dismissed (via triage). A test's absent issue quantity only includes issues that, after being detected the previous test, are no longer detected. Only the previous test is considered when calculating a test's absent issue quantity. |
| Tool dropdown | Use the Tool dropdown near the upper left corner of the chart to show/hide issues captured with different tools. Note: Built-in SAST and SCA tools appear at the top of each category. Separate filters appear for each third-party tool you import issues from (using external analysis tests). |
| Show Detected | Show or hide points on the chart that represent detected issue quantities. |
| Show Absent | Show or hide points on the chart that represent absent issue quantities. |
| Date ranges | Select a date range to narrow the scope of the chart to tests run in a period of time.  - 30D, 90D, 90D: Show the tests run on the branch in the last 30 (default), 60, or 90 days. - Since First Test: Show all the tests run on the branch. - Custom Range: Show the tests run on the branch between two dates. |
| Average Age of Outstanding Issues | A chart that shows the average age (in days) of issues in the branch, grouped by severity. Note: Issue age is the time between when an issue is detected (or redetected) and when the issue is no longer detected (absent) or triaged and dismissed.  Hover over a bar in the chart to see the value in days. |
| Legend | Select a severity in the legend (below the chart title) to hide/show it. |

### Issues tab

Lists issues in the project.

Table 5. Application > Project > Issues

|  |  |
| --- | --- |
| [image: ui project page] | |
| Clear All | Clear checkbox selections. |
| Triage Selected / Triage All | Triage one, multiple, or all issues. See [Ways to triage issues in Polaris](../how-to/ways-to-triage-issues-in-polaris.md) for more information. |
| Export Selected / Export all | Export one, multiple, or all issues. See [How to export issues to CSV or JSON](../how-to/how-to-export-issues-to-csv-or-json.md) for more information. |
| Filters panel | Click the filter [image: A screenshot of the icon used to open the filter panel.] icon to open and close the filter panel. Filter issues by:  - Pending Approvals (find triage requests that need approval) - Triage Status - Fix-By Status - Issue Type - Issue Category - Risk Score - Severity - Severity Modified - Tool Type — DAST, SAST (All, Full, or Rapid), and/or SCA (All, Package Manager, Signature Analysis or Binary Analysis) - Location - CWE (Common Weakness Enumeration, CWE™) - Standard - Owner (assignee) - Pull/Merge Request Policy - Policy Violations - Exposure (Reachable and/or Undetermined)  **Tool** (All, Black Duck SCA - External Analysis, Package Manager, or Signature Analysis). Select a non-default branch with the branch dropdown (near the top of the page) to enable issue comparisons. See [Compare default and non-default branches in a project](../how-to/compare-default-and-non-default-branches-in-a-project.md). Important: Polaris automatically deduplicates components so that, when a component is captured in package manager and signature analysis tests of the same branch, it only appears once on the Components tab. However, each issue associated with the component will be listed twice on the Issues tab (or, duplicate issues appear for each component captured in package manager and signature analysis tests of the same branch). Duplicate SCA issues must be triaged separately, but if you triage a component (exclude it from your SBOM), all of the component's issues (including duplicates) are dismissed.  Note: By default, issues captured in both types of SAST and SCA tests appear in the table. Use the Tool Type filter to show issues captured in specific tests. |
| Table fields | Issue Type: Select an Issue Type name to see the *Issue Details* tab, which includes:  - A description of the issue and its severity - Local effect - Links to related CWE and Common Vulnerabilities and Exposures (CVE®) codes (when available) - CISA KEV status (when the issue appears on the CISA Known Exploited Vulnerabilities catalog) Note: A red CISA KEV label appears in the Issue Type column, next to SCA issues on the CISA KEV list. - Black Duck® Security Advisory (BDSA) codes (when available) - A link to training resources in Secure Code Warrior (when available, and after the Secure Code Warrior integration is enabled by your Organization Administrator) - A list of branches the issue is found in - The Tool and Tool Type that detected the issue - And more   When you select a **SAST** issue, you can:   - Generate remediation guidance with Black Duck Assist. Note: See [Generate SAST remediation guidance with Black Duck Assist](../how-to/generate-sast-remediation-guidance-with-black-duck-assist.md) for more information. - Use the *Contributing Code Events* tab which lets you drill down into the code and see the file path.   For **SCA** issues, you can use the *Exposure* tab to see Reachable and/or Undetermined component vulnerabilities (if reachability analysis is enabled).  For issues captured in **DAST** tests, you can use the *Evidence* tab to find more information on attacks.  Hover over the policy status [image: policy status icon] icon to view the names of issue policies an issue violates. |

### Components tab

Lists a project's open source components, along with each component's version. Use this bill of materials to identify components that require updates and view upgrade recommendations for direct and transitive dependencies. You can use the branch dropdown (near the top of the page, next to the project name) to view components for different branches in your project.

Table 6. Application > Project > Components

|  |  |
| --- | --- |
| [image: components tab] | |
| Filters panel | Click the filter [image: A screenshot of the icon used to open the filter panel.] icon to open and close the filter panel. Filter a project's components by **Pending Approvals** (find triage requests that need approval), **SBOM** (included/excluded), **Component** (name), **License**, **License Family**, **Security Risk**, **Match Type**, **Match Score**, and/or **Policy Violations**. |
| Add Component | Manually add a component to the project. See [Add or modify components](../how-to/add-or-modify-components.md) and Add a component (or component origin) for more information. |
| Clear All | Clear checkbox selections. |
| Triage Selected / Triage All | Triage one, multiple, or all components. See [Ways to triage components in Polaris](../how-to/ways-to-triage-components-in-polaris.md) for more information. |
| Create Fix Pull Request | After selecting a component, if the requirements are met, a Fix Pull Request can be created. See [Fix Pull Requests (Fix PR)](../how-to/fix-pull-requests-fix-pr.md) for more information. |
| Table Fields | For each component, view Security Risk (severity), Policy Violations, Component Name (including version), Match Type, Match Score, Usage, and License Name. Note: If there is “?.?” next to a component name, no origin is specified (more common with components found with binary analysis). To add information, see edit a component.  Hover over the policy status [image: policy status icon] icon to view the names of component policies a component violates.  Important: Polaris automatically deduplicates components so that, when a component is captured in different SCA tests (for example, package manager and signature analysis tests) of the same branch, it only appears once on the Components tab. However, each issue associated with the component will be listed twice on the Issues tab (or, duplicate issues appear for each component captured in different SCA tests of the same branch). Duplicate SCA issues must be triaged separately, but if you triage a component (exclude it from your SBOM), all of the component's issues (including duplicates) are dismissed.  Note: By default, components from different SCA tests are displayed. Use the Match Type filter to only display components captured in package manager, signature analysis or binary analysis tests.  Each component captured in an SCA test is compared with a copy of the component in the Black Duck KnowledgeBase™ to generate additional metadata. Precise match types (beyond direct and transitive dependencies) and (percentage) match scores are generated for components captured in signature analysis tests.  Each component can have multiple match type values. Match types include:   - Direct Dependency: A direct dependency is a package your project requires to run and compile (typically, managed with package managers like pip, npm, ... etc.). It is possible for a package to be both a direct and transitive dependency. - Transitive Dependency: Transitive dependencies are packages that aren't directly referenced in your project, but rather, are packages that are referenced by your project's direct dependencies. It is possible for a package to be both a direct and transitive dependency. - Exact Directory: The component's directory structure matches the directory structure in the KnowledgeBase. - Exact File: The component's files match files in the KnowledgeBase. - Files Added/Deleted: The component includes additional files, or doesn't include some of the files in the KnowledgeBase. - Files Modified: One or more of the component's files were modified and don't match files in the KnowledgeBase. - Manually Added: The component was added to the project manually. - Manually Edited: The component was captured in a test, and then modified manually.   A higher match score indicates a closer match, and a lower match score indicates a component was modified. Precise match scores only appear for components identified in signature analysis tests; the match score for a component identified in a package manager test will always be 100%.  Select a component's name to view:   - **Component Details**   - View detailed information about the component including Match Types, Match Score, a description of the component, and helpful links.   - View Component Origins (different ways the component is included in the project). For each component origin, view upgrade guidance and a dependency tree (View Dependency Tree).   - View Upgrade Guidance and Create Fix Pull Request (if applicable). - **Security Details**   - A list of issues that match the component version, a link to issue details, triage status, origin, CWE and vulnerability ID. Note: A red CISA KEV label appears in the Issue Type column, next to SCA issues on the CISA KEV list. - **Licenses**   - List of licenses available for this component version.   - License information.   - License terms with definitions and categories.   - If available, you can select a different license depending on use case. - **Copyrights**   - View copyright text and component origins for the selected component.   - View security risk. |

### Licenses tab

View Licenses for your project. You can use the branch dropdown (near the top of the page, next to the project name) to view licenses for different branches in your project.

Table 7. Application > Project > Licenses

|  |  |
| --- | --- |
| [image: license tab] | |
| Filters panel | Click the filter [image: A screenshot of the icon used to open the filter panel.] icon to open and close the filter panel. Filter a project's licenses by **License** (name), **Last updated by**, **License Family**, **Source** and/or **Status** . |
| Table Fields | - License Name: The full name of the license. Click on name for screen that includes the following tabs:   - License Details - View license family and other details. Licenses cannot be edited here. See [Edit and review licenses](../how-to/edit-and-review-licenses.md).   - Terms - List of Required, Forbidden and Permitted terms.   - Usage - List of components used by license.   - History - Changes and license text. - License Family: Permissive, Reciprocal, Weak Reciprocal, Reciprocal Network, Restricted Proprietary or Unknown. - Component Count: Number of components using this license. - Source: Modified or Knowledge Base - Status: Review status:   - Unreviewed   - In Review   - Reviewed   - Approved   - Limited Approval   - Rejected   - DeprecatedSee [Edit and review licenses](../how-to/edit-and-review-licenses.md) for more information. - Last Updated: When modified last. - Expiration Date: Can be updated when editing license. Informational only. |

### Tests tab

View tests run on the project.

Table 8. Application > Project > Tests

|  |  |
| --- | --- |
| [image: Project Test Tab] | |
| Table fields | After you open a SAST & SCA project, Use SAST, SCA, and External Analysis tabs to the left of the table to view different types of tests. The DAST tab opens for DAST projects.   - Test ID: An ID that uniquely identifies the test. Hover over a completed SAST test ID to see the programming languages detected in the test, displayed as approximate percentages (for example, JavaScript 74.33%, HTML 24.2%, Makefile 1.47%). Note: If one or more languages are detected that cannot be scanned (given the test mode), and 90% or more of the code cannot be scanned, a warning [image: icon test metrics error] icon appears, indicating an alternative testing method is required to fully analyze the source. Typically, this occurs when a language in your source files can only be tested from your CI system using Black Duck Bridge. - Date: The date and time when the test started. - Test Status: The status of the test (Completed, Canceled, etc.). - Policy Violations: Shows the quantity of policy violations detected in the test, and the quantity of issue and component policies assigned to the project (or branch) when the test started. Select the info [image: policy total active info icon] icon to see the names of the issue and component policies, along with links to view issues that violate different rules. Note: Policy information only appears next to completed tests if issue/component policies were assigned to the branch (for SAST & SCA projects) or DAST project when the test started. Component policies only appear for SCA tests. See Monitor policy on the Tests page for more information. When you create non-default branches, policies are disabled by default. You can enable policies on non-default branches when you Add a branch to a project or Edit a branch (manually created).   Select a test ID to see:   - Detected Issues: Issues detected in the test. - Absent Issues: Issues found in the previous test, but not found in the current test. - Test Metrics: A comparative summary of the current and previous test that includes the programming languages found in the tests (SAST tests only), the number of files captured and analyzed, lines of code analyzed, and analysis time. Note: A warning [image: icon test metrics error] icon appears next to Test Metrics when one or more languages are detected that cannot be scanned (given the test mode), and 90% or more of the code cannot be scanned. Typically, this occurs when a language in your source files can only be tested from your CI system using Black Duck Bridge. - Debugging: Download a test's artifacts (if available) and retrieve its UID. |

### Branches tab

View and manage a SAST & SCA project's branches.

Table 9. Application > Project > Branches

|  |  |
| --- | --- |
| [image: ui branches tab] | |
| + Create New Branch | Add a branch to the project. Note: If you integrate a SCM repository, your default branch in your repository will become you default branch in your Polaris project. To test other branches in your SCM repository, you need to import them. See Add a branch to a project. |
| Show IDE Branches | By default, branches you test with Code Sight (from your IDE) are hidden. Use this toggle to show them. |
| Table fields | Lists all the branches in the SAST & SCA project. Here, you can see:   - The project's default branch - The date and time of the most recent test run against the branch   Click a branch name to modify the branch's settings, including:   - Branch Name - Branch Description - How often the branch needs to be tested before it's deleted automatically - Customizable SAST Analysis settings for branch - Customizable SCA Analysis settings for branch - Policy settings, including:   - If the branch's policies are set manually, or inherited from the project   - The branch's issue policies   - The branch's component policies   - The branch's test scheduling policies - Test Automation - Modify or reset events that will initiate scan (if available). See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md). - View Fix Pull Request settings and customize for branch. |

### DAST Profiles tab

View and manage the DAST profile associated with a DAST project.

Table 10. Application > Project > DAST Profiles

|  |  |
| --- | --- |
| [image: ui portfolio dast profiles] | |
| Table fields | Lists the profiles in the DAST project.  Here, you can see:   - The date and time of the most recent test run against the project - The quantity of issues captured in the most recent test, grouped by severity   Select a profile name to modify its settings, including:   - Profile Name - Allowed Hosts and Authentication - The profile's scan-settings.json file - Whether or not active attacks are performed when the project is tested |

### Settings tab

Manage settings for projects.

Table 11. Application > Project > Settings

|  |  |
| --- | --- |
| [image: project settings general] | |
| General | Edit the Project Name and Project Description. Apply or remove labels. Change the project's automatic branch deletion setting. View External Analysis projects—used for importing data automatically from third-party tools. See [Import issues from Black Duck SCA](../how-to/import-issues-from-black-duck-sca.md) for details of the supported connector. |
| Integrations | - Set up a Source Code Management (SCM) repository integration. See [Connect a Polaris project to a repository in your SCM](../how-to/connect-a-polaris-project-to-a-repository-in-your-scm.md). - Set up issue tracking integration for the project. You can select integration options (such as auto-close settings) from the Azure Options or Jira Options dropdown. See [Issue tracking integrations](../how-to/issue-tracking-integrations.md) for more information. - View and customize Fix Pull Request settings for the project. |
| Licenses | Enable or disable deep license data on a project level. |
| Policies | View project policies and add an existing policy to the project. |
| Analysis | Here you can:  - Manage a project's file and folder exclusion rules. - Customize event-based test automation for your project (if part of an onboarded SCM repositories). See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md) for more information. - Customize SAST Analysis settings for project. - Customize SCA Analysis settings for project. |
| Triage | Enable or disable triaging issue severity, unless this feature has been locked by your Org Admin. When enabled, users can change severity levels when triaging issues in the project. See [Ways to triage issues in Polaris](../how-to/ways-to-triage-issues-in-polaris.md) for more information. Manage a project's approval workflow. See [Set up triage approval workflows](../how-to/set-up-triage-approval-workflows.md) for more information. |
