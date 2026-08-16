---
title: "Configuring proxy settings"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-proxy-settings.html"
content_id: "6ml1va_J9M1~vRvMYbgMCg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:54.178222+00:00"
---

# Configuring proxy settings

Edit the `blackduck-config.env` file to configure proxy settings. You will
need to configure these settings if a proxy is required for external internet
access.

These are the containers that need access to services hosted by Black Duck Software:

- Authentication
- Registration
- Job runner
- Web app
- Scan
- Bomengine
- Integration

Proxy environment variables are:

- `HUB_PROXY_HOST`. Name of the proxy server host.
- `HUB_PROXY_PORT`. The port on which the proxy server host is listening.
- `HUB_PROXY_SCHEME`. Protocol to use to connect to the proxy server.
- `HUB_PROXY_USER`. Username to access the proxy server.

The environment variables for NTLM proxies are:

- `HUB_PROXY_WORKSTATION`. The workstation the authentication request is
  originating from. Essentially, the computer name for this machine.
- `HUB_PROXY_DOMAIN`. The domain to authenticate within.

## Proxy password

The following services require the proxy password if authentication is leveraged via
proxy:

- Authentication
- Bomengine
- Web App
- Registration
- Job Runner
- Scan
- Integration

There are three methods for specifying a proxy password:

- Mount a directory that contains a text file called `HUB_PROXY_PASSWORD_FILE`
  to `/run/secrets`. This is the most secure option.
- Specify an environment variable called `HUB_PROXY_PASSWORD` that contains the
  proxy password.
- Use the docker secret command to create a secret called
  `HUB_PROXY_PASSWORD_FILE` as described below:
  1. Use the docker secret command to tell Docker Swarm the secret. The
     name of the secret must include in the stack name. In the following
     example, the stack name is 'hub':

     ```
     docker secret create hub_HUB_PROXY_PASSWORD_FILE <file containing password>
     ```
  2. In the `docker-compose.local-overrides.yml` file,
     located in the `docker-swarm` directory, for each
     service (authentication, webapp, registration, jobrunner, Match
     engine, Bom engine, and scan), provide access to the secret. This
     example is for the scan service:

     ```
     scan:
      secrets:
        - HUB_PROXY_PASSWORD_FILE
     ```

     If necessary, remove the comment characters (#).
  3. In the `secrets` section at the end of the
     `docker-compose.local-overrides.yml` file, add
     the following:

     ```
     secrets:
       HUB_PROXY_PASSWORD_FILE:
         external: true
         name: "hub_HUB_PROXY_PASSWORD_FILE"
     ```

     If necessary, remove the comment characters (#).

You can use the `blackduck-config.env` file to specify an environment
variable if it is not specified in a separate mounted file or secret:

1. Remove the pound sign (#) located in front of `HUB_PROXY_PASSWORD` so that it
   is no longer commented out.
2. Enter the proxy password.
3. Save the file.

Note: If KB calls fail when the proxy password is provided by using the *docker secret
HUB_PROXY_PASSWORD_FILE* in a Docker Swarm deployment, provide the password
in the *blackduck-config.env* file to resolve the issue.

## Importing a proxy certificate

You can import a proxy certificate to work with the proxy.

1. Create a docker secret called `<stack name>_HUB_PROXY_CERT_FILE` with the
   proxy certificate file. For example

   ```
   docker secret create <stack name>_HUB_PROXY_CERT_FILE <certificate file>
   ```
2. In the `docker-compose.local-overrides.yml` file, located in the
   `docker-swarm` directory, provide access to the secret to
   these services: authentication, webapp, registration, jobrunner,
   integration, and scan. This example is for the scan service:

   ```
   scan:
    secrets:
      - HUB_PROXY_CERT_FILE
   ```

## Using an authenticated proxy

Due to changes made in JDK 8u111 ([Consolidated JDK 8 Release Notes
(oracle.com)](https://www.oracle.com/java/technologies/javase/8all-relnotes.html#R180_111)), customers using a proxy requiring basic authentication may
face issues communicating with the Black Duck registration services. To overcome
this, the following change should be made to `blackduck-config.env`
(Docker Swarm) or the ConfigMap (Kubernetes/Openshift):

```
REGISTRATION_SERVICE_OPTS="-Djdk.http.auth.tunneling.disabledSchemes=''"
```
