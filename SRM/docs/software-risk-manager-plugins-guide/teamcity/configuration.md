---
title: "Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuration.html"
content_id: "f~IVwCZIdy_z~0ZEHaz2Vg"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:05:49.505976+00:00"
content_hash: "4b690d36c3b8a113a9fa1b8d2314562bce427ca176d3a6c834cad6d389f73135"
---

# Configuration

After installing the plugin, the next step is to add a Software Risk Manager Build Step
to your project. Navigate to the "Build Steps" page for your project and click the "Add
build step" button. The "New Build Step" page will display and a dropdown will ask you
to "Choose build runner type". After selecting the "Code Dx" option, the configuration
fields will display.

## Publishing

The *Code Dx URL*, *API key*, and *Project* fields are required for
publishing. Ask your administrator to generate an API key
that has the `create`
role for the project it needs to interact with.

Once the *Code Dx URL* and *API key* fields are populated, the
*Project* dropdown will automatically list the projects available to the
API key. If you receive a warning regarding an invalid/untrusted certificate, refer
to the section on self-signed certificates.

The *Source and binary* field allows you to identify the files in the job
workspace for Software Risk Manager to analyze. The format of this field is a
comma-separated list of Ant glob file location patterns. You can populate this list
by specifying the files (relative to the workspace) that will be sent to Software
Risk Manager.

  
 [image: image]   

The *Files to exclude* field is an advanced option that can be displayed by
clicking "Show advanced options" near the bottom of the page. This field allows you
to specify files to omit in the source and binaries zip file that is uploaded to
Software Risk Manager. Ant glob file location patterns are also supported.

  
 [image: image]   

Software Risk Manager supports importing the results of more than 70 commercial and
open source analysis tools, in
addition to generic listing formats.
This feature is supported in the TeamCity plugin via the *Tool output files*
field, where you specify a comma-separated list of paths and filenames of each
output file.

  
 [image: image]   

The *Analysis Name* field allows you to name the analyses performed by TeamCity.
You can find the analysis names on the "First Seen by SRM" and "Last Modified"
filters on Software Risk Manager's Findings page. You can use build/environment
variables to construct a different name for each analysis. For example,
`Build #%build.number%` creates analysis name "Build #26" for the
26th build of the project. Clicking the icon next to the input control will list
possible values for parameter references. You can also construct links using a
syntax similar to markdown, i.e., `[link text](link url)`.

  
 [image: image]

### Handling a Self-Signed Certificate in TeamCity

If the server hosting Software Risk Manager is using a self-signed certificate,
you'll receive a warning:

  
 [image: image]   

Clicking *Show advanced options* will allow you to populate the
*Self-Signed Certificate Fingerprint* field with the SHA1 fingerprint
of the self-signed certificate used by the server. Contact your Software Risk
Manager administrator for the correct value. Or you can navigate to your
installation of Software Risk Manager in a browser, and obtain the fingerprint
by following the instructions for your particular browser:

- Chrome: Click the lock icon next to the URL, choose the *Connection*
  tab and follow the link for "Certificate Information". Expand the
  "Details" section; the SHA1 fingerprint is near the bottom.
- Firefox: Click the lock icon next to the URL, choose the *Security*
  tab, and click the *View Certificate* button. The SHA1 Fingerprint
  should be at the bottom of the resulting window.
- Safari: Click the lock icon next to the URL, click *Show
  Certificate*, expand the *Details* section, and the SHA1
  Fingerprint can be found near the bottom.
- Internet Explorer: Click on the *Certificate Error* text to the
  right of the URL, select the *Details* tab, and find
  *Thumbprint* and *Thumbprint algorithm* fields. Ensure
  that the value of the *Thumbprint algorithm* field is "sha1" and
  use the value of the *Thumbprint* field.

Once you have the correct fingerprint, populating the *Self-Signed Certificate
Fingerprint* field will allow you to proceed.

## Waiting for Analysis Results

When performing an analysis, the TeamCity build runner will zip up the specified
workspace files and send them to the Software Risk Manager server. By default,
TeamCity will not wait for the results of the analysis.

In some cases, you will want to wait for the analysis to complete so you may consider
the TeamCity job a success or failure. To take this even further, a team may also
want the resulting Software Risk Manager analysis data to influence the state of the
build. Additionally, you may want to see a summary of the Software Risk Manager
build and analysis results within TeamCity, including the resulting Software Risk
Manager tables. This is all possible by selecting the *Wait for results*
checkbox.

  
 [image: image]   

Upon enabling this option, the fields below will be enabled.

  
 [image: image]   

The *Report archive name* field allows you to name the build artifact that the
build runner produces. The artifact is a zip archive that contains an HTML file.
This zipped HTML file can be used to configure a build report tab. The build report
tab will display the build statistics tables. If this field is left blank, the build
artifact will not be generated.

  
 [image: image]   

The *Fail build on severity* field allows you to have the build marked as
"failed" if Software Risk Manager reports your project contains findings that match
the chosen option. This field is defaulted to "None" and the build step will finish
upon successfully uploading all files to Software Risk Manager. If a different
option is selected, the build step will not finish until the analysis is
complete.

  
 [image: image]   

The *Only fail on new findings* option, when checked, means that the build will
only be marked as failed if *new* findings that match the *Fail build on
severity* option are reported.

  
 [image: image]
