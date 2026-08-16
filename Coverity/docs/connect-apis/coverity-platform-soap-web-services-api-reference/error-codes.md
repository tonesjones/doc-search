---
title: "Error codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/error-codes.html"
content_id: "3Hb9r3BPrN5uYiHVKYDhIQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:01.601386+00:00"
---

# Error codes

Descriptions of error codes returned for invalid Web service requests. Codes that were
introduced in the latest release appear in bold font face.

**SOAP Example (Error 1300 to an updateProject() request):**

<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"> <S:Body>
<S:Fault xmlns:ns4="http://www.w3.org/2003/05/soap-envelope">
<faultcode>S:Server</faultcode> <faultstring>No stream found for name
EXAMPLE-cpp.</faultstring> <detail> <ns2:CoverityFault
xmlns:ns2="http://ws.coverity.com/v8"> <errorCode>1300</errorCode>
<message>No stream found for name EXAMPLE-cpp.</message>
</ns2:CoverityFault> </detail> </S:Fault>
</S:Body></S:Envelope>

**Authentication errors produce a error message without an error code. For example:**

<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"> <S:Body>
<S:Fault xmlns:ns4="http://www.w3.org/2003/05/soap-envelope">
<faultcode>S:Server</faultcode> <faultstring>User authentication
failed.</faultstring> </S:Fault> </S:Body></S:Envelope>
