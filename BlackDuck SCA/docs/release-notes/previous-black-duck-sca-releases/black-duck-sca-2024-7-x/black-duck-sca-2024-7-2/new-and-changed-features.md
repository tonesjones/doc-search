---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "7qEhHFiAY7ofKhqUPcRfrA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:01.557383+00:00"
---

# New and changed features

## New secure JWT key pair provisioning

We have enhanced our JWT handling by allowing the secure provisioning of
public/private key pairs, improving overall security and operational efficiency.
This provisioning is optional and not a requirement for deployment. Instead of
automatically generating and storing these key pairs in the database, you can now
securely provide them to the services that require them.

Currently, only RSA keys (PEM encoded) are supported. Specifically, public keys must
be in X.509 format, and private keys must be in PKCS#8 format. The private key is
primarily needed by services that issue JWTs, such as the Authentication service,
while the public key is required by any service offering public APIs that require
authorized access.

## Container versions

- blackducksoftware/blackduck-postgres:14-1.25
- blackducksoftware/blackduck-postgres-upgrader:14-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.13
- blackducksoftware/blackduck-cfssl:1.0.28
- blackducksoftware/blackduck-nginx:2024.7.2
- blackducksoftware/blackduck-logstash:1.0.38
- blackducksoftware/bdba-worker:2024.6.3
- blackducksoftware/rabbitmq:1.2.40
- blackducksoftware/blackduck-authentication:2024.7.2
- blackducksoftware/blackduck-bomengine:2024.7.2
- blackducksoftware/blackduck-documentation:2024.7.2
- blackducksoftware/blackduck-integration:2024.7.2
- blackducksoftware/blackduck-jobrunner:2024.7.2
- blackducksoftware/blackduck-matchengine:2024.7.2
- blackducksoftware/blackduck-redis:2024.7.2
- blackducksoftware/blackduck-registration:2024.7.2
- blackducksoftware/blackduck-scan:2024.7.2
- blackducksoftware/blackduck-storage:2024.7.2
- blackducksoftware/blackduck-webapp:2024.7.2
