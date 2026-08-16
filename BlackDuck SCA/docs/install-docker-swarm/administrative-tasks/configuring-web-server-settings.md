---
title: "Configuring Web server settings"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-web-server-settings.html"
content_id: "LNP~2WTXRwG4Ma7SN83kSg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:02.008815+00:00"
---

# Configuring Web server settings

Edit the `hub-webserver.env` file to:

- Configure the hostname.
- Configure the host port.
- Disable IPv6.

## Configuring the hostname

Edit the `hub-webserver.env` file to configure the hostname so the
certificate host name matches. The environment variable has the service name as the
default value.

When the web server starts up, it generates an HTTPS certificate if certificates are
not configured. You must specify a value for the PUBLIC_HUB_WEBSERVER_HOST
environment variable to tell the web server the hostname it will listen on so that
the hostnames can match. Otherwise, the certificate will only have the service name
to use as the hostname. This value should be changed to the publicly-facing hostname
that users will enter in their browser to access Black Duck. For
example:

```
PUBLIC_HUB_WEBSERVER_HOST=blackduck-docker01.dc1.lan
```

## Configuring the host port

You can configure a different value for the host port which, by default, is 443.

To configure the host port:

1. Add the new host port value to the
   `docker-compose.local-overrides.yml` file located in the
   `docker-swarm` directory.

   Use the `webserver` section to add the port information using
   the following format: `ports: ['NewValue:8443']` For
   example to change the port to 8443:

   ```
   webserver: 
    ports: ['8443:8443']
   ```
2. Edit the PUBLIC_HUB_WEBSERVER_PORT value in the
   `hub-webserver.env` file to add the new port value. For
   example:

   ```
   PUBLIC_HUB_WEBSERVER_PORT=8443
   ```
3. Comment out the following part in the `docker-compose.yml`
   file to disable access to port 443 on the host, otherwise, users can still
   access the host using port 443.

   ```
   webserver: 
    #ports: ['443:8443']
   ```

## Disabling IPv6

By default, NGiNX listens on IPv4 and IPv6. If IPv6 is disabled on a host machine,
change the value of the IPV4_ONLY environment variable to 1.
