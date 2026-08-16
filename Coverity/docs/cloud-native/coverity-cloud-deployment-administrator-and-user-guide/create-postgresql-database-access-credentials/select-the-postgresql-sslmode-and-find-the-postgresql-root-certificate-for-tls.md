---
title: "Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/select-the-postgresql-sslmode-and-find-the-postgresql-root-certificate-for-tls.html"
content_id: "jUYZCFwC2hfFzL3S5qpVyA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:33.859985+00:00"
---

# Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS

For TLS enabled communication between Coverity Connect and PostgreSQL, in the Helm chart,
set the `cim.postgres.sslmode` key to either `verify-ca`
or `verify-full`, and add the PostgreSQL root certificate to the Coverity
Connect truststore.

Note: Currently, Coverity cloud deployment supports only server
authentication for TLS.

The following table describes the options that can be configured in the
`postgres.sslmode` parameter in the following Helm keys:

- `global.postgres.sslmode`
- `cim.postgres`
- `scan-service.postgres`
- `storage-service.postgres`

Table 1. `cim.postgres.sslmode` options

| `sslmode` | Eavesdropping protection | Man-in-the-Middle (MITM) protection | Description |
| --- | --- | --- | --- |
| `disable` | No | No | No data encryption. No server verification. |
| `allow` | Maybe | No | Data encryption used if required by server. No server verification. |
| `prefer` | Maybe | No | Data encryption used if supported by server. No server verification. |
| `require` | Yes | No | Data encryption used. No server verification. |
| `verify-ca` | Yes | Depends on the Certificate Authority (CA) policy | Data encryption used. Assured connections to trusted server. TLS is enabled. This is the default value. |
| `verify-full` | Yes | Yes | Data encryption used. Assured trusted server connections to only specified server. TLS is enabled. `verify-full` cannot be configured for Google Cloud SQL as there might be issues related to specifying a hostname in the certificate. |

The following key supports the selected SSL mode on all relevant services, except where it
might be overriidden by a service.

- `global.postgres.sslmode` is a global value that applies to both the
  `cnc` chart and scan-services subchart.. See also Global Helm keys.

The following Helm keys can be used to set SSL mode on specific services, overriding
`global.postgres.sslmode` for each service:

- `cim.postgres.sslmode` in the `cnc` chart. See also cim.postgres Helm keys - create Connect cim PostgreSQL access job.
- `scan-service.postgres.sslmode` in the `scan-services` chart.
  See also scan-service.postgres Helm keys - configure access to a Scan Service PostgreSQL database.
- `storage-service.postgres.sslmode` in the `scan-services`
  chart. See also storage-service.postgres Helm keys - configure access to a Storage Service PostgreSQL database.

Certificates and keys can be in PKSC-12 or PKSC-8, PEM encoded X509v3 certificate. Refer
to <https://jdbc.postgresql.org/documentation/head/connect.html#ssl> for more
information.
