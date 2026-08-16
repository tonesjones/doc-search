---
title: "Using Visual Studio Code to edit the coverity.conf configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-visual-studio-code-to-edit-the-coverity.conf-configuration-file.html"
content_id: "k25INSTJd_QLUAl2A4HiDw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:52.920963+00:00"
---

# Using Visual Studio Code to edit the coverity.conf configuration file

The contents of coverity.conf are JSON code. The Microsoft Visual
Studio Code editor is a convenient way to maintain coverity.conf.

Note:
Visual Studio Code is available for most platforms. You can download its installer from the
Microsoft VS Code site: [code.visualstudio.com](https://code.visualstudio.com).
After the download completes, install the application.

To set up VS Code so that it can edit coverity.conf with useful highlighting,
use VS Code to associate coverity.conf with the JSON format, then
use a text editor to add the Coverity Configuration schema to the VS Code settings.

The Coverity Configuration schema is itself a JSON file, coverity.conf.schema.json,
and so is the VS Code Settings file, settings.json.
The schema tells VS Code how to correctly display and highlight the contents of
coverity.conf. It also lets VS Code validate the JSON
code, and autocomplete certain strings while the user types.

**To associate coverity.conf as a JSON file, for editing:**

1. Go to File → Preferences → Settings.
2. Navigate to User → Text Editor → Files.
3. In the Files section, under Associations, click
   Add Item.
4. Use the controls to associate coverity.conf with the JSON format.

   If you use other kinds of `.conf` files, you might want to associate
   those with JSON, as well.

   For example, you might set up the following
   associations:

   Table 1. File associations in VS Code

   | Item | Value |
   | --- | --- |
   | `*.conf` | `java` |
   | `coverity.conf` | `java` |

   Setting up these associations in VS Code creates a
   `"files.associations"` field in the
   settings.json file.

**(Recommended) Verify the location of the JSON schema for coverity.conf:**

1. If you run Coverity Connect locally, make sure it is running. If you run it via the web, make
   sure it is online. This way, VS Code can access the schema file.
2. Copy the URL you use for the schema file.

   The name of the schema is
   coverity.conf.schema.json. The URL typically has a
   format such as, https://<coverity-server-name>:8443/schemas/coverity.conf.schema.json.
3. Paste the URL in the search field of a web browser.

   If the address is correct, the browser
   displays the contents of the schema file, and possibly some of its metadata as
   well.

**To associate coverity.conf with a JSON schema:**

1. In VS Code, press `Ctrl+Shift+P` (`Command+Shift+P` on a Mac system).
2. At the prompt, type in `settings json`.
3. From the list that displays, choose Preferences: Open Settings (JSON).

   This opens the settings.json file.
4. In settings.json, add an array object named
   `"json.schemas"`.
   This array must contain the following two fields:

   `"fileMatch"`
   :   An array that must include an entry that specifies the string
       `"coverity.conf"`.

       This associates the schema with the coverity.conf file.

   `"url"`
   :   Set this to the address of the schema file; for example,
       "https://<coverity-server-name>:8443/schemas/coverity.conf.schema.json",
       where the server name and port number should match the system that users
       work with.
5. Save the updated settings.json file.

**(Optional) Enable comments in JSON code:**

Comments are not a standard JSON feature. By default, VS Code highlights them as errors.
If you want your JSON file to include comments, you must enable these in VS Code.

1. At the right side of the status bar, click the label JSON.

   VS Code displays a drop-down list with a search field.
2. In the search field at the top of the drop-down list, type `json`.

   VS Code updates the contents of the drop-down list.
3. Choose the entry {} Configure JSON with Comments (jsonc).

   Now the label on the status line reads, JSON with Comments.
4. Save the file once again.

The following listing shows a minimal settings.json file for use
with VS Code. You can copy and paste this code, but if you do, remember to modify the
server host name and the port value so they match the name and port of the Coverity
Connect server that users are working with.

```
{
    "files.associations": {
        "coverity.conf": "json"
    },
    "json.schemas": [
        {
            "fileMatch": [
                "coverity.conf"
            ],
            "url": "https://<coverity-server-name>:8443/schemas/coverity.conf.schema.json"
        }
    ]
}
```
