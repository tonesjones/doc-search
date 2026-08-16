---
title: "Analysis license files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-license-files.html"
content_id: "l7~x3VtCs8DYeK687IduTA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:56.508061+00:00"
---

# Analysis license files

You can use Coverity Connect to host your Coverity Analysis license files, and associate
them with their respective Coverity Connect projects. This allows Desktop Analysis users
to be covered by the analysis license file specified by their associated Coverity
Connect project.

To view or update your analysis license files, navigate to Configuration > System > Analysis License Files. This page displays your previously uploaded analysis licenses, and
allows you to perform the following tasks:

Default License
:   Select your default analysis license from a list of your previously uploaded
    license files. The default license will be associated with each Coverity
    Connect project that isn't specifically configured to use another
    license.

Import...
:   Import a new analysis license or FlexNet file. Use the pop-up dialog to
    choose a file and edit the license name.

Update...
:   Upload a license file to replace the selected analysis license.

Delete...
:   Delete the selected analysis license. If the default license is deleted, the
    value in the Default License drop-down will change to
    "None."

Export
:   Export the selected analysis license file.

Once you have uploaded your analysis license files, you can associate them with specific
projects. To do so, complete the following steps:

1. Navigate to Configuration > Projects & Streams.
2. Select the relevant project from the list in the left pane.
3. Click Edit and choose the correct license file from
   the Analysis License File drop-down menu.

Note: All projects not specifically associated with a license file using these
steps will use the default license.
