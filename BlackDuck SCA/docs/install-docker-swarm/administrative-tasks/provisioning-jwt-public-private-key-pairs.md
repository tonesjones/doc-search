---
title: "Provisioning JWT public/private key pairs"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/provisioning-jwt-public/private-key-pairs.html"
content_id: "kobof0o3xL4XRxYSEG_uQQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.650489+00:00"
content_hash: "3c3bdb4985d6274cb0d68df6e221d5acd54fd093bd9f77d517a13ce066297926"
---

# Provisioning JWT public/private key pairs

To enhance the security and flexibility of JWT management, our system now supports the optional provisioning of public/private key pairs. This allows you to securely provide and manage these keys, ensuring they are only used by the appropriate services, such as the Authentication service for private keys and public API services for public keys.

Currently, only RSA keys (PEM encoded) are supported. Specifically, public keys must be in X.509 format, and private keys must be in PKCS#8 format.

## Creating Docker secrets

To create public and private secrets in Docker:

1. Enter the following commands:

   ```
   docker secret create hub_JWT_PUBLIC_KEY public-key.pem
   docker secret create hub_JWT_PRIVATE_KEY private-key.pem
   ```
2. Edit `docker-compose.local-overrides.yml` to use JWT secrets and deploy:

   ```
   docker stack deploy -c docker-compose.yml -c docker-compose.local-overrides.yml jwt-swarm
   ```

## Sample overrides file

Here is a sample `docker-compose.local-overrides.yml` file (integration service configured as needed). The comments in this file show how to override some of the most popular set of options. However, it is possible to override any Docker configuration setting, for example Port mappings, by adding the override here.

```
version: '3.6'
services:
  authentication:
    secrets:
      - JWT_PUBLIC_KEY
      - JWT_PRIVATE_KEY
  webapp:
    secrets:
      - JWT_PUBLIC_KEY
      - JWT_PRIVATE_KEY
  scan:
    secrets:
      - JWT_PUBLIC_KEY
      - JWT_PRIVATE_KEY
  storage:
    secrets:
      - JWT_PUBLIC_KEY
      - JWT_PRIVATE_KEY
  jobrunner:
    secrets:
      - JWT_PUBLIC_KEY
      - JWT_PRIVATE_KEY
  bomengine:
    secrets:
      - JWT_PUBLIC_KEY
      - JWT_PRIVATE_KEY
  matchengine:
    secrets:
      - JWT_PUBLIC_KEY
      - JWT_PRIVATE_KEY
  #integration:
  #  secrets:
  #   - JWT_PUBLIC_KEY
  #   - JWT_PRIVATE_KEY
secrets:
  JWT_PUBLIC_KEY:
    external: true
    name: "hub_JWT_PUBLIC_KEY"
  JWT_PRIVATE_KEY:
    external: true
    name: "hub_JWT_PRIVATE_KEY"
```
