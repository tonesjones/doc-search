---
title: "Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuration.html"
content_id: "JyTt2CZqPdqDUdaj4O68sw"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:08.114037+00:00"
content_hash: "83a121c2944fc1729ca7a3eceae38f6e782a5e9d4466a9909718b52182be3cc2"
---

# Configuration

Under *Apps* in the Splunk home screen, click *Code Dx* to open the Software
Risk Manager add-on.

  
 [image: image]   

Go to *Configuration* and click *Add-on Settings*. Then input the URL of your
Software Risk Manager server. Keep in mind that your server's URL may or may not have
`/codedx` at the end.

Input your API key.

  
 [image: image]   

Click *Save*.

## Handling a Self-Signed Certificate

If the server hosting Software Risk Manager is using a self-signed certificate, you
must also populate the *CA Bundle* field with the path of a
`.pem` or `.cer` certificate file. Alternatively
(although not recommended), you can set the value for *CA Bundle* to
`ALL` to disable certificate verification.

  
 [image: image]

### Get a copy of the certificate as a file

The following steps use Windows and Chrome.

Navigate to the page with the untrusted certificate using your browser (i.e.
Chrome). Then bring up Chrome developer tools by opening the Chrome menu (⋮),
then going to *More Tools* -> *Developer Tools*.

  
 [image: image]   

Click the *Security tab* and click the *View certificate* button to
bring up the certificate details popup.

  
 [image: image]   

Go to the *Details* tab in the *Certificate* popup and click the
*Copy to File...* button.

  
 [image: image]   

Use the `Base-64 encoded X.509 (.CER)` format, then choose a name
and location for the file.

  
 [image: image]   

When you click the *Finish* button, it should say "the export was
successful."
