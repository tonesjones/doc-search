---
title: "Viewing trust-first-time Certificates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/viewing-trust-first-time-certificates.html"
content_id: "FjeXvKNVlSZq6CmTeOms2g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:21.284743+00:00"
---

# Viewing trust-first-time Certificates

Trust-first-time certificates are stored in DER format. They can be read using the
`openssl` command, present on most linux systems, or using the
`keytool` command, present in the Java Runtime Environment at
install-dir/jre/bin/keytool. For
example,

```
openssl x509 -in host-d-linux64-07,port-9090.der -inform der -noout -text
```

or

```
keytool -printcert -file host-d-linux64-07,port-9090.der -v
```
