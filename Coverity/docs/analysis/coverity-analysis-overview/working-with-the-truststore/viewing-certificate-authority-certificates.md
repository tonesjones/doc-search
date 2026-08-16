---
title: "Viewing Certificate Authority certificates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/viewing-certificate-authority-certificates.html"
content_id: "Pd3gpHof_mdRwoHIryN02g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:21.945239+00:00"
---

# Viewing Certificate Authority certificates

The certificate-authority certificates in ca-certs.pem are stored in
PEM format, which encodes the certificates as ASCII text. The file is a simple list of
certificates. An example certificate is shown below:

```
-----BEGIN CERTIFICATE-----
MIIDGzCCAoSgAwIBAgIJAPWdpLX3StEzMA0GCSqGSIb3DQEBBQUAMGcxCzAJBgNV
BAYTAlVTMRAwDgYDVQQIEwdVbmtub3duMQ8wDQYDVQQHEwZVbmtvd24xEDAOBgNV
BAoTB1Vua25vd24xEDAOBgNVBAsTB1Vua25vd24xETAPBgNVBAMTCFFBVGVzdENB
MCAXDTEzMDIyNTIyMTA1MloYDzIxMTMwMjAxMjIxMDUyWjBnMQswCQYDVQQGEwJV
UzEQMA4GA1UECBMHVW5rbm93bjEPMA0GA1UEBxMGVW5rb3duMRAwDgYDVQQKEwdV
bmtub3duMRAwDgYDVQQLEwdVbmtub3duMREwDwYDVQQDEwhRQVRlc3RDQTCBnzAN
BgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEA196ZPKzj6LKVrR9iZeDrqmrv25Zv3+9/
itiRN6xbJW0FvU/cIz2zoZxTIvlCFInC6qZ0BQcNJRsYmtJQsr/ka6MFuneULh3g
cYNxDTBRCJ2Lbs5xDjYMfEg6XJSwyBo/iG3fxb6IBdiAnjPdUFT5THkNheUhh62f
rISUU9zwAWcCAwEAAaOBzDCByTAdBgNVHQ4EFgQUn3hosvIlr4Md80enOS/kC/p3
JL4wgZkGA1UdIwSBkTCBjoAUn3hosvIlr4Md80enOS/kC/p3JL6ha6RpMGcxCzAJ
BgNVBAYTAlVTMRAwDgYDVQQIEwdVbmtub3duMQ8wDQYDVQQHEwZVbmtvd24xEDAO
BgNVBAoTB1Vua25vd24xEDAOBgNVBAsTB1Vua25vd24xETAPBgNVBAMTCFFBVGVz
dENBggkA9Z2ktfdK0TMwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOBgQAY
97hV0EM2uMg/kg2bUllyDtCnQLFdbv/NJ5b+SlHyAQAhaTchM7WBW7OVY4fTS9xZ
Uh8k7uvKicBAd48kdkU6K4LF3SowwjWdOmyGvOnyUHSvCCfa/+G/rPzMReIVQo2H
HIUtgMWvzOtZh6nYLV4JDbQcYJ0d7eBcvebetFAxyA==
-----END CERTIFICATE-----
```

To view these certificates you need to split them into separate files, with one
certificate per file. Then the commands to read them are

```
openssl x509 -in certificate-file-name -noout -text
```

or

```
keytool -printcert -file certificate-file-name -v
```
