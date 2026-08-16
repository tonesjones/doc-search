---
title: "Title page schema elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/title-page-schema-elements.html"
content_id: "aquN0t8RR5vjBFOV93UP9g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:00.289202+00:00"
---

# Title page schema elements

The schema for the title page should include the following key:

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `company-name` | String | Lists the customer's company name. | N/A | Yes |
| `logo` | String | Lists the file pathname to display the logo of the company. Valid image types are .bmp, .gif, .jpg, and .png. The maximum image size allowed is 210 pixels wide by 70 pixels high.  (If a backslash character is used in the file pathname, then it must be a double backslash. For example: `C:\\logo\\ourlogo.jpg`. You can also use a single forward slash, like this: /var/logo/ourlogo.png.) | N/A | No |
| `organizational-unit-name` | String | Lists the name of your division, group, team, or organizational unit. | N/A | Yes |
| `organizational-unit-term` | String | Lists the unit term used for the organization. | N/A | Yes |
| `prepared-by` | String | Lists the name of the entity or individual that prepared the report. | N/A | Yes |
| `prepared-for` | String | Lists the name of the entity or individual for which the report was prepared. | N/A | Yes |
| `project-contact-email` | String | Lists the email address of the project contact; the email address of the recipient of the report. This element is used by the following reports: CIR, CVSS, PCIDSS, Mobile OWASP, and OWASP. | N/A | Yes |
| `project-name` | String | Lists the project name for the report. | N/A | Yes |
| `project-version` | String | Lists the project version number. | N/A | Yes |
