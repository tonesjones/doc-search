---
title: "Update SAML configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-saml-configuration.html"
content_id: "j~BgYCsoGFTZSHCkqTbNGw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:40.747668+00:00"
---

# Update SAML configuration

Example PUT request to update the SAML configuration.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/samlConfigurations/my_saml_config" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "my_updated_saml_config",
  "entityId": "urn:test:coverity", 
  "disabled": false,
  "idpMetadataFile": "<md:EntityDescriptor \
xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" 
entityID=\"http://www.okta.com/exk2m1o2fs2zSK8LF5d7\"> \
<md:IDPSSODescriptor WantAuthnRequestsSigned=\"false\" \
protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"> \
<md:KeyDescriptor use=\"signing\"> \
<ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><ds:X509Data>\
<ds:X509Certificate>\
MIIDqDCCApCgAwIBAgIGAXzlRelnMA0GCSqGSIb3DQEBCwUAMIGUMQswCQYDVQQGEwJVUzETMBEG \
A1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzENMAsGA1UECgwET2t0YTEU \
MBIGA1UECwwLU1NPUHJvdmlkZXIxFTATBgNVBAMMDGRldi0xOTExMjQyOTEcMBoGCSqGSIb3DQEJ \
ARYNaW5mb0Bva3RhLmNvbTAeFw0yMTExMDMxMDA3NTZaFw0zMTExMDMxMDA4NTZaMIGUMQswCQYD \
VQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzENMAsG \
A1UECgwET2t0YTEUMBIGA1UECwwLU1NPUHJvdmlkZXIxFTATBgNVBAMMDGRldi0xOTExMjQyOTEc \
MBoGCSqGSIb3DQEJARYNaW5mb0Bva3RhLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC \
ggEBAIJmYj/3n1C8xU5f1UTeApGkvsGTMUALdLobSxbNrheBiKczWPYc6n+n1fPPxBvXGHEARuFt \
/avTlThdCDuJW3d2SiYan4D0dTg1ue0yZuSX7e2O6Rzm8TxJzpeNHquKUoOp4gyGJaXDciDecMp+ \
/j1kYOeXGOinQF/nYXpGWjHCQewwA3ObrU0xfCknARckLBr2p0ziQh3eGVkP9ybdD8U336IoeDNr \
sTEcG8KFpbqBhDJTjDSmcdsd3O9Dy8dCgoI63ghuH1NWYFI+18sfu1ramRsmKufGsEEysjAJjxpa \
P7v/8kWyCEyjAVJQTlCo6ikFhWTDpO+oEC4iF5bBRD8CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEA \
EuPhHv90bvqObPBK3ekOlmxZsxVglTOY8U+Xv6eh+QLodaC7700TKaayJCmNG1juij6NUTbBpQSY \
8PbBaJ5rwxBtMnRIMEam3NndM2e8ny7i7h5NWzVRPqWAhO+kgEmuusTNTB5v6/1a4gbRQGXI5uto \
JdPNS7PqiLp6ia/hNXqr2AGw6wwqdFYpGWu1wpFGE+Q5dCiGr8MCjoQwZ+h1IWB0AWqmrU2V+Zl4 \
B3+DcMIMfGtML/qYjcHhDSKoXxmhjehGnOTxyL6V+Y88bPLOYKPlSu1BQEaYkmqnDz57p5lfg/Hf \
e5kflkS4k4qKXxQScBVJvkb7P9qasf8K/af5OA==</ds:X509Certificate> \
</ds:X509Data> </ds:KeyInfo> </md:KeyDescriptor> <md:NameIDFormat>\
urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat> \
<md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>\
 <md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" \
Location=\"https://dev-19112429.okta.com/app/dev-19112429_connecthttps_1/exk2m1o2fs2zSK8\
LF5d7/sso/saml\" /> <md:SingleSignOnService \
Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" \
Location=\"https://dev-19112429.okta.com/app/dev-19112429_connecthttps_1/exk2m1o2fs2zSK8\
LF5d7/sso/saml\" />    </md:IDPSSODescriptor></md:EntityDescriptor>",
  "groupsEnabled": true
}'
```
