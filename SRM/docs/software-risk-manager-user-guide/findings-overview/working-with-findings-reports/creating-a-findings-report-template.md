---
title: "Creating a Findings Report Template"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/creating-a-findings-report-template.html"
content_id: "PFDwMWtXPWz3JVDBdLQcwQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:17.528331+00:00"
content_hash: "3030ec9cb4cd6df0893dd56ed1d49c56280466a3c100459ad2fbbf5d48aab0ee"
---

# Creating a Findings Report Template

Click the Reports icon in the navigation bar to open the Reports page. This page lists
all the existing custom report templates along with the following information:

- **Name.** The name of the report template.
- **Owner.** The owner of the report.
- **Type.** The type of report. Options are PDF, Compliance (PDF), XML, CSV,
  AlienVault/NBE, and Nessus.
- **Filter.** A dropdown list of available filters from the Findings page.
- **Schedule.** When a report should be generated.
- **Send To.** Email address to send the report.
- **In This Report.** The number of projects associated with the report. (Click
  the link to view the projects.)

Clicking the dropdown configuration icon allows you to view, edit, send now (report), or
delete the report template.

**To create a report template:**

1. Click the Reports icon in the navigation bar.
2. Click Create Report Template.

   [image: image]

   Creating a report template consists of three elements:
   - Report type and definition
   - Schedule
   - Projects
3. Enter a name for the template and a description (optional).
4. Add a filter by clicking the checkbox (optional) and selecting a filter from the
   dropdown list.

   Filter options will include your own saved filters, if any,
   along with any saved filters that are shared with you.

   Note: Saved
   filters that are shared with you must be copied before they can be used. A
   dialog will appear asking if you want to copy the shared filter.
5. Select and define a report type. (See Generating a Findings Report for detailed instructions.)
6. Click the Schedule tab.

   [image: image]
7. Define how often you want to run the report.

   You can select a recurring day
   and time or day of the week and time.
8. Enter an email address where you want the report to be sent.
9. Click the Projects tab or click Next.

   [image: image]
10. Click Add Project(s) to define which projects will be associated with this
    report.
11. Click Finish.
