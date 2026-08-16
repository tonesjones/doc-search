---
title: "Using custom certificates"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-custom-certificates.html"
content_id: "K9tiDgQUFsKlkK3vL3qYcQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:44.232036+00:00"
---

# Using custom certificates

The webserver container has a self-signed certificate obtained from Docker. You may want
to replace this certificate with a custom certificate-key pair.

1. Use the docker secret command to tell Docker Swarm the certificate and key by using
   `WEBSERVER_CUSTOM_CERT_FILE` and
   `WEBSERVER_CUSTOM_KEY_FILE`. The name of the secret must
   include the stack name. In the following example, the stack name is 'hub':

   ```
   docker secret create hub_WEBSERVER_CUSTOM_CERT_FILE <certificate file>
   docker secret create hub_WEBSERVER_CUSTOM_KEY_FILE <key file>
   ```
2. Add the secret to the webserver service in the
   `docker-compose.local-overrides.yml` file:

   ```
   webserver:
   secrets: 
    - WEBSERVER_CUSTOM_CERT_FILE
    - WEBSERVER_CUSTOM_KEY_FILE
   ```
3. Remove the comment character (#) from the `secrets` section
   located at the end of the `docker-compose.local-overrides.yml`
   file located in the `docker-swarm` directory:

   ```
   secrets:
     WEBSERVER_CUSTOM_CERT_FILE:
       external: true
       name: "hub_WEBSERVER_CUSTOM_CERT_FILE"  
     WEBSERVER_CUSTOM_KEY_FILE:
       external: true
       name: "hub_WEBSERVER_CUSTOM_KEY_FILE"
   ```
4. The healthcheck property in the webserver service the
   `docker-compose.local-overrides.yml` file must point to the
   new certificate from the secret:

   ```
   webserver:
     healthcheck:
       test: [CMD, /usr/local/bin/docker-healthcheck.sh, 'https://localhost:8443/health-checks/liveness',/run/secrets/WEBSERVER_CUSTOM_CERT_FILE]
   ```
5. Redeploy the stack by running the following command:

   ```
   docker stack deploy -c docker-compose.yml -c docker-compose.local-overrides.yml hub
   ```

## Troubleshooting

If you encounter the following error, follow the steps below:

`Error response from daemon: rpc error: code = AlreadyExists desc = secret
hub_WEBSERVER_CUSTOM_CERT_FILE already exists.`

1. Stop Black Duck.

   ```
   docker stack rm hub
   docker ps : to wait until all containers are down
   ```
2. Remove previous secrets.

   ```
   docker secret rm hub_WEBSERVER_CUSTOM_CERT_FILE
   docker secret rm hub_WEBSERVER_CUSTOM_KEY_FILE
   ```
3. Create secrets again with new valid ones.

   ```
   docker secret create hub_WEBSERVER_CUSTOM_CERT_FILE <certificate file>
   docker secret create hub_WEBSERVER_CUSTOM_KEY_FILE <key file>
   ```
4. Redeploy Black Duck.

   ```
   docker stack deploy -c docker-compose.yml -c docker-compose.local-overrides.yml hub
   ```
5. Wait until all containers are healthy including nginx.

Note: If you have already updated your certificate and made changes to the overrides file, ensure
you uncomment the secrets portions because the new version of Black Duck will have
new files.
