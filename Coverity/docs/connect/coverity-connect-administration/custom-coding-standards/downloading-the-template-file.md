---
title: "Downloading the template file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/downloading-the-template-file.html"
content_id: "ep55ciZaMIPwnIRDDPITIQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:35.382017+00:00"
---

# Downloading the template file

You can download a template coding standard file.
This can be a help when creating a custom coding standard.

To download the template from the Configuration > Standards
window, click Download Template. The template, a JSON file, is
downloaded to your local system. You can then edit this file to create your custom standard.

Like the JSON code for a built-in standard, the template contains
`"name"` and `"mapping"` objects.
It also contains an object called `"// unmapped-issue-type-codes"`.
This list contains an entry for each issue type code recognized by Coverity Connect.

When you use the template as a basis for a custom coding standard, these are the overall steps:

1. Edit the `"name"` string to give your custom standard a name that does not
   duplicate the name of any existing standard.
2. *Delete the contents* of the `"mapping"` list.

   Important:
   The fields in the `"mapping"` list are provided simply as examples.
   Their names duplicate issue keys already present in the `"mapping"` section, and if these
   entries are present when you upload your new JSON file, the new coding standard will fail.
3. In the `"// unmapped-issue-type-codes"` section, locate issues you want your custom standard to support.
   Copy these and paste them to the `"mapping"` section.
4. In the updated `"mapping"` section, edit the second string to the preferred value.
5. Save the new custom standard.
6. Upload the standard to Coverity Connect.

Now when a scan finds an issue of this type, and you have enabled this column in the Settings dialog,
Coverity Connect will display an additional column labeled Standard: <Custom name>.
The values in this column will be the custom values you have specified.
