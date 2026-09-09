---
title: "Customizing the Policy Email Template"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/customizing-the-policy-email-template.html"
content_id: "nBCOzxluThReR_ZCKCWW0A"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:41.579404+00:00"
content_hash: "a0ae0524f1f9c011f5b8413f5ccee18e4b27bb8b05783f513e9ab2246613ae67"
---

# Customizing the Policy Email Template

Software Risk Manager allows notifications to be sent by email when policy status
changes. (To enable email notifications, see Configuring
Email Notifications in the *SRM User Guide*.) There are three standard
email templates, which can be customized as needed.

**To customize a policy email template:**

1. Navigate to the AppData folder and locate the template files.

   There are three
   generic email templates, and each one is based on a policy violation
   status:

   - `error-builtin-template.json`

     This file is used to
     notify the user that a policy has been violated.
   - `success-builtin-template.json`

     This file is used to
     notify the user that the policy violation has been
     resolved.
   - `warning-builtin-template.json`

     This file is used to
     notify the user that a policy has a violation risk.

   (For more information on the SRM AppData directory, see Understanding the AppData
   Directory.)
2. Open the file you want to customize using any text editor.
3. Make changes to the text as needed.

   Changes should be limited to the actual
   text; variables or references, such as `\"{project-name}\"`,
   should not be altered.
4. Save the file using the form `*-custom-template.json`.

   Say, for
   example, you want to customize the "error" email template. You would locate
   the file `error-builtin-template.json`, edit the file, then
   save it as `error-custom-template.json`.
