---
title: "API"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/api.html"
content_id: "kzLdoNpgs6u3D7mpchobGA"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:06.001382+00:00"
content_hash: "874b4abace014744750311f460eb118faf60722d566bd1f88b1dd81f88b5a009"
---

# API

The plugin also provides an API to use its functions programmatically. More information
on how to use the ZAP API can be found on the [ZAP GitHub Wiki](https://github.com/zaproxy/zaproxy/wiki/ApiDetails).

Note that as a security measure, ZAP will not include messages with Exceptions by
default. If you want to enable messages, you can check *Report error details via
API* in *Tools -> Options -> API*.

## Actions

**uploadReport**

Uploads a report to Software Risk Manager. Note that uploading an empty report with
no alerts will cause an Exception to be thrown as Software Risk Manager won't be
able to read it and will return a non-200 response.

*Parameters*

- filePath: Absolute path to the report file
- serverUrl: Software Risk Manager server URL
- codeDxApiKey: Software Risk Manager API Key
- projectId: Software Risk Manager Project ID
- fingerprint: Optional SHA1 hash of an invalid certificate to make an
  exception for
- acceptPermanently: Optional boolean for if the exception should be stored
  permanently in a truststore file.

*Returns*

`OK` if the report is uploaded successfully.

**generateAndUpload**

Generates a Software Risk Manager report, saves it to a temporary file, uploads to
Software Risk Manager, then deletes the file.

*Parameters*

- serverUrl: Software Risk Manager server URL
- codeDxApiKey: Software Risk Manager API Key
- projectId: Software Risk Manager Project ID
- fingerprint: Optional SHA1 hash of an invalid certificate to make an
  exception for
- acceptPermanently: Optional boolean for if the exception should be stored
  permanently in a truststore file.

*Returns*

`OK` if the report is uploaded successfully.

`EMPTY` if the generated report is empty. The report will not be
uploaded to Software Risk Manager.

## Views

**generateReport**

Generates an XML report with request and response data.

*Returns*

An XML report String.
