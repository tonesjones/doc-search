---
title: "Create a report"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-a-report.html"
content_id: "XrLiLXqcxYs7TeAruxqJHA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:36.402241+00:00"
content_hash: "371a7eb4bec14aaebbcda7b437524430e16f871903eb8c85129f1f90814486ed"
---

# Create a report

## Overview

Use the Reporting page to generate detailed, customizable reports that summarize SAST, SCA, and DAST issues captured in tests. Report types range from developer-focused summaries to executive overviews and compliance reports, and offer insights into vulnerabilities, test trends, checkers used in testing, and the risk posture of applications in your portfolio. Note the following:

- Reports are automatically deleted after 30 days. Up to 1000 reports can be saved at a time.
- Only the user who created a report can download it. Share reports in PDF or JSON format.
- It can take up to 60 minutes for:
  - Issue data from a test to affect reports.
  - Issue and component triage actions to affect reports.

    Note: Dismissed issues and excluded components (via issue and component triage) are not included in reports. Issue and component triage actions only affect reports after changes are approved.
  - Components you add, edit, or delete to affect reports.
  - Changes made to application, project, and branch settings (including application labels) to affect reports.
  - Changes made to file and folder exclusion rules to affect reports.
- Reporting events are tracked in the audit logs.
- Issues you import from third-party tools appear in reports, but the components and licenses associated with issues you import do not.
- You can save report settings as report configurations to enable reports to be re-run. These saved configurations can also be shared with other users and groups in your organization. Each copy is unique to the recipient, letting them make changes without affecting the original configuration. Unless you're an admin for your organization, you can only share configurations with users or groups who have access to all applications mentioned in the configuration. If you are an organization admin, sharing with people who can't already access the relevant applications will allow recipients to see the configuration values, so you'll be warned of this before confirming the share action.

### Available reports

You can generate the following reports:

Table 1. Available reports

| Type of report | Description |
| --- | --- |
| Developer Detail Dynamic | An overview of the issues in the selected application scope. Provides DAST issue details organized by the issue type and includes severity, location, and first detected date. |
| Developer Detail SCA | An overview of the issues in the selected application scope. Provides issue details organized by the component and includes the severity, vulnerability ID, Issue type, CWE, exposure, and first detected date of each issue. |
| Developer Detail Static\* | An overview of the issues in the selected application scope. Provides issue details organized by the issue type and includes severity, location, file name, line number, and first detected date. |
| Executive Summary Report\* | Provides an overview of your portfolio and modules that detail the overall risk posture. It includes issue summaries at the portfolio and application levels, detected and absent issue charts, issue trend charts, top issue types and top issues with policy violations. |
| Issue Overview\* | A high level overview of your applications and projects. The report provides the total issue counts at the application level, and provides the new, recurrent, and total issue counts at the project level. This shows the risk posture across the entire portfolio. |
| Issue Summary\* | Includes a summary of its scope and issue summaries by severity, per application(s), per project(s), and by issue type including top 10 vulnerable applications, exposure (SCA only) and more. |
| Security Audit\* | Identifies vulnerable areas in the different components of your application that may be exploited by a malicious users, and estimates the application's protection from common attacks. This report also assesses the overall security risk for your application across all threat areas. It includes exposure (SCA only). |
| Software bill of materials (SBOM) | Creates a SPDX or CycloneDX-compatible SBOM report in JSON format. |
| Standard Compliance\* | Provides issue counts for each application as it relates to a selected standard, exposure (SCA only), as well as a view of the total issues found per standard. |
| Standard Compliance Detail\* | Along with the information in the Standard Compliance Report, this includes the issue counts for each project. It also provides issue details organized by test type and standard for each issue. |
| Test Summary Report | For applications and/or projects (depending on selected scope), shows first and last test, number of tests in a time period, test trends, assessment types scanned and a list of applications and/or projects not tested in time period. This report lists the versions of Coverity and Rapid Scan Static (Sigma) used in the latest SAST tests. |
| Notices File Report | The Notices File report provides a customizable list of open source components, the associated license text and copyright statements to help manage and leverage your licenses. If enabled, deep license data can be selected to be included. |

Note: \* This report includes the option to list checkers used during the latest tests (of projects and branches in the report's scope).

### Report modules

Most reports include a Report Modules section where you can control which modules appear in the generated report and, for select modules, customize their content. This lets you tailor reports for your audience — for example, removing sections that aren't relevant to your stakeholders, or editing narrative text to add organizational context.

Note the following:

- All modules are enabled by default, except Tool checker information, which must be manually enabled.
- For modules that include an Edit button, you can customize the module's content. Depending on the module, selecting Edit reveals editable text fields or checkboxes to include or exclude specific information, like charts or table columns.
- Module selections and content customizations can be saved in report configurations.

Note: The Report Modules section is available for all standard PDF reports. It is not available for SBOM reports.

### Allow reporting notifications

In order to receive email notifications that your report is ready, check that your personal notification settings are set correctly.

1. Select your profile name, then select **Account**.
2. Go to **Notifications**.
3. If necessary, enable **Reports**.

   Note: If you can't make changes, it means an Org Admin has turned off notifications for the organization. You won't be able to change settings and won't receive notifications until this is resolved.

### Save report configurations

If you find you generate the same report on a routine basis, consider saving the report's settings as a report configuration. Doing so allows you to quickly generate the same report without having to configure the report's settings each time. Additionally, you can automate report generation (on a daily, weekly, or monthly basis) by adding a schedule to report configurations.

Saved report configurations are unique to individual users. If you create one, only you have access to it, but you can share a copy of it with users and groups within your organization. Shared copies of saved configurations have the following characteristics:

- Don't include any schedules associated with the original configuration.
- Distinct from the original configuration, so making changes to a saved configuration won't affect anyone else who has a copy of it.
- Unless you're an organization admin, configurations can only be shared with users and groups that can already access all applications mentioned in the configuration. If you are an org admin, sharing with people who can't already access the relevant applications will allow recipients to see the configuration values, so you'll be warned of this before confirming the share action.
- Configuration name includes the name of the person who shared it. Also, if the shared configuration has the same name as one of your existing saved configurations, the end of its name will get a distinguishing instance number. For example, the shared configuration might be named `Overdue TPS data for April - shared by Bob Porter - 6`.

See [Create and manage report configurations](create-a-report/create-and-manage-report-configurations.md) for more information.

## Create a report

(For all reports except SBOM and Notices File.) Create customized PDF reports of your test results.

1. Navigate to Reporting (via the icon in the left-hand navigation).
2. Select **+ Create Report**.

   The Create Report page is displayed.
3. Select a Report Type. (See report types above for more information.)
4. Enter a Report Name.

   Report configuration names must be unique, are limited to 240 characters, and can include special characters.
5. (Optional) Select Append date to report name: to add a date suffix to the report name.
6. Adjust the scope of the report:
   - All applications and projects (default branches/profiles only) (default): Include data from all the applications and projects in your portfolio that you have access to. Only includes issues from default branches.
   - Applications, projects and branches/profiles matching specific filters (non-IDE branches only): Set up a filter to select the applications, projects, and branches (not IDE) to include in the report. After you select this option, select Manage Scope. Use the options in the Manage Scope dialog to set up your filter, and preview the applications, projects, and branches the filter selects on the right. If using branch labels, you can use the checkboxes under Labels to refine your selection. Click Save.

     Note: If you want to include IDE branches in your filter, select the next option.
   - Specific project branches/profiles: Select specific applications, projects, and branches to include in the report. After you select this option, select Manage Scope. Use the options on the Manage Scope window to select the branches to include in the report. If using branch labels, you can use the checkboxes under Labels to refine your selection. After you adjust a filter, use the checkboxes in the Branch/Profile column to select branches to include in the report. Click Save.
7. Use the Tools checkboxes to select DAST, External Analysis, SAST, and/or SCA (depending on the report) to include found by these tools in the report.

   Note: By default, reports that have Tools include all the results for the test type, unless you have the option to select specific test types and you use it. For example, SCA results include all types of SCA Tests (**Package Manager**, **Signature Analysis** and **Binary Analysis**), unless you can select one test type.
8. Use the Severity Levels checkboxes to select the severity of issues to include in the report.

   For a Security Audit, Issue Overview or Executive Summary Report, all severity levels are automatically selected.
9. (Optional) Use the Severity Modified checkboxes to filter issues by whether their severity has changed during triage:

   - Yes (modified): Include issues with modified severities.
   - No: Include issues with default severities.

   Note: By default, both options are selected, so all issues are included.
10. Select one option under **Standard**:

    - Required for the Standard Compliance Reports.
    - You can only select one standard per report (if available).
    - If optional and no standard is selected, all issues are retrieved from the other selected criteria (severity level, etc.). Some issues do not belong to any standards.
11. Select **Time Period** (for Security Audit and Test Summary Reports only) or **Trend Chart Time Period** (Executive Summary Report).
12. (Optional) Under Optional Report Modules, enable Tool checker information to include checkers used during the latest tests (of projects and branches in the report's scope) in the report.
13. (Optional) Under Report Modules, select which modules to include in the report:

    - Use the checkboxes to include or exclude modules from the report. All modules are enabled by default, except Tool checker information, which is disabled by default. Enable it to include a list of checkers used during the latest tests (of projects and branches in the report's scope).
    - For modules with an Edit button, select Edit to customize the module's content. Some modules reveal editable text fields; others reveal checkboxes to include or exclude specific information, such as charts and table columns.
14. Polaris sends you an email when your report is ready. Return to the Reporting page and select the Download [image: icon report download] icon to download the report (PDF).
15. (Optional) Select the report name to view more details about the completed report.

    - Select View Scope to see a granular view of the branches/profiles, applications, and projects that were included in the report scope. You can search for a specific component.
    - To download the report (PDF), click Download.
    - To run the report again, click Duplicate.

## Create a software bill of materials report

Create a JSON-compatible software bill of materials (SBOM) report of a project.

Note: The SBOM report is a JSON file compatible with SPDX (v. 2.3) or CycloneDX (v. 1.4 or 1.6).

To customize what is included in the report, see [Ways to triage components in Polaris](ways-to-triage-components-in-polaris.md). If a component is triaged as **Excluded**, it will not be in the report.

1. Navigate to Reporting (via the icon in the left-hand navigation).
2. Select **+ Create Report**.
3. Select SBOM from the Report Type dropdown menu and then enter a **Report Name**.
4. Select a project from the Scope dropdown menu.

   Note: The SBOM report only captures data from default branches. Data from non-default branches is ignored. Selecting a specific branch is not supported.
5. From the **Export Format** dropdown menu, select **SPDX V2.3 Report**, **CycloneDX V1.4 Report**, or **CycloneDX V1.6 Report**.
6. Use the **Tools** checkboxes to include or exclude components detected in different SCA tests.

   Note: By default, the SBOM report includes components detected in all types of SCA tests (**Package Manager**, **Signature Analysis** and **Binary Analysis**).
7. Select Run > Run. 

   Tip: You can create a report configuration when you run the report. Doing so allows you to quickly regenerate the report later on using the same settings. To do so, select Run > Run and Save Configuration. You can also create a report configuration without running the report (Run > Save Configuration).

   See [Create and manage report configurations](create-a-report/create-and-manage-report-configurations.md) for more information.

   Polaris sends you an email when your report is ready. Return to the Reporting page and select the Download [image: icon report download] icon to download the report (JSON).

## Create a Notices File report

The Notices File report provides options to list open source components, the associated license text, and copyright information. This report will help you to manage and leverage your licenses.

This report is available as a text file, HTML, or PDF. You can include the following modules in the report:

- Scope (maximum of five branches).
- License data (components). Lists of components and their associated license names.
- Lists of licenses with their text.
- Copyright text. When enabled, the report will contain a section that lists the component origins and the associated copyright statements.
  - Only available if components with origins are present in projects.
  - If there are no copyrights associated with this component origin in our database, a “No copyrights found” statement appears.

To generate a Notices File report, follow these steps:

1. Go to Reporting.
2. Select **+ Create Report**.
3. Select Polaris Notices File Report from the Report Type dropdown, and then enter a **Report Name**.
4. Select a Report Format (PDF, HTML Web Page, or Text File).
5. Select Manage Scope, and set the scope of the report.

   Note: The Polaris Notices File Report can include data from a maximum of five branches.
6. Select what type of license data to include (declared, deep license, or both.) Note: deep license data is only available if enabled. See [Create and manage report configurations](create-a-report/create-and-manage-report-configurations.md).
7. Select the Report Modules to include in the report. Options include:
   - Scope
   - License data (components)
   - License text
   - Copyright text (for each component origin)
8. Select Run > Run. The time it takes to generate the report will vary depending on the size of the project.

   Tip: You can create a report configuration when you run the report. Doing so allows you to quickly regenerate the report later on using the same settings. To do so, select Run > Run and Save Configuration. You can also create a report configuration without running the report (Run > Save Configuration).

   See [Create and manage report configurations](create-a-report/create-and-manage-report-configurations.md) for more information.

   Polaris sends you an email when your report is ready. Return to the Reporting page and select the Download [image: icon report download] icon to download the report.
