---
title: "Using mTLS with Docker Swarm for External Databases"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-mtls-with-docker-swarm-for-external-databases.html"
content_id: "zg4T7anwNqr_wO_FquwJvQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:53.598560+00:00"
---

# Using mTLS with Docker Swarm for External Databases

This section provides guidance for configuring mTLS (mutual Transport Layer
Security) with PostgreSQL in a Docker Swarm environment.

## Configure PostgreSQL

Customers are responsible for configuring PostgreSQL to use mTLS. Follow these steps
to ensure proper setup:

**Database Setup and configuration**:

1. Set up the database following the guidelines outlined in the Black Duck Documentation Portal.
2. **Update `hub-webserver.env`:**

   Configure the `PUBLIC_HUB_WEBSERVER_HOST` variable in the
   `hub-webserver.env` file as documented in other sections.
3. **Update `hub-postgres.env`:**

   Modify the `hub-postgres.env` file with the following
   values:

   - `HUB_POSTGRES_ENABLE_SSL` - Set to
     `true`
   - `HUB_POSTGRES_ENABLE_SSL_CERT_AUTH` - Set to
     `true`
   - `HUB_POSTGRES_HOST` - Enter your PostgreSQL host.
   - `HUB_POSTGRES_PORT` - Enter your PostgreSQL port.
   - `HUB_POSTGRES_USER` - If not using the default, specify
     the non-admin PostgreSQL user for Black Duck.
   - `HUB_POSTGRES_ADMIN` - If not using the default, specify
     the admin PostgreSQL user for Black Duck.

## Certificates and Keys

To utilize mTLS, you must have the following certificates and keys:

- **Certificates Required:**

  You need either:

  1. A root certificate, or
  2. A client certificate and key, or
  3. An admin certificate and key, or a combination of these.

  Note: If using a client certificate, the client key is also
  required. The same applies for the admin certificate. If either the
  certificate or key is missing, the startup script will not function
  properly. The root certificate is standalone and does not require a
  key.
- **File Ownership and Permissions:**

  All certificates and keys must be stored in the same directory, which
  should be owned by root and have permissions set to 755. The following
  naming and permission conventions must be followed:

  - `HUB_POSTGRES_CA` (Root Certificate): Owned by root,
    permissions 644.
  - `HUB_POSTGRES_CRT` (Client Certificate): Owned by
    root, permissions 644.
  - `HUB_POSTGRES_KEY` (Client Key): Owned by root,
    permissions 640. Must be in PKCS#8 format.
  - `HUB_ADMIN_POSTGRES_CRT` (Admin Certificate): Owned
    by root, permissions 644.
  - `HUB_ADMIN_POSTGRES_KEY` (Admin Key): Owned by root,
    permissions 640. Must be in PKCS#8 format.

## Volume Mount

A new YAML file has been introduced specifically for using mTLS with an external
database: `docker-compose.externaldb-cert-volume.yml`.
Incorporating this YAML into your deployment will enable mTLS and create a
volume mount for the certificates and keys.

**Required Edits to YAML File:**

1. **HUB_POSTGRES_SSL_MODE:**

   This setting configures the `sslmode` for authenticating with
   PostgreSQL. Supported modes are `verify-ca` (default) and
   `verify-full`. Using any other setting will disable mTLS
   authentication.
2. **Integrations Container:**

   If deploying with the integrations container, uncomment the relevant lines
   that are currently commented out, starting with
   `#integration:`.
3. **Volume Path:**

   Set the path for
   `volumes►hub-certificates►driver_opts►device` to the
   absolute path of the directory containing the certificates and keys.

## Starting Black Duck

When starting Black Duck, ensure to include
`docker-compose.externaldb-cert-volume.yml` in your command to
enable mTLS functionality.
