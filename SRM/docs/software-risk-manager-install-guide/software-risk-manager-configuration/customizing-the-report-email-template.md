---
title: "Customizing the Report Email Template"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/customizing-the-report-email-template.html"
content_id: "30ZTf8WGX0e6mA8igq2jWg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:40.981529+00:00"
content_hash: "3d5f679eab312dc774ca5477222753bf211e1a2b6e80441001c74c4314053409"
---

# Customizing the Report Email Template

Software Risk Manager allows notifications to be sent by email when report generated
. (To enable email notifications, see Configuring
Email Notifications in the *SRM User Guide*.) There is a standard report email template,
which can be customized as needed.

**To customize a report email template:**

1. Navigate to the AppData folder and locate the template files.

   There is a standard report email template that can be
   customized as needed.

   - `report-builtin-email-template.json`

     This file is used to
     notify the user that report has been generated.

   (For more information on the SRM AppData directory, see Understanding the AppData
   Directory.)
2. Open the file you want to customize using any text editor.
3. Make changes to the text as needed.

   Changes should be limited to the actual
   text; variables or references, such as `\"{reportName}\"`,
   should not be altered.
4. Save the file using the form `*-custom-template.json`.

   Say, for
   example, you want to customize the "report" email template. You would locate
   the file `report-builtin-email-template.json`, edit the file, then
   save it as `report-custom-email-template.json`.
