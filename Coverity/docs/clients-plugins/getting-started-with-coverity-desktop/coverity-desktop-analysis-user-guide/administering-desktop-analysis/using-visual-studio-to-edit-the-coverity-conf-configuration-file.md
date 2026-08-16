---
title: "Using Visual Studio to edit the coverity.conf configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-visual-studio-to-edit-the-coverity.conf-configuration-file.html"
content_id: "2cYJgNJBlW7ixPG4B77OEA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:53.578839+00:00"
---

# Using Visual Studio to edit the coverity.conf configuration file

If users are working with Visual Studio 2015 or later, and with Coverity 2019.09 or
later, they can add a "$schema" field to the
coverity.conf file, without having to update
settings.json.

Note: Visual Studio is available for most platforms. You can download its installer from the
Microsoft Visual Studio site: [visualstudio.microsoft.com](https://visualstudio.microsoft.com). After the download
completes, install the application.

The "$schema" field enables JSON support in both Visual Studio and
Visual Studio Code, even if user settings (settings.json) are not
modified as described in the previous section regarding VS Code.

**(Recommended) Verify the location of the JSON schema for
coverity.conf:**

1. See these instructions.

The following code listing shows a minimal coverity.conf file that
uses the `"$schema"` field:

```
{
    "$schema": "https://<coverity-server-name>:8443/schemas/coverity.conf.schema.json",
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        // ...
    }
}
```
