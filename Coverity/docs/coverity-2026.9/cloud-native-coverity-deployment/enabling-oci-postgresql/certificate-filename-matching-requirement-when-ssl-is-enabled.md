---
title: "Certificate Filename Matching Requirement when SSL is enabled"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/certificate-filename-matching-requirement-when-ssl-is-enabled.html"
content_id: "U9IchDHumjtBxa~6sFPP6A"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:34.635442+00:00"
---

# Certificate Filename Matching Requirement when SSL is enabled

Important:

The `certFilename` and `certKeyFilename` values
**MUST** match the filenames used in the `ssl_cert_file` and
`ssl_key_file` arguments(args). The Bitnami PostgreSQL chart
mounts certificates at `/opt/bitnami/postgresql/certs/`, so:

- Configured as follows, PostgreSQL reads from
  `/opt/bitnami/postgresql/certs/certificate.pem`.

  ```
  certFilename: "certificate.pem"
  ```
- Configured as follows, PostgreSQL reads from
  `/opt/bitnami/postgresql/certs/key.pem`.

  ```
  certKeyFilename: "key.pem"
  ```

  For
  example:

  - "-c"

  -
  "ssl_cert_file=/opt/bitnami/postgresql/certs/certificate.pem" -> Must Match
  `certFilename`

  - "-c"

  -
  "ssl_key_file=/opt/bitnami/postgresql/certs/key.pem" -> Must Match
  `certKeyFilename`

These filenames must also match the key names in the
`postgres-certificates-tls-secret` Kubernetes secret.
