---
title: "Adding a certificate to ca-certs.pem"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-certificate-to-ca-certs.pem.html"
content_id: "5Hrg~ttWAxKpT5lRm~BYbw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:23.235998+00:00"
---

# Adding a certificate to ca-certs.pem

You might want to add a certificate to ca-certs.pem if you want to
tell the application (for example, `cov-commit-defects`) that a certain
certificate is trusted as a certificate authority certificate. This is necessary if you
want to use the fully authenticated mode, but your certificate authority is not among
those listed in ca-certs.pem. This will be the case if you use an
internal certificate authority. To add it, there are two steps. First, if the
certificate is not already in PEM format, use `openssl` to convert it
to PEM format. For example, for a certificate in DER format, the
`openssl` command is

```
openssl x509 -in certificate-file-name -inform der -outform PEM > cert.pem
```

Alternatively, to do this using `keytool`, you first have to import the
certificate into a temporary keystore, then export it as a PEM file:

```
keytool -keystore new.jks -storepass newnew -importcert -alias 
new -file certificate-file-name
keytool -keystore new.jks -storepass newnew -exportcert -alias 
new -file cert.pem -rfc
```

After getting your certificate as a PEM file, prepend it
to the front of your ca-certs.pem file, or, if you are not using an
external certification authority, simply replace ca-certs.pem with
your certificate in PEM format.

On Linux:

```
> cat cert.pem ca-certs.pem > new-ca-certs.pem
> mv new-ca-certs.pem ca-certs.pem
```

On Windows:

```
> type cert.pem ca-certs.pem > new-ca-certs.pem
> del ca-certs.pem
> ren new-ca-certs.pem ca-certs.pem
```
