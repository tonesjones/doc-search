---
title: "Interpreting a certificate file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/interpreting-a-certificate-file.html"
content_id: "hxQzQ1koqGpAFxIwovcFAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:22.591384+00:00"
---

# Interpreting a certificate file

You typically will not need to interpret an individual certificate file, but a sample
certificate, as dumped by keytool, is displayed below. Descriptions of the individual
elements follow.

```
Owner: C=None, L=None, O=None, OU=None, CN=d-linux64-07
Issuer: C=None, L=None, O=None, OU=None, CN=d-linux64-07
Serial number: 555b70a6
Valid from: Fri Dec 20 16:21:15 PST 2013 until: Tue Dec 20 16:51:15 PST 2033
Certificate fingerprints:
       MD5:  78:0D:07:53:3E:BF:A2:76:B1:C2:9E:2C:86:A6:2C:5B
       SHA1: AD:66:3E:5C:40:FC:49:84:F6:21:3E:B2:37:9A:32:25:B2:33:38:4D
       Signature algorithm name: SHA256withRSA
       Version: 3
```

The `Owner` string identifies the peer. In particular the `CN`
portion of the owner field contains the host name of the peer. In TLS/SSL, the other
fields of the owner string are ignored. The `Issuer` string identifies
the entity that created the certificate. In this case, the issuer matches the owner,
which means the certificate is self-signed. The `Valid from` and
`until` fields show the dates on which the certificate will pass into
and out of validity. The `fingerprints` are `MD5` and
`SHA1` hashes of the DER form of the certificate.
