---
title: "GUI configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gui-configuration.html"
content_id: "LO_w8n2nHozXQsuaxMScRw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:12.886943+00:00"
---

# GUI configuration

To configure a new Security report, you use one of four panes to specify information:

- **Coverity Connect** to specify connection information.
- **Assurance Level** to specify the minimum passing score for the
  project.
- **Severity Mapping** to select one of the default severity mapping or to
  specify a custom severity mapping.
- **Customization** to specify company and organizational unit information;
  you can also select the locale for the report.

Note: Some reports display information about individual issues. These reports bound the
number of issues displayed in order to control the size of the report. This bound is
called the *issue cutoff count*. It is used for CVSS, Security, PCIDSS,
Mobile OWASP, and OWASP reports. Default value is 200. Maximum is 10000 for Security
report.

You can increase the maximum of 10,000 to a number as large as 50,000 by
setting the `ISSUE_CUTOFF_COUNT` environment variable to the desired
value.

CAUTION:

SANS report versions do not appear in the GUI. To
configure the version of a SANS report, you need to edit the
config.yaml file and use it from the command line or within a
script.

**To configure a report:**

1. Select Settings > Coverity Connect.
2. Select Coverity Connect Project.

   The projects available through the connection to Coverity Connect are displayed
   in the drop-down list. If the list is empty, click
   Refresh.
3. In the Assurance Level pane, select the minimum passing
   score for the project.
4. In the Severity mapping pane, select a severity mapping.
   Default severity mappings are read-only. If you select
   Custom, you can edit the
   Severity level of each Technical
   Impact.
5. In the Customization pane, enter information to customize
   the report. The names and terms are used throughout the report, and the company
   name and logo are featured on the cover page.

   Note: The
   Project mentioned here refers to the corporate
   project name, and should not be confused with the Coverity Connect
   project.

   The company logo is optional.

   You can use this
   pane to set the locale for your report
6. Click File > Save to save the configuration for future use.
7. You can now generate a report as described in the following section.
