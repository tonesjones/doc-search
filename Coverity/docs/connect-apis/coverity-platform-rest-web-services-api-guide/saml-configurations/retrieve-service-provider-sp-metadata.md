---
title: "Retrieve service provider (SP) metadata"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-service-provider-sp-metadata.html"
content_id: "1jN6GoRvyJIW3MVrK~nHPQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:42.698707+00:00"
---

# Retrieve service provider (SP) metadata

Example GET request to retrieve the service provider (SP) metadata.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/samlConfigurations/my_saml_config/spMetadata" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "spMetadataFile": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><EntityDescriptor 
xmlns=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"urn:test:cim:noop\">\n  
<md:SPSSODescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" 
WantAssertionsSigned=\"true\" 
protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\">\n 
<md:KeyDescriptor use=\"signing\">\n <ds:KeyInfo 
xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\">\n <ds:X509Data>\n 
<ds:X509Certificate>
MIIDIDCCAgigAwIBAgIELcLBoDANBgkqhkiG9w0BAQsFADBSMQ0wCwYDVQQGEwROb25lMQ0wCwYDVQQHEw
ROb25lMQ0wCwYDVQQKEwROb25lMQ0wCwYDVQQLEwROb25lMRQwEgYDVQQDEwsxMC4yNy4xMC4zMzAeFw0y
MTExMDkxODMxNTVaFw00MTExMDkxOTAxNTVaMFIxDTALBgNVBAYTBE5vbmUxDTALBgNVBAcTBE5vbmUxDT
ALBgNVBAoTBE5vbmUxDTALBgNVBAsTBE5vbmUxFDASBgNVBAMTCzEwLjI3LjEwLjMzMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlRMRNDneqLaTrA4raerocHENUTnRNWbonjH06YZpzr2nIElKx0H1ye
swu1rnfAOk08xnYnQq9klNzNh1XRrJ8NlIvh98K0cqHvuyDPtdWOIkBbk9pqXpjDTZzxgZn2mcu+BL8x/0
Qt2rbFZ2gFNrLS5V9rdQj+1UOl1f61sZ5FtZ52sbT2Fh5r1HwdlO8IaQvZ0rhydi7CQgNsMyslfSEJLR2q
759SIHe7TnCgF3EOkxXRxoUkoRGcn72XhHNUjPgSBQ4zd30hLXg5Oc2UF8Ds+X8MYo+uwt/n4lPVfYDYIh
hbVo9Gqh7y5EWuuKPwwwrvA6ncfgA5LWYH+rUb5nmQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQBiYjxGyi
ckfI6mLM9L4b3IJ5gDyGV+jChmLStMsv50VefjhJEaBqU3WEWGKtPDM3zy8UQJAT1+LIxUUJsoxlvaKSsK
6cgwYPGWg3+E0htTpDbnRJ2l7W3nf+n5nVtI2oxyLOTYJLiMpB8Kc9b2+wITtcttiuOOlgKOZumvwjhB6J
UGkgCn1YAz5eLRgwHsNliWr6I4uhO9Al7ffS4BLewr0MRqWzgpoJK3vYIi62SX1s3SnHE5x3AuVpI3L81t
Ps/MgbbRr0oxih2hr0BQXdb6nYA+6Ty+RsMx+49Pol8T4ImygsFwbK9yrtlR+A3Y1p97fEfhBo+8QoVRti
coSOmi</ds:X509Certificate>\n </ds:X509Data>\n </ds:KeyInfo>\n </md:KeyDescriptor>\n 
<md:KeyDescriptor use=\"encryption\">\n 
<ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\">\n 
<ds:X509Data>\n 
<ds:X509Certificate>MIIDIDCCAgigAwIBAgIELcLBoDANBgkqhkiG9w0BAQsFADBSMQ0wCwYDVQQGEw
ROb25lMQ0wCwYDVQQHEwROb25lMQ0wCwYDVQQKEwROb25lMQ0wCwYDVQQLEwROb25lMRQwEgYDVQQDEwsx
MC4yNy4xMC4zMzAeFw0yMTExMDkxODMxNTVaFw00MTExMDkxOTAxNTVaMFIxDTALBgNVBAYTBE5vbmUxDT
ALBgNVBAcTBE5vbmUxDTALBgNVBAoTBE5vbmUxDTALBgNVBAsTBE5vbmUxFDASBgNVBAMTCzEwLjI3LjEw
LjMzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlRMRNDneqLaTrA4raerocHENUTnRNWbonj
H06YZpzr2nIElKx0H1yeswu1rnfAOk08xnYnQq9klNzNh1XRrJ8NlIvh98K0cqHvuyDPtdWOIkBbk9pqXp
jDTZzxgZn2mcu+BL8x/0Qt2rbFZ2gFNrLS5V9rdQj+1UOl1f61sZ5FtZ52sbT2Fh5r1HwdlO8IaQvZ0rhy
di7CQgNsMyslfSEJLR2q759SIHe7TnCgF3EOkxXRxoUkoRGcn72XhHNUjPgSBQ4zd30hLXg5Oc2UF8Ds+X
8MYo+uwt/n4lPVfYDYIhhbVo9Gqh7y5EWuuKPwwwrvA6ncfgA5LWYH+rUb5nmQIDAQABMA0GCSqGSIb3DQ
EBCwUAA4IBAQBiYjxGyickfI6mLM9L4b3IJ5gDyGV+jChmLStMsv50VefjhJEaBqU3WEWGKtPDM3zy8UQJ
AT1+LIxUUJsoxlvaKSsK6cgwYPGWg3+E0htTpDbnRJ2l7W3nf+n5nVtI2oxyLOTYJLiMpB8Kc9b2+wITtc
ttiuOOlgKOZumvwjhB6JUGkgCn1YAz5eLRgwHsNliWr6I4uhO9Al7ffS4BLewr0MRqWzgpoJK3vYIi62SX
1s3SnHE5x3AuVpI3L81tPs/MgbbRr0oxih2hr0BQXdb6nYA+6Ty+RsMx+49Pol8T4ImygsFwbK9yrtlR+A
3Y1p97fEfhBo+8QoVRticoSOmi</ds:X509Certificate>\n </ds:X509Data>\n </ds:KeyInfo>\n 
</md:KeyDescriptor>\n <md:AssertionConsumerService 
Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" 
Location=\"http://10.27.10.33:8080/login/saml2/sso/default_registration_id\" 
index=\"1\"/>\n </md:SPSSODescriptor>\n</EntityDescriptor>\n",
  "code": null,
  "message": null
}
```
