---
title: "HTTPS Pre-work"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/https-pre-work.html"
content_id: "hTqkpfsHHpzeCvrfWtMPZg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:05.017241+00:00"
content_hash: "b55e1535f3fc27c27b794e5965aaea12db53e1ec5462218cce99cca5b7f2c513"
---

# HTTPS Pre-work

The Tomcat container can support HTTPS. For example, generate a self-signed certificate
with `openssl` or obtain a real certificate from a certificate
authority:

```
openssl req -new -newkey rsa:4096 -days 3650 -nodes -x509 -subj "/C=US/ST=New York/L=Northport/O=Software Risk Manager/CN=localhost" -keyout ./ssl.key -out ./ssl.crt
```

The [server.xml](https://github.com/codedx/srm-docker/blob/master/server.xml) file contains a configuration that
supports HTTPS using **[Tomcat's SSL/TLS capability](https://tomcat.apache.org/tomcat-9.0-doc/ssl-howto.html)**.

This template can be mounted over the existing `server.xml` in the Docker
image. The SSL certificate and private key must also be mounted.

Update the codedx-tomcat section in your Docker Compose file (either
`docker-compose.yml` or
`docker-compose-external-db.yml`) with SSL and
`server.xml` volume mounts, switching ports from
`8080:8080` to `8443:8443`. See what follows for
Docker Compose file content using port 8443 with extra volume mounts for
`server.xml`, `ssl.key`, and
`ssl.crt`.

```
    codedx-tomcat:
        ...
        volumes:
            - codedx-appdata:/opt/codedx
            - /path/to/ssl.crt:/usr/local/tomcat/conf/ssl.crt
            - /path/to/ssl.key:/usr/local/tomcat/conf/ssl.key
            - /path/to/server.xml:/usr/local/tomcat/conf/server.xml
        ports:
            - 8443:8443
        ...
```

Note: Append `:Z` to the extra volume mount when using [selinux](https://docs.docker.com/storage/bind-mounts/#configure-the-selinux-label).
