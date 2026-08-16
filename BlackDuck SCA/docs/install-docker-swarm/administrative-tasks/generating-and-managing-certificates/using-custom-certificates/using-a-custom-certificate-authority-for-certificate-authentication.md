---
title: "Using a custom certificate authority for certificate authentication"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-a-custom-certificate-authority-for-certificate-authentication.html"
content_id: "I~qF2Hsn0oK1AUlZP611~A"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:44.810466+00:00"
---

# Using a custom certificate authority for certificate authentication

You can use your own certificate authority for certificate authentication.

To use a custom certificate authority:

1. Add a docker secret called AUTH_CUSTOM_CA, the custom certificate authority
   certificate file, to the webserver and authentication services in the
   `docker-compose.local-overrides.yml` file located in the
   `docker-swarm` directory:

   ```
   webserver:
     secrets:
        - AUTH_CUSTOM_CA
   authentication:
     secrets:
       - AUTH_CUSTOM_CA
   ```
2. Add the following text to the end of the
   `docker-compose.local-overrides.yml` file located in the
   `docker-swarm` directory:

   ```
   secrets:
     AUTH_CUSTOM_CA:
       file: {file path on host machine}
   ```
3. Start the webserver container and the authentication service.
4. Once the Black Duck services are up, make an API request which will return the
   Json Web Token (JWT) with the certificate key pair that was signed with the
   trusted certificate authority. For example:

   ```
   curl https://localhost:443/jwt/token --cert user.crt --key user.key
   ```

Note: The user name of the certificate used for authentication must exist in the Black Duck system
as its Common Name (CN).
