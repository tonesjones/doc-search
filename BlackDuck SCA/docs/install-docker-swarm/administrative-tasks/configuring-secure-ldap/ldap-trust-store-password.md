---
title: "LDAP trust store password"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/ldap-trust-store-password.html"
content_id: "bzhFX2_S93gPkNJON3oAtQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:47.219951+00:00"
---

# LDAP trust store password

If you add a custom Black Duck web application trust store, use these
methods for specifying an LDAP trust store password.

Use these methods for specifying an LDAP trust store password when using Docker
Swarm.

- Use the docker secret command to tell Docker Swarm the password by using
  LDAP_TRUST_STORE_PASSWORD_FILE. The name of the secret must include the stack
  name. 'HUB' is the stack name in this example:

  ```
  docker secret create HUB_LDAP_TRUST_STORE_PASSWORD_FILE <file containing password>
  ```

  Add the password secret to the webapp service in the
  `docker-compose.local-overrides.yml` file located in the
  `docker-swarm` directory:

  ```
    secrets:
      - LDAP_TRUST_STORE_PASSWORD_FILE
  ```

  Add text, such as the following, to the `secrets` section located
  at the end of the `docker-compose.local-overrides.yml` file:

  ```
  secrets:
    LDAP_TRUST_STORE_PASSWORD_FILE:
       external: true
       name: "HUB_LDAP_TRUST_STORE_PASSWORD_FILE"
  ```
- Mount a directory that contains a file called LDAP_TRUST_STORE_PASSWORD_FILE to
  `/run/secrets` by adding a volumes section for the webapp
  service in the `docker-compose.local-overrides.yml` file located
  in the `docker-swarm` directory.

  ```
  webapp:
    volumes: ['/directory/where/file/is:/run/secrets']
  ```

  Note: You only need to mount a directory that contains the LDAP_trust_store_password_file if the
  trust store is fully replaced and it is protected by a different
  password.
